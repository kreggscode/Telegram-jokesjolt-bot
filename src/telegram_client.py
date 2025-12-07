import requests
from .config import BOT_TOKEN, CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_text(text: str):
    """Send text message to Telegram with error handling"""
    url = f"{BASE_URL}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    
    try:
        print(f"📤 Sending text message to chat_id: {CHAT_ID}")
        resp = requests.post(url, data=data, timeout=30)
        
        if resp.status_code == 200:
            print("✅ Message sent successfully!")
            return resp
        else:
            print(f"❌ Failed to send message. Status: {resp.status_code}")
            print(f"Response: {resp.text}")
            return resp
    except Exception as e:
        print(f"❌ Error sending text: {e}")
        raise


def send_photo(image_url: str, caption: str = ""):
    """Send photo to Telegram with error handling - downloads image first"""
    url = f"{BASE_URL}/sendPhoto"
    
    try:
        print(f"📤 Sending photo to chat_id: {CHAT_ID}")
        print(f"Image URL: {image_url[:100]}...")
        
        # Download the image first
        print("⬇️  Downloading image...")
        img_response = requests.get(image_url, timeout=30)
        
        if img_response.status_code != 200:
            print(f"❌ Failed to download image. Status: {img_response.status_code}")
            return img_response
        
        print(f"✅ Image downloaded ({len(img_response.content)} bytes)")
        
        # Send as multipart file upload
        files = {
            'photo': ('meme.jpg', img_response.content, 'image/jpeg')
        }
        data = {
            "chat_id": CHAT_ID,
            "caption": caption
        }
        
        print("📤 Uploading to Telegram...")
        resp = requests.post(url, data=data, files=files, timeout=60)
        
        if resp.status_code == 200:
            print("✅ Photo sent successfully!")
            return resp
        else:
            print(f"❌ Failed to send photo. Status: {resp.status_code}")
            print(f"Response: {resp.text}")
            return resp
    except Exception as e:
        print(f"❌ Error sending photo: {e}")
        raise


def send_poll(question: str, options: list[str]):
    """Send poll to Telegram with error handling"""
    import json
    url = f"{BASE_URL}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": question,
        "options": json.dumps(options),
        "is_anonymous": False
    }
    
    try:
        print(f"📤 Sending poll to chat_id: {CHAT_ID}")
        resp = requests.post(url, data=data, timeout=30)
        
        if resp.status_code == 200:
            print("✅ Poll sent successfully!")
            return resp
        else:
            print(f"❌ Failed to send poll. Status: {resp.status_code}")
            print(f"Response: {resp.text}")
            return resp
    except Exception as e:
        print(f"❌ Error sending poll: {e}")
        raise


def send_thread(messages: list[str]):
    """Send multiple messages as a thread"""
    print(f"📤 Sending thread with {len(messages)} messages")
    for i, msg in enumerate(messages, 1):
        print(f"Sending message {i}/{len(messages)}")
        send_text(msg)
