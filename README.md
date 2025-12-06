# 😂 Jokes & Memes Bot - Spread Laughter Daily!

An automated Telegram bot that posts hilarious jokes, funny memes, and entertaining content to keep your audience laughing and engaged!

## 🎯 Features

### 😄 **Real Jokes from APIs**
- **Dad Jokes**: Classic, corny, groan-worthy dad jokes
- **Programming Jokes**: Tech and coding humor
- **Puns**: Clever wordplay that makes you laugh and groan
- **Chuck Norris Facts**: Legendary Chuck Norris jokes
- **Random Jokes**: Variety from multiple joke APIs

### 🎨 **AI-Generated Content**
- **Funny Memes**: AI-generated meme images with hilarious captions
- **Observational Humor**: Stand-up comedy style observations
- **Work Humor**: Relatable office and career jokes
- **Food Humor**: Pizza, coffee, and food-related comedy
- **Tech Humor**: WiFi struggles, coding bugs, and tech fails
- **Animal Jokes**: Cute and funny animal humor
- **Shower Thoughts**: Mind-bending random thoughts
- **Random Facts**: Weird and funny facts with humorous twists

### 🎭 **Interactive Content**
- **Polls**: Fun multiple-choice questions
- **Daily Challenges**: Riddles and fun challenges
- **Joke Threads**: Connected series of jokes
- **Motivational Humor**: Inspiration with a funny twist

### 💬 **Chat Features**
Users can interact with the bot using commands:
- `/joke` - Random joke from our collection
- `/dadjoke` - Classic dad joke
- `/techjoke` - Programming/tech humor
- `/pun` - Clever pun
- `/animal` - Cute animal joke
- `/work` - Relatable work humor
- `/food` - Food-related jokes
- `/shower` - Mind-bending shower thought
- `/fact` - Funny random fact
- `/challenge` - Daily fun challenge
- `/motivate` - Motivational humor
- `/random` - Surprise me!

## 📅 Posting Schedule

The bot posts **4-6 times per day** at optimal times:

- **Morning (7-9 AM)**: 😊 Motivational & Dad Jokes (Start the day with a smile!)
- **Mid-Morning (10-12 PM)**: 🎲 API Jokes & Puns (Fresh content)
- **Afternoon (2-4 PM)**: 💼 Work & Tech Humor (Relatable!)
- **Evening (6-8 PM)**: 🎨 Memes with Images (HIGH ENGAGEMENT - 70% visual content)
- **Night (9-11 PM)**: 🎭 Variety (Random jokes, relationship humor, animal jokes)
- **Late Night (11 PM-1 AM)**: 🚿 Shower Thoughts & Deep Humor

## 🚀 Setup

### 1. Create Telegram Bot & Channel

1. Talk to **@BotFather** on Telegram:
   - `/newbot` → get your `BOT_TOKEN`
2. Create a **public or private channel**
3. Add the bot as **Admin** to your channel (with "Post Messages" permission)
4. Get your `CHAT_ID`:
   - Post something to your channel
   - Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Look for `"chat":{"id": -100...}` from your channel

### 2. Local Setup

```bash
git clone <this-repo>
cd telegram-jokes-bot

# Copy and edit environment variables
cp .env.example .env
# Edit .env with your BOT_TOKEN, CHAT_ID, and TIMEZONE_OFFSET_HOURS

# Install dependencies
pip install -r requirements.txt

# Test the bot (automated posting)
python -m src.main

# OR run the chat bot (interactive mode)
python -m src.chat_bot
```

### 3. GitHub Actions Automation

1. Push this repo to GitHub
2. Go to: **Settings → Secrets and variables → Actions**
3. Add these repository secrets:
   - `BOT_TOKEN` - Your Telegram bot token
   - `CHAT_ID` - Your channel chat ID
   - `TIMEZONE_OFFSET_HOURS` - Your timezone offset (e.g., 5.5 for IST)

The bot will automatically post 4-6 times daily via GitHub Actions!

### 4. Dashboard (Manual Control)

Run the Flask dashboard for manual posting:

