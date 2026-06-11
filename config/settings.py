import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')

# Bot Settings
BOT_NAME = os.getenv('BOT_NAME', 'Sonic Service')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

# Claude Model
CLAUDE_MODEL = 'claude-3-5-sonnet-20241022'
CLAUDE_MAX_TOKENS = 1024

# Sonic Brand Market Products
PRODUCTS = {
    'sonic_vip_pack': {
        'name': 'Sonic VIP প্যাক',
        'price': 299,
        'description': 'প্রিমিয়াম সেবা প্যাকেজ',
        'features': ['24/7 সাপোর্ট', 'প্রাথমিক অ্যাক্সেস', 'বিশেষ ছাড়']
    },
    'sonic_standard': {
        'name': 'Sonic স্ট্যান্ডার্ড',
        'price': 149,
        'description': 'মানসম্পন্ন সেবা',
        'features': ['নিয়মিত সাপোর্ট', 'মূল বৈশিষ্ট্য', 'সম্প্রদায় অ্যাক্সেস']
    },
    'sonic_basic': {
        'name': 'Sonic বেসিক',
        'price': 49,
        'description': 'প্রাথমিক স্তরের সেবা',
        'features': ['ইমেইল সাপোর্ট', 'মৌলিক বৈশিষ্ট্য']
    }
}

# Validation
if not TELEGRAM_BOT_TOKEN:
    raise ValueError('TELEGRAM_BOT_TOKEN পরিবেশ পরিবর্তনশীল প্রয়োজন')

if not CLAUDE_API_KEY:
    raise ValueError('CLAUDE_API_KEY পরিবেশ পরিবর্তনশীল প্রয়োজন')
