# Sonic Service Bot 🤖

এটি একটি অত্যাধুনিক Telegram Bot যা Claude AI দ্বারা চালিত এবং তিনটি প্রধান সেবা প্রদান করে:

## বৈশিষ্ট্য ✨

### 1. General AI Chatbot 💬
- Claude AI এর সাথে স্বাভাবিক কথোপকথন
- যেকোনো প্রশ্নের উত্তর
- সৃজনশীল এবং তথ্যপূর্ণ রেসপন্স

### 2. Customer Support 🆘
- গ্রাহক সেবা এবং সহায়তা
- সমস্যা সমাধান
- প্রোডাক্ট সম্পর্কিত তথ্য

### 3. Digital Product Selling 🛍️
- Sonic Brand Market এর ডিজিটাল প্রোডাক্ট বিক্রয়
- প্রোডাক্ট ক্যাটালগ এবং মূল্য
- অর্ডার ম্যানেজমেন্ট

## প্রয়োজনীয় API কী 🔑

```
1. Telegram Bot Token: আপনার Telegram Bot Token
2. Claude API Key: Anthropic এর Claude API Key
```

## ইনস্টলেশন 📦

```bash
# প্রয়োজনীয় প্যাকেজ ইনস্টল করুন
pip install -r requirements.txt

# কনফিগ করুন (.env ফাইল)
cp .env.example .env

# আপনার টোকেন এবং API কী যোগ করুন

# Bot চালু করুন
python main.py
```

## ফাইল স্ট্রাকচার 📁

```
.
├── main.py              # মূল এন্ট্রি পয়েন্ট
├── bot/
│   ├── __init__.py
│   ├── handlers.py      # সব হ্যান্ডলার
│   ├── claude_ai.py     # Claude AI ইন্টিগ্রেশন
│   └── products.py      # প্রোডাক্ট ম্যানেজমেন্ট
├── config/
│   └── settings.py      # কনফিগারেশন
├── requirements.txt     # ডিপেন্ডেন্সি
├── .env.example         # এনভায়রনমেন্ট টেমপ্লেট
└── README.md            # এই ফাইল
```

## ব্যবহার 🚀

Bot কে Telegram এ সার্চ করুন এবং শুরু করুন:

- `/start` - স্বাগতম বার্তা
- `/help` - সাহায্য
- `/chat` - AI চ্যাট
- `/support` - কাস্টমার সাপোর্ট
- `/products` - প্রোডাক্ট ক্যাটালগ

## লাইসেন্স 📜

MIT License
