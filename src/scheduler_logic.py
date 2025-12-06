"""
Scheduler Logic - Determines what type of content to post based on time
Optimized for jokes and memes content with 4-6 posts per day
"""
from datetime import datetime, timedelta
from .config import TIMEZONE_OFFSET_HOURS
import random


def get_local_hour_24() -> int:
    """Return current local hour (0-23) based on TIMEZONE_OFFSET_HOURS."""
    now_utc = datetime.utcnow()
    local = now_utc + timedelta(hours=TIMEZONE_OFFSET_HOURS)
    return local.hour


def decide_post_type() -> str:
    """
    Decide what to post based on hour.
    Posts 4-6 times per day optimized for jokes and memes:
    - Morning (7-9 AM): Motivational & Dad Jokes (Start the day with a smile!)
    - Mid-Morning (10-12 PM): API Jokes & Puns (Fresh jokes from APIs)
    - Afternoon (2-4 PM): Work Humor & Tech Jokes (Relatable content)
    - Evening (6-8 PM): Memes with Images (Visual content - HIGH ENGAGEMENT)
    - Night (9-11 PM): Random Jokes & Fun Facts (Variety)
    - Late Night (11 PM-1 AM): Shower Thoughts & Observational Humor

    Returns one of:
    - "api_joke" (Real jokes from APIs)
    - "dad_joke" (Classic dad jokes)
    - "programming_joke" (Tech/coding humor)
    - "pun" (Clever puns)
    - "funny_joke" (AI-generated jokes)
    - "tech_humor" (Technology jokes)
    - "food_humor" (Food-related jokes)
    - "animal_joke" (Cute animal humor)
    - "work_humor" (Office/work jokes)
    - "relationship_humor" (Dating/relationship jokes)
    - "observational_humor" (Stand-up style observations)
    - "random_fact" (Funny facts)
    - "shower_thought" (Mind-bending thoughts)
    - "motivational_funny" (Motivation with humor)
    - "daily_challenge" (Fun challenges)
    - "meme_with_image" (Memes with AI images)
    - "joke_with_image" (Jokes with images)
    - "poll" (Interactive polls)
    - "thread" (Joke threads)
    """
    hour = get_local_hour_24()

    # Morning Post (7-9 AM): MOTIVATIONAL & DAD JOKES (Start the day right!)
    if 7 <= hour < 9:
        morning_options = [
            "motivational_funny", "dad_joke", "api_joke",
            "funny_joke", "animal_joke"
        ]
        return random.choice(morning_options)
    
    # Mid-Morning Post (10-12 PM): API JOKES & PUNS (Fresh content)
    elif 10 <= hour < 12:
        mid_morning_options = [
            "api_joke", "pun", "programming_joke",
            "dad_joke", "random_fact"
        ]
        return random.choice(mid_morning_options)
    
    # Afternoon Post (2-4 PM): WORK & TECH HUMOR (Relatable!)
    elif 14 <= hour < 16:
        afternoon_options = [
            "work_humor", "tech_humor", "food_humor",
            "observational_humor", "api_joke"
        ]
        return random.choice(afternoon_options)
    
    # Evening Post (6-8 PM): MEMES WITH IMAGES (High engagement time!)
    elif 18 <= hour < 20:
        # 70% chance of visual content
        evening_weighted = (
            ["meme_with_image"] * 5 +
            ["joke_with_image"] * 2 +
            ["poll", "thread", "daily_challenge"]
        )
        return random.choice(evening_weighted)
    
    # Night Post (9-11 PM): VARIETY (Keep it fun!)
    elif 21 <= hour < 23:
        night_options = [
            "api_joke", "relationship_humor", "animal_joke",
            "funny_joke", "pun", "meme_with_image"
        ]
        return random.choice(night_options)
    
    # Late Night Post (11 PM-1 AM): SHOWER THOUGHTS & DEEP HUMOR
    elif 23 <= hour < 24 or 0 <= hour < 1:
        late_night_options = [
            "shower_thought", "observational_humor", "random_fact",
            "thread", "api_joke"
        ]
        return random.choice(late_night_options)
    
    # Fallback for manual runs outside scheduled times
    else:
        all_options = [
            "api_joke", "dad_joke", "programming_joke", "pun",
            "funny_joke", "tech_humor", "food_humor", "animal_joke",
            "work_humor", "relationship_humor", "observational_humor",
            "random_fact", "shower_thought", "motivational_funny",
            "daily_challenge", "meme_with_image", "joke_with_image",
            "poll", "thread"
        ]
        return random.choice(all_options)

