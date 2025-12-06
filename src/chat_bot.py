"""
Chat Bot Handler - Handles user commands and interactions
Allows users to request jokes, memes, and funny content on demand!
"""
import requests
from .config import BOT_TOKEN
from .jokes_client import jokes_client
from . import pollinations_client as ai
from .templates import TEXT_TEMPLATES

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def get_updates(offset=None):
    """Get new messages from Telegram"""
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 30, "offset": offset}
    try:
        response = requests.get(url, params=params, timeout=35)
        return response.json()
    except Exception as e:
        print(f"Error getting updates: {e}")
        return None


def send_message(chat_id, text):
    """Send a message to a specific chat"""
    url = f"{BASE_URL}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Error sending message: {e}")


def handle_command(message):
    """Process user commands"""
    chat_id = message['chat']['id']
    text = message.get('text', '').strip()
    
    if not text:
        return
    
    # Convert to lowercase for command matching
    text_lower = text.lower()
    
    # /start command
    if text_lower == '/start' or text_lower == '/help':
        help_text = """
😂 **Welcome to Jokes & Memes Bot!** 🎭

I'm here to make you laugh with hilarious jokes and memes!

**Joke Commands:**
😄 `/joke` - Random joke from our collection
👨 `/dadjoke` - Classic dad joke
💻 `/techjoke` - Programming/tech humor
🎭 `/pun` - Clever pun
🐶 `/animal` - Cute animal joke
💼 `/work` - Relatable work humor
🍕 `/food` - Food-related jokes
🚿 `/shower` - Mind-bending shower thought
🤯 `/fact` - Funny random fact

**Interactive:**
🎯 `/challenge` - Daily fun challenge
💪 `/motivate` - Motivational humor
🎲 `/random` - Surprise me!

**More Info:**
ℹ️ `/about` - About this bot
❓ `/help` - Show this message

*Let's spread some laughter!* 😂🎉
        """
        send_message(chat_id, help_text)
    
    # Random joke
    elif text_lower in ['/joke', '/random']:
        joke_data = jokes_client.get_any_joke()
        message_text = jokes_client.format_joke(joke_data)
        send_message(chat_id, message_text)
    
    # Dad joke
    elif text_lower in ['/dadjoke', '/dad']:
        joke_data = jokes_client.get_dad_joke()
        if joke_data:
            message_text = jokes_client.format_joke(joke_data)
            send_message(chat_id, message_text)
        else:
            prompt = TEXT_TEMPLATES["dad_joke"]
            text = ai.generate_text(prompt)
            send_message(chat_id, text)
    
    # Tech/Programming joke
    elif text_lower in ['/techjoke', '/tech', '/programming', '/code']:
        joke_data = jokes_client.get_programming_joke()
        if joke_data:
            message_text = jokes_client.format_joke(joke_data)
            send_message(chat_id, message_text)
        else:
            prompt = TEXT_TEMPLATES["tech_humor"]
            text = ai.generate_text(prompt)
            send_message(chat_id, text)
    
    # Pun
    elif text_lower in ['/pun', '/puns']:
        joke_data = jokes_client.get_pun()
        if joke_data:
            message_text = jokes_client.format_joke(joke_data)
            send_message(chat_id, message_text)
        else:
            prompt = TEXT_TEMPLATES["pun_joke"]
            text = ai.generate_text(prompt)
            send_message(chat_id, text)
    
    # Chuck Norris joke
    elif text_lower in ['/chuck', '/chucknorris']:
        joke_data = jokes_client.get_chuck_norris_joke()
        if joke_data:
            message_text = jokes_client.format_joke(joke_data)
            send_message(chat_id, message_text)
        else:
            send_message(chat_id, "❌ Couldn't fetch Chuck Norris joke right now!")
    
    # Animal joke
    elif text_lower in ['/animal', '/animals', '/pet']:
        prompt = TEXT_TEMPLATES["animal_joke"]
        text = ai.generate_text(prompt)
        send_message(chat_id, text)
    
    # Work humor
    elif text_lower in ['/work', '/office', '/job']:
        prompt = TEXT_TEMPLATES["work_humor"]
        text = ai.generate_text(prompt)
        send_message(chat_id, text)
    
    # Food humor
    elif text_lower in ['/food', '/pizza', '/coffee']:
        prompt = TEXT_TEMPLATES["food_humor"]
        text = ai.generate_text(prompt)
        send_message(chat_id, text)
    
    # Shower thought
    elif text_lower in ['/shower', '/thought', '/showerthought']:
        prompt = TEXT_TEMPLATES["shower_thoughts"]
        text = ai.generate_text(prompt)
        send_message(chat_id, text)
    
    # Random fact
    elif text_lower in ['/fact', '/facts']:
        prompt = TEXT_TEMPLATES["random_fact_funny"]
        text = ai.generate_text(prompt)
        send_message(chat_id, text)
    
    # Motivational
    elif text_lower in ['/motivate', '/motivation', '/inspire']:
        prompt = TEXT_TEMPLATES["motivational_funny"]
        text = ai.generate_text(prompt)
        send_message(chat_id, text)
    
    # Challenge
    elif text_lower in ['/challenge', '/riddle', '/quiz']:
        prompt = TEXT_TEMPLATES["daily_challenge"]
        text = ai.generate_text(prompt)
        send_message(chat_id, text)
    
    # Relationship humor
    elif text_lower in ['/relationship', '/dating', '/love']:
        prompt = TEXT_TEMPLATES["relationship_humor"]
        text = ai.generate_text(prompt)
        send_message(chat_id, text)
    
    # About
    elif text_lower == '/about':
        about_text = """
ℹ️ **About Jokes & Memes Bot**

I'm an automated comedy bot that provides:
✅ Real jokes from multiple free APIs
✅ AI-generated funny content
✅ Hilarious memes with images
✅ Interactive challenges and polls
✅ Daily doses of laughter

**Features:**
🔄 Auto-posts 4-6 times daily
😂 Multiple joke categories
🎨 AI-generated meme images
🎭 Dad jokes, puns, tech humor & more
🤖 Natural, human-like humor

**Joke Sources:**
- JokeAPI (v2.jokeapi.dev)
- icanhazdadjoke.com
- Chuck Norris API
- Official Joke API
- Pollinations.ai (AI content)

*Spreading laughter, one joke at a time!* 😄❤️
        """
        send_message(chat_id, about_text)
    
    # Unknown command
    elif text.startswith('/'):
        send_message(chat_id, "❓ Unknown command. Type /help to see available commands.")


def run_chat_bot():
    """
    Run the chat bot in polling mode
    This allows users to interact with the bot via commands
    """
    print("🤖 Starting Jokes & Memes Chat Bot...")
    print("📡 Listening for commands...")
    
    offset = None
    
    try:
        while True:
            updates = get_updates(offset)
            
            if updates and updates.get('ok'):
                for update in updates.get('result', []):
                    offset = update['update_id'] + 1
                    
                    if 'message' in update:
                        handle_command(update['message'])
    
    except KeyboardInterrupt:
        print("\n👋 Chat bot stopped by user")
    except Exception as e:
        print(f"❌ Chat bot error: {e}")


if __name__ == "__main__":
    run_chat_bot()
