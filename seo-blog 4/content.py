# Content for the blog. [[slug|anchor text]] creates an internal link with descriptive anchor text.
# Each post: slug, title (<=60 chars), desc (150-160 chars), main keyword, 2 related keywords,
# image file name, alt text, intro, sections (H2 question, paragraphs). ("ul", [items]) makes a list.

POSTS = [
dict(slug="what-is-seo-beginners-guide", title="What Is SEO? A Simple Beginner's Guide for 2026",
 desc="What is SEO? Learn how search engines crawl, index and rank pages, the main types of SEO and the first steps to get your new website found on Google.",
 kw="what is seo", rel=["seo for beginners", "how search engines work"], img="what-is-seo", icon="search",
 alt="Magnifying glass over a search results page showing ranked pages, illustrating what SEO is",
 intro="SEO, short for search engine optimization, is the practice of improving a website so that search engines like Google can find it, understand it and show it to people searching for related topics. In simple words, SEO helps the right visitors discover your pages without you paying for ads. This guide explains what SEO is, how it works and what a complete beginner should do first.",
 sections=[
 ("What does SEO stand for and why does it matter?", [
  "SEO stands for search engine optimization. It matters because most online journeys begin with a search. When someone types a question into Google, only a handful of results get most of the clicks, so a page that appears on the first page can bring steady, free traffic for months or even years.",
  "Unlike paid ads, which stop the moment your budget ends, good SEO keeps working in the background. A single helpful article can keep answering the same question for thousands of readers. That is why businesses, bloggers and students building portfolios all learn SEO early."]),
 ("How do search engines work?", [
  "Search engines work in three steps: crawling, indexing and ranking. First, automated bots called crawlers follow links across the web to discover pages. Second, the search engine reads each page and stores it in a giant database called the index. Third, when someone searches, the engine picks the indexed pages it believes are most relevant and helpful and orders them in the results.",
  "If a step fails, your page is invisible. A page that cannot be crawled will never be indexed, and a page that is not indexed can never rank. This is why tools like [[google-search-console-guide|Google Search Console]] are so useful: they show you exactly where Google is stuck."]),
 ("What are the main types of SEO?", [
  "There are three main types of SEO, and a healthy website needs a little of each:",
  ("ul", ["On-page SEO: the content, titles, headings, images and links on your pages. Our [[on-page-seo-checklist|on-page SEO checklist]] covers this in detail.",
          "Off-page SEO: signals from outside your site, mostly links from other trusted websites and mentions of your brand.",
          "Technical SEO: how fast, secure and crawlable your site is, including mobile friendliness and [[website-speed-and-core-web-vitals|Core Web Vitals]]."]),
  "Beginners should start with on-page SEO because it is fully in your control and costs nothing."]),
 ("How long does SEO take to work?", [
  "SEO usually takes several weeks to a few months to show results, and longer for competitive topics. A brand new website has no history, so Google needs time to discover it, test it and trust it. Pages that target specific, less competitive phrases tend to rank sooner than pages aimed at very broad keywords.",
  "Be patient and keep publishing. Consistency matters more than any single trick, and you can track progress for free with Search Console once your site is verified."]),
 ("What are the first SEO steps for a new website?", [
  "Start with five simple steps. First, choose one clear topic for the site. Second, do basic [[keyword-research-for-beginners|keyword research]] to learn what people actually search for. Third, write helpful pages that answer one question each and give every page its own title, description and clean URL. Fourth, add descriptive alt text to every image. Fifth, submit your sitemap to Google Search Console so crawlers can find all your pages quickly.",
  "Once these basics are in place, improve one page at a time instead of trying to fix everything at once."]),
 ("What SEO mistakes should beginners avoid?", [
  "The most common mistakes are stuffing the same keyword into every sentence, copying text from other websites, using vague titles such as 'Home' or 'Page 1', forgetting alt text and publishing very thin pages with only a few lines. Google rewards pages that genuinely help the reader, so write for people first and search engines second.",
  "Another mistake is expecting overnight results. Treat SEO like a habit: publish, measure, improve and repeat."]),
 ]),

dict(slug="keyword-research-for-beginners", title="Keyword Research for Beginners: A Step-by-Step Guide",
 desc="Keyword research for beginners made simple. Learn how to find long tail keywords, check search intent and build a keyword map using free tools like Google.",
 kw="keyword research", rel=["long tail keywords", "search intent"], img="keyword-research", icon="tags",
 alt="Search bar surrounded by keyword tags showing how keyword research finds search phrases",
 intro="Keyword research is the process of finding the words and phrases people type into search engines so you can create pages that answer them. It tells you what your audience wants before you write a single paragraph. This step-by-step guide shows beginners how to do keyword research with free tools and turn the results into a simple keyword map.",
 sections=[
 ("What is a keyword in SEO?", [
  "A keyword is a word or phrase that someone types into a search engine, such as 'eggless cakes in Pune' or 'how to store cake'. In SEO, your goal is to match each page on your site with the keyword that best describes what the page offers, so Google knows when to show it.",
  "Every page should have one main keyword and two related keywords. The main keyword is the central topic. Related keywords are close variations that support it and help the page rank for more searches."]),
 ("What are long tail keywords and why are they better for beginners?", [
  "Long tail keywords are longer, more specific search phrases, usually three words or more, like 'free ai tools for students'. They get fewer searches than short phrases, but they face far less competition and the people searching them know exactly what they want.",
  "A new website will struggle to rank for 'marketing', but it can realistically rank for 'social media marketing for small business'. Start with long tail keywords, win those pages first and move to bigger phrases later."]),
 ("What is search intent and how do you check it?", [
  "Search intent is the reason behind a search. There are three common types: know (the person wants information), do (the person wants to take an action such as ordering or signing up) and compare or buy (the person is choosing between options). Google tries hard to match intent, so your page type must fit it.",
  "To check intent, search your keyword and look at the top results. If they are all how-to guides, write a guide. If they are product pages, a blog post will rarely rank. Matching intent is often the difference between page one and page ten."]),
 ("How do you find keywords for free?", [
  "You can find good keywords without paying for any tool:",
  ("ul", ["Type your topic into Google and note the autocomplete suggestions.",
          "Scroll to the 'People also ask' box and 'Related searches' at the bottom of the results.",
          "Use free tools such as Google Keyword Planner, Google Trends and Ubersuggest to check approximate search volume.",
          "Read the headings of top ranking pages to see how competitors structure the topic."]),
  "Write down five to ten candidates for each page, then pick the clearest one as the main keyword."]),
 ("How do you build a keyword map?", [
  "A keyword map is a simple table that assigns keywords to pages. Create columns for the page, the main keyword, two related keywords, the intent, the approximate monthly search volume and the question the page answers. Fill it for your homepage and each important article.",
  "A keyword map prevents two of your pages from competing for the same phrase and gives you a clear brief before writing. Keep it updated as you add new articles."]),
 ("Where should you place keywords on a page?", [
  "Place the main keyword naturally in the page title, the main heading, the first paragraph, at least one subheading, the URL, the meta description and the image alt text. Use related keywords in other subheadings and body paragraphs. Do not repeat them unnaturally.",
  "After placing keywords, run through the [[on-page-seo-checklist|on-page SEO checklist]] to confirm the page is fully optimized, and read [[how-to-write-blog-posts-that-rank|how to write blog posts that rank]] for the writing side."]),
 ]),

dict(slug="on-page-seo-checklist", title="On-Page SEO Checklist: 10 Fixes for Every Page",
 desc="Use this on-page SEO checklist to fix titles, meta descriptions, headings, URLs, images and links so every page on your website is fully optimized for Google.",
 kw="on-page seo checklist", rel=["meta description", "title tag"], img="on-page-seo-checklist", icon="checklist",
 alt="Checklist document with ticked items illustrating an on-page SEO checklist",
 intro="An on-page SEO checklist is a list of the things you control inside each page that help search engines understand it, such as the title tag, meta description, headings, URL, images and links. Running through the same checklist on every page is the fastest way to improve your rankings. Here are ten fixes to apply to every page you publish.",
 sections=[
 ("What is the ideal title tag?", [
  "The title tag is the clickable headline shown in search results. Keep it under about 60 characters so it is not cut off, put the main keyword near the start and make it clear and specific. Every page needs its own unique title; never reuse the same one across pages.",
  "A good example is 'On-Page SEO Checklist: 10 Fixes for Every Page'. It is short, contains the keyword and promises something concrete."]),
 ("How should you write a meta description?", [
  "A meta description is the short summary shown under the title in search results. Write about 150 to 160 characters, include the main keyword once and describe the benefit of clicking. It does not directly raise rankings, but a strong description increases the number of people who click your result.",
  "Make each meta description unique and written for humans. Avoid generic lines such as 'Welcome to my website'."]),
 ("What makes a good URL?", [
  "A good URL is short, lowercase, uses hyphens between words and includes the main keyword, for example /on-page-seo-checklist. Avoid spaces, capital letters, random numbers and long strings of symbols. Every page must have its own unique URL, and once a page is live you should avoid changing it."]),
 ("How should you use headings?", [
  "Use exactly one H1 per page for the main title, then H2 subheadings for the major sections and H3 for details beneath them. Write H2s as questions where possible, such as 'What is a meta description?', and answer them directly in the first sentence below. This question and answer format helps with answer engine optimization, because AI assistants and Google snippets prefer clear, direct answers."]),
 ("How do you optimize images?", [
  "Images should be small in file size, ideally under 200 KB, so pages load fast. Compress them, give them descriptive file names such as keyword-research.svg instead of image1.png, and always add alt text that describes what the image shows. Alt text helps visually impaired users and lets search engines understand the picture."]),
 ("What is good anchor text for links?", [
  "Anchor text is the clickable words of a link. Use descriptive text that tells readers where the link goes, such as 'our [[keyword-research-for-beginners|keyword research guide]]', instead of vague phrases like 'click here' or 'read more'. Link to related pages on your own site to help visitors and crawlers move around, and make sure every link has anchor text."]),
 ("What else should you check before publishing?", [
  "Before you publish, confirm that the page has one main keyword and two related keywords, that the content fully answers the question, that paragraphs are short, and that the page works on mobile. Then submit or refresh your sitemap in [[google-search-console-guide|Google Search Console]].",
  "If you are new to SEO, start with [[what-is-seo-beginners-guide|our beginner's guide to SEO]] first and come back to this checklist when you publish your next page."]),
 ]),

dict(slug="how-ai-is-changing-digital-marketing", title="How AI Is Changing Digital Marketing in 2026",
 desc="Discover how AI in digital marketing speeds up content creation, ad testing, analytics and support, and how beginners can use it without losing quality.",
 kw="ai in digital marketing", rel=["marketing automation", "ai content creation"], img="ai-in-digital-marketing", icon="chip",
 alt="Glowing AI chip connected to marketing icons showing how AI is changing digital marketing",
 intro="AI in digital marketing means using artificial intelligence tools to research audiences, create content, test ads, analyze data and answer customers faster than manual work allows. It does not replace marketers, but it changes what they spend time on. This guide explains where AI helps most, where it falls short and how beginners can start using it responsibly.",
 sections=[
 ("How is AI used in digital marketing today?", [
  "Marketers use AI for five main jobs: brainstorming ideas and outlines, drafting and editing copy, generating images and short videos, analyzing campaign data and automating routine replies. Tools can summarize a long report in seconds, suggest headline variations and group customers by behavior.",
  "The common thread is speed. Tasks that used to take hours, like researching a topic or writing ten ad variations, now take minutes, which leaves more time for strategy and creativity."]),
 ("Can AI create content that ranks on Google?", [
  "AI can help you create content that ranks, but only when the final result is genuinely helpful. Google has said it rewards quality content however it is produced, and it targets spam. Pages that are generic, copied or filled with errors perform badly whether a human or a machine wrote them.",
  "The best approach is to use AI for outlines and first drafts, then add your own experience, examples and fact checks. Read [[how-to-write-blog-posts-that-rank|how to write blog posts that rank]] to see the structure that works."]),
 ("What is marketing automation and how does AI improve it?", [
  "Marketing automation is software that performs repetitive marketing tasks for you, such as sending a welcome email, scheduling posts or following up with leads. AI makes automation smarter by deciding who should get which message and when, based on past behavior.",
  "For a small business, a simple automation like an instant WhatsApp or email reply to every new enquiry can save hours every week and stop leads from going cold."]),
 ("How does AI help with ads and analytics?", [
  "AI helps advertisers test many versions of an ad quickly, predict which audiences will respond and shift budget to what works. In analytics, AI tools spot trends, flag unusual drops in traffic and explain results in plain language, so you do not need to be a data analyst to understand a dashboard."]),
 ("What are the risks of using AI in marketing?", [
  "The main risks are inaccurate facts, generic writing that sounds like everyone else, copyright confusion with generated images and over-automation that makes customers feel ignored. AI can also repeat bias from its training data.",
  "Reduce these risks by reviewing everything before it goes live, keeping your brand voice, disclosing AI use where required and never publishing statistics you have not verified."]),
 ("How can beginners start using AI in marketing?", [
  "Pick one task and one tool. For example, use an AI assistant to draft blog outlines for a week, then compare the results to your own writing. Explore our list of [[best-free-ai-tools-for-content-creators|best free AI tools for content creators]], and build a small project such as a blog hosted on Vercel by following our [[build-and-host-a-free-website-with-vercel|free hosting guide]]. Hands-on practice teaches more than reading about AI."]),
 ]),

dict(slug="best-free-ai-tools-for-content-creators", title="Best Free AI Tools for Content Creators in 2026",
 desc="Looking for free AI tools for content creators? Compare free AI writing, design, video and research tools that save hours each week on a zero budget.",
 kw="free ai tools for content creators", rel=["ai writing tools", "ai image generator"], img="free-ai-tools", icon="grid",
 alt="Grid of colorful tool tiles representing free AI tools for content creators",
 intro="Free AI tools for content creators are apps that use artificial intelligence to help you write, design, edit video and research ideas without paying a subscription. You do not need a big budget to create professional content, because many tools offer generous free plans. This guide compares the main categories and explains how to choose.",
 sections=[
 ("Which free AI writing tools are worth using?", [
  "General AI assistants are the most useful free writing tools. They can brainstorm topics, outline posts, rewrite clumsy sentences, suggest headlines and summarize research. Free plans usually limit how much you can use per day, which is fine for a beginner publishing a few posts a week.",
  "Always edit the output. Treat the tool as a fast first draft, then add your own examples and fix facts before publishing."]),
 ("What is the best free AI image generator?", [
  "Several tools let you generate images from a text prompt on a free tier, and design platforms such as Canva include AI image features in their free plans. Use them for blog thumbnails, social posts and simple illustrations.",
  "Check the licensing terms before using images commercially, give each image a descriptive file name and add alt text. Compress images before uploading so your pages stay fast, as explained in our guide to [[website-speed-and-core-web-vitals|website speed and Core Web Vitals]]."]),
 ("Are there free AI tools for video and audio?", [
  "Yes. Free video editors now offer automatic captions, background noise removal and clip suggestions, and some tools can turn a script into a short video with a voiceover. These are especially helpful for short-form content on Instagram Reels and YouTube Shorts, where captions improve watch time."]),
 ("Which free tools help with research and SEO?", [
  "For SEO research, combine Google's own free tools with AI. Google Search Console shows what you already rank for, Google Trends shows seasonal interest, and AI assistants can cluster keywords into topics. Our [[keyword-research-for-beginners|keyword research guide]] shows how to combine them step by step."]),
 ("Can AI tools build a website for free?", [
  "Yes. AI studio style tools can generate a complete website from a prompt, and you can publish it for free by pushing the code to GitHub and deploying it on Vercel. We explain every click in [[build-and-host-a-free-website-with-vercel|how to build and host a free website with Vercel]]."]),
 ("How do you choose the right tool?", [
  "Choose by the job, not the hype. List the three tasks that take you the most time, test one free tool for each for a week, and keep only the ones that save real time. Check privacy terms before uploading client or personal information. For the bigger picture, read [[how-ai-is-changing-digital-marketing|how AI is changing digital marketing]]."]),
 ]),

dict(slug="how-to-write-blog-posts-that-rank", title="How to Write Blog Posts That Rank on Google",
 desc="Learn how to write blog posts that rank on Google with a simple structure: pick a keyword, match search intent, use question headings and edit for clarity.",
 kw="how to write blog posts", rel=["blog post structure", "seo copywriting"], img="write-blog-posts", icon="pen",
 alt="Pen writing on a blog page with headings and paragraphs illustrating how to write blog posts",
 intro="Writing a blog post that ranks on Google means choosing a keyword people search for, answering the question clearly and organizing the page so both readers and search engines understand it. You do not need to be a professional writer to do this. Follow this step-by-step method to turn any topic into a helpful, well-structured post.",
 sections=[
 ("How do you choose a blog topic?", [
  "Choose a topic that your audience actually searches for and that you can explain well. Start with [[keyword-research-for-beginners|keyword research]], pick a long tail keyword and check the first page of Google to see what kind of content is ranking. If every result is a list, a list post is the safest format."]),
 ("What is the best blog post structure?", [
  "A reliable blog post structure has five parts: a title containing the main keyword, a short introduction that gives the answer immediately, several H2 subheadings that each answer one question, short paragraphs with examples, and a conclusion with a next step.",
  "Starting with the answer is important. Readers decide within seconds whether to stay, and Google often pulls the opening lines of a section into featured snippets."]),
 ("How long should a blog post be?", [
  "There is no magic word count. A post should be as long as it takes to fully answer the question. For most beginner topics that means roughly 600 to 1,500 words. Thin posts of a few lines rarely rank, while padding with filler hurts readers. Cover the topic completely and stop."]),
 ("How do you write headings and paragraphs for SEO?", [
  "Write H2 headings as questions people would actually ask, such as 'How long does SEO take?', and answer each in the first sentence below. Keep paragraphs to two or four sentences, use simple words and add bullet lists when you have steps or options. This question and answer style is also ideal for answer engine optimization.",
  "Include the main keyword in the title, first paragraph and at least one heading, and use the two related keywords in other sections. Never force them."]),
 ("How do you add images and links?", [
  "Add at least one original or properly licensed image with a descriptive alt text and a small file size. Link to related posts using descriptive anchor text, for example our [[on-page-seo-checklist|on-page SEO checklist]], and to trusted outside sources when you cite a fact. Avoid anchor text such as 'click here'."]),
 ("How do you edit and publish a post?", [
  "Read the post aloud, cut anything that does not help the reader and check facts. Confirm the title, meta description and URL are unique, then publish and submit the page in [[google-search-console-guide|Google Search Console]]. Revisit the post every few months and update outdated information. If you want AI help with drafting, see [[best-free-ai-tools-for-content-creators|our favorite free AI tools]]."]),
 ]),

dict(slug="social-media-marketing-basics", title="Social Media Marketing Basics for Small Business",
 desc="Social media marketing basics for small business: choose the right platform, plan a simple content calendar, use three content pillars and track what works.",
 kw="social media marketing", rel=["social media content calendar", "small business marketing"], img="social-media-marketing", icon="bubbles",
 alt="Overlapping social media speech bubbles with heart and share icons illustrating social media marketing",
 intro="Social media marketing is the use of platforms like Instagram, LinkedIn, YouTube and Facebook to build awareness, earn trust and bring customers to your business. For a small business, the goal is not to be everywhere but to be consistent where your customers already spend time. These basics will help you start without feeling overwhelmed.",
 sections=[
 ("Which social media platform should a small business use?", [
  "Choose the platform where your customers already are. Instagram and YouTube suit visual products like food, fashion and fitness. LinkedIn suits services and business to business offers. Facebook and WhatsApp work well for local communities. Start with one or two platforms and do them well rather than posting everywhere."]),
 ("What should you post on social media?", [
  "Use three content pillars: educate, entertain and sell. Educational posts answer common questions, entertaining posts show personality and behind-the-scenes moments, and selling posts promote an offer. A good mix is about two educational, one entertaining and one selling post for every four posts.",
  "Each post should have one clear idea, a strong first line and a simple call to action."]),
 ("How do you build a social media content calendar?", [
  "A social media content calendar is a simple schedule of what you will post and when. Open a spreadsheet, list the days of the week, assign a content pillar to each day and write the post idea next to it. Aim for three to five posts per week to begin. Batch your work by creating a week of posts in one sitting so you never scramble for ideas."]),
 ("How does social media connect with SEO?", [
  "Social posts do not directly raise rankings, but they bring visitors, build brand searches and help new pages get discovered. Share each new blog post from your profiles and link to it with descriptive text. For example, you could share our [[how-to-write-blog-posts-that-rank|guide to writing blog posts that rank]] and reuse its main points as posts."]),
 ("How do you measure social media results?", [
  "Track reach, saves, shares, comments, profile visits and link clicks, not just likes. Saves and shares show that content is genuinely useful. Review your numbers every two weeks, repeat the formats that perform well and drop those that do not. Platform insights are free."]),
 ("How can AI help with social media marketing?", [
  "AI tools can suggest post ideas, write caption variations, create simple graphics and schedule content. Use them for first drafts, then add your own voice. Explore our list of [[best-free-ai-tools-for-content-creators|free AI tools for content creators]] and learn the wider context in [[how-ai-is-changing-digital-marketing|how AI is changing digital marketing]]."]),
 ]),

dict(slug="google-search-console-guide", title="Google Search Console Guide: Setup and Sitemap",
 desc="Set up Google Search Console in minutes: add your site, verify ownership, submit your sitemap, request indexing and read the Pages and Performance reports.",
 kw="google search console", rel=["submit sitemap", "index my website"], img="google-search-console", icon="chart",
 alt="Bar chart with rising line representing Google Search Console performance reports",
 intro="Google Search Console is a free tool from Google that shows how your website appears in search, which pages are indexed, which queries bring visitors and which errors need fixing. Every website owner should set it up on day one. This guide walks through adding your site, verifying ownership, submitting your sitemap and reading the key reports.",
 sections=[
 ("What is Google Search Console and why use it?", [
  "Google Search Console is a free service that reports on your site's presence in Google Search. It tells you whether Google can crawl and index your pages, which searches show your site, how many clicks and impressions you receive and whether anything is broken. Without it you are guessing."]),
 ("How do you add your website to Google Search Console?", [
  "Sign in at search.google.com/search-console, click Add property and choose URL prefix. Paste your full website address, including https, and click Continue. URL prefix is simplest for beginners because it supports easy verification methods and matches exactly the address you enter."]),
 ("How do you verify website ownership?", [
  "Google needs proof that the site is yours. The easiest method for a static site is the HTML file method: download the verification file Google gives you, upload it to the root of your website next to index.html, redeploy, and click Verify. Alternatively, copy the HTML tag and paste it inside the head section of your homepage.",
  "Leave the verification file or tag in place permanently, because removing it can un-verify your property."]),
 ("How do you submit a sitemap?", [
  "A sitemap is a file, usually sitemap.xml, that lists the pages you want Google to find. After verification, open Sitemaps in the left menu, type sitemap.xml and click Submit. A status of Success and a count of discovered pages means Google read it correctly. Make sure your robots.txt file also points to the sitemap."]),
 ("How do you ask Google to index a page?", [
  "Paste a full page address into the search bar at the top of Search Console to open URL Inspection, then click Request indexing. New properties have small daily quotas, so if you see 'Quota exceeded', try again the next day. Your sitemap still lets Google discover pages on its own; requesting indexing just speeds it up."]),
 ("Which reports should beginners check first?", [
  "Check the Pages report to see which URLs are indexed and why others are not, the Sitemaps report for submission status and the Performance report for clicks, impressions and the queries that find you. Expect data to appear after several days. Use what you learn to improve titles and content with our [[on-page-seo-checklist|on-page SEO checklist]], and review [[what-is-seo-beginners-guide|the basics of SEO]] if any term is unfamiliar."]),
 ]),

dict(slug="website-speed-and-core-web-vitals", title="Website Speed and Core Web Vitals Explained",
 desc="Understand Core Web Vitals and website speed: what LCP, INP and CLS mean, how to test your pages and simple ways to make your website load faster.",
 kw="core web vitals", rel=["website speed", "improve page speed"], img="core-web-vitals", icon="gauge",
 alt="Speedometer gauge pointing to fast representing website speed and Core Web Vitals",
 intro="Core Web Vitals are three measurements Google uses to judge how fast, responsive and visually stable a web page feels to real visitors. Fast pages keep readers happy and are a small but real ranking factor. This guide explains each metric in plain language and shows simple ways to improve your website speed.",
 sections=[
 ("What are Core Web Vitals?", [
  "Core Web Vitals are Google's key page experience metrics: Largest Contentful Paint (LCP), Interaction to Next Paint (INP) and Cumulative Layout Shift (CLS). Together they describe how quickly the main content loads, how fast the page reacts when someone taps or clicks and how stable the layout is while loading."]),
 ("What is LCP and what is a good score?", [
  "Largest Contentful Paint measures how long the biggest visible element, usually a hero image or large heading, takes to appear. Google considers an LCP of 2.5 seconds or less good. Big uncompressed images are the most common cause of a slow LCP."]),
 ("What are INP and CLS?", [
  "Interaction to Next Paint measures how quickly the page responds after a user interaction; 200 milliseconds or less is considered good. Cumulative Layout Shift measures unexpected movement, like a button jumping down just as you try to tap it; a score of 0.1 or less is good. Setting image width and height prevents most layout shifts."]),
 ("How do you test your website speed?", [
  "Use PageSpeed Insights, a free Google tool. Paste your page address and it reports your Core Web Vitals and lists the fixes that would help most. Search Console also has a Core Web Vitals report once your site has enough visitors. Test on mobile first, since most searches happen on phones."]),
 ("How can you improve page speed?", [
  "Start with the biggest wins:",
  ("ul", ["Compress images and keep each one small, ideally under 200 KB.",
          "Use modern formats such as WebP or lightweight SVG illustrations.",
          "Set width and height on images so the layout does not jump.",
          "Remove scripts and plugins you do not need.",
          "Host on a fast network, such as Vercel's global edge."]),
  "Our [[best-free-ai-tools-for-content-creators|free AI tools]] include image compressors that make this easy."]),
 ("Does hosting on Vercel help with speed?", [
  "Yes. Static sites on Vercel are served from a global network close to your visitors, which keeps loading times low by default. Follow our guide to [[build-and-host-a-free-website-with-vercel|building and hosting a free website with Vercel]] and then check your results in [[google-search-console-guide|Google Search Console]]."]),
 ]),

dict(slug="build-and-host-a-free-website-with-vercel", title="Build and Host a Free Website with Vercel",
 desc="How to host a website on Vercel for free: generate the code with AI, push it to GitHub, deploy on Vercel and register your site in Google Search Console.",
 kw="host a website on vercel", rel=["deploy a website from github", "free website hosting"], img="host-website-vercel", icon="rocket",
 alt="Rocket launching from a cloud with an upload arrow showing how to host a website on Vercel",
 intro="You can host a website on Vercel for free by generating the code with an AI tool, pushing it to a GitHub repository and importing that repository into Vercel. The whole process takes less than an hour and gives you a live link with HTTPS. This guide covers every step, from the first prompt to registering your site on Google.",
 sections=[
 ("What is Vercel and is it really free?", [
  "Vercel is a hosting platform that publishes websites straight from a GitHub repository. Its Hobby plan is free for personal, non-commercial projects, which makes it ideal for portfolios, class assignments and small blogs. Choose the Hobby option when you sign up so you are not moved onto a paid trial."]),
 ("How do you generate a website with AI?", [
  "Open an AI studio tool, describe the website you want, such as a blog with ten articles, and ask for plain HTML and CSS with every file in one folder. Tell the tool the main keyword and two related keywords for each page so titles and headings are optimized from the start."]),
 ("How do you push the code to GitHub?", [
  "Create a free GitHub account, click New repository, give it a lowercase name, keep it public and create it. Then upload your files or use the push option in your AI studio's settings. Make sure index.html sits at the top level of the repository, not inside a subfolder, or Vercel will show a 404 error."]),
 ("How do you deploy on Vercel?", [
  "Sign in at vercel.com with GitHub, click Add New then Project, select your repository and click Import. Set the Application Preset to Other, leave the build settings empty and click Deploy. After about thirty seconds you receive a link ending in .vercel.app. Every time you push a change to GitHub, Vercel redeploys automatically."]),
 ("What should you do after the site is live?", [
  "Replace placeholder web addresses in your sitemap, robots.txt and canonical tags with your real Vercel link, upload the changes and then register the site in Search Console. Our [[google-search-console-guide|Google Search Console guide]] shows how to verify ownership and submit your sitemap."]),
 ("How do you fix common Vercel errors?", [
  "Most deployment problems are simple: files uploaded inside a subfolder, capital letters in file names, a missing index.html or a project name that is not lowercase. Copy the error text from the build log and paste it into an AI assistant for a fix. Then improve your pages using the [[on-page-seo-checklist|on-page SEO checklist]] and keep your pages quick with tips from [[website-speed-and-core-web-vitals|our website speed guide]]."]),
 ]),
]

