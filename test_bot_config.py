"""
Quick Test Script - Verify Bot Configuration and Connectivity
Run this to check if your bot is properly configured
"""
import os
import sys
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

def test_env_variables():
    """Test if environment variables are set"""
    print("=" * 60)
    print("🔍 STEP 1: Checking Environment Variables")
    print("=" * 60)
    
    bot_token = os.getenv("BOT_TOKEN", "").strip()
    chat_id = os.getenv("CHAT_ID", "").strip()
    timezone = os.getenv("TIMEZONE_OFFSET_HOURS", "5.5")
    
    issues = []
    
    if not bot_token:
        print("❌ BOT_TOKEN is not set!")
        issues.append("BOT_TOKEN missing")
    elif bot_token == "your_bot_token_here":
        print("❌ BOT_TOKEN is still the placeholder value!")
        issues.append("BOT_TOKEN not configured")
    else:
        print(f"✅ BOT_TOKEN is set: {bot_token[:10]}...{bot_token[-5:]}")
    
    if not chat_id:
        print("❌ CHAT_ID is not set!")
        issues.append("CHAT_ID missing")
    elif chat_id == "your_channel_chat_id_here":
        print("❌ CHAT_ID is still the placeholder value!")
        issues.append("CHAT_ID not configured")
    else:
        print(f"✅ CHAT_ID is set: {chat_id}")
    
    print(f"✅ TIMEZONE_OFFSET_HOURS: {timezone}")
    
    return bot_token, chat_id, issues


def test_bot_token(bot_token):
    """Test if bot token is valid"""
    print("\n" + "=" * 60)
    print("🤖 STEP 2: Testing Bot Token Validity")
    print("=" * 60)
    
    try:
        url = f"https://api.telegram.org/bot{bot_token}/getMe"
        resp = requests.get(url, timeout=10)
        
        if resp.status_code == 200:
            data = resp.json()
            if data.get("ok"):
                bot_info = data.get("result", {})
                print(f"✅ Bot token is VALID!")
                print(f"   Bot Name: {bot_info.get('first_name')}")
                print(f"   Username: @{bot_info.get('username')}")
                print(f"   Bot ID: {bot_info.get('id')}")
                return True
        
        print(f"❌ Bot token is INVALID!")
        print(f"   Status: {resp.status_code}")
        print(f"   Response: {resp.text}")
        return False
        
    except Exception as e:
        print(f"❌ Error testing bot token: {e}")
        return False


def test_send_message(bot_token, chat_id):
    """Test sending a message to the channel"""
    print("\n" + "=" * 60)
    print("📤 STEP 3: Testing Message Sending")
    print("=" * 60)
    
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": "🧪 **Test Message**\n\nThis is a test message from your Jokes Bot!\n\nIf you see this, your bot is working correctly! 🎉",
            "parse_mode": "Markdown"
        }
        
        print(f"Sending test message to chat_id: {chat_id}...")
        resp = requests.post(url, data=data, timeout=30)
        
        if resp.status_code == 200:
            print("✅ Test message sent SUCCESSFULLY!")
            print("   Check your Telegram channel for the message!")
            return True
        else:
            print(f"❌ Failed to send message!")
            print(f"   Status Code: {resp.status_code}")
            print(f"   Response: {resp.text}")
            
            # Parse common errors
            if "chat not found" in resp.text.lower():
                print("\n💡 SOLUTION: Your CHAT_ID might be incorrect.")
                print("   Run: python get_chat_id.py")
            elif "bot was blocked" in resp.text.lower():
                print("\n💡 SOLUTION: The bot was blocked by the user/channel.")
                print("   Make sure the bot is added to your channel as admin!")
            elif "forbidden" in resp.text.lower():
                print("\n💡 SOLUTION: Bot doesn't have permission to post.")
                print("   Add the bot as admin with 'Post Messages' permission!")
            
            return False
            
    except Exception as e:
        print(f"❌ Error sending test message: {e}")
        return False


def test_pollinations_api():
    """Test Pollinations AI API"""
    print("\n" + "=" * 60)
    print("🎨 STEP 4: Testing Pollinations AI API")
    print("=" * 60)
    
    try:
        import urllib.parse
        prompt = "Tell me a short funny joke"
        encoded = urllib.parse.quote(prompt)
        url = f"https://text.pollinations.ai/{encoded}"
        
        print("Generating test joke from Pollinations AI...")
        resp = requests.get(url, timeout=30)
        
        if resp.status_code == 200:
            joke = resp.text.strip()
            print("✅ Pollinations AI is working!")
            print(f"\nGenerated joke:\n{joke}\n")
            return True
        else:
            print(f"❌ Pollinations AI request failed!")
            print(f"   Status: {resp.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing Pollinations AI: {e}")
        return False


def main():
    """Run all tests"""
    print("\n" + "🧪" * 30)
    print("   TELEGRAM JOKES BOT - CONFIGURATION TEST")
    print("🧪" * 30 + "\n")
    
    # Test 1: Environment variables
    bot_token, chat_id, issues = test_env_variables()
    
    if issues:
        print("\n" + "=" * 60)
        print("⚠️  CONFIGURATION ISSUES FOUND")
        print("=" * 60)
        for issue in issues:
            print(f"  • {issue}")
        print("\n💡 Please create a .env file with your bot credentials:")
        print("   BOT_TOKEN=your_actual_bot_token")
        print("   CHAT_ID=your_actual_chat_id")
        print("   TIMEZONE_OFFSET_HOURS=5.5")
        sys.exit(1)
    
    # Test 2: Bot token validity
    if not test_bot_token(bot_token):
        print("\n❌ Bot token test failed. Please check your BOT_TOKEN.")
        sys.exit(1)
    
    # Test 3: Send test message
    if not test_send_message(bot_token, chat_id):
        print("\n❌ Message sending test failed. Please check the errors above.")
        sys.exit(1)
    
    # Test 4: Pollinations AI
    test_pollinations_api()
    
    # Final summary
    print("\n" + "=" * 60)
    print("🎉 ALL TESTS PASSED!")
    print("=" * 60)
    print("Your bot is properly configured and ready to post jokes!")
    print("\nNext steps:")
    print("  1. Check your Telegram channel for the test message")
    print("  2. Run the bot: python -m src.main")
    print("  3. Push to GitHub to enable scheduled posts")
    print("\n✨ Happy joke posting! ✨\n")


if __name__ == "__main__":
    main()
