# Vercel Hosting Guide: SEO Internal Project

Site: 10-post blog with images. Already built in this folder (index.html, blog/, images/, sitemap.xml, robots.txt).

## Step 1: Generate the code (done)
If your task needs your own AI prompt, use this one in any AI:

> Build a static blog website with at least 10 blog posts on SEO and digital marketing. Each post needs its own page, a featured image, a unique title and meta description. Add a homepage grid, dark theme, responsive layout, sitemap.xml and robots.txt. Output plain HTML, CSS and images, no frameworks.

## Step 2: Replace stock images with your own photos
1. Put 10 photos in the `images/` folder named `post-1.jpg` ... `post-10.jpg`.
2. Run: `python build.py jpg https://YOUR-SITE.vercel.app`
   (use your real Vercel URL once you have it, otherwise run it once now and again after deploy).
3. Or, in Google AI Studio: paste the code, ask it to "replace image paths with my local images", and download the result.
Tip: keep each image under 300 KB (compress at squoosh.app) for faster loading.

## Step 3: Push to GitHub
1. Create a free account at github.com.
2. Click **New repository**, name it `seo-blog`, keep it Public, click Create.
3. Click **uploading an existing file**, drag in ALL files and folders from this project (index.html, style.css, blog, images, sitemap.xml, robots.txt), click **Commit changes**.
   (Command line alternative: `git init`, `git add .`, `git commit -m "first"`, `git remote add origin <repo-url>`, `git push -u origin main`.)

## Step 4: Connect to Vercel
1. Go to vercel.com, click **Sign Up**, choose **Continue with GitHub**.
2. Click **Add New > Project**, find `seo-blog`, click **Import**.

## Step 5: Publish
1. Framework Preset: **Other**. Leave Build Command and Output Directory empty.
2. Click **Deploy**. In about 30 seconds you get a link like `https://seo-blog-xyz.vercel.app`.
3. Open the link and click through all 10 posts to check images.

## Step 6: Fix your real URL (important for SEO)
1. Run `python build.py jpg https://seo-blog-xyz.vercel.app` (your actual link).
2. Upload the changed files to GitHub. Vercel redeploys automatically.
3. Check `your-url/sitemap.xml` and `your-url/robots.txt` open correctly.

## Step 7: Register in Google Search Console
1. Go to search.google.com/search-console and sign in.
2. **Add property > URL prefix**, paste your full Vercel URL.
3. Verify with the **HTML tag** method: copy the meta tag, add it inside `<head>` of `index.html`, push to GitHub, wait for redeploy, click **Verify**.
4. Open **Sitemaps**, enter `sitemap.xml`, click **Submit**.
5. Use **URL Inspection**, paste your homepage URL, click **Request indexing**.
6. Check back in 2 to 7 days for indexing and impressions.

## If you get an error
- Copy the full error text from the Vercel build log (Deployments > click failed build > Logs).
- Paste it into AI Studio or any AI with: "Fix this Vercel deployment error for a static HTML site".
- Common fixes: 404 means `index.html` must be in the repo root (not inside a subfolder); broken images mean filenames are case sensitive (`post-1.jpg` not `Post-1.JPG`).

## Submission checklist
- [ ] 10 posts live with images
- [ ] Vercel URL works
- [ ] Sitemap submitted in Search Console
- [ ] Screenshots of: Vercel deployment, GitHub repo, Search Console property
