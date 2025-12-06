# 🚀 GitHub Deployment Guide

## 📋 Pre-Deployment Checklist

Before pushing to GitHub, make sure:
- [x] ✅ `.gitignore` file exists (protects `.env`)
- [x] ✅ `.env.example` has placeholder values only
- [x] ✅ No hardcoded tokens in code
- [x] ✅ All files use environment variables

---

## 🔐 IMPORTANT: Regenerate Your Bot Token First!

**Your token was exposed in the code, so regenerate it:**

1. Open Telegram → @BotFather
2. Send: `/mybots`
3. Select your bot
4. Click: **API Token**
5. Click: **Revoke current token**
6. Copy the **NEW** token
7. Update your `.env` file:
   ```
   BOT_TOKEN=your_new_token_here
   CHAT_ID=your_chat_id_here
   TIMEZONE_OFFSET_HOURS=5.5
   ```

---

## 📤 Push to GitHub

### Step 1: Initialize Git (if not already done)
```bash
cd "c:\Users\kreg9\Downloads\kreggscode\Anti gravity\bots\telgram bots\Telegram jokes bot"

git init
```

### Step 2: Add Remote Repository
```bash
git remote add origin https://github.com/kreggscode/Telegram-jokesjolt-bot.git
```

### Step 3: Stage All Files
```bash
git add .
```

### Step 4: Commit
```bash
git commit -m "Initial commit: Jokes & Memes Telegram Bot"
```

### Step 5: Push to GitHub
```bash
git branch -M main
git push -u origin main
```

---

## 🔑 Add GitHub Secrets

After pushing, add your secrets:

### Step 1: Go to Repository Settings
1. Open: https://github.com/kreggscode/Telegram-jokesjolt-bot
2. Click: **Settings** (top menu)
3. Click: **Secrets and variables** → **Actions**

### Step 2: Add Secrets
Click **New repository secret** for each:

| Secret Name | Value | Example |
|-------------|-------|---------|
| `BOT_TOKEN` | Your NEW bot token | `1234567890:ABCdef...` |
| `CHAT_ID` | Your channel chat ID | `-1001234567890` |
| `TIMEZONE_OFFSET_HOURS` | Your timezone offset | `5.5` (for IST) |

### Step 3: Verify Secrets
- Go to **Actions** tab
- Secrets should be listed (values hidden)

---

## ⚙️ Enable GitHub Actions

### Step 1: Check Workflow File
The workflow is already in `.github/workflows/auto-post.yml`

### Step 2: Enable Actions
1. Go to **Actions** tab on GitHub
2. If prompted, click **I understand my workflows, go ahead and enable them**

### Step 3: Verify Schedule
Current schedule (6 posts/day):
```yaml
- cron: '30 1,4,8,12,15,17 * * *'
```

Times (UTC → IST):
- 1:30 UTC = 7:00 AM IST
- 4:30 UTC = 10:00 AM IST
- 8:30 UTC = 2:00 PM IST
- 12:30 UTC = 6:00 PM IST (PEAK!)
- 15:30 UTC = 9:00 PM IST
- 17:30 UTC = 11:00 PM IST

---

## 🎯 Recommended: Change to 3 Posts/Day

If you want 3 posts/day instead of 6:

### Edit `.github/workflows/auto-post.yml`

Change this line:
```yaml
- cron: '30 1,4,8,12,15,17 * * *'
```

To this (3 posts/day):
```yaml
- cron: '30 2,6,12 * * *'
```

New schedule:
- 2:30 UTC = 8:00 AM IST (Morning)
- 6:30 UTC = 12:00 PM IST (Lunch)
- 12:30 UTC = 6:00 PM IST (Evening - PEAK!)

---

## 🧪 Test Deployment

### Manual Trigger (Test Before Automation)
1. Go to **Actions** tab
2. Click **Auto Post Jokes & Memes**
3. Click **Run workflow** → **Run workflow**
4. Check your Telegram channel for a post!

