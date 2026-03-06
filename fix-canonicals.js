const fs = require('fs');
const path = require('path');
const dir = 'C:/dev/Potty Pal Landing Page/blog';

const posts = [
  'potty-training-fear-rebuild-confidence',
  'potty-training-new-years-resolution',
  'potty-training-regression-preschool',
  'potty-training-airplane-flying',
  'potty-training-accidents-in-public',
  'potty-training-regression-bounce-back',
  'potty-training-readiness-8-signs',
  'poop-withholding-why-it-happens',
  'potty-training-resistance-5-strategies',
  'potty-training-small-spaces',
  'nighttime-potty-training-dry-day-wet-night'
];

posts.forEach(slug => {
  const file = path.join(dir, slug + '.html');
  let html = fs.readFileSync(file, 'utf8');
  const correctUrl = 'https://www.pottypalai.com/blog/' + slug + '.html';

  // Fix og:url
  html = html.replace(
    /property="og:url" content="https?:\/\/(www\.)?pottypalai\.com\/blog\/[^"]+"/,
    'property="og:url" content="' + correctUrl + '"'
  );
  // Fix canonical
  html = html.replace(
    /rel="canonical" href="https?:\/\/(www\.)?pottypalai\.com\/blog\/[^"]+"/,
    'rel="canonical" href="' + correctUrl + '"'
  );

  fs.writeFileSync(file, html, 'utf8');

  // Verify
  const check = fs.readFileSync(file, 'utf8');
  const canon = check.match(/rel="canonical" href="([^"]+)"/);
  const ogurl = check.match(/property="og:url" content="([^"]+)"/);
  console.log(slug + ':');
  console.log('  canonical: ' + (canon ? canon[1] : 'NOT FOUND'));
  console.log('  og:url:    ' + (ogurl ? ogurl[1] : 'NOT FOUND'));
});
