# 🚀 Deployment গাইড

## Railway.app এ Deploy করুন (সুপারিশকৃত)

### Step 1: Railway এ সাইন আপ করুন

যান: https://railway.app এবং GitHub দিয়ে সাইন আপ করুন

### Step 2: নতুন প্রজেক্ট তৈরি করুন

1. "New Project" ক্লিক করুন
2. "Deploy from GitHub repo" নির্বাচন করুন
3. আপনার `dohar097-blip/Telegram-bot` রিপো সিলেক্ট করুন

### Step 3: Environment Variables যোগ করুন

Railway Dashboard এ যান এবং Variables যোগ করুন:

```
TELEGRAM_BOT_TOKEN=আপনার_টোকেন
CLAUDE_API_KEY=আপনার_এপিআই_কী
BOT_NAME=Sonic Service
LOG_LEVEL=INFO
```

### Step 4: Deploy করুন

সব কিছু হয়ে গেলে Railway স্বয়ংক্রিয়ভাবে Deploy করবে!

---

## Heroku এ Deploy করুন

### Step 1: Heroku CLI ইনস্টল করুন

```bash
# macOS
brew tap heroku/brew && brew install heroku

# Windows (Chocolatey)
choco install heroku-cli

# Ubuntu
curl https://cli-assets.heroku.com/install.sh | sh
```

### Step 2: Heroku এ লগইন করুন

```bash
heroku login
```

### Step 3: Procfile তৈরি করুন

```bash
echo "worker: python main.py" > Procfile
```

### Step 4: Deploy করুন

```bash
heroku create your-app-name
git push heroku main
```

### Step 5: Config Variables সেট করুন

```bash
heroku config:set TELEGRAM_BOT_TOKEN="your_token"
heroku config:set CLAUDE_API_KEY="your_key"
```

---

## VPS/Server এ চালান

### ডিজিটাল ওশেন/Linode এ

```bash
# SSH এ লগইন করুন
ssh root@your_server_ip

# পাইথন ইনস্টল করুন
apt update
apt install python3 python3-pip git

# রিপো Clone করুন
git clone https://github.com/dohar097-blip/Telegram-bot.git
cd Telegram-bot

# Setup করুন
pip install -r requirements.txt

# .env তৈরি করুন
nano .env

# systemd service তৈরি করুন
sudo nano /etc/systemd/system/sonic-bot.service
```

**systemd service ফাইল:**

```ini
[Unit]
Description=Sonic Service Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/Telegram-bot
ExecStart=/usr/bin/python3 /root/Telegram-bot/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### চালু করুন

```bash
sudo systemctl daemon-reload
sudo systemctl enable sonic-bot
sudo systemctl start sonic-bot
sudo systemctl status sonic-bot
```

---

## Docker এ চালান

### Dockerfile তৈরি করুন

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

### Build এবং Run করুন

```bash
docker build -t sonic-bot .
docker run -e TELEGRAM_BOT_TOKEN="your_token" -e CLAUDE_API_KEY="your_key" sonic-bot
```

---

## ✅ সবকিছু কাজ করছে কি চেক করুন?

1. Bot এ `/start` দিন
2. `/weather Dhaka` দিন
3. `/todo add test` দিন
4. `/todo list` দিন

যদি সব কাজ করে - সফল! 🎉
