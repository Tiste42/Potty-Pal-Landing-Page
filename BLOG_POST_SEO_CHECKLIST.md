# Blog Post SEO Checklist

Use this checklist when creating a new blog post to ensure optimal SEO and performance.

## Pre-Publication Checklist

### 1. File Setup
- [ ] Create HTML file in `blog/` directory with slug-based filename (e.g., `potty-training-topic.html`)
- [ ] Copy from `blog/post-template.html` as starting point
- [ ] Ensure filename matches the slug in URLs

### 2. SEO Meta Tags (Required)

#### Title Tag
- [ ] **Character count:** 50-60 characters (including "| Potty Pal AI")
- [ ] **Format:** "Main Title Here | Potty Pal AI"
- [ ] **Includes primary keyword** near the beginning
- [ ] **Compelling and click-worthy**

**Example:**
```html
<title>Is Your Toddler Ready? 8 Signs of Potty Training Readiness | Potty Pal AI</title>
```

#### Meta Description
- [ ] **Character count:** 150-160 characters
- [ ] **Includes primary keyword** naturally
- [ ] **Clear value proposition** - what will reader learn?
- [ ] **Call to action** or compelling reason to click

**Example:**
```html
<meta name="description" content="Not sure if your toddler is ready for potty training? Learn 8 clear signs of readiness and when to start—plus what to avoid." />
```

#### Keywords Meta Tag
- [ ] **5-10 relevant keywords** (comma-separated)
- [ ] **Primary keyword first**, then related terms
- [ ] **Natural keyword variations** included

**Example:**
```html
<meta name="keywords" content="potty training readiness, signs toddler ready potty training, when to start potty training, potty training age, toddler readiness signs" />
```

### 3. Open Graph Tags (Social Sharing)

- [ ] `og:title` - Same as title tag (without "| Potty Pal AI" is fine)
- [ ] `og:description` - Same as meta description
- [ ] `og:image` - Featured image URL (1200x630px recommended)
- [ ] `og:type` - Set to "article"
- [ ] `og:url` - Full canonical URL (no .html extension)
- [ ] `og:site_name` - "Potty Pal AI"

**Example:**
```html
<meta property="og:title" content="Is Your Toddler Ready? 8 Signs of Potty Training Readiness | Potty Pal AI" />
<meta property="og:description" content="Not sure if your toddler is ready for potty training? Learn 8 clear signs of readiness and when to start—plus what to avoid." />
<meta property="og:image" content="https://pottypalai.com/images/blog/potty-training-readiness-8-signs.png" />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://pottypalai.com/blog/potty-training-readiness-8-signs" />
<meta property="og:site_name" content="Potty Pal AI" />
```

### 4. Twitter Card Tags

- [ ] `twitter:card` - Set to "summary_large_image"
- [ ] `twitter:title` - Same as og:title
- [ ] `twitter:description` - Same as og:description
- [ ] `twitter:image` - Same as og:image

**Example:**
```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Is Your Toddler Ready? 8 Signs of Potty Training Readiness | Potty Pal AI" />
<meta name="twitter:description" content="Not sure if your toddler is ready for potty training? Learn 8 clear signs of readiness and when to start—plus what to avoid." />
<meta name="twitter:image" content="https://pottypalai.com/images/blog/potty-training-readiness-8-signs.png" />
```

### 5. Canonical URL

- [ ] **Full URL** without .html extension
- [ ] **Matches og:url** exactly
- [ ] **Uses https://pottypalai.com** domain

**Example:**
```html
<link rel="canonical" href="https://pottypalai.com/blog/potty-training-readiness-8-signs" />
```

### 6. JSON-LD Structured Data (Article Schema)

- [ ] `@type` - Set to "Article"
- [ ] `headline` - Main title (without "| Potty Pal AI")
- [ ] `description` - Same as meta description
- [ ] `image` - Featured image URL
- [ ] `datePublished` - ISO 8601 format (YYYY-MM-DDTHH:MM:SS+00:00)
- [ ] `dateModified` - Same as datePublished (or update when editing)
- [ ] `author` - Organization: "Potty Pal AI"
- [ ] `publisher` - Organization with logo URL
- [ ] `articleSection` - Category name (e.g., "Readiness & Starting Out")
- [ ] `mainEntityOfPage` - Full URL matching canonical

