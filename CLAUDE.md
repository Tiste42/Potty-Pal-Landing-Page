# Potty Pal AI -- Project Intelligence

## What This Is
Potty Pal AI is a personalized potty training app for parents of toddlers.
Live at pottypalai.com. Hosted on GitHub Pages. App available on iOS and Android.

## Tech Stack
- Static HTML/CSS/JS site (no framework, no build step)
- GitHub Pages hosting with custom domain (pottypalai.com / www.pottypalai.com)
- Google Analytics (G-VV8TGNN2S1) + Facebook Pixel (907678131685393)
- Fonts: Quicksand (body) + Fredoka (display headings)
- CSS variables: --accent (#4ECDC4), --accent2 (#1A535C)

## Site Structure
- / -- Homepage with app download CTAs, How It Works, Pricing, FAQ
- /products.html -- Products/Essentials page
- /blog/ -- Blog hub (grid layout)
- /blog/<slug>.html -- Individual blog posts (static HTML files)
- /blog/category/<category-slug>.html -- Category pages
- /privacy.html -- Privacy policy
- /terms.html -- Terms of use
- /delete.html -- Data deletion page
- /update-password.html -- Password update page
- /sitemap.xml -- Static sitemap (must be updated manually with each new post)
- /robots.txt -- References sitemap
- /llms.txt -- AI/LLM discoverability endpoint

## Blog System
- 10 posts as of Mar 2026
- Content format: Static HTML files in /blog/ (not JSON-backed)
- Template: blog/post-template.html (copy for new posts)
- Images: /images/blog/ directory, WebP preferred
- Categories (6): potty-training-tips, common-problems, readiness-starting-out, night-training, regression-setbacks, special-situations
- Category pages: blog/category/<category-slug>.html
- Author: "Potty Pal AI" on all posts
- Related posts: hardcoded in each post's JavaScript relatedPosts array

## Blog Post HTML Structure
Each post is a standalone HTML file containing:
- Google Analytics + Facebook Pixel scripts in <head>
- Full SEO meta tags (title, description, keywords, OG, Twitter, canonical)
- JSON-LD structured data (Article schema)
- Inline CSS (full stylesheet, no external CSS file)
- Hamburger mobile menu
- Breadcrumb navigation
- Article header with category link, date, and H1
- Featured image
- Article content (H2/H3 sections)
- CTA section with download button
- Related posts grid (rendered via JS)
- Footer
- Smart download link JS (detects iOS vs Android)

## Required Meta Tags Per Post
- <title>: 50-60 chars including "| Potty Pal AI"
- meta description: 150-160 chars
- meta keywords: 5-10 terms
- og:title, og:description, og:image, og:type, og:url, og:site_name
- twitter:card, twitter:title, twitter:description, twitter:image
- link rel="canonical"
- JSON-LD Article schema with datePublished, dateModified, author, publisher

## URL Conventions
- Canonical URLs: https://pottypalai.com/blog/<slug> (no www, no .html)
- OG/Twitter image URLs: https://www.pottypalai.com/images/blog/<filename>
- Internal links in HTML: use relative paths with .html (e.g., potty-training-readiness-8-signs.html)

## Images
- Format: WebP preferred, PNG acceptable
- Location: /images/blog/
- Featured images: 16:9 aspect ratio, displayed with object-fit: cover
- Hero image generation: cheerful children's book illustration style, no text, no logos
- Alt text: descriptive, includes relevant keywords naturally

## SEO & Schema Already Implemented
- Full OG and Twitter meta tags on all blog posts
- Schema.org Article structured data per post
- BreadcrumbList in HTML (Home > Blog > Category > Post)
- Static sitemap.xml
- robots.txt

## Code Conventions
- Never use em dashes in any content
- Never use AI-sounding words: "delve", "landscape", "leverage", "unleash", "comprehensive", "robust"
- Short paragraphs (2-4 sentences max)
- All blog images should be WebP format
- Always use contractions in blog content
- Disclaimer: "Educational coaching, not medical advice" in footer

## Reference Files
- BLOG_STYLE_GUIDE.md -- Voice, tone, and content structure rules
- SEO_GUIDELINES.md -- SEO and GEO optimization rules
- voice-profile.md -- Potty Pal voice profile (tone, vocabulary, banned words)
- BLOG_POST_SEO_CHECKLIST.md -- Manual checklist for new posts
- SITEMAP_GUIDE.md -- How to update sitemap.xml
- PERFORMANCE_GUIDE.md -- Core Web Vitals and image optimization
- .claude/topics.md -- Blog topic queue with status tracking

## Commands
- `/project:blog <topic>` -- Full automated blog pipeline
- `/project:blog auto` -- Picks next topic from .claude/topics.md
- Git commit format: "Add blog post: <post-title>"

## App Store Links
- iOS: https://apps.apple.com/app/id6751612917
- Android: https://play.google.com/store/apps/details?id=com.pottypalai.app
