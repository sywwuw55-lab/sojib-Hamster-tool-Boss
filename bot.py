import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

# আপনার বটের টোকেন
TOKEN = "8930566725:AAHOZ2riJ-sFV-1bz0AqrQBku_rRxYgCLuM"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# সিমুলেটেড ইউজার ডাটাবেজ (যেখানে ইউজার আইডিগুলো সেভ থাকবে)
REGISTERED_USERS = [] # বোট স্টার্ট বা ইন্টারেক্ট করলে ইউজার আইডি এখানে যুক্ত হতে পারে

# /start কমান্ড বা মূল মেনু দেখানোর ফাংশন
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # কোনো ইউজার স্টার্ট করলে তাকে লিস্টে সেভ করে রাখা
    user = update.effective_user
    if user and user.id not in REGISTERED_USERS:
        REGISTERED_USERS.append(user.id)

    keyboard = [
        [
            InlineKeyboardButton("📋 User List", callback_data="userlist"),
            InlineKeyboardButton("🚫 Block User", callback_data="block"),
        ],
        [
            InlineKeyboardButton("✅ Unblock User", callback_data="unblock"),
            InlineKeyboardButton("📅 Set Date", callback_data="set_date"),
        ],
        [
            InlineKeyboardButton("➕ Add Extra Date", callback_data="add_extra_date"),
            InlineKeyboardButton("📊 User Status", callback_data="user_status"),
        ],
        [
            InlineKeyboardButton("⏳ Trial Key (1 Hour)", callback_data="trial_key"),
            InlineKeyboardButton("🔔 Update Alert", callback_data="update_alert"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(
            "🐰 **RABBIT Admin Control Panel**\n\nChoose an option below:",
            reply_markup=reply_markup,
            parse_mode="Markdown",
        )
    elif update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(
            "🐰 **RABBIT Admin Control Panel**\n\nChoose an option below:",
            reply_markup=reply_markup,
            parse_mode="Markdown",
        )

# বাটনগুলোতে ক্লিক করলে যে কাজগুলো হবে
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    back_button = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔙 Back to Menu", callback_data="back_to_menu")]]
    )

    if data == "userlist":
        text = f"📋 **Registered User List:**\nTotal Users: {len(REGISTERED_USERS)}\n1. User_Alpha (Active)\n2. User_Beta (Blocked)"
    elif data == "block":
        text = "🚫 **Block User:**\nPlease send the user ID or username to block.\n*(Ex: /block 123456789)*"
    elif data == "unblock":
        text = "✅ **Unblock User:**\nPlease send the user ID or username to unblock.\n*(Ex: /unblock 123456789)*"
    elif data == "set_date":
        text = "📅 **Set Expiry Date:**\nFormat: `/setdate <userid> YYYY-MM-DD`\nSend command in chat."
    elif data == "add_extra_date":
        text = "➕ **Add Extra Date:**\nFormat: `/adddays <userid> <days>`\nSend command in chat."
    elif data == "user_status":
        text = "📊 **User Status:**\nSend user ID to check their current subscription status."
    elif data == "trial_key":
        text = "⏳ **Trial Key Generated:**\n`RABBIT-TRIAL-99X8A2`\nValid for: **1 Hour**"
    elif data == "update_alert":
        # আপডেট অ্যালার্টের জন্য স্পেশাল ব্রডকাস্ট বাটন যুক্ত করা
        alert_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("📢 Send Alert to All Users", callback_data="broadcast_alert")],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data="back_to_menu")]
        ])
        await query.edit_message_text(
            "🔔 **Update Alert Manager**\n\nClick the button below to broadcast a new update notification to all registered users.",
            reply_markup=alert_markup,
            parse_mode="Markdown"
        )
        return
    elif data == "broadcast_alert":
        # সকল ইউজারের কাছে নোটিফিকেশন পাঠানোর লজিক
        success_count = 0
        for uid in REGISTERED_USERS:
            try:
                await context.bot.send_message(
                    chat_id=uid,
                    text="🚨 **NEW UPDATE AVAILABLE!**\n\nRabbit tool has been updated with new security patches and features. Type /start to refresh your panel!",
                    parse_mode="Markdown"
                )
                success_count += 1
            except Exception as e:
                pass
        
        text = f"✅ **Broadcast Successful!**\nUpdate alert sent to {success_count} user(s)."
    elif data == "back_to_menu":
        await start(update, context)
        return

    await query.edit_message_text(
        text, reply_markup=back_button, parse_mode="Markdown"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Rabbit Admin Bot is running with Update Alert...")
    app.run_polling()

if __name__ == "__main__":
    main()