HOME = dict(
 title="Digital Marketing for Beginners: SEO and AI Guides",
 desc="Digital marketing for beginners made simple. Read 10 long, practical guides on SEO basics, keyword research, AI marketing tools, blogging and hosting a website.",
 kw="digital marketing for beginners", rel=["seo basics", "ai marketing tools"],
 h1="Digital Marketing for Beginners",
 intro="Digital marketing for beginners starts with understanding how people find things online. The AI Marketing Playbook gives you ten long, practical guides on SEO basics, keyword research, AI marketing tools, blogging, social media and hosting your own website, all written in simple language with step-by-step answers.",
 faqs=[
  ("What will I learn from these guides?", "You will learn how search engines work, how to research keywords, how to optimize every page, how to use AI tools safely and how to publish a free website that Google can find. Start with [[what-is-seo-beginners-guide|what SEO is]] if you are new."),
  ("Which guide should I read first?", "Read the SEO beginner's guide first, then [[keyword-research-for-beginners|keyword research for beginners]] and the [[on-page-seo-checklist|on-page SEO checklist]]. Together these three explain the foundations of getting found on Google."),
  ("Are these guides free?", "Yes. Every article is free to read, and the tools we recommend, from Google Search Console to Vercel, have free plans suitable for students and small businesses."),
 ])
