import os
import telebot
from telebot import types
from datetime import datetime, timedelta

TOKEN = "8930566725:AAHOZ2riJ-sFV-1bz0AqrQBku_rRxYgCLuM"
bot = telebot.TeleBot(TOKEN)

USER_DB = os.path.expanduser("~/sojib-Hamster-tool-Boss/users_list.txt")

def load_users():
    if not os.path.exists(USER_DB):
        return {}
    users = {}
    with open(USER_DB, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) >= 2:
                uid = parts[0].strip()
                status = parts[1].strip()
                expiry = parts[2].strip() if len(parts) > 2 else "2030-01-01"
                users[uid] = {"status": status, "expiry": expiry}
    return users

def save_users(users):
    with open(USER_DB, "w") as f:
        for uid, data in users.items():
            f.write(f"{uid}|{data['status']}|{data['expiry']}\n")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    users = load_users()
    
    if not users:
        bot.reply_to(message, "🤖 Admin Hamster Remote Control Panel Active!\n\n📂 No users registered in database yet.")
        return

    msg = "🤖 **Admin Hamster Control Panel**\nSelect a user action or run your tool:\n\n"
    markup = types.InlineKeyboardMarkup()
    
    for uid, data in users.items():
        status_icon = "🟢" if data['status'] == "active" else "🔴"
        msg += f"🆔 `{uid}`\nStatus: {status_icon} *{data['status']}* | Exp: *{data['expiry']}*\n\n"
        
        markup.add(
            types.InlineKeyboardButton(f"❌ Block", callback_data=f"block_{uid}"),
            types.InlineKeyboardButton(f"✅ Unblock", callback_data=f"unblock_{uid}")
        )
        markup.add(
            types.InlineKeyboardButton(f"📅 +30 Days", callback_data=f"add_date_{uid}")
        )
    
    markup.add(types.InlineKeyboardButton("🔄 Refresh User List", callback_data="user_list"))
    bot.reply_to(message, msg, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    data = call.data
    users = load_users()
    
    if data.startswith("block_"):
        uid = data.split("_", 1)[1].strip()
        if uid in users:
            users[uid]["status"] = "blocked"
            save_users(users)
            bot.answer_callback_query(call.id, "User Blocked Successfully!")
            bot.send_message(call.message.chat.id, f"❌ User Blocked!\n🆔 ID: `{uid}`", parse_mode="Markdown")
        else:
            bot.answer_callback_query(call.id, "User not found in database!")
            
    elif data.startswith("unblock_"):
        uid = data.split("_", 1)[1].strip()
        if uid in users:
            users[uid]["status"] = "active"
            save_users(users)
            bot.answer_callback_query(call.id, "User Unblocked!")
            bot.send_message(call.message.chat.id, f"✅ User Unblocked!\n🆔 ID: `{uid}`", parse_mode="Markdown")
        else:
            bot.answer_callback_query(call.id, "User not found!")
            
    elif data.startswith("add_date_"):
        uid = data.split("_", 1)[1].strip()
        if uid in users:
            try:
                current_expiry = datetime.strptime(users[uid]["expiry"], "%Y-%m-%d")
            except:
                current_expiry = datetime.now()
            new_expiry = (current_expiry + timedelta(days=30)).strftime("%Y-%m-%d")
            users[uid]["expiry"] = new_expiry
            save_users(users)
            bot.answer_callback_query(call.id, "Extra 30 days added!")
            bot.send_message(call.message.chat.id, f"📅 Added 30 days validity!\n🆔 ID: `{uid}`\n⏳ New Expiry: {new_expiry}", parse_mode="Markdown")
        else:
            bot.answer_callback_query(call.id, "User not found!")
            
    elif data == "user_list":
        users = load_users()
        if not users:
            bot.answer_callback_query(call.id, "No users found yet.")
            bot.send_message(call.message.chat.id, "📂 No active users registered yet.")
        else:
            msg = "📋 **Registered Users List:**\n\n"
            for uid, data in users.items():
                msg += f"🆔 `{uid}`\nStatus: *{data['status']}*\nExpiry: *{data['expiry']}*\n\n"
            bot.answer_callback_query(call.id, "Fetching user list...")
            bot.send_message(call.message.chat.id, msg, parse_mode="Markdown")

print("Python Telegram Bot is running continuously...")
while True:
    try:
        bot.infinity_polling(skip_pending=True, timeout=60, long_polling_timeout=60)
    except Exception as e:
        print(f"Bot error: {e}. Reconnecting...")
        import time
        time.sleep(5)
