# Performance Optimization Guide

This guide covers performance best practices for maintaining fast page loads and optimal Core Web Vitals scores.

## Core Web Vitals Targets

- **LCP (Largest Contentful Paint):** < 2.5 seconds
- **FID (First Input Delay):** < 100 milliseconds
- **CLS (Cumulative Layout Shift):** < 0.1

## Image Optimization

### Format Guidelines

**Preferred Format: WebP**
- 30-50% smaller file sizes than PNG/JPEG
- Supported by all modern browsers
- Use PNG as fallback for older browsers

**When to Use Each Format:**
- **WebP** - All images (primary choice)
- **PNG** - Images with transparency, simple graphics
- **JPEG** - Photos (if WebP not available)

### Image Optimization Workflow

1. **Create/Edit Image**
   - Use appropriate dimensions (don't use oversized images)
   - Blog featured images: 1200x630px
   - Logo: Appropriate size for usage

2. **Convert to WebP**
   - Use online tools: [Squoosh](https://squoosh.app/), [CloudConvert](https://cloudconvert.com/)
   - Or command line: `cwebp input.png -q 80 -o output.webp`
   - Quality: 80-85 for photos, 90-95 for graphics

3. **Compress Further**
   - Use [TinyPNG](https://tinypng.com/) or [ImageOptim](https://imageoptim.com/)
   - Target file size: < 200KB for featured images
   - Target file size: < 100KB for content images

4. **Add to Project**
   - Place in `images/blog/` directory
   - Use descriptive filename matching post slug

5. **Implement in HTML**
   ```html
   <!-- Modern browsers: WebP -->
   <picture>
     <source srcset="images/blog/image.webp" type="image/webp">
     <!-- Fallback: PNG -->
     <img src="images/blog/image.png" alt="Descriptive alt text" loading="lazy">
   </picture>
   
   <!-- Or simple (if WebP only) -->
   <img src="images/blog/image.webp" alt="Descriptive alt text" loading="lazy">
   ```

### Image Best Practices

✅ **Do:**
- Use WebP format
- Compress all images
- Add descriptive alt text
- Use `loading="lazy"` for below-the-fold images
- Specify width/height to prevent layout shift
- Use appropriate dimensions (don't scale down large images)

❌ **Don't:**
- Upload images > 500KB
- Use images without alt text
- Use oversized images and scale with CSS
- Load all images immediately (use lazy loading)

## CSS Optimization

### Current Setup

CSS is currently inline in HTML files. For better performance:

### Option 1: External CSS File (Recommended for Production)

1. **Extract CSS to `css/main.css`**
2. **Minify CSS** using [CSS Minifier](https://www.minifier.org/) or build tools
3. **Link in HTML:**
   ```html
   <link rel="stylesheet" href="css/main.css">
   ```

**Benefits:**
- Browser caching (CSS loads once, cached for future visits)
- Smaller HTML files
- Better separation of concerns

**Considerations:**
- First page load may be slightly slower (extra HTTP request)
- Need to ensure CSS loads before content renders

### Option 2: Keep Inline (Current - Good for Small Sites)

**Benefits:**
- No extra HTTP request
- CSS loads with HTML
- Good for small sites with minimal CSS

**Optimization:**
- Minify inline CSS
- Remove unused CSS
- Keep CSS organized

### CSS Minification

Use tools to minify CSS:
- Online: [CSS Minifier](https://www.minifier.org/)
- Build tools: PostCSS, cssnano
- Command line: `cssnano input.css output.css`

**Before:**
```css
.hero-main {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: clamp(2rem, 4.8vw, 3.1rem);
}
```

**After (minified):**
```css
.hero-main{font-family:var(--font-display);font-weight:700;font-size:clamp(2rem,4.8vw,3.1rem)}
```

## JavaScript Optimization

### Current Setup

JavaScript is inline in HTML files. Optimization options:

### Best Practices

1. **Use async/defer attributes**
   ```html
   <!-- Async: Loads in parallel, executes immediately -->
   <script async src="script.js"></script>
   
   <!-- Defer: Loads in parallel, executes after HTML parsed -->
   <script defer src="script.js"></script>
   ```

2. **Minify JavaScript**
   - Use [JavaScript Minifier](https://www.minifier.org/)
   - Or build tools: Terser, UglifyJS

3. **Move to external file** (if script is large)
   - Extract to `js/main.js`
   - Link with async/defer

### Current Scripts Status

✅ **Google Analytics:** Already using `async` (good)
✅ **Facebook Pixel:** Script tag creation uses `async` (good)
⚠️ **Inline scripts:** Consider extracting if they grow large

## Resource Hints

### Preconnect

Establishes early connection to important third-party domains:

```html
<link rel="preconnect" href="https://www.googletagmanager.com" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
```

**When to use:**
- External fonts (Google Fonts)
- Analytics (Google Analytics)
- Social media (Facebook Pixel)
- CDN resources

### DNS Prefetch

Resolves DNS for external domains:

```html
<link rel="dns-prefetch" href="https://www.googletagmanager.com" />
```

**Use for:**
- Third-party services
- External resources that may load later

## Caching

### Browser Caching

Configure server to set cache headers:

**For static assets (CSS, JS, images):**
```
Cache-Control: public, max-age=31536000
```

**For HTML files:**
```
Cache-Control: public, max-age=3600
```

### Implementation

**Apache (.htaccess):**
```apache
# Cache static assets for 1 year
<FilesMatch "\.(css|js|jpg|jpeg|png|gif|webp|svg)$">
  Header set Cache-Control "public, max-age=31536000"
</FilesMatch>

# Cache HTML for 1 hour
<FilesMatch "\.(html)$">
  Header set Cache-Control "public, max-age=3600"
</FilesMatch>
```

**Nginx:**
```nginx
location ~* \.(css|js|jpg|jpeg|png|gif|webp|svg)$ {
  expires 1y;
  add_header Cache-Control "public, immutable";
}

location ~* \.(html)$ {
  expires 1h;
  add_header Cache-Control "public";
}
```

## CDN (Content Delivery Network)

### Benefits

- Faster global load times
- Reduced server load
- Better reliability

### When to Consider

- Site receives traffic from multiple countries
- Large file sizes (images, videos)
- High traffic volume

### Options

- **Cloudflare** (free tier available)
- **Amazon CloudFront**
- **Google Cloud CDN**

## Performance Testing Tools

### Recommended Tools

1. **Google PageSpeed Insights**
   - URL: https://pagespeed.web.dev/
   - Tests mobile and desktop
   - Provides specific recommendations

2. **GTmetrix**
   - URL: https://gtmetrix.com/
   - Detailed performance metrics
   - Waterfall chart analysis

3. **WebPageTest**
   - URL: https://www.webpagetest.org/
   - Advanced testing options
   - Multiple locations

4. **Chrome DevTools**
   - Built into Chrome
   - Lighthouse tab for performance audit
   - Network tab for resource analysis

### Regular Testing Schedule

- **After major changes:** Test immediately
- **Monthly:** Regular performance check
- **Before launches:** Always test new pages

## Performance Checklist

Use this checklist for all new pages:

### Images
- [ ] Images converted to WebP
- [ ] Images compressed (< 200KB for featured, < 100KB for content)
- [ ] Alt text added to all images
- [ ] Lazy loading for below-the-fold images
- [ ] Appropriate dimensions (not oversized)

### CSS
- [ ] CSS minified (if external)
- [ ] Unused CSS removed
- [ ] Critical CSS inline (if needed)

### JavaScript
- [ ] Scripts use async/defer
- [ ] JavaScript minified
- [ ] No blocking scripts

### Resource Hints
- [ ] Preconnect for external fonts
- [ ] Preconnect for analytics
- [ ] DNS-prefetch for third-party services

### Caching
- [ ] Cache headers configured
- [ ] Static assets cached long-term
- [ ] HTML cached appropriately

### Testing
- [ ] PageSpeed Insights score > 90
- [ ] LCP < 2.5 seconds
- [ ] FID < 100ms
- [ ] CLS < 0.1
- [ ] Tested on mobile device

## Quick Wins

These optimizations provide the biggest impact:

1. **Optimize images** (WebP, compress) - 30-50% size reduction
2. **Add resource hints** - Faster third-party resource loading
3. **Enable caching** - Faster repeat visits
4. **Minify CSS/JS** - Smaller file sizes
5. **Lazy load images** - Faster initial page load

## Maintenance

### Regular Tasks

- **Monthly:** Review PageSpeed Insights scores
- **Quarterly:** Audit and optimize images
- **After updates:** Test performance impact
- **Annually:** Review and update optimization strategy

## Need Help?

- Test with PageSpeed Insights for specific recommendations
- Check browser DevTools for performance bottlenecks
- Review this guide for optimization opportunities
- Consider professional optimization if scores remain low
