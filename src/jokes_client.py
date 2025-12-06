"""
Jokes API Client - Fetches jokes from multiple free APIs
No API keys required!
"""
import requests
import random


class JokesClient:
    """Client for fetching jokes from various free APIs"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_random_joke(self):
        """Get a random joke from JokeAPI (supports multiple categories)"""
        try:
            url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
            response = self.session.get(url, timeout=10)
            data = response.json()
            
            if data.get('error'):
                return None
            
            # Handle both single and two-part jokes
            if data.get('type') == 'single':
                return {
                    'joke': data.get('setup', data.get('joke', '')),
                    'category': data.get('category', 'General'),
                    'type': 'single'
                }
            else:
                return {
                    'setup': data.get('setup', ''),
                    'delivery': data.get('delivery', ''),
                    'category': data.get('category', 'General'),
                    'type': 'twopart'
                }
        except Exception as e:
            print(f"Error fetching joke from JokeAPI: {e}")
            return None
    
    def get_dad_joke(self):
        """Get a dad joke from icanhazdadjoke API"""
        try:
            url = "https://icanhazdadjoke.com/"
            headers = {'Accept': 'application/json'}
            response = self.session.get(url, headers=headers, timeout=10)
            data = response.json()
            
            return {
                'joke': data.get('joke', ''),
                'category': 'Dad Joke',
                'type': 'single'
            }
        except Exception as e:
            print(f"Error fetching dad joke: {e}")
            return None
    
    def get_programming_joke(self):
        """Get a programming joke"""
        try:
            url = "https://official-joke-api.appspot.com/jokes/programming/random"
            response = self.session.get(url, timeout=10)
            data = response.json()
            
            if data and len(data) > 0:
                joke = data[0]
                return {
                    'setup': joke.get('setup', ''),
                    'delivery': joke.get('punchline', ''),
                    'category': 'Programming',
                    'type': 'twopart'
                }
        except Exception as e:
            print(f"Error fetching programming joke: {e}")
            return None
    
    def get_chuck_norris_joke(self):
        """Get a Chuck Norris joke"""
        try:
            url = "https://api.chucknorris.io/jokes/random"
            response = self.session.get(url, timeout=10)
            data = response.json()
            
            return {
                'joke': data.get('value', ''),
                'category': 'Chuck Norris',
                'type': 'single'
            }
        except Exception as e:
            print(f"Error fetching Chuck Norris joke: {e}")
            return None
    
    def get_pun(self):
        """Get a pun from JokeAPI"""
        try:
            url = "https://v2.jokeapi.dev/joke/Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
            response = self.session.get(url, timeout=10)
            data = response.json()
            
            if data.get('error'):
                return None
            
            if data.get('type') == 'single':
                return {
                    'joke': data.get('joke', ''),
                    'category': 'Pun',
                    'type': 'single'
                }
            else:
                return {
                    'setup': data.get('setup', ''),
                    'delivery': data.get('delivery', ''),
                    'category': 'Pun',
                    'type': 'twopart'
                }
        except Exception as e:
            print(f"Error fetching pun: {e}")
            return None
    
    def get_any_joke(self):
        """Get a random joke from any available API"""
        joke_functions = [
            self.get_random_joke,
            self.get_dad_joke,
            self.get_programming_joke,
            self.get_chuck_norris_joke,
            self.get_pun
        ]
        
        # Try random APIs until we get a joke
        random.shuffle(joke_functions)
        for func in joke_functions:
            joke = func()
            if joke:
                return joke
        
        # Fallback joke if all APIs fail
        return {
            'joke': "Why don't scientists trust atoms? Because they make up everything! 😄",
            'category': 'Science',
            'type': 'single'
        }
    
    def format_joke(self, joke_data):
        """Format joke data into a nice message"""
        if not joke_data:
            return "😅 Couldn't fetch a joke right now. Try again!"
        
        category = joke_data.get('category', 'General')
        
        # Emoji mapping for categories
        emoji_map = {
            'Programming': '💻',
            'Dad Joke': '👨',
            'Pun': '🎭',
            'Chuck Norris': '🥋',
            'Misc': '🎲',
            'Dark': '🌑',
            'General': '😄'
        }
        
        emoji = emoji_map.get(category, '😂')
        
        if joke_data.get('type') == 'single':
            joke_text = joke_data.get('joke', '')
            message = f"{emoji} **{category} Joke**\n\n{joke_text}\n\n😂 Hope that made you laugh!"
        else:
            setup = joke_data.get('setup', '')
            delivery = joke_data.get('delivery', '')
            message = f"{emoji} **{category} Joke**\n\n{setup}\n\n...{delivery}\n\n😂 Hope that made you laugh!"
        
        return message
    
    def get_joke_of_the_day(self):
        """Get a specially curated joke"""
        # Mix of different joke types for variety
        joke_types = [
            self.get_dad_joke,
            self.get_random_joke,
            self.get_pun,
            self.get_programming_joke
        ]
        
        func = random.choice(joke_types)
        return func()


# Global instance
jokes_client = JokesClient()
