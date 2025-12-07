"""
Test Real Meme API
"""
from src.meme_client import get_random_meme, format_meme
from src import telegram_client as tg

print("=" * 60)
print("🎨 REAL MEME API TEST")
print("=" * 60)
print()

print("📥 Fetching random meme...")
meme = get_random_meme()

if meme:
    print(f"✅ Got meme: {meme['title']}")
    print(f"📍 From: r/{meme['subreddit']}")
    print(f"🖼️  Image URL: {meme['image_url'][:80]}...")
    print()
    
    caption = format_meme(meme)
    print(f"💬 Caption: {caption[:100]}...")
    print()
    
    print("📤 Sending to Telegram...")
    result = tg.send_photo(meme['image_url'], caption)
    print(f"Status: {result.status_code}")
    
    if result.status_code == 200:
        print()
        print("=" * 60)
        print("✅ REAL MEME SENT! Check your Telegram channel!")
        print("=" * 60)
else:
    print("❌ Failed to fetch meme from all APIs")
