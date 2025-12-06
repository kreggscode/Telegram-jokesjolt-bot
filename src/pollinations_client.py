import urllib.parse
import requests
import time
import random


def generate_text(prompt: str) -> str:
    """Generate free-form text from Pollinations.ai with timestamp and seed for variety."""
    # Add timestamp and random seed to ensure unique content every time
    timestamp = int(time.time())
    seed = random.randint(1000, 9999)
    
    # Enhance prompt with variety instructions
    enhanced_prompt = f"{prompt}\n\nIMPORTANT: Generate completely NEW and UNIQUE content. Timestamp: {timestamp}, Seed: {seed}. Do NOT repeat previous jokes or content."
    
    encoded = urllib.parse.quote(enhanced_prompt)
    url = f"https://text.pollinations.ai/{encoded}?seed={seed}"
    
    try:
        resp = requests.get(url, timeout=30)
        if resp.status_code == 200:
            return resp.text.strip()
    except Exception as e:
        print(f"Error generating text: {e}")
    
    return "AI generation failed. Please try again."


def image_url(prompt: str) -> str:
    """Return an image URL from Pollinations based on prompt with seed for variety."""
    # Add random seed to ensure different images
    seed = random.randint(1000, 9999)
    encoded = urllib.parse.quote(prompt)
    return f"https://image.pollinations.ai/prompt/{encoded}?seed={seed}&width=1024&height=1024&nologo=true"
