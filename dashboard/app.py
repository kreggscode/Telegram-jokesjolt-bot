"""
Flask Dashboard for Manual Jokes & Memes Bot Control
"""
import os
import random
from flask import Flask, render_template, redirect, url_for, flash
from dotenv import load_dotenv

# Allow dashboard to use same bot config
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"), override=False)

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src import telegram_client as tg
from src import pollinations_client as ai
from src.templates import TEXT_TEMPLATES, IMAGE_TEMPLATES
from src.jokes_client import jokes_client

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")


@app.route("/")
def index():
    return render_template("dashboard.html")


# ============ REAL JOKES FROM APIs ============

@app.route("/send/api-joke")
def send_api_joke():
    joke_data = jokes_client.get_any_joke()
    message = jokes_client.format_joke(joke_data)
    tg.send_text(message)
    flash("😂 Random joke sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/dad-joke")
def send_dad_joke():
    joke_data = jokes_client.get_dad_joke()
    if joke_data:
        message = jokes_client.format_joke(joke_data)
        tg.send_text(message)
        flash("👨 Dad joke sent!", "success")
    else:
        text = ai.generate_text(TEXT_TEMPLATES["dad_joke"])
        tg.send_text(text)
        flash("👨 Dad joke sent (AI-generated)!", "success")
    return redirect(url_for("index"))


@app.route("/send/programming-joke")
def send_programming_joke():
    joke_data = jokes_client.get_programming_joke()
    if joke_data:
        message = jokes_client.format_joke(joke_data)
        tg.send_text(message)
        flash("💻 Programming joke sent!", "success")
    else:
        text = ai.generate_text(TEXT_TEMPLATES["tech_humor"])
        tg.send_text(text)
        flash("💻 Tech joke sent (AI-generated)!", "success")
    return redirect(url_for("index"))


@app.route("/send/pun")
def send_pun():
    joke_data = jokes_client.get_pun()
    if joke_data:
        message = jokes_client.format_joke(joke_data)
        tg.send_text(message)
        flash("🎭 Pun sent!", "success")
    else:
        text = ai.generate_text(TEXT_TEMPLATES["pun_joke"])
        tg.send_text(text)
        flash("🎭 Pun sent (AI-generated)!", "success")
    return redirect(url_for("index"))


@app.route("/send/chuck-norris")
def send_chuck_norris():
    joke_data = jokes_client.get_chuck_norris_joke()
    if joke_data:
        message = jokes_client.format_joke(joke_data)
        tg.send_text(message)
        flash("🥋 Chuck Norris joke sent!", "success")
    else:
        flash("❌ Failed to fetch Chuck Norris joke", "error")
    return redirect(url_for("index"))


# ============ AI-GENERATED HUMOR ============

@app.route("/send/funny-joke")
def send_funny_joke():
    text = ai.generate_text(TEXT_TEMPLATES["funny_joke"])
    tg.send_text(text)
    flash("😄 Funny joke sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/tech-humor")
def send_tech_humor():
    text = ai.generate_text(TEXT_TEMPLATES["tech_humor"])
    tg.send_text(text)
    flash("💻 Tech humor sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/food-humor")
def send_food_humor():
    text = ai.generate_text(TEXT_TEMPLATES["food_humor"])
    tg.send_text(text)
    flash("🍕 Food humor sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/animal-joke")
def send_animal_joke():
    text = ai.generate_text(TEXT_TEMPLATES["animal_joke"])
    tg.send_text(text)
    flash("🐶 Animal joke sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/work-humor")
def send_work_humor():
    text = ai.generate_text(TEXT_TEMPLATES["work_humor"])
    tg.send_text(text)
    flash("💼 Work humor sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/relationship-humor")
def send_relationship_humor():
    text = ai.generate_text(TEXT_TEMPLATES["relationship_humor"])
    tg.send_text(text)
    flash("💑 Relationship humor sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/observational-humor")
def send_observational_humor():
    text = ai.generate_text(TEXT_TEMPLATES["observational_humor"])
    tg.send_text(text)
    flash("🤔 Observational humor sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/shower-thought")
def send_shower_thought():
    text = ai.generate_text(TEXT_TEMPLATES["shower_thoughts"])
    tg.send_text(text)
    flash("🚿 Shower thought sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/random-fact")
def send_random_fact():
    text = ai.generate_text(TEXT_TEMPLATES["random_fact_funny"])
    tg.send_text(text)
    flash("🤯 Random fact sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/motivational")
def send_motivational():
    text = ai.generate_text(TEXT_TEMPLATES["motivational_funny"])
    tg.send_text(text)
    flash("💪 Motivational humor sent!", "success")
    return redirect(url_for("index"))


# ============ VISUAL CONTENT ============

@app.route("/send/meme-with-image")
def send_meme_with_image():
    # Random meme image and caption
    selected_image = random.choice(list(IMAGE_TEMPLATES.keys()))
    caption_options = [
        "meme_caption", "funny_joke", "observational_humor",
        "work_humor", "food_humor", "tech_humor"
    ]
    selected_caption = random.choice(caption_options)
    
    caption = ai.generate_text(TEXT_TEMPLATES[selected_caption])
    img_url = ai.image_url(IMAGE_TEMPLATES[selected_image])
    tg.send_photo(img_url, caption)
    flash("🎨 Meme with image sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/joke-with-image")
def send_joke_with_image():
    # Real joke with funny image
    joke_data = jokes_client.get_any_joke()
    caption = jokes_client.format_joke(joke_data)
    
    selected_image = random.choice(list(IMAGE_TEMPLATES.keys()))
    img_url = ai.image_url(IMAGE_TEMPLATES[selected_image])
    tg.send_photo(img_url, caption)
    flash("😂 Joke with image sent!", "success")
    return redirect(url_for("index"))


# ============ INTERACTIVE CONTENT ============

@app.route("/send/daily-challenge")
def send_daily_challenge():
    text = ai.generate_text(TEXT_TEMPLATES["daily_challenge"])
    tg.send_text(text)
    flash("🎯 Daily challenge sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/poll")
def send_poll():
    raw = ai.generate_text(TEXT_TEMPLATES["poll_question"])
    if "|" in raw:
        q_part, opts_part = raw.split("|", 1)
        question = q_part.strip()
        options = [o.strip() for o in opts_part.split(",") if o.strip()]
        if len(options) >= 2:
            tg.send_poll(question, options[:10])
            flash("📊 Poll sent!", "success")
        else:
            # Fallback poll
            tg.send_poll(
                "What makes you laugh the most? 😂",
                ["Dad Jokes 👨", "Memes 🖼️", "Puns 🎭", "Animal Videos 🐶"]
            )
            flash("📊 Fallback poll sent!", "success")
    else:
        # Fallback poll
        tg.send_poll(
            "What's your favorite way to relax? 😌",
            ["Netflix & Chill 📺", "Sleep 😴", "Food 🍕", "Memes 😂"]
        )
        flash("📊 Fallback poll sent!", "success")
    return redirect(url_for("index"))


@app.route("/send/thread")
def send_thread():
    raw = ai.generate_text(TEXT_TEMPLATES["thread_jokes"])
    parts = [p.strip() for p in raw.split("\n\n") if p.strip()]
    if parts:
        tg.send_thread(parts)
        flash("🧵 Joke thread sent!", "success")
    else:
        flash("Thread generation failed.", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

