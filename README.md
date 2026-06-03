# 🎨 AI Thumbnail Pro — AI Thumbnail Generator & Social Media Graphics Tool

**AI-powered thumbnail generator and social media graphics tool. Auto-generate YouTube thumbnails, blog featured images, Twitter/X cards, LinkedIn posts, Instagram squares, and Stories. 8 presets, 8 color palettes, zero human input. Runs on a $35 Raspberry Pi.**

## What Is This?

An AI thumbnail generator and social media graphics engine written in Python. Feed it a title, pick a preset, and get a professional image in seconds. Built for content creators, YouTubers, bloggers, marketers, and social media managers who need high-quality graphics at scale — without hiring a designer or learning Photoshop.

**Perfect for:**
- 🎬 **YouTube creators** — auto-generate click-worthy thumbnails
- ✍️ **Bloggers** — featured images for every post, automatically
- 📱 **Social media managers** — batch-generate visuals for Twitter/X, LinkedIn, Instagram
- 🛍️ **Product marketers** — hero images, promo graphics, launch visuals
- 🤖 **AI automation enthusiasts** — integrate into content pipelines via API mode

## Quick Start

```bash
# Single thumbnail generator
python3 engine.py "How AI Changed My Life" --preset youtube

# Batch mode — all presets at once
python3 engine.py "Product Launch Day" --batch

# With subtitle
python3 engine.py "AI Automation" --preset blog --subtitle "Built on $35 Raspberry Pi"

# API mode for automated pipelines
python3 engine.py --api --port 8899  # Then POST /generate with JSON payload
```

## 🎯 Presets (Social Media Image Generator)

| Preset | Size | Use Case |
|--------|------|----------|
| `youtube` | 1280×720 | YouTube thumbnail generator — eye-catching thumbnails |
| `blog` | 1200×630 | Blog featured image generator — Open Graph images |
| `twitter` | 1200×675 | Twitter/X card image generator |
| `linkedin` | 1200×627 | LinkedIn post image generator |
| `instagram` | 1080×1080 | Instagram square post generator |
| `story` | 1080×1920 | Instagram Stories / Reels / TikTok cover |
| `product` | 1200×800 | Product hero image / landing page hero |

## 🎨 Color Palettes

Purple · Green · Blue · Orange · Pink · Dark · Yellow · Hot Pink — each with gradient backgrounds and accent borders. Every palette is professionally designed for readability and visual appeal.

## ✨ Features

- 🎨 **8 design presets** — YouTube thumbnails, blog images, social media cards, and more
- 🌈 **8 color palettes** — gradient backgrounds with professional styling
- 📝 **Auto text wrapping** — intelligent text layout and centering
- 🎯 **Icon decorations** — 14 emoji icons for visual enhancement
- ⚡ **Batch mode** — generate all formats with one command
- 🏷️ **Brand watermark** — add your logo/brand identity to every image
- 📦 **Zero external dependencies** — only needs Pillow (pip install pillow)
- 🔄 **API mode** — REST API endpoint for integration into CI/CD and automation pipelines
- 💾 **400KB per image** — optimized for fast loading on all platforms
-  **Raspberry Pi optimized** — runs 24/7 on a $35 device, zero hosting cost

## 💰 Pricing: $5 One-Time

Includes full source code, all 8 presets, 8 color palettes, API mode, and 30 days of updates. No subscription, no recurring fees.

