# 🚀 Cryptocurrency Bot - Complete Setup Guide

This guide will walk you through setting up your cryptocurrency Telegram bot from scratch.

## 📋 Prerequisites

- Python 3.8 or higher
- A Telegram account
- A GitHub account (for automation)
- Basic command line knowledge

## 🤖 Step 1: Create Your Telegram Bot

1. **Open Telegram** and search for `@BotFather`

2. **Start a conversation** and send `/newbot`

3. **Follow the prompts**:
   - Choose a name for your bot (e.g., "Crypto Price Bot")
   - Choose a username (must end in 'bot', e.g., "my_crypto_price_bot")

4. **Save your bot token**:
   - BotFather will give you a token like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`
   - ⚠️ **Keep this secret!** Anyone with this token can control your bot

## 📢 Step 2: Create Your Telegram Channel

1. **Create a new channel** in Telegram:
   - Open Telegram → Menu → New Channel
   - Choose a name (e.g., "Crypto Updates")
   - Choose public or private (your choice)

2. **Add your bot as an administrator**:
   - Go to your channel
   - Click on channel name → Administrators → Add Administrator
   - Search for your bot's username
   - Grant "Post Messages" permission
   - Click ✓ to save

## 🔑 Step 3: Get Your Chat ID

1. **Post a message** in your channel (any message)

2. **Open your browser** and visit:
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
   Replace `<YOUR_BOT_TOKEN>` with your actual bot token

3. **Find your Chat ID**:
   - Look for `"chat":{"id":-100...}`
   - The number after `"id":` is your CHAT_ID (including the minus sign!)
   - Example: `-1001234567890`

4. **Alternative method** (if above doesn't work):
   - Run the included script:
     ```bash
     python get_chat_id.py
     ```
   - Follow the prompts

## 💻 Step 4: Local Setup

### Clone or Download the Repository

```bash
# If using git
git clone <repository-url>
cd telegram-crypto-bot

# Or download and extract the ZIP file
```

### Install Python Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Or if you use pip3
pip3 install -r requirements.txt
```

### Configure Environment Variables

1. **Copy the example file**:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file** with your favorite text editor:
   ```
   BOT_TOKEN=your_bot_token_here
   CHAT_ID=your_chat_id_here
   TIMEZONE_OFFSET_HOURS=5.5
   ```

   - `BOT_TOKEN`: Your bot token from BotFather
   - `CHAT_ID`: Your channel chat ID (with the minus sign!)
   - `TIMEZONE_OFFSET_HOURS`: Your timezone offset from UTC
     - IST (India): `5.5`
     - EST (US East): `-5`
     - PST (US West): `-8`
     - GMT (UK): `0`
     - CET (Europe): `1`

### Test Your Bot Locally

**Option 1: Automated Posting**
```bash
python -m src.main
```
This will make ONE post based on the current time.

**Option 2: Interactive Chat Bot**
```bash
python -m src.chat_bot
```
This runs the bot in chat mode. Users can send commands like `/price`, `/news`, etc.

**Option 3: Manual Dashboard**
```bash
cd dashboard
python app.py
```
Then open `http://127.0.0.1:5000` in your browser to manually trigger posts.

## 🤖 Step 5: GitHub Actions Automation (Recommended)

This will make your bot post automatically 3-4 times per day!

### Push to GitHub

1. **Create a new repository** on GitHub (can be private)

2. **Push your code**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

   ⚠️ **Make sure `.env` is in `.gitignore`!** (It already is by default)

### Configure GitHub Secrets

1. **Go to your repository** on GitHub

2. **Navigate to**: Settings → Secrets and variables → Actions

3. **Click "New repository secret"** and add these three secrets:

   | Name | Value |
   |------|-------|
   | `BOT_TOKEN` | Your bot token from BotFather |
   | `CHAT_ID` | Your channel chat ID (with minus sign) |
   | `TIMEZONE_OFFSET_HOURS` | Your timezone offset (e.g., `5.5`) |

### Enable GitHub Actions

1. **Go to the "Actions" tab** in your repository

