import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)
from telegram.constants import ParseMode
from bot.claude_ai import ClaudeAI
from bot.products import ProductManager
from config.settings import TELEGRAM_BOT_TOKEN

# লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Claude AI ইনস্ট্যান্স
ai = ClaudeAI()
product_manager = ProductManager()

# কথোপকথন অবস্থা
CHAT, SUPPORT, PRODUCT_INQUIRY = range(3)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """স্বাগত বার্তা"""
    welcome_message = """🎉 **Sonic Service Bot এ স্বাগতম!**

আমি আপনাকে তিনটি প্রধান সেবা প্রদান করি:

🤖 **/chat** - Claude AI এর সাথে কথা বলুন
🆘 **/support** - গ্রাহক সেবা সহায়তা
🛍️ **/products** - Sonic Brand Market এর প্রোডাক্ট দেখুন
❓ **/help** - সাহায্য পান
🔄 **/clear** - কথোপকথনের ইতিহাস সাফ করুন

কোন সেবা বেছে নিন!"""
    
    await update.message.reply_text(
        welcome_message,
        parse_mode=ParseMode.MARKDOWN
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """সাহায্য কমান্ড"""
    help_text = """📚 **সাহায্য এবং নির্দেশাবলী**

**উপলব্ধ কমান্ড:**

/start - স্বাগত বার্তা দেখান
/chat - Claude AI এর সাথে চ্যাট মোডে যান
/support - গ্রাহক সেবা মোডে যান
/products - প্রোডাক্ট ক্যাটালগ দেখান
/clear - আপনার চ্যাট ইতিহাস সাফ করুন
/help - এই সাহায্য বার্তা

**কিভাবে ব্যবহার করবেন:**

1️⃣ একটি কমান্ড নির্বাচন করুন
2️⃣ আপনার বার্তা বা প্রশ্ন টাইপ করুন
3️⃣ আমি তাৎক্ষণিক সহায়তা প্রদান করব

❓ আরও সাহায্য প্রয়োজন? আমাদের সাথে যোগাযোগ করুন!"""
    
    await update.message.reply_text(
        help_text,
        parse_mode=ParseMode.MARKDOWN
    )


async def chat_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """চ্যাট মোড শুরু করুন"""
    message = "🤖 **চ্যাট মোড সক্রিয়**\n\nআপনি এখন Claude AI এর সাথে কথা বলতে পারেন। যেকোনো প্রশ্ন করুন!\n\nচ্যাট থেকে বের হতে /start লিখুন"
    await update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
    context.user_data['mode'] = 'chat'
    return CHAT


async def support_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """গ্রাহক সেবা মোড শুরু করুন"""
    message = "🆘 **গ্রাহক সেবা মোড সক্রিয়**\n\nআমি আপনার সমস্যা সমাধানে সাহায্য করতে প্রস্তুত। আপনার সমস্যা বর্ণনা করুন।\n\nসেবা থেকে বের হতে /start লিখুন"
    await update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
    context.user_data['mode'] = 'support'
    return SUPPORT


async def products_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """প্রোডাক্ট ক্যাটালগ দেখান"""
    catalog = product_manager.format_product_catalog()
    await update.message.reply_text(
        catalog,
        parse_mode=ParseMode.MARKDOWN
    )
    await update.message.reply_text(
        "🛍️ কোন প্রোডাক্ট সম্পর্কে আরও জানতে চান? নাম বা ID লিখুন।"
    )
    context.user_data['mode'] = 'products'
    return PRODUCT_INQUIRY


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """বার্তা হ্যান্ডলিং"""
    user_id = update.effective_user.id
    user_message = update.message.text
    mode = context.user_data.get('mode', 'chat')
    
    # টাইপিং ইন্ডিকেটর দেখান
    await update.message.chat.send_action("typing")
    
    try:
        if mode == 'chat':
            response = ai.chat(user_id, user_message)
        elif mode == 'support':
            response = ai.customer_support(user_id, user_message)
        elif mode == 'products':
            response = ai.product_advisor(user_id, user_message)
        else:
            response = ai.chat(user_id, user_message)
        
        await update.message.reply_text(
            response,
            parse_mode=ParseMode.MARKDOWN
        )
    
    except Exception as e:
        error_message = f"❌ একটি ত্রুটি ঘটেছে: {str(e)}"
        logger.error(f"Error in handle_message: {e}")
        await update.message.reply_text(error_message)


async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """চ্যাট ইতিহাস সাফ করুন"""
    user_id = update.effective_user.id
    ai.clear_history(user_id)
    await update.message.reply_text(
        "✅ আপনার চ্যাট ইতিহাস সাফ করা হয়েছে। নতুন করে শুরু করুন!"
    )


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ত্রুটি হ্যান্ডলিং"""
    logger.error(f"Update {update} caused error {context.error}")


def setup_handlers(app: Application):
    """সকল হ্যান্ডলার সেটআপ করুন"""
    
    # কমান্ড হ্যান্ডলার
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('clear', clear_command))
    app.add_handler(CommandHandler('products', products_command))
    
    # মোড হ্যান্ডলার
    app.add_handler(CommandHandler('chat', chat_mode))
    app.add_handler(CommandHandler('support', support_mode))
    
    # বার্তা হ্যান্ডলার
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # ত্রুটি হ্যান্ডলার
    app.add_error_handler(error_handler)
    
    logger.info("সকল হ্যান্ডলার সেটআপ সম্পন্ন")