```bash
cd dashboard
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

From the dashboard you can manually trigger:
- 😂 **Jokes**: Dad Jokes, Puns, Tech Jokes, API Jokes
- 🎨 **Memes**: Memes with Images, Joke with Image
- 🎯 **Interactive**: Challenges, Polls, Threads, Facts

## 📁 Project Structure

```
telegram-jokes-bot/
├── .github/workflows/     # GitHub Actions automation (4-6x daily posts)
├── dashboard/             # Flask web UI for manual posting
│   ├── app.py            # Flask routes
│   ├── templates/        # HTML templates
│   └── static/           # CSS styles
├── src/                   # Core bot logic
│   ├── config.py         # Configuration management
│   ├── telegram_client.py # Telegram API wrapper
│   ├── jokes_client.py   # Jokes API client (multiple free APIs)
│   ├── pollinations_client.py # AI generation (free!)
│   ├── templates.py      # AI prompt templates
│   ├── scheduler_logic.py # Time-based posting logic
│   ├── chat_bot.py       # Interactive chat bot handler
│   └── main.py           # Main orchestrator
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── README.md            # This file
```

## 🎨 Customization

- **Edit prompts**: Modify `src/templates.py` to change AI generation prompts
- **Change schedule**: Edit `.github/workflows/auto-post.yml` cron times
- **Adjust posting logic**: Modify `src/scheduler_logic.py` to change what posts when
- **Add new post types**: Add templates and functions following the existing pattern
- **Customize joke sources**: Modify `src/jokes_client.py` for different APIs

## 🔑 API Information

### **JokeAPI** (Free, No Key Required)
- Multiple joke categories (Programming, Misc, Pun, Dark)
- Blacklist filtering for safe content
- **URL**: https://v2.jokeapi.dev
- **Rate Limit**: Very generous

### **icanhazdadjoke** (Free, No Key Required)
- Classic dad jokes
- **URL**: https://icanhazdadjoke.com
- **Rate Limit**: Unlimited

### **Chuck Norris API** (Free, No Key Required)
- Chuck Norris facts/jokes
- **URL**: https://api.chucknorris.io
- **Rate Limit**: Unlimited

### **Official Joke API** (Free, No Key Required)
- Programming and general jokes
- **URL**: https://official-joke-api.appspot.com
- **Rate Limit**: Generous

### **Pollinations.ai** (Free)
- AI-generated text content
- AI-generated meme images
- No API key required

## 💡 Why This Bot?

✅ **Real Jokes**: Genuine funny jokes from multiple APIs  
✅ **AI-Enhanced**: Natural, human-like humor generation  
✅ **Interactive**: Chat commands allow users to request jokes on-demand  
✅ **Automated**: Posts 4-6 times daily without manual intervention  
✅ **Free APIs**: Uses completely free APIs - no costs!  
✅ **Customizable**: Easy to modify content, schedule, and features  
✅ **Visual Appeal**: AI-generated meme images make posts engaging  
✅ **Relatable**: Content that people actually find funny and share  

## 🤖 Chat Bot Usage

To enable interactive chat features, run the chat bot:

```bash
python -m src.chat_bot
```

Users can then send commands to your bot:
- Get random jokes
- Request specific joke types
- Daily challenges
- Motivational humor
- And much more!

## 🎭 Content Categories

The bot covers a wide range of humor:
- 👨 **Dad Jokes** - Wholesome and corny
- 💻 **Tech Humor** - For programmers and tech enthusiasts
- 🎭 **Puns** - Clever wordplay
- 🐶 **Animal Jokes** - Cute and funny
- 💼 **Work Humor** - Relatable office life
- 🍕 **Food Jokes** - Pizza, coffee, and more
- 💑 **Relationship Humor** - Lighthearted dating jokes
- 🚿 **Shower Thoughts** - Mind-bending observations
- 🤯 **Random Facts** - Weird and funny facts
- 💪 **Motivational** - Inspiration with humor

## 📝 License

MIT

---

**Powered by JokeAPI, icanhazdadjoke, Chuck Norris API & Pollinations.ai**

*Spreading laughter, one joke at a time! 😂❤️*

