Write, image, publish, and push a complete Potty Pal blog post. Fully automated end-to-end.

**Topic:** $ARGUMENTS

If $ARGUMENTS is empty or says "auto", pick the next available topic from `.claude/topics.md` (first unchecked `[ ]` item).

---

## PHASE 1: TOPIC SELECTION & RESEARCH

1. **If no topic given**, read `.claude/topics.md` and pick the first `[ ]` topic. Mark it `[~]` (in progress).

2. **Research the topic** using WebSearch. Search 3-5 angles: pediatric guidance, parent forums, competing blog posts, age-specific advice, and common myths. Get real data, real scenarios, real ages. No generic filler.

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

9. **Generate a hero image** using Gemini (google-genai Python library):
   - First, ensure the library is installed: `pip install google-genai` (skip if already installed)
   - Ask the user for their Gemini API key if not found in environment variables (GEMINI_API_KEY)
   - Use `google.genai.Client` with model `gemini-2.0-flash-exp-image-generation`
   - **Prompt:** "Pixar-style 3D cartoon illustration of [scene directly related to the post topic]. Cute, colorful, warm lighting, expressive characters, clean background. No text, no logos."
   - Set `config=types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"])`
   - Extract the image from `response.candidates[0].content.parts`, find the part with `inline_data`, and save the raw bytes
   - **Resize using crop-to-fit (NEVER force-stretch):**
     1. Open image with Pillow, convert to RGB
     2. Calculate scale factor to fit **width** first: `scale = 1200 / img.width`
     3. Resize maintaining aspect ratio: `(1200, int(img.height * scale))` with `Image.LANCZOS`
     4. If resized height < 675, recalculate using height instead: `scale = 675 / img.height`, resize to `(int(img.width * scale), 675)`, then center-crop width
     5. Center-crop to exactly 1200x675 (16:9): `top = (h - 675) // 2; img.crop((left, top, left + 1200, top + 675))`
     6. Save as WebP (quality=85) to `images/blog/<slug>.webp`
   - This ensures no distortion regardless of source image dimensions

## PHASE 4: QUALITY CHECKS

Run all checks BEFORE publishing. Fix any issues and recheck until everything passes.

### Step 10: Word Count & Readability

Use the **`word-stats`** skill on the post content (strip HTML tags first) to confirm:
- Standard posts hit 1,000-1,500 words
- In-depth posts hit 1,500-2,000 words
- Quick posts hit 600-900 words

Then use the **`readability`** skill to verify:
- Flesch-Kincaid grade level is between 5-8 (parents reading on their phones at 2 AM)
- If grade level is above 8, simplify long sentences and recheck

### Step 11: AI Detection & Humanization

Use the **`detect-ai`** skill on the post content. This returns a 0-100 AI detection score.
- **Score 0-30:** Pass. Move on.
- **Score 31-50:** Borderline. Use the **`humanizer`** skill to rewrite flagged sections, then re-run `detect-ai` to confirm the score dropped below 30.
- **Score 51+:** Fail. Use the **`humanizer`** skill on the full post, then re-run `detect-ai`. If still above 30, manually rewrite the worst sections.

After humanization (if needed), scan for banned words from voice-profile.md.

### Step 12: SEO Audit

Use the **`seo-audit`** skill on the HTML content. Verify:
- Meta description is under 160 characters
- Heading structure is valid (one H1, H2s for sections, H3s under H2s only)
- Primary keyword appears in the first paragraph
- At least 2 internal links exist
- Featured image alt text is descriptive
- No broken internal links

### Step 13: GEO / AI Search Optimization

Use the **`ai-seo`** skill on the post content to check AI citation readiness:
- At least 2 paragraphs contain direct-answer statements an AI search engine could extract
- Post includes specific ages, timeframes, or statistics (not vague generalities)
- Content is structured with clear H2 question/topic headers that AI can parse
- FAQ section present with real parent questions

### Step 14: Fix & Recheck Loop

If any check from Steps 10-13 failed:
- Fix the issue in the post content
- Re-run the failed check to confirm it passes
- Repeat until all checks pass

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
    - **Verify related post image filenames** by checking what actually exists in `images/blog/` with Glob. Do NOT guess filenames — use the real file that exists on disk.
    - Update the CTA section heading and description (vary from other posts)
    - **Store picker modal:** The download button must show both App Store and Play Store on desktop (not default to one store). Include the `trackAndNavigate()`, `showStorePicker()`, `closeStorePicker()` functions and the `storePicker` modal HTML before `</body>`. The `handleDownloadClick()` must call `showStorePicker()` when `storeLink === 'both'`. Copy this exactly from `blog/post-template.html`.

## PHASE 6: UPDATE SITE FILES

17. **Update `sitemap.xml`:**
    - Add a new `<url>` entry for the blog post
    - Use format: `https://www.pottypalai.com/blog/<slug>.html`
    - Set lastmod to today's date
    - Set changefreq to "monthly" and priority to "0.8"

18. **Update `blog/index.html`:**
    - Add a new **hardcoded HTML post card** inside the `<div class="posts-container" id="postsGrid">` element, BEFORE the first existing card
    - Also add the post to the `const blogPosts = [...]` JavaScript array at the top
    - The HTML card is what actually displays on the page (the JS array is not rendered by default)
    - Match the exact HTML structure of existing cards (a.post-card > img.post-card-image + div.post-card-content)
    - Place it at the top (newest first)

19. **Update the relevant category page** (`blog/category/<category-slug>.html`):
    - Add a new **hardcoded HTML post card** inside the `<div class="posts-container" id="postsGrid">` element, BEFORE existing cards
    - Also add the post to the `const blogPosts = [...]` JavaScript array at the top
    - Same HTML card structure as blog/index.html

20. **Update topics queue** (if topic came from `.claude/topics.md`):
    - Change the topic from `[~]` to `[x]`

## PHASE 7: COMMIT AND PUSH

21. **Stage and commit:**
    - `git add blog/<slug>.html images/blog/<slug>.webp sitemap.xml blog/index.html blog/category/<category-slug>.html`
    - Also add .claude/topics.md if it was modified
    - Commit message: "Add blog post: <post-title>"
    - `git push origin master`

22. **Report what was done:**
    - Post title and slug
    - Category
    - Word count and readability grade
    - AI detection score
    - Image filename
    - Commit hash
    - URL: `https://www.pottypalai.com/blog/<slug>.html`
