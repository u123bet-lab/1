

import logging
import os
import random
import time

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

# ========= 基础配置 =========
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# ========= 菜单区域 =========
def main_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("😊 心情工具", callback_data="menu_mood")],
        [
            InlineKeyboardButton("🎮 轻小游戏", callback_data="menu_games"),
            InlineKeyboardButton("🧠 脑力训练", callback_data="menu_brain"),
        ],
        [
            InlineKeyboardButton("🧺 日常小助手", callback_data="menu_daily"),
            InlineKeyboardButton("📌 每日卡片", callback_data="menu_cards"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def mood_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("💬 心情一句话", callback_data="mood_sentence"),
            InlineKeyboardButton("🎨 心情颜色", callback_data="mood_color"),
        ],
        [
            InlineKeyboardButton("🧘 放松小练习", callback_data="mood_relax"),
            InlineKeyboardButton("📖 安慰小语录", callback_data="mood_quote"),
        ],
        [InlineKeyboardButton("⬅ 返回主菜单", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def games_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("✊ 石头剪刀布", callback_data="game_rps"),
            InlineKeyboardButton("🎲 掷骰子", callback_data="game_dice"),
        ],
        [
            InlineKeyboardButton("🔢 数字竞猜", callback_data="game_guess"),
            InlineKeyboardButton("😊 表情组合", callback_data="game_emoji"),
        ],
        [InlineKeyboardButton("⬅ 返回主菜单", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def brain_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("🧠 今日脑力任务", callback_data="brain_task")],
        [
            InlineKeyboardButton("🔢 记忆数字", callback_data="brain_memory"),
            InlineKeyboardButton("🧩 小谜题", callback_data="brain_puzzle"),
        ],
        [
            InlineKeyboardButton("🎯 反应测试", callback_data="brain_reaction"),
        ],
        [InlineKeyboardButton("⬅ 返回主菜单", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def daily_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("📋 今日小待办", callback_data="daily_todo"),
            InlineKeyboardButton("🍵 休息提醒", callback_data="daily_break"),
        ],
        [
            InlineKeyboardButton("🧹 整理一下", callback_data="daily_clean"),
            InlineKeyboardButton("📨 联络一下", callback_data="daily_contact"),
        ],
        [InlineKeyboardButton("⬅ 返回主菜单", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(daily_menu)


def cards_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("📌 今日提示卡", callback_data="card_tip"),
            InlineKeyboardButton("💡 灵感小卡片", callback_data="card_idea"),
        ],
        [
            InlineKeyboardButton("❤️ 自我关怀卡", callback_data="card_self"),
            InlineKeyboardButton("⭐ 小目标卡", callback_data="card_goal"),
        ],
        [InlineKeyboardButton("⬅ 返回主菜单", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


# ========= 指令：/start /help /about =========
START_TEXT = (
    "👋 欢迎来到「轻松日常 FunBox」！\n\n"
    "这是一个专注于 *轻娱乐·小工具·放松心情* 的中文机器人，你可以在这里：\n\n"
    "😊 *心情工具*\n"
    "• 随机心情一句话\n"
    "• 心情颜色提示\n"
    "• 放松小练习、安慰语录\n\n"
    "🎮 *轻小游戏*\n"
    "• 石头剪刀布\n"
    "• 掷骰子\n"
    "• 数字竞猜\n"
    "• 表情组合灵感\n\n"
    "🧠 *脑力训练*\n"
    "• 简单脑力任务\n"
    "• 数字记忆练习\n"
    "• 思维小谜题\n"
    "• 反应速度测试\n\n"
    "🧺 *日常小助手*\n"
    "• 今日小待办建议\n"
    "• 适时休息提醒\n"
    "• 整理一下的小任务\n"
    "• 联系朋友的轻提醒\n\n"
    "📌 *每日卡片*\n"
    "• 今日提示卡\n"
    "• 灵感卡片\n"
    "• 自我关怀卡\n"
    "• 小目标卡\n\n"
    "本机器人仅提供轻松娱乐和日常小提醒，不包含任何金钱、奖励、博彩、投资或敏感内容，适合所有用户使用。\n\n"
    "👇 点击下方菜单开始体验吧！"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            START_TEXT, reply_markup=main_menu(), parse_mode="Markdown"
        )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📝 使用说明\n\n"
        "• 发送 /start 打开主菜单\n"
        "• 底部按钮可进入：心情工具、小游戏、脑力训练、日常小助手、每日卡片\n"
        "• 每个功能都是轻量互动或文字提示，不涉及任何敏感或现实奖励内容\n"
        "• 如遇无响应，可再次发送 /start 重新进入主菜单\n"
    )
    await update.message.reply_text(text)


async def about_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "ℹ️ 关于本机器人\n\n"
        "「轻松日常 FunBox」是一个帮助你在碎片时间放松一下的小工具合集：\n"
        "• 通过小游戏和脑力小练习轻松一下\n"
        "• 用心情工具和每日卡片照顾自己\n"
        "• 完全免费，无任何金钱、奖励或敏感元素\n"
        "欢迎在私聊或群聊中一起使用。"
    )
    await update.message.reply_text(text)


# ========= 按钮路由 =========
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    # 菜单切换
    if data == "menu_main":
        await query.edit_message_text("🏠 已返回主菜单：", reply_markup=main_menu())
        return
    if data == "menu_mood":
        await query.edit_message_text("😊 心情工具：", reply_markup=mood_menu())
        return
    if data == "menu_games":
        await query.edit_message_text("🎮 轻小游戏：", reply_markup=games_menu())
        return
    if data == "menu_brain":
        await query.edit_message_text("🧠 脑力训练：", reply_markup=brain_menu())
        return
    if data == "menu_daily":
        await query.edit_message_text("🧺 日常小助手：", reply_markup=daily_menu())
        return
    if data == "menu_cards":
        await query.edit_message_text("📌 每日卡片：", reply_markup=cards_menu())
        return

    # 心情工具
    if data == "mood_sentence":
        await mood_sentence(query)
        return
    if data == "mood_color":
        await mood_color(query)
        return
    if data == "mood_relax":
        await mood_relax(query)
        return
    if data == "mood_quote":
        await mood_quote(query)
        return

    # 小游戏
    if data == "game_rps":
        await game_rps(query)
        return
    if data.startswith("game_rps_"):
        await game_rps_result(query, data)
        return
    if data == "game_dice":
        await game_dice(query)
        return
    if data == "game_guess":
        await game_guess(query, context)
        return
    if data.startswith("game_guess_"):
        await game_guess_result(query, context, data)
        return
    if data == "game_emoji":
        await game_emoji(query)
        return

    # 脑力训练
    if data == "brain_task":
        await brain_task(query)
        return
    if data == "brain_memory":
        await brain_memory_start(query, context)
        return
    if data.startswith("brain_memory_answer_"):
        await brain_memory_answer(query, context, data)
        return
    if data == "brain_puzzle":
        await brain_puzzle(query)
        return
    if data == "brain_reaction":
        await brain_reaction(query, context)
        return
    if data == "brain_reaction_click":
        await brain_reaction_click(query, context)
        return

    # 日常小助手
    if data == "daily_todo":
        await daily_todo(query)
        return
    if data == "daily_break":
        await daily_break(query)
        return
    if data == "daily_clean":
        await daily_clean(query)
        return
    if data == "daily_contact":
        await daily_contact(query)
        return

    # 每日卡片
    if data == "card_tip":
        await card_tip(query)
        return
    if data == "card_idea":
        await card_idea(query)
        return
    if data == "card_self":
        await card_self(query)
        return
    if data == "card_goal":
        await card_goal(query)
        return

    # 兜底
    await query.edit_message_text("操作暂不支持，请发送 /start 返回主菜单。")


# ========= 心情工具实现 =========
async def mood_sentence(query):
    sentences = [
        "今天也要温柔地对待自己一点点。",
        "不一定要很厉害，能保持前进就很好。",
        "允许自己偶尔慢一点，也是一种勇气。",
        "你已经做得比自己想象中更好了。",
    ]
    await query.edit_message_text(
        "💬 心情一句话：\n\n" + random.choice(sentences),
        reply_markup=mood_menu(),
    )


async def mood_color(query):
    colors = [
        "🔵 蓝色：适合安静思考，给大脑一点空间。",
        "🟢 绿色：适合放松，像在公园散步一样。",
        "🟡 黄色：适合分享笑话或和朋友聊聊天。",
        "🟣 紫色：适合做点小创作，比如写几句文字。",
        "🔴 红色：适合完成一件一直想做的小事。",
    ]
    await query.edit_message_text(
        "🎨 心情颜色提示：\n\n" + random.choice(colors),
        reply_markup=mood_menu(),
    )


async def mood_relax(query):
    text = (
        "🧘 放松小练习：\n\n"
        "1️⃣ 找个舒服的姿势坐好或站好\n"
        "2️⃣ 闭上眼睛（如果方便）\n"
        "3️⃣ 缓慢地做 5 次深呼吸\n"
        "   吸气数到 4，呼气数到 4\n\n"
        "只需要半分钟，给自己一点小休息。"
    )
    await query.edit_message_text(text, reply_markup=mood_menu())


async def mood_quote(query):
    quotes = [
        "有时候，停下来深呼吸一下，就已经很棒了。",
        "情绪来来去去，但你一直都在。",
        "不必把今天过得完美，把它过成“还可以”就已经很不错。",
    ]
    await query.edit_message_text(
        "📖 安慰小语录：\n\n" + random.choice(quotes),
        reply_markup=mood_menu(),
    )


# ========= 小游戏实现 =========
async def game_rps(query):
    keyboard = [
        [
            InlineKeyboardButton("✊ 石头", callback_data="game_rps_rock"),
            InlineKeyboardButton("✋ 布", callback_data="game_rps_paper"),
            InlineKeyboardButton("✌ 剪刀", callback_data="game_rps_scissors"),
        ],
        [InlineKeyboardButton("⬅ 返回小游戏", callback_data="menu_games")],
    ]
    await query.edit_message_text(
        "✊ 石头剪刀布：请选择你的出拳：",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def game_rps_result(query, data: str):
    user = data.split("_")[-1]
    options = ["rock", "paper", "scissors"]
    bot = random.choice(options)
    emoji = {"rock": "✊ 石头", "paper": "✋ 布", "scissors": "✌ 剪刀"}

    if user == bot:
        result = "平局～ 我们很有默契 😆"
    elif (
        (user == "rock" and bot == "scissors")
        or (user == "scissors" and bot == "paper")
        or (user == "paper" and bot == "rock")
    ):
        result = "你赢啦！今天手感不错 ✨"
    else:
        result = "这局我略胜一筹，再来一把？😉"

    text = (
        "🎮 石头剪刀布结果：\n\n"
        f"你出：{emoji[user]}\n"
        f"我出：{emoji[bot]}\n\n"
        f"{result}"
    )
    await query.edit_message_text(text, reply_markup=games_menu())


async def game_dice(query):
    n = random.randint(1, 6)
    await query.edit_message_text(
        f"🎲 你掷出了：{n} 点！\n\n可以多试几次，看今天的“点数运气”。",
        reply_markup=games_menu(),
    )


async def game_guess(query, context: ContextTypes.DEFAULT_TYPE):
    secret = random.randint(1, 5)
    context.user_data["guess_number"] = secret

    keyboard = [
        [
            InlineKeyboardButton("1", callback_data="game_guess_1"),
            InlineKeyboardButton("2", callback_data="game_guess_2"),
            InlineKeyboardButton("3", callback_data="game_guess_3"),
            InlineKeyboardButton("4", callback_data="game_guess_4"),
            InlineKeyboardButton("5", callback_data="game_guess_5"),
        ],
        [InlineKeyboardButton("⬅ 返回小游戏", callback_data="menu_games")],
    ]
    await query.edit_message_text(
        "🔢 数字竞猜：我在 1~5 里想了一个数字，你猜是几？",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def game_guess_result(
    query, context: ContextTypes.DEFAULT_TYPE, data: str
):
    secret = context.user_data.get("guess_number")
    try:
        user = int(data.split("_")[-1])
    except ValueError:
        user = None

    if secret is None or user is None:
        text = "游戏数据已失效，请重新开始数字竞猜～"
    elif secret == user:
        text = f"🎉 你猜对了！我想的就是 {secret}。"
    else:
        text = f"😆 有点可惜！我其实想的是 {secret}。"

    await query.edit_message_text(text, reply_markup=games_menu())


async def game_emoji(query):
    emojis = ["😀", "😆", "😎", "🥳", "🤩", "🤗", "🙌", "🌈", "⭐", "✨", "🔥", "🍀"]
    seq = " ".join(random.sample(emojis, 5))
    text = (
        "😊 表情组合灵感：\n\n"
        f"{seq}\n\n"
        "可以复制这串表情，发到群里玩接龙或者当成“今天的心情组合”。"
    )
    await query.edit_message_text(text, reply_markup=games_menu())


# ========= 脑力训练实现 =========
async def brain_task(query):
    tasks = [
        "🧠 任务：在心里从 30 倒数到 1，尽量不要中断。",
        "🧠 任务：回想今天让你开心的三件小事。",
        "🧠 任务：尝试记住身边你看到的 5 个物品，并在心里复述一遍。",
    ]
    await query.edit_message_text(
        "🧠 今日脑力任务：\n\n" + random.choice(tasks),
        reply_markup=brain_menu(),
    )


async def brain_memory_start(query, context: ContextTypes.DEFAULT_TYPE):
    number = random.randint(100, 9999)
    context.user_data["brain_memory_number"] = number
    keyboard = [
        [
            InlineKeyboardButton(
                "我记住了，开始回答", callback_data=f"brain_memory_answer_{number}"
            )
        ],
        [InlineKeyboardButton("⬅ 返回脑力训练", callback_data="menu_brain")],
    ]
    await query.edit_message_text(
        f"🔢 数字记忆练习：\n\n请记住这个数字：\n\n👉 {number}\n\n准备好后点击按钮。",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def brain_memory_answer(
    query, context: ContextTypes.DEFAULT_TYPE, data: str
):
    original = context.user_data.get("brain_memory_number")
    try:
        answer = int(data.split("_")[-1])
    except ValueError:
        answer = None

    if original is None or answer is None:
        text = "记忆练习数据已失效，请重新开始一次吧。"
    elif original == answer:
        text = f"🎉 很棒！你成功记住了：{original}"
    else:
        text = f"😆 有点出入，正确数字是：{original}"

    await query.edit_message_text(text, reply_markup=brain_menu())


async def brain_puzzle(query):
    puzzles = [
        "🧩 谜题：\n一个房间里有一盏灯，外面有三个开关，你只能进房间一次，如何判断哪个开关控制这盏灯？",
        "🧩 谜题：\n有一根绳子，从一头烧到另一头刚好需要 1 小时，但燃烧速度不均匀，如何用它量出 15 分钟？",
    ]
    await query.edit_message_text(random.choice(puzzles), reply_markup=brain_menu())


async def brain_reaction(query, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["reaction_start"] = time.time()
    keyboard = [
        [InlineKeyboardButton("⚡ 现在点我！", callback_data="brain_reaction_click")],
        [InlineKeyboardButton("⬅ 返回脑力训练", callback_data="menu_brain")],
    ]
    await query.edit_message_text(
        "🎯 看到这个按钮后立刻点击，测试你的反应速度：",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def brain_reaction_click(query, context: ContextTypes.DEFAULT_TYPE):
    start = context.user_data.get("reaction_start")
    if not start:
        text = "测试数据已失效，请重新开始。"
    else:
        ms = int((time.time() - start) * 1000)
        text = f"🎯 你的反应时间是：{ms} ms\n\n可以多试几次看看有没有进步。"
    await query.edit_message_text(text, reply_markup=brain_menu())


# ========= 日常小助手实现 =========
async def daily_todo(query):
    todos = [
        "📋 今日建议待办：\n\n• 完成一件真正重要的小任务\n• 回复一条你一直没回的消息\n• 给自己留 10 分钟放空时间",
        "📋 今日建议待办：\n\n• 整理一个文件夹或抽屉\n• 喝一杯水\n• 想一件明天想做的事情并记下来",
    ]
    await query.edit_message_text(random.choice(todos), reply_markup=daily_menu())


async def daily_break(query):
    text = (
        "🍵 休息小提醒：\n\n"
        "如果你已经连续盯着屏幕一段时间，可以考虑：\n"
        "• 起身走动一下\n"
        "• 看看远处的风景\n"
        "• 活动一下肩颈\n\n"
        "短暂的休息有助于恢复专注力。"
    )
    await query.edit_message_text(text, reply_markup=daily_menu())


async def daily_clean(query):
    tasks = [
        "🧹 试着用 3 分钟整理一下桌面或周围环境的一小块区域。",
        "🧹 把桌上的纸张/笔/小物件稍微归类放好，给自己一点“清爽感”。",
    ]
    await query.edit_message_text(
        "🧹 整理一下：\n\n" + random.choice(tasks),
        reply_markup=daily_menu(),
    )


async def daily_contact(query):
    text = (
        "📨 联络小提醒：\n\n"
        "可以考虑给其中一位人发个消息：\n"
        "• 很久没联系的朋友\n"
        "• 最近帮过你的人\n"
        "• 家人或重要的人\n\n"
        "一句简单的问候，也是一种温柔的连接。"
    )
    await query.edit_message_text(text, reply_markup=daily_menu())


# ========= 每日卡片实现 =========
async def card_tip(query):
    tips = [
        "📌 今日提示卡：\n\n把注意力多放在“能做什么”上，而不是“做不到什么”。",
        "📌 今日提示卡：\n\n如果事情很多，可以先确定一件最小、最容易完成的事，从它开始。",
    ]
    await query.edit_message_text(random.choice(tips), reply_markup=cards_menu())


async def card_idea(query):
    ideas = [
        "💡 灵感卡片：\n\n写下一句今天突然想到的想法或句子，不需要完整，只要真实。",
        "💡 灵感卡片：\n\n如果把今天拍成一张照片，你会拍下什么画面？在心里简单想象一下。",
    ]
    await query.edit_message_text(random.choice(ideas), reply_markup=cards_menu())


async def card_self(query):
    texts = [
        "❤️ 自我关怀卡：\n\n你不需要时时刻刻都很坚强，有时承认“有点累了”也没关系。",
        "❤️ 自我关怀卡：\n\n试着对自己说一句“谢谢你坚持到现在”，哪怕今天没有做到完美。",
    ]
    await query.edit_message_text(random.choice(texts), reply_markup=cards_menu())


async def card_goal(query):
    texts = [
        "⭐ 小目标卡：\n\n今天只需要完成一件“小而具体”的事情，比如：整理一页、写一段话、走 5 分钟路。",
        "⭐ 小目标卡：\n\n想一个可以在 10 分钟内完成的小目标，完成之后给自己一个小小的肯定。",
    ]
    await query.edit_message_text(random.choice(texts), reply_markup=cards_menu())


# ========= 主入口 =========
def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN 环境变量未设置！")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("about", about_cmd))

    app.add_handler(CallbackQueryHandler(button_handler))

    logger.info("轻松日常 FunBox 加强版机器人已启动。")
    app.run_polling()


if __name__ == "__main__":
    main()
