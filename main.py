import os
import random
import time
import logging

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ========== Basic Config ==========
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# ========== Menus ==========
def main_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("🌤 Daily Start", callback_data="menu_day")],
        [
            InlineKeyboardButton("✅ Habits & Goals", callback_data="menu_habit"),
            InlineKeyboardButton("😊 Mood & Emotions", callback_data="menu_mood"),
        ],
        [
            InlineKeyboardButton("🧠 Quizzes & Q&A", callback_data="menu_quiz"),
            InlineKeyboardButton("📚 Light Reading", callback_data="menu_read"),
        ],
        [InlineKeyboardButton("🎲 Random Tools", callback_data="menu_random")],
    ]
    return InlineKeyboardMarkup(keyboard)


def day_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("📅 Daily Quote", callback_data="day_sentence"),
            InlineKeyboardButton("📋 Daily Tip", callback_data="day_tip"),
        ],
        [InlineKeyboardButton("🧭 Daily Direction", callback_data="day_direction")],
        [InlineKeyboardButton("⬅ Back to Home", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def habit_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("✅ Small Goal", callback_data="habit_goal"),
            InlineKeyboardButton("🔁 Habit Micro‑Action", callback_data="habit_action"),
        ],
        [
            InlineKeyboardButton("🧹 Mini Clean‑up", callback_data="habit_clean"),
            InlineKeyboardButton("🚶 Micro Movement", callback_data="habit_move"),
        ],
        [InlineKeyboardButton("⬅ Back to Home", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def mood_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("💬 Mood Quote", callback_data="mood_text"),
            InlineKeyboardButton("🎨 Mood Color", callback_data="mood_color"),
        ],
        [
            InlineKeyboardButton("🧘 Simple Relax", callback_data="mood_relax"),
            InlineKeyboardButton("❤️ Self‑Care", callback_data="mood_selfcare"),
        ],
        [InlineKeyboardButton("⬅ Back to Home", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def quiz_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("🧠 Think Question", callback_data="quiz_think"),
            InlineKeyboardButton("🔢 Number Test", callback_data="quiz_number"),
        ],
        [InlineKeyboardButton("👀 Reaction Speed", callback_data="quiz_reaction")],
        [InlineKeyboardButton("⬅ Back to Home", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def read_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("📖 Gentle Sentence", callback_data="read_soft"),
            InlineKeyboardButton("💡 Idea Spark", callback_data="read_idea"),
        ],
        [InlineKeyboardButton("📝 Reflection Question", callback_data="read_question")],
        [InlineKeyboardButton("⬅ Back to Home", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def random_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("🎲 Random Number", callback_data="rand_number"),
            InlineKeyboardButton("😊 Random Emoji", callback_data="rand_emoji"),
        ],
        [
            InlineKeyboardButton("📌 Random Task", callback_data="rand_task"),
            InlineKeyboardButton("✨ Random Inspiration", callback_data="rand_inspire"),
        ],
        [InlineKeyboardButton("⬅ Back to Home", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


# ========== /start /help /about ==========
START_TEXT = (
    "👋 Welcome to *Light Time · Life Hub*!\n\n"
    "This is a bot focused on *small daily goals, emotional care, light quizzes, and random inspiration*.\n\n"
    "You can:\n"
    "🌤 Get gentle tips to start your day\n"
    "✅ Generate small goals and habit micro‑actions\n"
    "😊 Express your mood with words or colors\n"
    "🧠 Try light thinking questions and mini tests\n"
    "📚 Read gentle sentences and reflections\n"
    "🎲 Get random numbers, emojis, tasks, or inspiration\n\n"
    "This bot provides only relaxed, healthy text interactions. No money, rewards, gambling, investment, or sensitive content involved.\n\n"
    "👇 Use the buttons below to choose what you want to try now:"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            START_TEXT, reply_markup=main_menu(), parse_mode="Markdown"
        )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📝 How to Use\n\n"
        "• Send /start to open the main menu\n"
        "• Use the buttons to explore different modules\n"
        "• Each button gives a short text or interaction\n"
        "• If the interface freezes, send /start to reset\n"
    )
    await update.message.reply_text(text)


async def about_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "ℹ️ About *Light Time · Life Hub*\n\n"
        "A small bot to help you relax in short moments:\n"
        "• Gentle goals and micro‑tasks for small progress\n"
        "• Emotional tools to care for your mood\n"
        "• Light quizzes and reading to refresh your mind\n"
        "All content is healthy, non‑commercial, and text‑only."
    )
    await update.message.reply_text(text, parse_mode="Markdown")


# ========== Button Router ==========
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == "menu_main":
        await query.edit_message_text("🏠 Back to Home:", reply_markup=main_menu())
        return
    if data == "menu_day":
        await query.edit_message_text("🌤 Daily Start:", reply_markup=day_menu())
        return
    if data == "menu_habit":
        await query.edit_message_text("✅ Habits & Goals:", reply_markup=habit_menu())
        return
    if data == "menu_mood":
        await query.edit_message_text("😊 Mood & Emotions:", reply_markup=mood_menu())
        return
    if data == "menu_quiz":
        await query.edit_message_text("🧠 Quizzes & Q&A:", reply_markup=quiz_menu())
        return
    if data == "menu_read":
        await query.edit_message_text("📚 Light Reading:", reply_markup=read_menu())
        return
    if data == "menu_random":
        await query.edit_message_text("🎲 Random Tools:", reply_markup=random_menu())
        return

    # Daily Start
    if data == "day_sentence":
        sentences = [
            "You can go slowly today, just don’t stop.",
            "A very small goal for today is more than enough.",
            "Even eating one good meal counts as living well.",
        ]
        await query.edit_message_text(
            "📅 Daily Quote:\n\n" + random.choice(sentences),
            reply_markup=day_menu(),
        )
        return

    if data == "day_tip":
        tips = [
            "Try using your phone a little less today and save some time for yourself.",
            "Pick one small corner to tidy up for just 3 minutes.",
            "If today feels busy, sort tasks into ‘must do’ and ‘can wait’.",
        ]
        await query.edit_message_text(
            "📋 Daily Tip:\n\n" + random.choice(tips),
            reply_markup=day_menu(),
        )
        return

    if data == "day_direction":
        directions = [
            "Treat today as a ‘foundation day’ and do small things that help long‑term.",
            "Treat today as an ‘adjustment day’ and allow yourself to slow down.",
            "Treat today as an ‘experiment day’ and try one small new thing.",
        ]
        await query.edit_message_text(
            "🧭 Daily Direction:\n\n" + random.choice(directions),
            reply_markup=day_menu(),
        )
        return

    # Habits & Goals
    if data == "habit_goal":
        goals = [
            "Complete one small goal that takes only 5 minutes.",
            "Focus on just one thing that matters most to you today.",
            "Set a goal of ‘done is enough, not perfect’.",
        ]
        await query.edit_message_text(
            "✅ Small Goal:\n\n" + random.choice(goals),
            reply_markup=habit_menu(),
        )
        return

    if data == "habit_action":
        actions = [
            "Drink a glass of water and say ‘good job’ to yourself.",
            "Stand up and stretch your shoulders for 30 seconds.",
            "Put away one item on your desk you don’t often use.",
        ]
        await query.edit_message_text(
            "🔁 Habit Micro‑Action:\n\n" + random.choice(actions),
            reply_markup=habit_menu(),
        )
        return

    if data == "habit_clean":
        texts = [
            "Choose one drawer or folder and remove a few unnecessary items in 2 minutes.",
            "Group scattered items neatly to make your space feel lighter.",
        ]
        await query.edit_message_text(
            "🧹 Mini Clean‑up:\n\n" + random.choice(texts),
            reply_markup=habit_menu(),
        )
        return

    if data == "habit_move":
        moves = [
            "Walk gently in place for 30 seconds.",
            "Take 10 slow deep breaths while rolling your shoulders.",
            "Stand up, walk to another room, then come back — a mini walk.",
        ]
        await query.edit_message_text(
            "🚶 Micro Movement:\n\n" + random.choice(moves),
            reply_markup=habit_menu(),
        )
        return

    # Mood & Emotions
    if data == "mood_text":
        moods = [
            "Feeling tired is okay — it means you’ve been trying.",
            "Your emotions change, but you’re always worthy of care.",
            "You’re allowed to have an ‘off’ day.",
        ]
        await query.edit_message_text(
            "💬 Mood Quote:\n\n" + random.choice(moods),
            reply_markup=mood_menu(),
        )
        return

    if data == "mood_color":
        colors = [
            "🔵 Blue mood: good for calm and organizing thoughts.",
            "🟢 Green mood: good for relaxing and listening to music.",
            "🟡 Yellow mood: good for chatting with friends.",
            "🟣 Purple mood: good for writing or creative thinking.",
        ]
        await query.edit_message_text(
            "🎨 Mood Color:\n\n" + random.choice(colors),
            reply_markup=mood_menu(),
        )
        return

    if data == "mood_relax":
        text = (
            "🧘 Simple Relaxation:\n\n"
            "1️⃣ Sit in a comfortable position\n"
            "2️⃣ Take 5 slow deep breaths\n"
            "3️⃣ With each exhale, imagine releasing a bit of tension\n"
        )
        await query.edit_message_text(text, reply_markup=mood_menu())
        return

    if data == "mood_selfcare":
        texts = [
            "You can be a little kinder to yourself — perfection isn’t required.",
            "Try giving yourself one small compliment today.",
        ]
        await query.edit_message_text(
            "❤️ Self‑Care:\n\n" + random.choice(texts),
            reply_markup=mood_menu(),
        )
        return

    # Quizzes
    if data == "quiz_think":
        qs = [
            "🧠 Think: What title would you give today?",
            "🧠 Think: What small progress are you quietly proud of lately?",
        ]
        await query.edit_message_text(random.choice(qs), reply_markup=quiz_menu())
        return

    if data == "quiz_number":
        number = random.randint(10, 99)
        text = f"🔢 Number Test:\n\nStart from {number} and subtract 3 each time in your head."
        await query.edit_message_text(text, reply_markup=quiz_menu())
        return

    if data == "quiz_reaction":
        context.user_data["reaction_start"] = time.time()
        keyboard = [
            [InlineKeyboardButton("⚡ Click Now!", callback_data="quiz_reaction_click")],
            [InlineKeyboardButton("⬅ Back", callback_data="menu_quiz")],
        ]
        await query.edit_message_text(
            "Click the button as fast as you can:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return

    if data == "quiz_reaction_click":
        start = context.user_data.get("reaction_start")
        if not start:
            msg = "Test expired. Please start again from the menu."
        else:
            ms = int((time.time() - start) * 1000)
            msg = f"🎯 Your reaction time: {ms} ms"
        await query.edit_message_text(msg, reply_markup=quiz_menu())
        return

    # Reading
    if data == "read_soft":
        sentences = [
            "You don’t have to be amazing all the time.",
            "Many things don’t need to be done all at once.",
        ]
        await query.edit_message_text(
            "📖 Gentle Sentence:\n\n" + random.choice(sentences),
            reply_markup=read_menu(),
        )
        return

    if data == "read_idea":
        ideas = [
            "Write down one small thing that felt good today.",
            "Write one line to your future self — just one line.",
        ]
        await query.edit_message_text(
            "💡 Idea Spark:\n\n" + random.choice(ideas),
            reply_markup=read_menu(),
        )
        return

    if data == "read_question":
        qs = [
            "📝 Reflection: If this week were weather, what would it be?",
            "📝 Reflection: What have you already improved compared to before?",
        ]
        await query.edit_message_text(random.choice(qs), reply_markup=read_menu())
        return

    # Random Tools
    if data == "rand_number":
        n = random.randint(0, 100)
        await query.edit_message_text(
            f"🎲 Random Number (0–100): {n}", reply_markup=random_menu()
        )
        return

    if data == "rand_emoji":
        emojis = ["😀", "😆", "😎", "🥳", "🤩", "🤗", "🙌", "🌈", "⭐", "✨", "🍀"]
        seq = " ".join(random.sample(emojis, 5))
        await query.edit_message_text(
            "😊 Random Emoji Combo:\n\n" + seq,
            reply_markup=random_menu(),
        )
        return

    if data == "rand_task":
        tasks = [
            "Take a photo of something that looks nice right now.",
            "Finish one small task within 3 minutes.",
            "Put your phone down for 2 minutes and do nothing.",
        ]
        await query.edit_message_text(
            "📌 Random Task:\n\n" + random.choice(tasks),
            reply_markup=random_menu(),
        )
        return

    if data == "rand_inspire":
        ins = [
            "Choose one theme word for today: slow / reset / light.",
            "Think of one thing that could make you feel better in 5 minutes.",
        ]
        await query.edit_message_text(
            "✨ Random Inspiration:\n\n" + random.choice(ins),
            reply_markup=random_menu(),
        )
        return

    await query.edit_message_text(
        "Command not supported. Send /start to return home.",
        reply_markup=main_menu(),
    )


# ========== Entry ==========
def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is not set!")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("about", about_cmd))
    app.add_handler(CallbackQueryHandler(button_handler))

    logger.info("Light Time · Life Hub Bot started")
    app.run_polling()


if __name__ == "__main__":
    main()
