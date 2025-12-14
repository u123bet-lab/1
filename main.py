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
            InlineKeyboardButton("✅ Habits & Mini Goals", callback_data="menu_habit"),
            InlineKeyboardButton("😊 Mood & Emotions", callback_data="menu_mood"),
        ],
        [
            InlineKeyboardButton("🧠 Mini Quiz & Q&A", callback_data="menu_quiz"),
            InlineKeyboardButton("📚 Light Reading", callback_data="menu_read"),
        ],
        [
            InlineKeyboardButton("🎲 Random Features", callback_data="menu_random"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def day_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("📅 Sentence of the Day", callback_data="day_sentence"),
            InlineKeyboardButton("📋 Daily Tip", callback_data="day_tip"),
        ],
        [
            InlineKeyboardButton("🧭 Daily Direction", callback_data="day_direction"),
        ],
        [InlineKeyboardButton("⬅ Back to Home", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def habit_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("✅ Mini Goal Generator", callback_data="habit_goal"),
            InlineKeyboardButton("🔁 Habit Micro Action", callback_data="habit_action"),
        ],
        [
            InlineKeyboardButton("🧹 Quick Tidy", callback_data="habit_clean"),
            InlineKeyboardButton("🚶 Micro Movement", callback_data="habit_move"),
        ],
        [InlineKeyboardButton("⬅ Back to Home", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(habit_menu)


def mood_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("💬 Mood Sentence", callback_data="mood_text"),
            InlineKeyboardButton("🎨 Mood Color", callback_data="mood_color"),
        ],
        [
            InlineKeyboardButton("🧘 Simple Relaxation", callback_data="mood_relax"),
            InlineKeyboardButton("❤️ Self Care", callback_data="mood_selfcare"),
        ],
        [InlineKeyboardButton("⬅ Back to Home", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def quiz_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("🧠 Thinking Question", callback_data="quiz_think"),
            InlineKeyboardButton("🔢 Number Test", callback_data="quiz_number"),
        ],
        [
            InlineKeyboardButton("👀 Reaction Speed", callback_data="quiz_reaction"),
        ],
        [InlineKeyboardButton("⬅ Back to Home", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(quiz_menu)


def read_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("📖 Gentle Sentence", callback_data="read_soft"),
            InlineKeyboardButton("💡 Idea Spark", callback_data="read_idea"),
        ],
        [
            InlineKeyboardButton("📝 Reflection Question", callback_data="read_question"),
        ],
        [InlineKeyboardButton("⬅ Back to Home", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(read_menu)


def random_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("🎲 Random Number", callback_data="rand_number"),
            InlineKeyboardButton("😊 Random Emojis", callback_data="rand_emoji"),
        ],
        [
            InlineKeyboardButton("📌 Random Task", callback_data="rand_task"),
            InlineKeyboardButton("✨ Random Inspiration", callback_data="rand_inspire"),
        ],
        [InlineKeyboardButton("⬅ Back to Home", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(random_menu)


# ========== /start /help /about ==========
START_TEXT = (
    "👋 Welcome to *Light Moments · Life Hub*!\n\n"
    "This is a Chinese-text-based bot focused on *daily mini goals, emotional care, light quizzes, and random inspiration*.\n\n"
    "Here you can:\n"
    "🌤 Get a gentle start for today\n"
    "✅ Generate simple goals and habit micro-actions\n"
    "😊 Express your mood with words or colors\n"
    "🧠 Try light thinking questions and mini tests\n"
    "📚 Read gentle sentences and reflection prompts\n"
    "🎲 Get random numbers, emojis, tasks, or inspiration\n\n"
    "This bot only provides light, healthy text interactions. No money, rewards, gambling, investment, or sensitive content is involved.\n\n"
    "👇 Use the buttons below to choose what you want to experience right now:"
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
        "• Use the buttons to enter different modules: Daily Start / Habits / Mood / Quiz / Reading / Random\n"
        "• Each button provides text or light interaction\n"
        "• If the interface freezes, send /start to return to home\n"
    )
    await update.message.reply_text(text)


async def about_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "ℹ️ About *Light Moments · Life Hub*\n\n"
        "This is a small bot designed to help you relax during fragmented moments:\n"
        "• Encourage tiny progress with mini goals\n"
        "• Take care of your mood with gentle tools\n"
        "• Activate your mind with light quizzes and reading\n"
        "All content is healthy, non-commercial, and free of sensitive information."
    )
    await update.message.reply_text(text)


# ========== Button Router ==========
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    # Menu navigation
    if data == "menu_main":
        await query.edit_message_text("🏠 Back to Home:", reply_markup=main_menu())
        return
    if data == "menu_day":
        await query.edit_message_text("🌤 Daily Start:", reply_markup=day_menu())
        return
    if data == "menu_habit":
        await query.edit_message_text("✅ Habits & Mini Goals:", reply_markup=habit_menu())
        return
    if data == "menu_mood":
        await query.edit_message_text("😊 Mood & Emotions:", reply_markup=mood_menu())
        return
    if data == "menu_quiz":
        await query.edit_message_text("🧠 Mini Quiz & Q&A:", reply_markup=quiz_menu())
        return
    if data == "menu_read":
        await query.edit_message_text("📚 Light Reading:", reply_markup=read_menu())
        return
    if data == "menu_random":
        await query.edit_message_text("🎲 Random Features:", reply_markup=random_menu())
        return

    # ===== Daily Start =====
    if data == "day_sentence":
        sentences = [
            "You can take it slow today, just don’t stop completely.",
            "A very tiny goal for today is already enough.",
            "Even enjoying one proper meal counts as living well.",
        ]
        await query.edit_message_text(
            "📅 Sentence of the Day:\n\n" + random.choice(sentences),
            reply_markup=day_menu(),
        )
        return

    if data == "day_tip":
        tips = [
            "Try using your phone a little less today and keep some time for yourself.",
            "Pick one small corner you want to organize and spend 3 minutes on it.",
            "If today feels busy, sort things into “must do” and “can wait.”",
        ]
        await query.edit_message_text(
            "📋 Daily Tip:\n\n" + random.choice(tips),
            reply_markup=day_menu(),
        )
        return

    if data == "day_direction":
        directions = [
            "Treat today as a ‘foundation day’ and do small things that help long-term.",
            "Treat today as an ‘adjustment day’ and allow yourself to slow down.",
            "Treat today as an ‘experiment day’ and try one small new action.",
        ]
        await query.edit_message_text(
            "🧭 Daily Direction:\n\n" + random.choice(directions),
            reply_markup=day_menu(),
        )
        return

    # ===== Habits & Mini Goals =====
    if data == "habit_goal":
        goals = [
            "Complete a mini goal that takes only 5 minutes.",
            "Focus on finishing just one small thing you care about.",
            "Set a goal of ‘done is enough, not perfect.’",
        ]
        await query.edit_message_text(
            "✅ Mini Goal Suggestion:\n\n" + random.choice(goals),
            reply_markup=habit_menu(),
        )
        return

    if data == "habit_action":
        actions = [
            "Drink a glass of water and tell yourself ‘good job.’",
            "Stand up and stretch your shoulders and neck for 30 seconds.",
            "Put away one item on your desk that you don’t use often.",
        ]
        await query.edit_message_text(
            "🔁 Habit Micro Action:\n\n" + random.choice(actions),
            reply_markup=habit_menu(),
        )
        return

    if data == "habit_clean":
        texts = [
            "Pick one drawer or folder and spend 2 minutes removing unnecessary items.",
            "Group scattered items on your desk to make it visually calmer.",
        ]
        await query.edit_message_text(
            "🧹 Quick Tidy:\n\n" + random.choice(texts),
            reply_markup=habit_menu(),
        )
        return

    if data == "habit_move":
        moves = [
            "Walk lightly in place for 30 seconds.",
            "Do 10 slow deep breaths with shoulder rolls.",
            "Walk to another room and back as a ‘mini walk.’",
        ]
        await query.edit_message_text(
            "🚶 Micro Movement:\n\n" + random.choice(moves),
            reply_markup=habit_menu(),
        )
        return

    # ===== Mood & Emotions =====
    if data == "mood_text":
        moods = [
            "It’s okay to feel tired—it means you’ve been trying.",
            "Emotions fluctuate, but you always deserve kindness.",
            "You’re allowed to have an ‘off’ day.",
        ]
        await query.edit_message_text(
            "💬 Mood Sentence:\n\n" + random.choice(moods),
            reply_markup=mood_menu(),
        )
        return

    if data == "mood_color":
        colors = [
            "🔵 Blue mood: good for quiet time and organizing thoughts.",
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
            "You can be a little more forgiving to yourself—you don’t need perfection.",
            "Try giving yourself a small affirmation like ‘I’ve done my best.’",
        ]
        await query.edit_message_text(
            "❤️ Self Care:\n\n" + random.choice(texts),
            reply_markup=mood_menu(),
        )
        return

    # ===== Mini Quiz & Q&A =====
    if data == "quiz_think":
        qs = [
            "🧠 Thinking:\n\nIf you had to give today a title, what would it be?",
            "🧠 Thinking:\n\nWhat small progress recently made you feel ‘not bad’?",
        ]
        await query.edit_message_text(
            random.choice(qs),
            reply_markup=quiz_menu(),
        )
        return

    if data == "quiz_number":
        number = random.randint(10, 99)
        text = (
            f"🔢 Number Test:\n\nStart from {number} in your head and subtract 3 each time. How far can you go?"
        )
        await query.edit_message_text(text, reply_markup=quiz_menu())
        return

    if data == "quiz_reaction":
        context.user_data["reaction_start"] = time.time()
        keyboard = [
            [InlineKeyboardButton("⚡ Tap Now!", callback_data="quiz_reaction_click")],
            [InlineKeyboardButton("⬅ Back", callback_data="menu_quiz")],
        ]
        await query.edit_message_text(
            "Tap the button as fast as you can to test your reaction speed:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return

    if data == "quiz_reaction_click":
        start = context.user_data.get("reaction_start")
        if not start:
            msg = "Test expired. Please restart from the menu."
        else:
            ms = int((time.time() - start) * 1000)
            msg = f"🎯 Your reaction time: {ms} ms."
        await query.edit_message_text(msg, reply_markup=quiz_menu())
        return

    # ===== Light Reading =====
    if data == "read_soft":
        sentences = [
            "You don’t have to be great all the time—remembering to like yourself is enough.",
            "Many things don’t need to be done at once; little by little is fine.",
        ]
        await query.edit_message_text(
            "📖 Gentle Sentence:\n\n" + random.choice(sentences),
            reply_markup=read_menu(),
        )
        return

    if data == "read_idea":
        ideas = [
            "Try noting one small thing today that felt ‘pretty nice.’",
            "Write one single line to your future self one month from now.",
        ]
        await query.edit_message_text(
            "💡 Idea Spark:\n\n" + random.choice(ideas),
            reply_markup=read_menu(),
        )
        return

    if data == "read_question":
        qs = [
            "📝 Reflection:\n\nIf the past week were weather, what would it be?",
            "📝 Reflection:\n\nWhat is something you’re actually doing better than before?",
        ]
        await query.edit_message_text(
            random.choice(qs),
            reply_markup=read_menu(),
        )
        return

    # ===== Random Features =====
    if data == "rand_number":
        n = random.randint(0, 100)
        await query.edit_message_text(
            f"🎲 Random Number (0–100): {n}",
            reply_markup=random_menu(),
        )
        return

    if data == "rand_emoji":
        emojis = ["😀", "😆", "😎", "🥳", "🤩", "🤗", "🙌", "🌈", "⭐", "✨", "🍀"]
        seq = " ".join(random.sample(emojis, 5))
        await query.edit_message_text(
            "😊 Random Emoji Set:\n\n" + seq,
            reply_markup=random_menu(),
        )
        return

    if data == "rand_task":
        tasks = [
            "Take a photo of something you find ‘nice’ right now.",
            "Find one small task you can finish in 3 minutes and do it.",
            "Put your phone down for 2 minutes and just daydream.",
        ]
        await query.edit_message_text(
            "📌 Random Task:\n\n" + random.choice(tasks),
            reply_markup=random_menu(),
        )
        return

    if data == "rand_inspire":
        ins = [
            "Pick a theme word for today, like: slow / adjust / ease.",
            "Think of one small thing that could make you feel better in 5 minutes.",
        ]
        await query.edit_message_text(
            "✨ Random Inspiration:\n\n" + random.choice(ins),
            reply_markup=random_menu(),
        )
        return

    # Fallback
    await query.edit_message_text(
        "This action is not supported. Please send /start to return home.",
        reply_markup=main_menu()
    )


# ========== Entry Point ==========
def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is not set!")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("about", about_cmd))
    app.add_handler(CallbackQueryHandler(button_handler))

    logger.info("Light Moments · Life Hub Bot started")
    app.run_polling()


if __name__ == "__main__":
    main()

