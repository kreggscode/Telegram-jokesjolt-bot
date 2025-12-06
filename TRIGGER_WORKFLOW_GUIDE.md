# 🚀 Quick Guide: Manually Trigger Your Bot on GitHub

## ✅ Code Has Been Pushed!

I've successfully pushed all the fixes to your GitHub repository:
- ✅ Content variety system (timestamp + random seeds)
- ✅ Enhanced error logging
- ✅ Better error handling

**Repository:** https://github.com/kreggscode/Telegram-jokesjolt-bot

---

## 🎯 How to Manually Trigger the Workflow (Test It Now!)

### Step 1: Open Your Repository
Go to: https://github.com/kreggscode/Telegram-jokesjolt-bot/actions/workflows/auto-post.yml

### Step 2: Click "Run workflow"
You should see a **green "Run workflow"** button on the right side of the page.

![Run Workflow Button Location](https://docs.github.com/assets/cb-33501/mw-1440/images/help/actions/workflow-dispatch-button.webp)

### Step 3: Trigger It
1. Click the "Run workflow" button
2. A dropdown will appear
3. Make sure "Branch: main" is selected
4. Click the green "Run workflow" button in the dropdown

### Step 4: Watch It Run
1. Go to the "Actions" tab: https://github.com/kreggscode/Telegram-jokesjolt-bot/actions
2. You should see a new workflow run appear at the top
3. Click on it to see the logs in real-time

### Step 5: Check Your Telegram Channel
Within 30-60 seconds, you should see a new joke/meme posted to your Telegram channel!

---

## 🔍 Checking Recent Workflow Runs

To see why your bot stopped working:

1. Go to: https://github.com/kreggscode/Telegram-jokesjolt-bot/actions
2. Look at the recent workflow runs
3. Click on any failed runs (marked with ❌ or red X)
4. Click on the job name to see detailed logs
5. Look for error messages

### Common Issues to Look For:

#### ❌ "BOT_TOKEN or CHAT_ID is not set"
**Solution:** Check your GitHub Secrets
- Go to: Settings → Secrets and variables → Actions
- Verify `BOT_TOKEN`, `CHAT_ID`, and `TIMEZONE_OFFSET_HOURS` exist

#### ❌ "Unauthorized" or "403 Forbidden"
**Solution:** Bot token might be invalid
- Get a new token from @BotFather
- Update the `BOT_TOKEN` secret in GitHub

#### ❌ "Chat not found"
**Solution:** CHAT_ID is incorrect
- Run `python get_chat_id.py` locally
- Update the `CHAT_ID` secret in GitHub

#### ❌ "Bot was blocked by the user"
**Solution:** Bot needs to be added to channel
- Add your bot to the Telegram channel
- Make it an administrator
- Give it "Post Messages" permission

---

## 📊 What Changed in the Latest Push

### File: `src/pollinations_client.py`
```python
# OLD (repetitive content)
url = f"https://text.pollinations.ai/{encoded}"

# NEW (unique content every time)
timestamp = int(time.time())
seed = random.randint(1000, 9999)
enhanced_prompt = f"{prompt}\n\nIMPORTANT: Generate completely NEW and UNIQUE content. Timestamp: {timestamp}, Seed: {seed}..."
url = f"https://text.pollinations.ai/{encoded}?seed={seed}"
```

### File: `src/telegram_client.py`
```python
# Added detailed logging
print(f"📤 Sending text message to chat_id: {CHAT_ID}")
resp = requests.post(url, data=data, timeout=30)

if resp.status_code == 200:
    print("✅ Message sent successfully!")
else:
    print(f"❌ Failed to send message. Status: {resp.status_code}")
    print(f"Response: {resp.text}")
```

---

## 🧪 Testing Locally (Optional)

If you want to test locally before relying on GitHub Actions:

1. **Create `.env` file:**
```env
BOT_TOKEN=your_actual_bot_token
CHAT_ID=your_actual_chat_id
TIMEZONE_OFFSET_HOURS=5.5
```

2. **Run the test script:**
```bash
python test_bot_config.py
```

3. **Run the bot:**
```bash
python -m src.main
```

4. **Test variety (run 3 times):**
```bash
python -m src.main
python -m src.main
python -m src.main
```
Each run should generate different content!

---

## ⏰ Current Schedule

Your bot is scheduled to post **3 times per day**:

| Time (IST) | Time (UTC) | Content Type |
|------------|------------|--------------|
| 8:00 AM    | 2:30 AM    | Morning jokes, motivational |
| 2:00 PM    | 8:30 AM    | API jokes, puns, tech humor |
| 6:00 PM    | 12:30 PM   | Memes with images (peak!) |

**Note:** GitHub Actions can have 5-15 minute delays.

---

## 🎉 Next Steps

1. **Manually trigger the workflow** using the steps above
2. **Check the Actions tab** for the workflow run
3. **Look at the logs** to see detailed output (now with emojis!)
4. **Check your Telegram channel** for the new post
5. **Monitor scheduled runs** to ensure they work automatically

---

## 🆘 If It Still Doesn't Work

If the manual trigger fails:

1. **Check the workflow logs** - they will now show detailed error messages
2. **Verify GitHub Secrets** - make sure all three are set correctly
3. **Check bot permissions** - ensure bot is admin in your channel
4. **Share the error logs** - the new logging will show exactly what's wrong

The enhanced error logging will make it much easier to diagnose issues! 🔍

---

**Ready to test? Go trigger that workflow!** 🚀
https://github.com/kreggscode/Telegram-jokesjolt-bot/actions/workflows/auto-post.yml
