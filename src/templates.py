"""
AI Prompt Templates for Jokes & Memes Content Generation
"""

TEXT_TEMPLATES = {
    "funny_joke": (
        "Create an absolutely hilarious, relatable joke that feels natural and human. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '😂 Joke of the Day' at the top\n"
        "- The joke itself (setup and punchline)\n"
        "- Use emojis for extra fun\n"
        "- Keep it clean but genuinely funny\n"
        "Make it feel like a friend telling a joke, not AI-generated. "
        "Topics: everyday life, relationships, work, technology, food, etc. "
        "Under 100 words."
    ),
    "dad_joke": (
        "Create a classic dad joke - corny, punny, and groan-worthy in the best way! "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '👨 Dad Joke Alert!' at the top\n"
        "- The joke with setup and punchline\n"
        "- Use emojis like 😄🤦‍♂️\n"
        "Make it wholesome and family-friendly. The cornier, the better! "
        "Under 80 words."
    ),
    "meme_caption": (
        "Create a hilarious meme caption that's relatable and shareable. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** at the top\n"
        "- The meme text/caption\n"
        "- Use emojis\n"
        "Make it about everyday struggles, funny observations, or relatable moments. "
        "Think: Monday mornings, procrastination, food cravings, social awkwardness. "
        "Under 100 words."
    ),
    "pun_joke": (
        "Create a clever pun that makes people laugh and groan at the same time! "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '🎭 Pun Time!' at the top\n"
        "- The pun joke\n"
        "- Use emojis\n"
        "Make it witty and clever. Word play is key! "
        "Under 80 words."
    ),
    "observational_humor": (
        "Share a funny observation about everyday life that everyone can relate to. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '🤔 Ever Notice...' at the top\n"
        "- The funny observation\n"
        "- Use emojis\n"
        "Think: weird habits, funny coincidences, relatable struggles. "
        "Make it feel like a stand-up comedy bit. "
        "Under 120 words."
    ),
    "tech_humor": (
        "Create a funny joke about technology, programming, or internet culture. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '💻 Tech Humor' at the top\n"
        "- The joke\n"
        "- Use emojis like 💻🤖🔌\n"
        "Topics: coding bugs, WiFi problems, autocorrect fails, tech support. "
        "Make it relatable to anyone who uses technology. "
        "Under 100 words."
    ),
    "food_humor": (
        "Create a funny joke about food, eating, or cooking. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '🍕 Food Humor' at the top\n"
        "- The joke\n"
        "- Use food emojis\n"
        "Topics: pizza, coffee addiction, diet struggles, cooking fails. "
        "Make it deliciously funny! "
        "Under 100 words."
    ),
    "animal_joke": (
        "Create a cute and funny joke about animals. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '🐶 Animal Humor' at the top\n"
        "- The joke\n"
        "- Use animal emojis\n"
        "Make it wholesome and adorable while being funny. "
        "Under 80 words."
    ),
    "work_humor": (
        "Create a relatable joke about work, office life, or career struggles. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '💼 Work Life' at the top\n"
        "- The joke\n"
        "- Use emojis like 💼😴☕\n"
        "Topics: Monday blues, meetings, deadlines, coffee addiction. "
        "Make it super relatable! "
        "Under 100 words."
    ),
    "relationship_humor": (
        "Create a funny, lighthearted joke about relationships or dating. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '💑 Relationship Humor' at the top\n"
        "- The joke\n"
        "- Use emojis like ❤️😅💕\n"
        "Keep it wholesome and relatable. No mean-spirited content. "
        "Under 100 words."
    ),
    "random_fact_funny": (
        "Share a weird, funny, or mind-blowing fact with a humorous twist. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '🤯 Did You Know?' at the top\n"
        "- The funny fact\n"
        "- Add a humorous comment about it\n"
        "- Use emojis\n"
        "Make it educational AND entertaining. "
        "Under 100 words."
    ),
    "thread_jokes": (
        "Create a mini joke thread with 3-4 connected funny observations or jokes. "
        "FORMAT STRICTLY AS:\n"
        "**😂 Joke Thread 🧵**\n\n"
        "**1️⃣** [First joke/observation]\n\n"
        "**2️⃣** [Second joke/observation]\n\n"
        "**3️⃣** [Third joke/observation]\n\n"
        "**4️⃣** [Fourth joke/observation]\n\n"
        "Make them flow together thematically. Use emojis!"
    ),
    "poll_question": (
        "Create ONE funny multiple choice question for a poll. "
        "Format strictly as: Question? | Option A, Option B, Option C, Option D. "
        "Make it lighthearted and fun. "
        "Examples: 'What's the best pizza topping?', 'Which superpower would you choose?'"
    ),
    "daily_challenge": (
        "Create a fun daily challenge or riddle. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '🎯 Daily Challenge!' at the top\n"
        "- The challenge or riddle\n"
        "- Use emojis\n"
        "- End with an encouraging message\n"
        "Make it engaging and fun! "
        "Under 100 words."
    ),
    "motivational_funny": (
        "Create a motivational message with a funny twist. "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '💪 Motivation Monday' at the top\n"
        "- Inspirational message with humor\n"
        "- Use emojis\n"
        "Make people smile while inspiring them! "
        "Under 100 words."
    ),
    "shower_thoughts": (
        "Share a funny 'shower thought' - those random deep thoughts that make you go 'hmm...' "
        "FORMAT YOUR RESPONSE WITH:\n"
        "- A **bold heading** like '🚿 Shower Thought' at the top\n"
        "- The thought\n"
        "- Use emojis like 🤔💭\n"
        "Make it mind-bending and funny! "
        "Under 80 words."
    )
}


IMAGE_TEMPLATES = {
    "laughing_emoji": "3D rendered laughing emoji with tears of joy, vibrant yellow, glossy finish, fun and playful style, white background",
    "funny_cat": "hilarious cat making a funny face, meme style, bright colors, photorealistic with exaggerated expression",
    "dog_meme": "adorable dog with funny expression wearing sunglasses, meme template style, colorful background",
    "office_humor": "funny office scene with stressed worker surrounded by coffee cups and papers, cartoon illustration style, relatable humor",
    "monday_mood": "exhausted person vs energetic person, split screen meme style, Monday vs Friday vibes, colorful illustration",
    "food_meme": "person dramatically reaching for pizza, funny exaggerated style, vibrant colors, meme aesthetic",
    "procrastination": "person avoiding work by doing random things, funny cartoon style, relatable humor illustration",
    "coffee_addict": "person hugging giant coffee cup with hearts, cute illustration style, warm brown colors",
    "gym_humor": "person struggling at gym vs eating donuts, funny contrast meme, bright colors",
    "sleep_meme": "person sleeping vs alarm clock battle, funny illustration, relatable morning struggle",
    "wifi_struggle": "person desperately searching for WiFi signal, funny tech humor illustration, modern style",
    "pizza_love": "person in love with pizza slice, romantic comedy style, warm colors, funny and cute",
    "weekend_vibes": "happy person celebrating weekend, energetic and fun illustration, bright colors",
    "study_procrastination": "student with books vs phone distraction, funny relatable meme style",
    "pet_humor": "cat or dog doing something hilariously human-like, cute and funny, photorealistic style",
}