**Example:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Is Your Toddler Ready? 8 Signs of Potty Training Readiness",
  "description": "Not sure if your toddler is ready for potty training? Learn 8 clear signs of readiness and when to start—plus what to avoid.",
  "image": "https://pottypalai.com/images/blog/potty-training-readiness-8-signs.png",
  "datePublished": "2025-11-05T00:00:00+00:00",
  "dateModified": "2025-11-05T00:00:00+00:00",
  "author": {
    "@type": "Organization",
    "name": "Potty Pal AI"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Potty Pal AI",
    "logo": {
      "@type": "ImageObject",
      "url": "https://pottypalai.com/images/pottypallogolargetransparent.png"
    }
  },
  "articleSection": "Readiness & Starting Out",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://pottypalai.com/blog/potty-training-readiness-8-signs"
  }
}
</script>
```

### 7. Content Structure

#### Heading Hierarchy
- [ ] **One H1 tag** - Main article title
- [ ] **H2 tags** for main sections
- [ ] **H3 tags** for subsections
- [ ] **Proper hierarchy:** H1 > H2 > H3 (never skip levels)

#### Content Quality
- [ ] **Minimum 800 words** (1000+ preferred)
- [ ] **Primary keyword** in first paragraph
- [ ] **Keywords used naturally** throughout (not keyword stuffing)
- [ ] **Internal links** to related blog posts (2-3 minimum)
- [ ] **External links** to authoritative sources (when relevant)
- [ ] **Readable and engaging** content

### 8. Images

#### Featured Image
- [ ] **File format:** WebP (preferred) or PNG
- [ ] **File size:** Under 200KB (optimize if larger)
- [ ] **Dimensions:** 1200x630px for social sharing
- [ ] **Filename:** Descriptive (e.g., `potty-training-readiness-8-signs.png`)
- [ ] **Location:** `images/blog/` directory
- [ ] **Alt text:** Descriptive, includes primary keyword naturally

#### Content Images
- [ ] **All images have alt text**
- [ ] **Alt text is descriptive** (not just "image" or filename)
- [ ] **Images optimized** (WebP format, compressed)
- [ ] **Loading attribute:** `loading="lazy"` for images below the fold

**Example:**
```html
<img src="images/blog/potty-training-readiness-8-signs.png" 
     alt="8 signs your toddler is ready for potty training" 
     loading="lazy" />
```

### 9. Internal Linking

- [ ] **Link to blog index** page
- [ ] **Link to 2-3 related blog posts** within content
- [ ] **Link to relevant category pages**
- [ ] **Link to homepage** (in navigation/footer)
- [ ] **Use descriptive anchor text** (not "click here")

### 10. Sitemap Update

- [ ] **Add entry to `sitemap.xml`**
- [ ] **URL format:** No .html extension (e.g., `https://pottypalai.com/blog/post-slug`)
- [ ] **lastmod date:** Current date (YYYY-MM-DD format)
- [ ] **changefreq:** "monthly" for blog posts
- [ ] **priority:** "0.8" for blog posts

**Example sitemap entry:**
```xml
<url>
  <loc>https://pottypalai.com/blog/potty-training-readiness-8-signs</loc>
  <lastmod>2025-11-05</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```

### 11. Blog Index Update

- [ ] **Add post to `blog/index.html`** posts array
- [ ] **Include:** title, slug, date, excerpt, category, image, imageAlt
- [ ] **Verify post appears** in blog listing

### 12. Performance Check

- [ ] **Page loads quickly** (test on mobile)
- [ ] **Images are optimized** (check file sizes)
- [ ] **No console errors** (check browser DevTools)
- [ ] **Mobile responsive** (test on phone/tablet)

### 13. Final Verification

- [ ] **Preview page** in browser
- [ ] **Check all links** work correctly
- [ ] **Verify meta tags** using [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
- [ ] **Test Twitter Card** using [Twitter Card Validator](https://cards-dev.twitter.com/validator)
- [ ] **Validate structured data** using [Google Rich Results Test](https://search.google.com/test/rich-results)
- [ ] **Spell check** entire content
- [ ] **Proofread** for grammar and clarity

## Quick Reference: Template Locations

- **Blog Post Template:** `blog/post-template.html`
- **Sitemap:** `sitemap.xml`
- **Blog Index:** `blog/index.html`
- **Image Directory:** `images/blog/`

## Common Mistakes to Avoid

❌ **Don't:**
- Use multiple H1 tags
- Skip heading levels (H1 → H3)
- Forget alt text on images
- Use generic meta descriptions
- Forget to update sitemap
- Use .html in canonical URLs
- Make images too large (>500KB)
- Keyword stuff in content
- Use "click here" as anchor text

✅ **Do:**
- Use one H1 per page
- Maintain proper heading hierarchy
- Write descriptive alt text
- Create unique, compelling meta descriptions
- Update sitemap immediately
- Use clean URLs (no .html)
- Optimize all images
- Write naturally for humans first
- Use descriptive anchor text

## Need Help?

- Check existing blog posts for examples
- Review `blog/post-template.html` for structure
- Refer to this checklist for each new post
- Test all changes before publishing
