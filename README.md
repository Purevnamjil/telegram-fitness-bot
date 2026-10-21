# Telegram Fitness Bot

Энэ төсөл нь Telegram бот бөгөөд өдөр бүр өглөө/оройн сануулагч мессеж илгээдэг.

## Суурилуулалт

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Тохиргоо

Бот ажиллуулахын өмнө `BOT_TOKEN` болон `CHAT_ID` environment хувьсгуудыг тохируулна.

```bash
export BOT_TOKEN="your_bot_token"
export CHAT_ID="your_chat_id"
python bot.py
```

## Функц

- `/start` команд ажиллуулна
- Өглөөний 08:00 цагт сануулагч мессеж илгээдэг
- Оройн 20:00 цагт сануулагч мессеж илгээдэг

## GitHub руу байршуулалт

```bash
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```
