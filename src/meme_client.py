"""
Free Meme Client - Fetches real memes from meme APIs
"""
import requests
import random


def get_random_meme():
    """Get a random meme from free meme APIs"""
    
    # Try multiple meme APIs
    apis = [
        "https://meme-api.com/gimme",
        "https://memes.blademaker.tv/api",
    ]
    
    for api_url in apis:
        try:
            print(f"🎨 Fetching meme from {api_url}...")
            resp = requests.get(api_url, timeout=10)
            
            if resp.status_code == 200:
                data = resp.json()
                
                # Different APIs have different response formats
                if 'url' in data:
                    return {
                        'image_url': data['url'],
                        'title': data.get('title', 'Random Meme'),
                        'subreddit': data.get('subreddit', 'memes')
                    }
                elif 'image' in data:
                    return {
                        'image_url': data['image'],
                        'title': data.get('title', 'Random Meme'),
                        'subreddit': 'memes'
                    }
        except Exception as e:
            print(f"❌ Failed to fetch from {api_url}: {e}")
            continue
    
    # Fallback - return None if all APIs fail
    return None


def format_meme(meme_data):
    """Format meme data into a nice caption"""
    if not meme_data:
        return "😂 Random Meme!"
    
    title = meme_data.get('title', 'Random Meme')
    subreddit = meme_data.get('subreddit', 'memes')
    
    caption = f"😂 **{title}**\n\n"
    caption += f"📍 From r/{subreddit}\n\n"
    caption += "#meme #funny #humor"
    
    return caption
