#!/usr/bin/env python3
"""Sonic Service Bot - Claude AI চালিত Telegram Bot"""

import logging
import sys
from telegram.ext import Application
from bot.handlers import setup_handlers

# লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Config লোড করুন
try:
    from config.settings import TELEGRAM_BOT_TOKEN, BOT_NAME
    logger.info("✅ Config লোড হয়েছে")
except ImportError as e:
    logger.error(f"❌ Config লোড করতে ব্যর্থ: {e}")
    sys.exit(1)


async def main():
    """মূল ফাংশন"""
    try:
        logger.info(f"🚀 {BOT_NAME} শুরু হচ্ছে...")
        logger.info(f"Token: {TELEGRAM_BOT_TOKEN[:20]}...")
        
        # অ্যাপ্লিকেশন তৈরি করুন
        app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        logger.info("✅ Application builder তৈরি হয়েছে")
        
        # হ্যান্ডলার সেটআপ করুন
        setup_handlers(app)
        logger.info("✅ হ্যান্ডলার সেটআপ হয়েছে")
        
        logger.info(f"✅ {BOT_NAME} সফলভাবে চালু হয়েছে!")
        logger.info("🤖 Bot polling শুরু হয়েছে...")
        logger.info("💬 Bot এ বার্তা পাঠানো শুরু করুন...")
        
        # Bot চালু করুন
        await app.run_polling(allowed_updates=['message', 'edited_channel_post'])
    
    except Exception as e:
        logger.error(f"❌ ত্রুটি: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    import asyncio
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("⛔ Bot বন্ধ করা হয়েছে")
    except Exception as e:
        logger.error(f"❌ মারাত্মক ত্রুটি: {e}", exc_info=True)
