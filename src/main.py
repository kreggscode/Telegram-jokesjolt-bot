"""
Main Bot Logic - Jokes & Memes Bot
Spreads laughter and joy with hilarious jokes and memes!
"""
from . import pollinations_client as ai
from . import telegram_client as tg
from . import scheduler_logic as sched
from .templates import TEXT_TEMPLATES, IMAGE_TEMPLATES
from .jokes_client import jokes_client
import random


def post_api_joke():
    """Post a joke from real joke APIs"""
    print("Fetching joke from API...")
    joke_data = jokes_client.get_any_joke()
    message = jokes_client.format_joke(joke_data)
    tg.send_text(message)


def post_dad_joke():
    """Post a classic dad joke"""
    print("Fetching dad joke...")
    joke_data = jokes_client.get_dad_joke()
    if joke_data:
        message = jokes_client.format_joke(joke_data)
        tg.send_text(message)
    else:
        # Fallback to AI-generated dad joke
        prompt = TEXT_TEMPLATES["dad_joke"]
        text = ai.generate_text(prompt)
        tg.send_text(text)


def post_programming_joke():
    """Post a programming/tech joke"""
    print("Fetching programming joke...")
    joke_data = jokes_client.get_programming_joke()
    if joke_data:
        message = jokes_client.format_joke(joke_data)
        tg.send_text(message)
    else:
        # Fallback to AI-generated tech humor
        prompt = TEXT_TEMPLATES["tech_humor"]
        text = ai.generate_text(prompt)
        tg.send_text(text)


def post_pun():
    """Post a clever pun"""
    print("Fetching pun...")
    joke_data = jokes_client.get_pun()
    if joke_data:
        message = jokes_client.format_joke(joke_data)
        tg.send_text(message)
    else:
        # Fallback to AI-generated pun
        prompt = TEXT_TEMPLATES["pun_joke"]
        text = ai.generate_text(prompt)
        tg.send_text(text)


def post_funny_joke():
    """Post AI-generated funny joke"""
    prompt = TEXT_TEMPLATES["funny_joke"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_tech_humor():
    """Post tech/programming humor"""
    prompt = TEXT_TEMPLATES["tech_humor"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_food_humor():
    """Post food-related humor"""
    prompt = TEXT_TEMPLATES["food_humor"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_animal_joke():
    """Post cute animal jokes"""
    prompt = TEXT_TEMPLATES["animal_joke"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_work_humor():
    """Post relatable work humor"""
    prompt = TEXT_TEMPLATES["work_humor"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_relationship_humor():
    """Post lighthearted relationship humor"""
    prompt = TEXT_TEMPLATES["relationship_humor"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_observational_humor():
    """Post observational comedy"""
    prompt = TEXT_TEMPLATES["observational_humor"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_random_fact():
    """Post funny random facts"""
    prompt = TEXT_TEMPLATES["random_fact_funny"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_shower_thought():
    """Post funny shower thoughts"""
    prompt = TEXT_TEMPLATES["shower_thoughts"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_motivational_funny():
    """Post motivational content with humor"""
    prompt = TEXT_TEMPLATES["motivational_funny"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_daily_challenge():
    """Post a fun daily challenge or riddle"""
    prompt = TEXT_TEMPLATES["daily_challenge"]
    text = ai.generate_text(prompt)
    tg.send_text(text)


def post_meme_with_image():
    """Post a hilarious meme with AI-generated image"""
    # Select random meme template
    image_keys = list(IMAGE_TEMPLATES.keys())
    selected_image = random.choice(image_keys)
    
    # Select random caption type
    caption_options = [
        "meme_caption", "funny_joke", "observational_humor",
        "work_humor", "food_humor", "tech_humor"
    ]
    selected_caption = random.choice(caption_options)
    
    text_prompt = TEXT_TEMPLATES[selected_caption]
    img_prompt = IMAGE_TEMPLATES[selected_image]

    caption = ai.generate_text(text_prompt)
    img_url = ai.image_url(img_prompt)

    tg.send_photo(img_url, caption)


def post_joke_with_image():
    """Post a joke with a funny image"""
    # Get a real joke from API
    joke_data = jokes_client.get_any_joke()
    caption = jokes_client.format_joke(joke_data)
    
    # Select a fun image
    image_keys = list(IMAGE_TEMPLATES.keys())
    selected_image = random.choice(image_keys)
    img_prompt = IMAGE_TEMPLATES[selected_image]
    img_url = ai.image_url(img_prompt)
    
    tg.send_photo(img_url, caption)


def post_poll():
    """Post a fun poll"""
    poll_prompt = TEXT_TEMPLATES["poll_question"]
    raw = ai.generate_text(poll_prompt)

    # Expect format: "Question? | A, B, C, D"
    if "|" in raw:
        q_part, opts_part = raw.split("|", 1)
        question = q_part.strip()
        options = [o.strip() for o in opts_part.split(",") if o.strip()]
        if len(options) >= 2:
            tg.send_poll(question, options[:10])
        else:
            # Fallback poll
            tg.send_poll(
                "What's your favorite way to relax? 😌",
                ["Netflix & Chill 📺", "Sleep 😴", "Food 🍕", "Memes 😂"]
            )
    else:
        # Fallback poll
        tg.send_poll(
            "What makes you laugh the most? 😂",
            ["Dad Jokes 👨", "Memes 🖼️", "Puns 🎭", "Animal Videos 🐶"]
        )


def post_thread():
    """Post a thread of connected jokes"""
    thread_prompt = TEXT_TEMPLATES["thread_jokes"]
    raw = ai.generate_text(thread_prompt)
    # Split by double-newline into sections
    parts = [p.strip() for p in raw.split("\n\n") if p.strip()]
    if len(parts) == 0:
        tg.send_text(raw)
    else:
        tg.send_thread(parts)


def main():
    """Main entry point - decides what type of post to make"""
    post_type = sched.decide_post_type()
    print(f"Decided post type: {post_type}")

    # Map post types to functions
    post_functions = {
        "api_joke": post_api_joke,
        "dad_joke": post_dad_joke,
        "programming_joke": post_programming_joke,
        "pun": post_pun,
        "funny_joke": post_funny_joke,
        "tech_humor": post_tech_humor,
        "food_humor": post_food_humor,
        "animal_joke": post_animal_joke,
        "work_humor": post_work_humor,
        "relationship_humor": post_relationship_humor,
        "observational_humor": post_observational_humor,
        "random_fact": post_random_fact,
        "shower_thought": post_shower_thought,
        "motivational_funny": post_motivational_funny,
        "daily_challenge": post_daily_challenge,
        "meme_with_image": post_meme_with_image,
        "joke_with_image": post_joke_with_image,
        "poll": post_poll,
        "thread": post_thread,
    }

    # Execute the selected post function
    post_function = post_functions.get(post_type)
    if post_function:
        post_function()
    else:
        tg.send_text(f"No valid post type decided: {post_type}")


if __name__ == "__main__":
    main()