### Monitor Runs
- Go to **Actions** tab
- See all workflow runs
- Check logs if something fails

---

## 📊 Posting Frequency Recommendations

### 🏆 Best Practice: 3-4 Posts/Day

**Why?**
- ✅ Keeps audience engaged
- ✅ Doesn't overwhelm followers
- ✅ Each post gets proper attention
- ✅ Prevents unfollows

### 📅 Recommended Schedules:

#### **Option 1: Conservative (3 posts)** ⭐ RECOMMENDED
```
8:00 AM  - Dad Joke/Motivational
2:00 PM  - Work/Tech Humor
6:00 PM  - Meme with Image (PEAK!)
```

Cron: `'30 2,8,12 * * *'`

#### **Option 2: Active (4 posts)**
```
8:00 AM  - Dad Joke
12:00 PM - Work Humor
6:00 PM  - Meme (PEAK!)
10:00 PM - Random Joke
```

Cron: `'30 2,6,12,16 * * *'`

#### **Option 3: Very Active (6 posts)** - Current
```
7:00 AM  - Motivational
10:00 AM - API Jokes
2:00 PM  - Work Humor
6:00 PM  - Memes (PEAK!)
9:00 PM  - Variety
11:00 PM - Shower Thoughts
```

Cron: `'30 1,4,8,12,15,17 * * *'`

### 🎯 My Recommendation:
**Start with 3 posts/day**, then increase if your audience wants more!

---

## 🔧 Troubleshooting

### Bot not posting?
1. Check **Actions** tab for errors
2. Verify secrets are set correctly
3. Check bot is admin in channel
4. Verify bot has "Post Messages" permission

### Workflow not running?
1. Check cron schedule is correct
2. Enable Actions in repository settings
3. Check for YAML syntax errors

### Want to change posting times?
1. Edit `.github/workflows/auto-post.yml`
2. Change cron schedule
3. Commit and push changes

---

## 📝 Quick Reference

### Cron Time Converter (UTC to IST)
IST = UTC + 5:30

| IST Time | UTC Time | Cron Hour |
|----------|----------|-----------|
| 7:00 AM  | 1:30 AM  | 1         |
| 8:00 AM  | 2:30 AM  | 2         |
| 10:00 AM | 4:30 AM  | 4         |
| 12:00 PM | 6:30 AM  | 6         |
| 2:00 PM  | 8:30 AM  | 8         |
| 6:00 PM  | 12:30 PM | 12        |
| 9:00 PM  | 3:30 PM  | 15        |
| 10:00 PM | 4:30 PM  | 16        |
| 11:00 PM | 5:30 PM  | 17        |

### Cron Format
```
'30 2,8,12 * * *'
 │  │  │   │ │ │
 │  │  │   │ │ └─ Day of week (0-6)
 │  │  │   │ └─── Month (1-12)
 │  │  │   └───── Day of month (1-31)
 │  │  └───────── Hours (0-23, UTC)
 │  └──────────── Multiple hours
 └─────────────── Minute (30)
```

---

## ✅ Deployment Complete!

Once you've:
1. ✅ Regenerated bot token
2. ✅ Pushed to GitHub
3. ✅ Added secrets
4. ✅ Enabled Actions
5. ✅ (Optional) Adjusted posting frequency

Your bot will automatically post jokes to your channel! 🎉

---

## 🎯 Next Steps

1. **Monitor first few posts** - Check they're working
2. **Adjust schedule** if needed
3. **Track engagement** - See which jokes perform best
4. **Customize templates** - Match your audience's humor
5. **Enjoy!** Your bot is spreading laughter! 😂

---

**Questions?** Check the other documentation files:
- `README.md` - Full documentation
- `QUICK_START.md` - 5-minute setup
- `SECURITY_AUDIT.md` - Security info
- `FINAL_SUMMARY.md` - Complete overview
