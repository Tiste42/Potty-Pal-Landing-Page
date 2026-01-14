# SEO & Performance Quick Reference

Quick reference guide for maintaining SEO and performance standards.

## ✅ What's Been Optimized

### Homepage (index.html)
- ✅ Meta description added
- ✅ Resource hints (preconnect, dns-prefetch) added
- ✅ Structured data (Organization, SoftwareApplication) added
- ✅ Canonical URL added
- ✅ Proper heading hierarchy (H1, H2)
- ✅ Facebook Pixel already async

### Sitemap
- ✅ Correct domain (pottypalai.com)
- ✅ All blog posts included
- ✅ Proper URL format (no .html for blog posts)
- ✅ Updated lastmod dates

### robots.txt
- ✅ Correct sitemap reference
- ✅ Appropriate disallow rules
- ✅ All important paths allowed

### Blog Post Template
- ✅ Comprehensive SEO comments added
- ✅ Related posts section included
- ✅ All required meta tags documented

## 📋 Quick Checklists

### Adding a New Blog Post

1. **Create HTML file** from `blog/post-template.html`
2. **Fill in all SEO fields** (see `BLOG_POST_SEO_CHECKLIST.md`)
3. **Add to sitemap.xml** (see `SITEMAP_GUIDE.md`)
4. **Add to blog/index.html** posts array
5. **Optimize images** (WebP, compress, alt text)
6. **Test and validate** (see checklist)

### Performance Check

- [ ] Images optimized (WebP, <200KB)
- [ ] All images have alt text
- [ ] PageSpeed Insights score > 90
- [ ] No console errors
- [ ] Mobile responsive

## 🔗 Important URLs

- **Sitemap:** https://pottypalai.com/sitemap.xml
- **Google Search Console:** https://search.google.com/search-console
- **PageSpeed Insights:** https://pagespeed.web.dev/

## 📚 Documentation Files

- **`BLOG_POST_SEO_CHECKLIST.md`** - Complete SEO checklist for blog posts
- **`SITEMAP_GUIDE.md`** - How to update the sitemap
- **`PERFORMANCE_GUIDE.md`** - Performance optimization guide
- **`SEO_QUICK_REFERENCE.md`** - This file (quick reference)

## 🎯 Key Rules to Remember

### URLs
- ✅ Blog posts: `https://pottypalai.com/blog/post-slug` (NO .html)
- ✅ Category pages: `https://pottypalai.com/blog/category/name.html` (WITH .html)
- ✅ Main pages: `https://pottypalai.com/page.html` (WITH .html)

### Meta Tags
- Title: 50-60 characters
- Description: 150-160 characters
- Always include primary keyword

### Images
- Format: WebP (preferred) or PNG
- Size: < 200KB for featured, < 100KB for content
- Always include descriptive alt text
- Use `loading="lazy"` for below-the-fold images

### Structured Data
- Always include Article schema for blog posts
- Use correct date format: YYYY-MM-DDTHH:MM:SS+00:00
- Match canonical URL exactly

## 🚀 Next Steps (Optional Optimizations)

### High Impact
1. **Extract CSS to external file** - Better caching
2. **Convert all images to WebP** - 30-50% size reduction
3. **Add caching headers** - Faster repeat visits

### Medium Impact
4. **Add related posts** to all blog posts
5. **Implement CDN** - Faster global load times
6. **Minify CSS/JS** - Smaller file sizes

See `PERFORMANCE_GUIDE.md` for detailed instructions.

## 🆘 Need Help?

1. Check the relevant documentation file
2. Review existing blog posts for examples
3. Use the checklists in each guide
4. Test with PageSpeed Insights for specific recommendations

## ✅ Verification Checklist

Before publishing any new content:

- [ ] All SEO meta tags filled in
- [ ] Images optimized and have alt text
- [ ] Added to sitemap.xml
- [ ] Canonical URL correct (no .html for blog posts)
- [ ] Structured data complete
- [ ] Internal links added
- [ ] Tested in browser
- [ ] Validated with PageSpeed Insights
- [ ] Checked mobile responsiveness

---

**Last Updated:** January 15, 2025