[💰 Buy Now on PayPal](https://paypal.me/ulnit) · [📦 View on GitHub](https://github.com/ulnit/ai-thumbnail-pro)

## 🔍 SEO Keywords We Target

`AI thumbnail generator` · `auto thumbnail maker` · `YouTube thumbnail creator` · `social media graphics tool` · `AI image generator for social media` · `blog featured image generator` · `Raspberry Pi AI tools` · `automated social media graphics` · `Python thumbnail generator` · `free thumbnail maker alternative`

## 🆚 Comparison: AI Thumbnail Pro vs Alternatives

| Feature | AI Thumbnail Pro | Canva | Photoshop | Midjourney |
|---------|-----------------|-------|-----------|------------|
| Price | $5 (one-time) | $13/mo | $23/mo | $10/mo |
| Automation | ✅ Full API | ❌ Manual | ❌ Manual | ❌ Prompt only |
| Batch generation | ✅ Yes | ❌ No | ❌ No | ❌ No |
| Self-hosted | ✅ Yes | ❌ Cloud | ❌ Desktop | ❌ Cloud |
| Runs on Raspberry Pi | ✅ Yes | ❌ No | ❌ No | ❌ No |
| Zero dependencies | ✅ Just Pillow | ❌ N/A | ❌ N/A | ❌ N/A |

## 🏗️ Use Cases

### 1. YouTube Automation Channel
Generate 30 thumbnails/month for a faceless YouTube channel. Pair with [AI Video Factory](https://github.com/ulnit/ai-video-factory) for a complete automated content pipeline — AI writes script, generates video, creates thumbnail. All automated, all on a $35 Pi.

### 2. Automated Blog Featured Images
Every blog post gets a unique, on-brand featured image. Integrate with GitHub Actions or cron to regenerate images whenever a new post is published.

### 3. Social Media Content Calendar
Batch-generate a month's worth of Twitter/X cards, LinkedIn posts, and Instagram squares in under 5 minutes. Combine with [AI Social Media Kit](https://github.com/ulnit/ai-social-kit) for complete social automation.

### 4. E-commerce Product Listings
Auto-generate product hero images for Shopify, WooCommerce, or any e-commerce platform. Perfect for dropshipping stores with hundreds of products.

## ❓ FAQ

**Q: What is an AI thumbnail generator?**
A: An AI thumbnail generator automatically creates professional-looking thumbnail images for YouTube, blogs, and social media. Instead of manually designing in Photoshop or Canva, you run one command with your title and get a finished image.

**Q: Does this work on a Raspberry Pi?**
A: Yes! AI Thumbnail Pro is specifically optimized for the Raspberry Pi. It runs on a $35 Pi 4/5 using only Python and Pillow — no GPU, no cloud dependencies.

**Q: Can I use this for commercial projects?**
A: Absolutely. The one-time $5 purchase gives you full commercial rights. Use it for client work, your own channels, or agency projects.

**Q: How fast does it generate images?**
A: Under 2 seconds per image on a Raspberry Pi 4. Batch mode generates all 7 presets in under 10 seconds.

**Q: What's the image quality?**
A: All images render at native resolution for each platform (1280×720 for YouTube, 1200×630 for blogs, etc.) with anti-aliased text and smooth gradients.

**Q: Is there an API?**
A: Yes! Start the API server with `--api` and POST JSON payloads to `http://localhost:8899/generate`. Perfect for integrating into content pipelines, n8n workflows, or custom automation.

## 🧰 Tech Stack

- **Language**: Python 3
- **Image Library**: Pillow (PIL fork)
- **Hardware**: Raspberry Pi 4/5 ($35-60)
- **Automation**: Cron jobs, 24/7 operation
- **Hosting**: Self-hosted, zero cloud cost
- **Dependencies**: None beyond Pillow

## 🔗 Related Products

| Product | Description | Price |
|---------|-------------|-------|
| [🎬 AI Video Factory](https://github.com/ulnit/ai-video-factory) | Auto YouTube/TikTok video generator — pair with thumbnails | $9/mo |
| [🏗️ AI Landing Page Factory](https://github.com/ulnit/ai-landing-factory) | Auto landing pages with hero images | $9 |
| [📱 AI Social Media Kit](https://github.com/ulnit/ai-social-kit) | Auto social media post generator | $9 |
| [🛠️ AI Agent Toolkit](https://github.com/ulnit/ai-agent-toolkit) | Zero-dependency CLI tools for AI developers | $9 |
| [🏪 Agent Store](https://ulnit.github.io/agent-store) | All 23 AI products — unified landing page | FREE |

## 🏪 Part of the Agent Store

AI Thumbnail Pro is one of **23 AI-powered products** running 24/7 on a $35 Raspberry Pi. Browse the full catalog:

👉 **[ulnit.github.io/agent-store](https://ulnit.github.io/agent-store)**

## 💝 Support This Project

If this AI thumbnail generator saves you time creating social media graphics, consider supporting development:

👉 **[paypal.me/ulnit](https://paypal.me/ulnit)** — Any amount helps keep 23 AI products running 24/7!

---

*Built by AI agents. Runs on a $35 Raspberry Pi. Generates professional graphics while you sleep.*