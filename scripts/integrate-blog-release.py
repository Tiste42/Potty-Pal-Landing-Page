"""Add one validated article to the existing catalogs without model edits."""
from __future__ import annotations
import argparse
import datetime as dt
import html
import json
import re
from pathlib import Path
from html.parser import HTMLParser

CATEGORIES = {
    'potty-training-tips': 'Potty Training Tips',
    'common-problems': 'Common Problems',
    'readiness-starting-out': 'Readiness & Starting Out',
    'night-training': 'Night Training',
    'regression-setbacks': 'Regression & Setbacks',
    'special-situations': 'Special Situations',
}

class Article(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_h1 = False
        self.title = ''
        self.description = ''
        self.hero_alt = ''
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h1': self.in_h1 = True
        if tag == 'meta' and attrs.get('name') == 'description':
            self.description = attrs.get('content', '')
        if tag == 'img' and attrs.get('src', '').startswith('../images/blog/') and not self.hero_alt:
            self.hero_alt = attrs.get('alt', '')
    def handle_endtag(self, tag):
        if tag == 'h1': self.in_h1 = False
    def handle_data(self, data):
        if self.in_h1: self.title += data

def integrate(root: Path, slug: str, category: str, expected_title: str) -> None:
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        raise ValueError('Invalid article slug')
    if category not in CATEGORIES:
        raise ValueError('Unknown category')
    source = (root / 'blog' / f'{slug}.html').read_text(encoding='utf-8')
    parsed = Article()
    parsed.feed(source)
    title = parsed.title.strip()
    if title != expected_title:
        raise ValueError('Article title must exactly match the approved queue topic')
    if not (20 <= len(parsed.description) <= 160) or not parsed.hero_alt:
        raise ValueError('Missing or invalid article description/hero alt')
    if any(c in title + parsed.description + parsed.hero_alt for c in '<>'):
        raise ValueError('Article metadata cannot contain HTML markup')
    dates = re.findall(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})', source)
    if not dates or set(dates) != {dt.date.today().isoformat()}:
        raise ValueError('New article publication date must be today')
    date = dt.date.fromisoformat(dates[0])
    entry = dict(title=title, slug=slug, excerpt=parsed.description, date=date.isoformat(),
                 category=category, categoryName=CATEGORIES[category], image=f'{slug}.webp', imageAlt=parsed.hero_alt)
    prepared = {}
    for path, article_prefix, image_prefix in [
        (root/'blog/index.html', '', '../'),
        (root/'blog/category'/f'{category}.html', '../', '../../'),
    ]:
        content = path.read_text(encoding='utf-8')
        if re.search(rf'slug\s*:\s*["\']{re.escape(slug)}["\']|"slug"\s*:\s*"{re.escape(slug)}"', content):
            if f'href="{article_prefix}{slug}.html"' not in content:
                raise ValueError(f'Partial existing catalog entry in {path.name}')
            continue
        anchor = '<div class="posts-container" id="postsGrid">'
        js_anchor = 'const blogPosts = ['
        if content.count(anchor) != 1 or content.count(js_anchor) != 1:
            raise ValueError(f'Unexpected catalog structure in {path.name}')
        esc = html.escape
        card = f'''\n      <a href="{article_prefix}{slug}.html" class="post-card">
        <img src="{image_prefix}images/blog/{slug}.webp" alt="{esc(parsed.hero_alt, quote=True)}" class="post-card-image" loading="lazy">
        <div class="post-card-content">
          <div class="post-card-categories"><span class="post-card-category">{esc(CATEGORIES[category])}</span></div>
          <h2 class="post-card-title">{esc(title)}</h2>
          <p class="post-card-excerpt">{esc(parsed.description)}</p>
          <span class="post-card-date">{date.strftime('%B')} {date.day}, {date.year}</span>
        </div>
      </a>\n'''
        content = content.replace(anchor, anchor + card, 1)
        content = content.replace(js_anchor, js_anchor + '\n      ' + json.dumps(entry, ensure_ascii=True) + ',', 1)
        prepared[path] = content
    sitemap_path = root/'sitemap.xml'
    sitemap = sitemap_path.read_text(encoding='utf-8')
    url = f'https://www.pottypalai.com/blog/{slug}.html'
    if url not in sitemap:
        if sitemap.count('</urlset>') != 1: raise ValueError('Unexpected sitemap structure')
        block = f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{date.isoformat()}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
        prepared[sitemap_path] = sitemap.replace('</urlset>', block + '</urlset>', 1)
    # Check every target before making any writes; only known catalog paths change.
    for path, content in prepared.items(): path.write_text(content, encoding='utf-8')
    print(f'Integrated {slug} into {len(prepared)} catalog files')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--slug', required=True)
    parser.add_argument('--category', required=True)
    parser.add_argument('--title', required=True)
    args = parser.parse_args()
    integrate(Path.cwd(), args.slug, args.category, args.title)
