# Sitemap Update Guide

This guide explains how to add new pages to the sitemap for proper search engine indexing.

## Sitemap Location

- **File:** `sitemap.xml`
- **URL:** `https://pottypalai.com/sitemap.xml`
- **Google Search Console:** Submit at `sitemap.xml` (or full URL)

## When to Update Sitemap

Update the sitemap when you:
- ✅ Add a new blog post
- ✅ Add a new category page
- ✅ Add a new main page (privacy, terms, etc.)
- ✅ Update an existing page significantly (update lastmod date)

## URL Format Rules

### Important: No .html Extension
- ✅ **Correct:** `https://pottypalai.com/blog/potty-training-topic`
- ❌ **Wrong:** `https://pottypalai.com/blog/potty-training-topic.html`

The server is configured to serve pages without the .html extension, so the sitemap should match this.

### Domain
- Always use: `https://pottypalai.com` (not http, not www)

## Adding a New Blog Post

1. **Open `sitemap.xml`**

2. **Find the "Blog Posts" section** (after "Blog Index" section)

3. **Add new entry** in alphabetical or chronological order:

```xml
<url>
  <loc>https://pottypalai.com/blog/your-post-slug</loc>
  <lastmod>2025-01-15</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```

**Field Explanations:**
- `<loc>` - Full URL without .html extension
- `<lastmod>` - Date in YYYY-MM-DD format (use publication date)
- `<changefreq>` - "monthly" for blog posts (how often content changes)
- `<priority>` - "0.8" for blog posts (0.0 to 1.0, where 1.0 is most important)

4. **Save the file**

## Adding a Category Page

Category pages use `.html` extension in the URL:

```xml
<url>
  <loc>https://pottypalai.com/blog/category/category-name.html</loc>
  <lastmod>2025-01-15</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.7</priority>
</url>
```

**Settings:**
- `<changefreq>` - "weekly" (category pages update more frequently)
- `<priority>` - "0.7" (slightly lower than blog posts)

## Adding a Main Page

Main pages (homepage, privacy, terms):

```xml
<url>
  <loc>https://pottypalai.com/page-name.html</loc>
  <lastmod>2025-01-15</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.5</priority>
</url>
```

**Settings:**
- Homepage: `<priority>1.0</priority>` (highest priority)
- Other main pages: `<priority>0.5</priority>`
- `<changefreq>` - "monthly" for static pages

## Updating Existing Pages

When you significantly update a page:

1. **Find the entry** in sitemap.xml
2. **Update `<lastmod>`** to current date
3. **Save the file**

**Example:**
```xml
<!-- Before -->
<url>
  <loc>https://pottypalai.com/blog/potty-training-topic</loc>
  <lastmod>2025-01-01</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>

<!-- After update -->
<url>
  <loc>https://pottypalai.com/blog/potty-training-topic</loc>
  <lastmod>2025-01-15</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```

## Priority Guidelines

Use these priority values:

- **1.0** - Homepage only
- **0.9** - Blog index page
- **0.8** - Individual blog posts
- **0.7** - Category pages
- **0.5** - Other main pages (privacy, terms, etc.)

## Change Frequency Guidelines

- **weekly** - Pages that update frequently (blog index, category pages)
- **monthly** - Pages that update occasionally (blog posts, main pages)
- **yearly** - Pages that rarely change (privacy, terms)

## Complete Example: Adding a New Blog Post

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- ... existing entries ... -->
  
  <!-- Blog Posts -->
  <url>
    <loc>https://pottypalai.com/blog/potty-training-new-topic</loc>
    <lastmod>2025-01-15</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  
  <!-- ... rest of entries ... -->
</urlset>
```

## Validation

After updating the sitemap:

1. **Check XML syntax** - Ensure all tags are properly closed
2. **Validate online** - Use [XML Sitemap Validator](https://www.xml-sitemaps.com/validate-xml-sitemap.html)
3. **Test URL** - Visit `https://pottypalai.com/sitemap.xml` to verify it loads
4. **Submit to Google** - In Google Search Console, submit or resubmit the sitemap

## Google Search Console

### Submitting the Sitemap

1. Go to [Google Search Console](https://search.google.com/search-console)
2. Select your property (`https://pottypalai.com`)
3. Navigate to **Sitemaps** in the left menu
4. Enter: `sitemap.xml` (or full URL: `https://pottypalai.com/sitemap.xml`)
5. Click **Submit**

### After Updates

- Google will automatically re-crawl the sitemap periodically
- You can also click **Test** in Search Console to verify the sitemap
- Check for any errors or warnings

## Common Mistakes

❌ **Don't:**
- Add .html extension to blog post URLs
- Use wrong date format (must be YYYY-MM-DD)
- Forget to update lastmod when editing pages
- Use priority > 1.0 (max is 1.0)
- Add duplicate URLs

✅ **Do:**
- Use clean URLs (no .html for blog posts)
- Use current date for new posts
- Update lastmod when content changes
- Keep priorities between 0.0 and 1.0
- Maintain alphabetical or chronological order

## File Structure Reference

```
sitemap.xml
├── Main Pages (priority 1.0, 0.5)
├── Blog Index (priority 0.9)
├── Blog Posts (priority 0.8)
└── Category Pages (priority 0.7)
```

## Need Help?

- Check existing entries in `sitemap.xml` for examples
- Refer to this guide for format requirements
- Validate XML syntax before committing
- Test the sitemap URL in browser
