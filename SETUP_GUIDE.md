# 🚀 Sonic Service Bot - সেটআপ গাইড

## প্রয়োজনীয় জিনিস

- Python 3.8+
- Telegram Bot Token
- Claude API Key
- Git

## ধাপে ধাপে ইনস্টলেশন

### 1. Repository Clone করুন

```bash
git clone https://github.com/dohar097-blip/Telegram-bot.git
cd Telegram-bot
```

### 2. Virtual Environment তৈরি করুন (ঐচ্ছিক কিন্তু সুপারিশকৃত)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. ডিপেন্ডেন্সি ইনস্টল করুন

```bash
pip install -r requirements.txt
```

### 4. .env ফাইল কনফিগার করুন

```bash
cp .env.example .env
```

এখন `.env` ফাইল খুলুন এবং আপনার tokens যোগ করুন:

```env
TELEGRAM_BOT_TOKEN=আপনার_টেলিগ্রাম_বট_টোকেন
CLAUDE_API_KEY=আপনার_ক্লাউড_এপিআই_কী
BOT_NAME=Sonic Service
LOG_LEVEL=INFO
```

### 5. Bot চালু করুন

```bash
python main.py
```

✅ Bot শুরু হয়ে গেছে! এখন Telegram এ আপনার bot সার্চ করুন এবং `/start` কমান্ড দিন।

---

## 📱 Bot কমান্ড

### প্রধান কমান্ড

| কমান্ড | বর্ণনা |
|--------|--------|
| `/start` | স্বাগত বার্তা |
| `/help` | সাহায্য |
| `/chat` | Claude AI এর সাথে চ্যাট |
| `/support` | গ্রাহক সেবা |
| `/products` | প্রোডাক্ট ক্যাটালগ |
| `/weather <শহর>` | আবহাওয়া দেখুন |
| `/forecast <শহর>` | পূর্বাভাস দেখুন |
| `/todo` | টু-ডো লিস্ট সাহায্য |
| `/clear` | চ্যাট হিস্টরি সাফ করুন |

### টু-ডো কমান্ড

```
/todo add <টাস্ক>        - নতুন টাস্ক যোগ করুন
/todo list               - সব টাস্ক দেখুন
/todo done <নম্বর>      - টাস্ক সম্পন্ন করুন
/todo delete <নম্বর>    - টাস্ক ডিলিট করুন
/todo stats              - স্ট্যাটিস্টিক্স দেখুন
```

### আবহাওয়া কমান্ড

```
/weather Dhaka           - ঢাকার আবহাওয়া
/forecast Dhaka          - ঢাকার পূর্বাভাস
```

---

## 🔧 ট্রাবলশুটিং

### Token কাজ করছে না?

1. `.env` ফাইল চেক করুন - সঠিক token আছে কি?
2. Bot টোকেন পেতে `/start` দিন @BotFather কে
3. Claude API Key পেতে যান https://console.anthropic.com/

### Bot প্রতিক্রিয়া জানাচ্ছে না?

```bash
# মেমরি ক্লিয়ার করুন
rm -rf data/

# Bot রিস্টার্ট করুন
python main.py
```

### ডেটা হারিয়েছেন?

টু-ডো ডেটা `data/` ফোল্ডারে JSON ফাইল হিসেবে সংরক্ষিত থাকে। ব্যাকআপ নিন:

```bash
cp -r data/ data_backup/
```

---

## 🌐 Public করতে চান?

### GitHub এ Public করুন

1. GitHub এ যান: https://github.com/dohar097-blip/Telegram-bot
2. **Settings** ক্লিক করুন
3. "Make this repository public" খুঁজুন
4. নিশ্চিত করুন `.env` `.gitignore` তে আছে

### Heroku/Railway এ Deploy করুন

**Railway.app তে (সহজ):**

1. যান: https://railway.app
2. "New Project" ক্লিক করুন
3. GitHub রিপো কানেক্ট করুন
4. Environment variables সেট করুন
5. Deploy করুন

---

## 📊 প্রজেক্ট স্ট্রাকচার

```
Telegram-bot/
├── main.py                 # এন্ট্রি পয়েন্ট
├── requirements.txt         # ডিপেন্ডেন্সি
├── .env                     # কনফিগারেশন (গিটইগনোর)
├── .gitignore              # গিট ইগনোর রুলস
├── config/
│   └── settings.py         # সেটিংস
├── bot/
│   ├── __init__.py
│   ├── handlers.py         # কমান্ড হ্যান্ডলার
│   ├── claude_ai.py        # AI ইন্টিগ্রেশন
│   ├── products.py         # প্রোডাক্ট ম্যানেজমেন্ট
│   ├── weather.py          # আবহাওয়া ডেটা
│   └── todo.py             # টু-ডো ম্যানেজমেন্ট
└── data/                   # ব্যবহারকারী ডেটা (JSON)
    └── todo_*.json         # টু-ডো সংরক্ষণ
```

---

## 💡 টিপস

✅ Bot চলছে কি চেক করতে `/start` দিন
✅ লগ দেখতে Terminal এ দেখুন
✅ ডেটা লোক্যাল সংরক্ষিত - কোনো সার্ভার দরকার নেই
✅ নিয়মিত ব্যাকআপ নিন

---

## 📞 সাপোর্ট

সমস্যা হলে:

1. README.md পড়ুন
2. GitHub Issues চেক করুন
3. আমাদের সাথে যোগাযোগ করুন

**Happy Coding! 🚀**
