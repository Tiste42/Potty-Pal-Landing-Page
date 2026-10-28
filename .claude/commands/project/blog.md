Generate one complete Potty Pal blog release for the outer publisher. The PowerShell runner integrates catalogs, validates, updates the queue, commits, and pushes. Never commit, push, edit the queue, or modify infrastructure yourself.

**Topic:** $ARGUMENTS

If $ARGUMENTS is empty or says "auto", pick the next available topic from `.claude/topics.md` (first unchecked `[ ]` item).

---

## PHASE 1: TOPIC SELECTION & RESEARCH

1. **If no topic given**, read `.claude/topics.md` and pick the first `[ ]` topic. If there is no unchecked topic, stop with no file changes. Never invent an unapproved topic. Leave queue state to the outer runner; do not edit `.claude/topics.md`.

2. **Research the topic** using WebSearch. Use current primary pediatric guidance (such as AAP/HealthyChildren, NHS, NIDDK) for factual health claims; distinguish everyday coaching from medical diagnosis or treatment. Read the primary source itself with WebFetch, not just search snippets, and include at least one directly relevant source link in the article. Do not promise fixed recovery timelines or blanket rules about diapers. Respect the pediatric source's guidance to assess physical causes and allow a break when needed. Never invent studies, statistics, or outcomes. Get real data, real scenarios, real ages. No generic filler.

3. **Read these files:**
   - `voice-profile.md` (tone, banned words, sentence architecture)
   - `BLOG_STYLE_GUIDE.md` (structure, formatting, CTA rules)
   - `SEO_GUIDELINES.md` (keywords, meta, GEO optimization)

4. **Scan existing blog posts** in `blog/` to check for duplicate topics and avoid repeating CTA phrasing.

## PHASE 2: WRITE THE POST

5. **Classify the post type:**
   - **Standard posts** (tips, guides, how-tos): 1,000-1,500 words.
   - **In-depth posts** (research-backed, multi-strategy): 1,500-2,000 words.
   - **Quick posts** (seasonal, situational): 600-900 words.

6. **Determine the category** (one of): potty-training-tips, common-problems, readiness-starting-out, night-training, regression-setbacks, special-situations.

7. **Write the post following all rules:**
   - Voice: warm, honest, parent-to-parent. See voice-profile.md.
   - Use the correct post structure from the style guide.
   - Include 2+ internal links to other pages (blog posts, homepage sections, products page).
   - Content must be full HTML (not markdown).
   - No em dashes. No banned words. No paragraphs over 4 sentences. Use contractions.
   - At least one specific, actionable tip with a number or timeframe.
   - At least one reassuring moment.
   - Include 3-5 FAQs at the end of the article content (as an H2 "Frequently Asked Questions" section with H3s for each question).

8. **Self-check** (voice verification):
   - Opens with a scenario or relatable moment, never a definition
   - Zero banned words/phrases from voice-profile.md
   - No paragraphs over 4 sentences
   - Short/medium/short rhythm present
   - Contractions used throughout
   - CTA uses unique language not repeated from other posts
   - Reads like advice from a friend, not a textbook or sales page

## PHASE 3: GENERATE HERO IMAGE

9. **Generate a dependable branded hero image** with the local generator:
   - Run `python scripts/generate-blog-hero.py --title "<post title>" --slug "<slug>" --category "<category-slug>" --output "images/blog/<slug>.webp"`.
   - Do not install packages, call an external image API, copy another article's image, or substitute a placeholder.
   - Confirm the command succeeds and the output is a 1200x675 WebP. If it fails, stop and report the failure without publishing or changing the queue.

## PHASE 4: QUALITY CHECKS

Run all checks BEFORE publishing. If any check fails, stop and report the failure; leave the queue unchanged. Do not commit or push a partial or failed release.

### Step 10: Voice and factual review

Check the article directly against voice-profile.md: contractions, concrete advice,
varied sentence length, short paragraphs, no banned phrases or em dashes.
Do not claim an AI-detection score; no external detector is required or installed.
Recheck health claims against the primary sources. Include ordinary signs for
when to contact a pediatrician without diagnosing or prescribing treatment.

### Step 11: SEO Audit

Verify the following directly in the HTML:
- Meta description is under 160 characters
- Heading structure is valid (one H1, H2s for sections, H3s under H2s only)
- Primary keyword appears in the first paragraph
- At least 2 internal links exist
- Featured image alt text is descriptive
- No broken internal links

### Step 12: GEO / AI Search Optimization

Check answer clarity directly in the article:
- At least 2 paragraphs contain direct-answer statements an AI search engine could extract
- Post includes specific ages, timeframes, or statistics (not vague generalities)
- Content is structured with clear H2 question/topic headers that AI can parse
- FAQ section present with real parent questions

## PHASE 5: BUILD THE HTML FILE

Everything has passed quality checks. Now assemble the final HTML.

15. **Read `blog/post-template.html`** to get the exact HTML structure.

16. **Create the blog post HTML file** at `blog/<slug>.html`:
    - Copy the full template structure
    - Fill in ALL meta tags: title, description, keywords, OG tags, Twitter tags, canonical URL
    - Fill in JSON-LD structured data (Article schema with datePublished, dateModified, author, publisher, articleSection)
    - Set the breadcrumb with correct category name and slug
    - Set the article-meta category link and date
    - Set the H1 to the post title
    - Set the featured image src to `../images/blog/<slug>.webp` with descriptive alt text
    - Insert the article content HTML
    - Fill in the relatedPosts JavaScript array with 2-3 related posts
    - **Verify related post image filenames** by checking what actually exists in `images/blog/` with Glob. Do NOT guess filenames â€” use the real file that exists on disk.
    - Update the CTA section heading and description (vary from other posts)
    - **Store picker modal:** The download button must show both App Store and Play Store on desktop (not default to one store). Include the `trackAndNavigate()`, `showStorePicker()`, `closeStorePicker()` functions and the `storePicker` modal HTML before `</body>`. The `handleDownloadClick()` must call `showStorePicker()` when `storeLink === 'both'`. Copy this exactly from `blog/post-template.html`.

## PHASE 6: HAND OFF TO THE OUTER RUNNER

Do not edit sitemap.xml, blog/index.html, any category page, the topic queue, existing articles, memory files, or infrastructure. Do not stage, commit, or push.

The outer runner reads the new article's H1, description, hero alt, category and publication date, inserts catalog entries deterministically, independently validates the whole release, and publishes. The H1 must exactly match the approved queue title. Use today's publication date.

Before handing off, check the new article and its hero image. The full release validator is run by the outer runner after catalog integration, so missing catalog references at this generation stage are expected.

Report the article title/slug, category, word count, primary sources actually read and checks actually completed. Never claim the article is published; that happens in the outer runner.
