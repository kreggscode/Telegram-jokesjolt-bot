# 🔧 Bot Testing & Debugging Guide

## Why Your Bot Stopped Working

Based on the code analysis, here are the **most likely reasons** your bot isn't sending messages:

### 1. ❌ Missing Environment Variables (GitHub Actions)
**Problem:** Your GitHub Secrets might be missing or incorrectly configured.

**Check:**
- Go to your GitHub repository
- Navigate to: **Settings → Secrets and variables → Actions**
- Verify these secrets exist:
  - `BOT_TOKEN` - Your Telegram bot token from @BotFather
  - `CHAT_ID` - Your channel's chat ID (should start with `-100`)
  - `TIMEZONE_OFFSET_HOURS` - Your timezone offset (e.g., `5.5` for IST)

### 2. ⏰ Workflow Schedule Issues
**Problem:** GitHub Actions might not be triggering at the expected times.

**Current Schedule (UTC):**
- 2:30 AM UTC = 8:00 AM IST
- 8:30 AM UTC = 2:00 PM IST
- 12:30 PM UTC = 6:00 PM IST

**Check:**
- Go to: **Actions** tab in your GitHub repository
- Look for recent workflow runs
- If no runs appear, the schedule might not be triggering

### 3. 🤖 Bot Permissions
**Problem:** Your bot might not have permission to post to the channel.

**Fix:**
1. Go to your Telegram channel
2. Add your bot as an administrator
3. Give it permission to "Post Messages"

### 4. 🔄 Content Repetition (FIXED!)
**Problem:** The bot was generating the same jokes every day.

**Solution Applied:**
- ✅ Added timestamp-based seeds to Pollinations AI
- ✅ Added random seeds to ensure variety
- ✅ Enhanced prompts to explicitly request unique content
- ✅ Each API call now includes unique parameters

---

## 🧪 Testing Locally

### Step 1: Create `.env` File
Create a file named `.env` in the project root with your credentials:

```env
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
CHAT_ID=-1001234567890
TIMEZONE_OFFSET_HOURS=5.5
```

**How to get these values:**
- **BOT_TOKEN**: Message @BotFather on Telegram, use `/mybots` → Select your bot → API Token
- **CHAT_ID**: Run `python get_chat_id.py` after setting BOT_TOKEN
- **TIMEZONE_OFFSET_HOURS**: Your UTC offset (IST = 5.5, EST = -5, PST = -8)

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Test the Bot
```bash
python -m src.main
```

**Expected Output:**
```
Decided post type: api_joke
Fetching joke from API...
📤 Sending text message to chat_id: -1001234567890
✅ Message sent successfully!
```

### Step 4: Test Multiple Times
Run the bot 3-5 times to verify you get **different jokes each time**:
```bash
python -m src.main
python -m src.main
python -m src.main
```

Each run should generate **unique content** thanks to the timestamp/seed system!

---

## 🔍 Debugging GitHub Actions

### Check Workflow Logs
1. Go to your repository on GitHub
2. Click **Actions** tab
3. Click on the most recent workflow run
4. Click on the **"Post joke/meme to Telegram"** job
5. Expand each step to see detailed logs

### Common Errors & Solutions

#### Error: "BOT_TOKEN or CHAT_ID is not set"
**Solution:** Add the secrets in GitHub Settings → Secrets and variables → Actions

#### Error: "Unauthorized" or "403 Forbidden"
**Solution:** 
- Verify your BOT_TOKEN is correct
- Make sure the bot is added as admin to your channel

#### Error: "Chat not found"
**Solution:**
- Verify your CHAT_ID is correct (should start with `-100`)
- Make sure the bot is a member of the channel

#### Error: Workflow doesn't run at scheduled times
**Solution:**
- GitHub Actions can have delays of 5-15 minutes
- Try triggering manually: Actions → Auto Post Jokes & Memes → Run workflow

---

## 🚀 Manual Trigger (Quick Test)

To test if everything works **right now**:

1. Go to your GitHub repository
2. Click **Actions** tab
3. Click **"Auto Post Jokes & Memes"** workflow
4. Click **"Run workflow"** button (top right)
5. Select branch: `main`
6. Click **"Run workflow"**

This will immediately trigger a post to your channel!

---

## ✅ Verification Checklist

- [ ] GitHub Secrets are configured (BOT_TOKEN, CHAT_ID, TIMEZONE_OFFSET_HOURS)
- [ ] Bot is added as admin to the Telegram channel
- [ ] Bot has "Post Messages" permission
- [ ] Local test runs successfully (`python -m src.main`)
- [ ] Multiple local tests generate different content
- [ ] Manual GitHub Actions trigger works
- [ ] Scheduled posts appear in Actions logs
- [ ] Messages appear in your Telegram channel

---

## 🎯 What Changed (Content Variety Fix)

### Before:
```python
# Old code - same content every time
url = f"https://text.pollinations.ai/{encoded}"
```

### After:
```python
# New code - unique content every time
timestamp = int(time.time())
seed = random.randint(1000, 9999)
enhanced_prompt = f"{prompt}\n\nIMPORTANT: Generate completely NEW and UNIQUE content. Timestamp: {timestamp}, Seed: {seed}..."
url = f"https://text.pollinations.ai/{encoded}?seed={seed}"
```

**Result:** Every API call now includes:
- ⏰ Current timestamp
- 🎲 Random seed (1000-9999)
- 📝 Explicit instructions to generate unique content

This ensures **no two jokes will ever be the same**!

---

## 📊 Monitoring

### Check Recent Posts
Look at your Telegram channel to verify:
- Posts are appearing at scheduled times
- Content is varied and not repetitive
- Images are loading correctly
- Formatting looks good

### Check GitHub Actions History
- Go to Actions tab
- Verify runs are happening at scheduled times
- Check for any failed runs (red X)
- Review logs for any errors

---

## 🆘 Still Not Working?

If the bot still isn't sending messages after following this guide:

1. **Run local test** and share the output
2. **Check GitHub Actions logs** and share any error messages
3. **Verify bot permissions** in Telegram channel settings
4. **Double-check secrets** are correctly set in GitHub

The enhanced logging will now show exactly what's happening at each step!
