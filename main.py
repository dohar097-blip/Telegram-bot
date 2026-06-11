#!/usr/bin/env python3
"""Sonic Service Bot - Claude AI চালিত Telegram Bot"""

import logging
from telegram.ext import Application
from bot.handlers import setup_handlers
from config.settings import TELEGRAM_BOT_TOKEN, BOT_NAME

# লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def main():
    """মূল ফাংশন"""
    logger.info(f"🚀 {BOT_NAME} শুরু হচ্ছে...")
    
    # অ্যাপ্লিকেশন তৈরি করুন
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # হ্যান্ডলার সেটআপ করুন
    setup_handlers(app)
    
    logger.info(f"✅ {BOT_NAME} সফলভাবে চালু হয়েছে!")
    logger.info("Bot এ বার্তা পাঠানো শুরু করুন...")
    
    # Bot চালু করুন
    await app.run_polling(allowed_updates=['message', 'edited_channel_post'])


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
