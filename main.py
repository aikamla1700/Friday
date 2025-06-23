from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatMemberHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

import os

# Get token from environment variable (safer)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Set your image URL here
WELCOME_IMAGE = 'https://i.imgur.com/dQw4w9g.jpg'  # Replace this with your image URL

async def welcome_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.chat_member.new_chat_member.status == "member":
        user = update.chat_member.new_chat_member.user
        name = user.first_name or "Friend"
        username = f"@{user.username}" if user.username else "Not Available"

        welcome_text = f"""**ᴛᴏ ᴋᴀɪꜱᴇ ʜᴀɪɴ ᴀᴀᴘ ʟᴏɢ!** 😎

✲ 𝑵𝑨𝑴𝑬 ➟ {name}  
✲ 𝑼𝑺𝑬𝑹𝑵𝑨𝑴𝑬 ➟ {username}  

📜  **𝗚𝗿𝗼𝘂𝗽 𝗥𝘂𝗹𝗲𝘀**:  
╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲  
𝟏. 🚫 𝐍𝐨 𝐚𝐛𝐮𝐬𝐞 𝐨𝐫 𝐡𝐚𝐭𝐞 𝐬𝐩𝐞𝐞𝐜𝐡  
𝟐. 🔞 𝐍𝐨 𝐍𝐒𝐅𝐖 𝐜𝐨𝐧𝐭𝐞𝐧𝐭  
𝟑. 📢 𝐍𝐨 𝐬𝐩𝐚𝐦 𝐨𝐫 𝐬𝐞𝐥𝐟 𝐩𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧  
𝟒. 🧠 𝐓𝐡𝐢𝐧𝐤 𝐛𝐞𝐟𝐨𝐫𝐞 𝐲𝐨𝐮 𝐩𝐨𝐬𝐭  
╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲"""

        await context.bot.send_photo(
            chat_id=update.chat_member.chat.id,
            photo=WELCOME_IMAGE,
            caption=welcome_text,
            parse_mode="Markdown"
        )

async def delete_system_join_leave(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.delete()
    except:
        pass

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(ChatMemberHandler(welcome_user, ChatMemberHandler.CHAT_MEMBER))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS | filters.StatusUpdate.LEFT_CHAT_MEMBER, delete_system_join_leave))

    app.run_polling()
