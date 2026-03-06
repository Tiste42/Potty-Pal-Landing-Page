# Potty Pal Blog Style Guide

## Voice Baseline
Warm, honest, practical. Parent-to-parent energy. See `voice-profile.md` for full tone rules.
- Always use contractions. Short paragraphs. No paragraphs over 4 sentences.
- Never use banned words (delve, landscape, leverage, unleash, comprehensive, robust, etc.).
- Never use em dashes.
- Author: "Potty Pal AI" on all posts.

## Heading Structure
- **H1:** Post title only. One per post.
- **H2:** Major sections. Use keyword-rich, conversational phrasing. No generic labels like "Introduction."
- **H3:** Subsections under H2s. Use for breakdowns or lists that need a label.
- **No H4+.** If you need that depth, restructure.

## Post Length
- **Standard posts** (tips, guides, how-tos): 1,000-1,500 words.
- **In-depth posts** (research-backed, multi-strategy): 1,500-2,000 words.
- **Quick posts** (seasonal, situational): 600-900 words.

## Post Structure

### Standard Posts
1. Relatable opening (put the parent in the moment)
2. Core insight (what they need to know)
3. Practical strategies with specific tips
4. Reassurance section (normalize the struggle)
5. Key Takeaways (bulleted, scannable)
6. Natural CTA to download Potty Pal (woven in, not bolted on)

### Situational Posts (travel, daycare, new sibling, etc.)
1. Scene-setting (the specific situation)
2. Why this situation is tricky
3. Step-by-step strategies
4. What to expect (realistic timeline)
5. Key Takeaways

## Key Takeaways Section
- Place near the end, before any closing CTA.
- Use an H2: "Key Takeaways"
- 3-5 bullet points. Each bullet is one clear, actionable sentence.
- No filler bullets. Every point should be something the parent can do today.

## Image Requirements
- **Hero image:** One per post. WebP preferred. Stored in /images/blog/. 16:9 aspect ratio.
- **Style:** Soft faded watercolor illustration on textured paper. Thin delicate line work, NOT thick outlines. Muted washed-out earth tones (faded browns, soft creams, dusty teal, pale yellows). Colors should bleed and fade like real watercolor on paper. Visible paper grain texture. Realistic toddler and parent proportions with gentle expressive faces. Detailed but soft backgrounds showing home environments with furniture, toys, books. Natural diffused lighting. Must look hand-painted, NOT digital illustration. No text, no logos, no real photographs.
- **Prompt template:** "Soft faded watercolor illustration on textured paper of [scene related to post topic]. Thin delicate line work, NOT thick outlines. Muted washed-out earth tones — faded browns, soft creams, dusty teal, pale yellows. Colors should bleed and fade like real watercolor on paper. Visible paper grain texture. Realistic toddler and parent proportions with gentle expressive faces. Detailed but soft background — home environment with furniture, toys, books. Natural diffused lighting. Must look hand-painted, NOT digital illustration. No text, no logos. Reference: classic children's picture book watercolor art."
- **Alt text:** Descriptive and specific. Not "potty training" but "toddler sitting on a small potty chair with a proud expression."

## Internal Linking
- Every post links to at least 2 other Potty Pal pages (other blog posts, homepage sections, products page).
- Link with descriptive anchor text, not "click here."
- Prioritize linking to: homepage (#how, #pricing, #faq sections), products page, related blog posts.
- New posts should link to related older posts. Update older posts to link back when relevant.

## CTA Rules
- No dedicated CTA sections with hard sells.
- Use the existing CTA box in the template (it's already styled).
- Vary the CTA heading and description every post.
- Frame helpfully: "That's exactly what Potty Pal helps with" not "Download our amazing app."
- Skip modifying the CTA if the default works fine for the post.

## Related Posts
- Include 2-3 related posts in the relatedPosts JavaScript array.
- Choose posts from the same or adjacent categories.
- Fill in: title, slug (no .html), date (YYYY-MM-DD), image filename, descriptive alt text.

## Post File Checklist
When creating a new blog post:
1. Copy blog/post-template.html to blog/<slug>.html
2. Fill in all SEO meta tags (title, description, keywords, OG, Twitter, canonical)
3. Fill in JSON-LD structured data
4. Write article content between <!-- START CONTENT HERE --> and <!-- END CONTENT HERE -->
5. Update breadcrumb with correct category
6. Set featured image src and alt text
7. Fill in relatedPosts array
8. Update sitemap.xml with new URL and date
9. Update blog/index.html to include the new post card
10. Update the relevant category page to include the new post card

## Formatting Rules
- Use <strong> for emphasis, not ALL CAPS
- Use <ul> or <ol> for lists, not dash-separated paragraphs
- One space after periods
- Numbers under 10 spelled out in prose, digits for ages and statistics
- Use "2- to 3-year-old" not "2-3 year old" in running text
