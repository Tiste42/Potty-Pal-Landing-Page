# Potty Pal SEO & GEO Guidelines

## What GEO Is
Generative Engine Optimization. AI search engines (Perplexity, ChatGPT, Gemini) pull answers from web content. GEO is writing so those engines cite YOU instead of a competitor. For Potty Pal, this means being the definitive source AI models reference for potty training questions.

## Keyword Placement
- **Title (H1):** Primary keyword within the first 60 characters.
- **First 100 words:** Primary keyword appears naturally in the opening paragraph.
- **H2 headings:** Work primary or secondary keywords into at least 2 H2s.
- **Meta description:** Primary keyword included. Don't force it if it kills the hook.
- **URL slug:** Short, keyword-rich, hyphenated. e.g., `/blog/potty-training-regression`
- **Image alt text:** Descriptive, includes relevant keywords naturally.

## Meta Descriptions
- **Length:** 150-160 characters. Google truncates beyond this.
- **Voice:** Second person, empathetic, hook-first. Lead with the parent's problem, not a summary.
- **Format:** One punchy sentence, sometimes two short ones.
- **Examples:**
  - "Your toddler was fully trained and now they're having accidents again. Here's why regression happens and how to fix it."
  - "Poop withholding is more common than you think. Here's what causes it and what actually works."

## Writing for AI Citation (GEO)
AI search engines prefer content that is:
1. **Directly answerable.** Structure content so key claims stand alone as quotable statements. If an AI asks "when should I start potty training," your content should have a clear, extractable answer.
2. **Structured with clear headings.** Use H2s as questions or topic labels. AI parses heading hierarchies to find relevant sections.
3. **Authoritative and specific.** Reference specific ages, timeframes, and research. "Most children show readiness signs between 18 and 24 months" beats "kids are ready at different ages."
4. **FAQ-rich.** Include an FAQs section with 3-5 real questions parents ask. Use FAQ schema markup when possible.
5. **Factually consistent.** Don't contradict yourself across posts. AI models cross-reference. If you say regression is normal in one post, don't frame it as alarming in another.
6. **Source-worthy.** Include original advice, real scenarios, or unique strategies. AI engines deprioritize content that just rephrases what every other parenting blog says.

## Structured Data
Already implemented in post template:
- **Article schema:** Set per-post via JSON-LD in <head>.
- **BreadcrumbList:** In HTML markup (Home > Blog > Category > Post).

To maximize schema value:
- Fill all JSON-LD fields completely for every post.
- Keep dateModified current when updating posts.
- Write FAQs as natural questions, not keyword-stuffed headers.
- Consider adding FAQPage schema for posts with FAQ sections.

## Internal Linking for SEO
- Every post links to 2+ internal pages with descriptive anchor text.
- Pages to link to: homepage (#how, #pricing, #faq), /products.html, related blog posts.
- Use contextual links within paragraphs, not a "Related Links" dump.
- When publishing a new post, update 1-2 older related posts to link to the new one.

## Technical SEO Checklist Per Post
- [ ] Title tag: 50-60 chars including "| Potty Pal AI"
- [ ] Meta description: 150-160 chars with primary keyword
- [ ] Canonical URL set (https://pottypalai.com/blog/<slug>, no .html)
- [ ] OG tags filled (title, description, image, url, type, site_name)
- [ ] Twitter card tags filled
- [ ] JSON-LD Article schema with all fields
- [ ] H1 is the post title (only one H1)
- [ ] H2/H3 hierarchy is valid
- [ ] Primary keyword in first paragraph
- [ ] At least 2 internal links
- [ ] All images have descriptive alt text
- [ ] Featured image is WebP format
- [ ] sitemap.xml updated with new URL
- [ ] blog/index.html updated with new post card
- [ ] Relevant category page updated

## Content Freshness
- Update dateModified when making meaningful edits to existing posts.
- Revisit top-performing posts quarterly to keep information current.
- Outdated parenting content hurts both traditional SEO and AI citation likelihood.
- Check that age recommendations and medical guidance remain current.

## Domain & URL Rules
- Canonical domain: https://pottypalai.com (no www)
- OG/Twitter images: https://www.pottypalai.com/images/blog/
- Blog URLs in sitemap: https://www.pottypalai.com/blog/<slug>.html
- Internal links in HTML: relative paths with .html
