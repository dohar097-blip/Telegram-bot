import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from telegram.constants import ParseMode
from bot.claude_ai import ClaudeAI
from bot.products import ProductManager
from bot.weather import WeatherManager
from bot.todo import TodoManager

# লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ইন্সট্যান্স তৈরি করুন
try:
    ai = ClaudeAI()
    product_manager = ProductManager()
    weather_manager = WeatherManager()
    todo_manager = TodoManager()
    logger.info("✅ সব ম্যানেজার সফলভাবে লোড হয়েছে")
except Exception as e:
    logger.error(f"❌ ম্যানেজার লোড করতে ব্যর্থ: {e}")
    raise

# কথোপকথন অবস্থা
CHAT, SUPPORT, PRODUCT_INQUIRY, WEATHER_CITY, TODO_ACTION = range(5)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """স্বাগত বার্তা"""
    try:
        welcome_message = """🎉 **Sonic Service Bot এ স্বাগতম!**

আমি আপনাকে পাঁচটি প্রধান সেবা প্রদান করি:

🤖 **/chat** - Claude AI এর সাথে কথা বলুন
🛒 **/support** - গ্রাহক সেবা সহায়তা
🛍️ **/products** - Sonic Brand Market প্রোডাক্ট
🌤️ **/weather** - আবহাওয়া তথ্য
✅ **/todo** - টু-ডু লিস্ট ম্যানেজমেন্ট
❓ **/help** - সাহায্য

কোন সেবা চান?"""
        
        await update.message.reply_text(
            welcome_message,
            parse_mode=ParseMode.MARKDOWN
        )
        logger.info(f"✅ User {update.effective_user.id} /start কমান্ড দিয়েছে")
    except Exception as e:
        logger.error(f"❌ start command এ ত্রুটি: {e}")
        await update.message.reply_text(f"❌ ত্রুটি: {str(e)}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """সাহায্য কমান্ড"""
    try:
        help_text = """📚 **সাহায্য এবং নির্দেশাবলী**

**প্রধান কমান্ড:**
/start - স্বাগত বার্তা
/chat - Claude AI চ্যাট
/support - গ্রাহক সেবা
/products - প্রোডাক্ট ক্যাটালগ
/weather - আবহাওয়া তথ্য
/todo - টু-ডু লিস্ট
/clear - চ্যাট হিস্টরি সাফ করুন

**টু-ডু কমান্ড:**
/todo add <টাস্ক> - নতুন টাস্ক যোগ করুন
/todo list - সব টাস্ক দেখুন
/todo done <নম্বর> - টাস্ক সম্পন্ন করুন
/todo delete <নম্বর> - টাস্ক ডিলিট করুন
/todo stats - স্ট্যাটিস্টিক্স দেখুন

**আবহাওয়া কমান্ড:**
/weather <শহর> - বর্তমান আবহাওয়া
/forecast <শহর> - ৫ দিনের পূর্বাভাস

**উদাহরণ:**
/weather Dhaka
/todo add বাজারে যেতে হবে
/todo done 1
"""
        
        await update.message.reply_text(
            help_text,
            parse_mode=ParseMode.MARKDOWN
        )
        logger.info(f"✅ User {update.effective_user.id} /help কমান্ড দিয়েছে")
    except Exception as e:
        logger.error(f"❌ help command এ ত্রুটি: {e}")
        await update.message.reply_text(f"❌ ত্রুটি: {str(e)}")


async def chat_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """চ্যাট মোড শুরু করুন"""
    try:
        message = "🤖 **চ্যাট মোড সক্রিয়**\n\nআপনি এখন Claude AI এর সাথে কথা বলতে পারেন। যেকোনো প্রশ্ন করুন!\n\nচ্যাট থেকে বেরোতে /start লিখুন"
        await update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
        context.user_data['mode'] = 'chat'
        logger.info(f"✅ User {update.effective_user.id} chat mode এ গেছে")
    except Exception as e:
        logger.error(f"❌ chat_mode এ ত্রুটি: {e}")


async def support_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """গ্রাহক সেবা মোড শুরু করুন"""
    try:
        message = "🛒 **গ্রাহক সেবা মোড সক্রিয়**\n\nআমি আপনার সমস্যা সমাধানে সাহায্য করতে প্রস্তুত। আপনার সমস্যা বর্ণনা করুন।\n\nবেরোতে /start লিখুন"
        await update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
        context.user_data['mode'] = 'support'
        logger.info(f"✅ User {update.effective_user.id} support mode এ গেছে")
    except Exception as e:
        logger.error(f"❌ support_mode এ ত্রুটি: {e}")


async def products_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """প্রোডাক্ট ক্যাটালগ দেখুন"""
    try:
        catalog = product_manager.format_product_catalog()
        await update.message.reply_text(
            catalog,
            parse_mode=ParseMode.MARKDOWN
        )
        await update.message.reply_text(
            "🛍️ প্রোডাক্ট সম্পর্কে আরও জানতে প্রোডাক্ট ID লিখুন। (যেমন: sonic_vip_pack)"
        )
        logger.info(f"✅ User {update.effective_user.id} /products কমান্ড দিয়েছে")
    except Exception as e:
        logger.error(f"❌ products_command এ ত্রুটি: {e}")
        await update.message.reply_text(f"❌ ত্রুটি: {str(e)}")


async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """আবহাওয়া কমান্ড"""
    try:
        if not context.args:
            await update.message.reply_text(
                "🌤️ ব্যবহার: /weather <শহর>\n\nউদাহরণ: /weather Dhaka"
            )
            return
        
        city = ' '.join(context.args)
        await update.message.chat.send_action("typing")
        
        weather_data = weather_manager.get_current_weather(city)
        weather_text = weather_manager.format_weather(weather_data)
        
        await update.message.reply_text(
            weather_text,
            parse_mode=ParseMode.MARKDOWN
        )
        logger.info(f"✅ User {update.effective_user.id} {city} এর আবহাওয়া দেখেছে")
    except Exception as e:
        logger.error(f"❌ weather_command এ ত্রুটি: {e}")
        await update.message.reply_text(f"❌ ত্রুটি: {str(e)}")


async def forecast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """পূর্বাভাস কমান্ড"""
    try:
        if not context.args:
            await update.message.reply_text(
                "📅 ব্যবহার: /forecast <শহর>\n\nউদাহরণ: /forecast Dhaka"
            )
            return
        
        city = ' '.join(context.args)
        await update.message.chat.send_action("typing")
        
        forecast_data = weather_manager.get_forecast(city)
        forecast_text = weather_manager.format_forecast(forecast_data)
        
        await update.message.reply_text(
            forecast_text,
            parse_mode=ParseMode.MARKDOWN
        )
        logger.info(f"✅ User {update.effective_user.id} {city} এর পূর্বাভাস দেখেছে")
    except Exception as e:
        logger.error(f"❌ forecast_command এ ত্রুটি: {e}")
        await update.message.reply_text(f"❌ ত্রুটি: {str(e)}")


async def todo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """টু-ডু কমান্ড"""
    try:
        user_id = update.effective_user.id
        
        if not context.args:
            help_text = """✅ **টু-ডু লিস্ট কমান্ড:**

/todo add <টাস্ক> - নতুন টাস্ক যোগ করুন
/todo list - সব টাস্ক দেখুন
/todo done <নম্বর> - টাস্ক সম্পন্ন করুন
/todo delete <নম্বর> - টাস্ক ডিলিট করুন
/todo stats - স্ট্যাটিস্টিক্স দেখুন

**উদাহরণ:**
/todo add আজ বাজার যেতে হবে
/todo list
/todo done 1"""
            await update.message.reply_text(
                help_text,
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        action = context.args[0].lower()
        
        if action == 'add':
            if len(context.args) < 2:
                await update.message.reply_text("❌ ব্যবহার: /todo add <টাস্ক>")
                return
            
            task = ' '.join(context.args[1:])
            result = todo_manager.add_todo(user_id, task)
            await update.message.reply_text(result, parse_mode=ParseMode.MARKDOWN)
            logger.info(f"✅ User {user_id} টাস্ক যোগ করেছে: {task}")
        
        elif action == 'list':
            result = todo_manager.get_all_todos(user_id)
            await update.message.reply_text(result, parse_mode=ParseMode.MARKDOWN)
            logger.info(f"✅ User {user_id} টু-ডু লিস্ট দেখেছে")
        
        elif action == 'done':
            if len(context.args) < 2:
                await update.message.reply_text("❌ ব্যবহার: /todo done <নম্বর>")
                return
            
            try:
                task_id = int(context.args[1])
                result = todo_manager.mark_complete(user_id, task_id)
                await update.message.reply_text(result, parse_mode=ParseMode.MARKDOWN)
                logger.info(f"✅ User {user_id} টাস্ক #{task_id} সম্পন্ন করেছে")
            except ValueError:
                await update.message.reply_text("❌ নম্বর সঠিক নয়")
        
        elif action == 'delete':
            if len(context.args) < 2:
                await update.message.reply_text("❌ ব্যবহার: /todo delete <নম্বর>")
                return
            
            try:
                task_id = int(context.args[1])
                result = todo_manager.delete_todo(user_id, task_id)
                await update.message.reply_text(result, parse_mode=ParseMode.MARKDOWN)
                logger.info(f"✅ User {user_id} টাস্ক #{task_id} ডিলিট করেছে")
            except ValueError:
                await update.message.reply_text("❌ নম্বর সঠিক নয়")
        
        elif action == 'stats':
            result = todo_manager.get_stats(user_id)
            await update.message.reply_text(result, parse_mode=ParseMode.MARKDOWN)
            logger.info(f"✅ User {user_id} স্ট্যাটিস্টিক্স দেখেছে")
        
        else:
            await update.message.reply_text("❌ অজানা কমান্ড। /todo লিখুন সাহায্যের জন্য।")
    
    except Exception as e:
        logger.error(f"❌ todo_command এ ত্রুটি: {e}")
        await update.message.reply_text(f"❌ ত্রুটি: {str(e)}")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """বার্তা হ্যান্ডলিং"""
    try:
        user_id = update.effective_user.id
        user_message = update.message.text
        mode = context.user_data.get('mode', 'chat')
        
        await update.message.chat.send_action("typing")
        
        if mode == 'chat':
            response = ai.chat(user_id, user_message)
        elif mode == 'support':
            response = ai.customer_support(user_id, user_message)
        else:
            response = ai.chat(user_id, user_message)
        
        await update.message.reply_text(
            response,
            parse_mode=ParseMode.MARKDOWN
        )
        logger.info(f"✅ User {user_id} এর বার্তা প্রক্রিয়া করা হয়েছে")
    
    except Exception as e:
        error_message = f"❌ ত্রুটি: {str(e)}"
        logger.error(f"❌ handle_message এ ত্রুটি: {e}", exc_info=True)
        await update.message.reply_text(error_message)


async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """চ্যাট হিস্টরি সাফ করুন"""
    try:
        user_id = update.effective_user.id
        ai.clear_history(user_id)
        await update.message.reply_text(
            "✅ আপনার চ্যাট হিস্টরি সাফ করা হয়েছে। নতুন করে শুরু করুন!"
        )
        logger.info(f"✅ User {user_id} এর চ্যাট হিস্টরি সাফ হয়েছে")
    except Exception as e:
        logger.error(f"❌ clear_command এ ত্রুটি: {e}")
        await update.message.reply_text(f"❌ ত্রুটি: {str(e)}")


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ত্রুটি হ্যান্ডলিং"""
    logger.error(f"❌ Error: Update {update} caused error {context.error}", exc_info=True)


def setup_handlers(app: Application):
    """সব হ্যান্ডলার সেটআপ করুন"""
    
    # কমান্ড হ্যান্ডলার
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('clear', clear_command))
    app.add_handler(CommandHandler('products', products_command))
    app.add_handler(CommandHandler('weather', weather_command))
    app.add_handler(CommandHandler('forecast', forecast_command))
    app.add_handler(CommandHandler('todo', todo_command))
    
    # মোড হ্যান্ডলার
    app.add_handler(CommandHandler('chat', chat_mode))
    app.add_handler(CommandHandler('support', support_mode))
    
    # বার্তা হ্যান্ডলার
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # ত্রুটি হ্যান্ডলার
    app.add_error_handler(error_handler)
    
    logger.info("✅ সব হ্যান্ডলার সেটআপ সম্পন্ন")