2. **Enable workflows** if prompted

3. **Check the workflow**:
   - You should see "Auto Post Crypto Content"
   - It runs 3-4 times per day automatically!

### Posting Schedule

The default schedule (in UTC):
- **Morning**: 2:30 AM UTC (8:00 AM IST) - Crypto Prices
- **Afternoon**: 8:30 AM UTC (2:00 PM IST) - Educational Content
- **Evening**: 2:30 PM UTC (8:00 PM IST) - Interactive Content
- **Late Night**: 5:30 PM UTC (11:00 PM IST) - Trending/Analysis

**To customize the schedule**, edit `.github/workflows/auto-post.yml` and change the cron times.

## 🎨 Step 6: Customize Your Bot

### Change Post Content

Edit `src/templates.py` to modify:
- AI prompt templates
- Image generation prompts
- Content themes

### Adjust Posting Logic

Edit `src/scheduler_logic.py` to:
- Change what posts at what time
- Add new post types
- Adjust posting frequency

### Add New Features

1. **Add new post types** in `src/main.py`
2. **Add new templates** in `src/templates.py`
3. **Add new dashboard buttons** in `dashboard/templates/dashboard.html`
4. **Add new routes** in `dashboard/app.py`

## 🔧 Troubleshooting

### Bot doesn't post to channel
- ✅ Check that bot is admin in channel with "Post Messages" permission
- ✅ Verify CHAT_ID is correct (should start with `-100`)
- ✅ Verify BOT_TOKEN is correct

### "Unauthorized" error
- ✅ Check your BOT_TOKEN is correct
- ✅ Make sure there are no extra spaces in `.env` file

### Posts at wrong time
- ✅ Check TIMEZONE_OFFSET_HOURS is correct
- ✅ Remember GitHub Actions runs in UTC
- ✅ Adjust cron schedule in `.github/workflows/auto-post.yml`

### API rate limit errors
- ✅ CoinGecko free tier: 10-50 calls/minute
- ✅ Add delays between API calls if needed
- ✅ Consider caching data for a few minutes

### Chat bot not responding
- ✅ Make sure you're running `python -m src.chat_bot`
- ✅ Send commands to the bot directly (not the channel)
- ✅ Commands must start with `/` (e.g., `/price`)

## 📊 Using the Dashboard

1. **Start the dashboard**:
   ```bash
   cd dashboard
   python app.py
   ```

2. **Open in browser**: `http://127.0.0.1:5000`

3. **Click any button** to manually post that content type

4. **See flash messages** confirming posts were sent

## 💬 Chat Bot Commands

To enable chat features:

1. **Run the chat bot**:
   ```bash
   python -m src.chat_bot
   ```

2. **Users can send commands**:
   - `/start` - Welcome message and help
   - `/price` - Top 15 crypto prices
   - `/news` - Latest crypto news
   - `/trending` - Trending coins
   - `/btc` - Bitcoin price
   - `/eth` - Ethereum price
   - `/price sol` - Solana price (any symbol)
   - `/learn` - Random crypto education
   - `/tip` - Trading tip
   - `/security` - Security advice
   - `/quiz` - Crypto quiz

## 🌟 Best Practices

1. **Test locally first** before enabling GitHub Actions
2. **Monitor your channel** for the first few days
3. **Adjust posting frequency** based on audience engagement
4. **Keep API keys secret** - never commit `.env` to git
5. **Backup your bot token** in a secure location
6. **Customize content** to match your audience's interests

## 📈 Next Steps

- ✅ Customize AI prompts for your audience
- ✅ Add more cryptocurrency symbols to track
- ✅ Enable chart generation (optional)
- ✅ Add more interactive features
- ✅ Integrate with other crypto APIs
- ✅ Create custom alerts for price movements

## 🆘 Need Help?

- Check the main `README.md` for feature documentation
- Review `BOT_SUMMARY.md` for technical details
- Check GitHub Issues for common problems
- Review Telegram Bot API documentation

---

**You're all set! Your crypto bot should now be posting automatically.** 🚀💰

*Happy crypto posting!* 💎
