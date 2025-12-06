# 🚀 Quick Start Guide - Jokes & Memes Bot

Get your bot up and running in 5 minutes!

## ⚡ Super Quick Setup

### 1. Get Your Bot Token (2 minutes)

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` and follow the instructions
3. Choose a name (e.g., "My Jokes Bot")
4. Choose a username (e.g., "my_jokes_bot")
5. **Copy the bot token** - it looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

### 2. Create Your Channel (1 minute)

1. Create a new Telegram channel (public or private)
2. Add your bot as an **Administrator** with "Post Messages" permission
3. Post any message to your channel

### 3. Get Your Chat ID (1 minute)

1. Visit this URL in your browser (replace `YOUR_BOT_TOKEN`):
   ```
   https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
   ```
2. Look for `"chat":{"id":-100...}` in the response
3. **Copy the chat ID** (including the minus sign!)

### 4. Configure the Bot (30 seconds)

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your credentials:
   ```
   BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
   CHAT_ID=-1001234567890
   TIMEZONE_OFFSET_HOURS=5.5
   ```

### 5. Install & Run (1 minute)

```bash
# Install dependencies
pip install -r requirements.txt

# Test the bot (it will post one joke/meme)
python -m src.main
```

**That's it!** 🎉 Your bot should have posted to your channel!

---

## 🎮 Try Different Features

### Test Automated Posting
```bash
python -m src.main
```
Each run posts one random joke/meme based on current time.

### Test Interactive Chat Bot
```bash
python -m src.chat_bot
```
Then send commands to your bot:
- `/joke` - Get a random joke
- `/dadjoke` - Get a dad joke
- `/techjoke` - Get a programming joke
- `/help` - See all commands

### Test Dashboard (Manual Control)
```bash
cd dashboard
pip install flask
python app.py
```
Open http://127.0.0.1:5000 in your browser.

---

## 🤖 Deploy to GitHub Actions (Auto-posting)

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit - Jokes & Memes Bot"
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### 2. Add GitHub Secrets
1. Go to your repo on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** and add:
   - Name: `BOT_TOKEN`, Value: your bot token
   - Name: `CHAT_ID`, Value: your channel chat ID
   - Name: `TIMEZONE_OFFSET_HOURS`, Value: `5.5` (or your timezone)

### 3. Enable GitHub Actions
1. Go to **Actions** tab
2. Enable workflows if prompted
3. The bot will now post automatically 4-6 times per day!

---

## 📅 Posting Schedule

Once deployed, your bot will automatically post:

| Time | Content Type | Examples |
|------|-------------|----------|
| 7-9 AM | Motivational & Dad Jokes | Start the day with smiles! |
| 10-12 PM | API Jokes & Puns | Fresh jokes from APIs |
| 2-4 PM | Work & Tech Humor | Relatable office humor |
| 6-8 PM | **Memes with Images** | HIGH ENGAGEMENT! 🔥 |
| 9-11 PM | Variety | Random jokes, animals, etc. |
| 11 PM-1 AM | Shower Thoughts | Deep humor |

---

## 🎨 Customize Your Bot

### Change Posting Times
Edit `.github/workflows/auto-post.yml`:
```yaml
schedule:
  - cron: '0 2,7,9,13,16,18 * * *'  # Modify these times
```

### Add More Jokes
Edit `src/jokes_client.py` to add more free joke APIs.

### Change Humor Style
Edit `src/templates.py` to modify AI-generated joke prompts.

### Adjust Schedule Logic
Edit `src/scheduler_logic.py` to change what posts when.

---

## 🔧 Troubleshooting

### Bot not posting?
- Check your `BOT_TOKEN` and `CHAT_ID` in `.env`
- Make sure bot is admin in your channel
- Check bot has "Post Messages" permission

### Getting errors?
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Chat bot not responding?
- Make sure you're sending commands to the bot (not the channel)
- Bot must be running: `python -m src.chat_bot`

### Want to test without posting?
Comment out the `tg.send_text()` lines in `src/main.py` temporarily.

---

## 📊 What Gets Posted?

Your bot will post a mix of:
- ✅ **40%** Real jokes from APIs (dad jokes, puns, programming)
- ✅ **30%** AI-generated humor (work, food, tech, animals)
- ✅ **20%** Visual content (memes with AI-generated images)
- ✅ **10%** Interactive (polls, challenges, threads)

---

## 🎯 Next Steps

1. ✅ Test locally with `python -m src.main`
2. ✅ Try chat commands with `python -m src.chat_bot`
3. ✅ Deploy to GitHub Actions for automation
4. ✅ Customize content to match your style
5. ✅ Share your channel and spread laughter!

---

## 💡 Pro Tips

1. **Peak Engagement**: Evening posts (6-8 PM) are memes with images - highest engagement!
2. **Test First**: Run locally a few times before deploying
3. **Monitor**: Check your channel to see what content performs best
4. **Customize**: Adjust `templates.py` to match your audience's humor
5. **Interact**: Enable chat bot so users can request jokes on-demand

---

## 🆘 Need Help?

- Check `README.md` for detailed documentation
- Check `TRANSFORMATION_SUMMARY.md` for what changed
- All code is well-commented
- Free joke APIs used (no costs!)

---

**Ready to spread some laughter?** 😂🎉

Run `python -m src.main` and watch the magic happen!
