# Miras_gdz Bot

Telegram-бот для приёма заказов на учебные работы.
mira-gdz/
├── amvera.yml
├── main.py
├── config.py
├── requirements.txt
├── database/
│   ├── __init__.py
│   ├── db.py
│   └── models.py
├── handlers/
│   ├── __init__.py
│   ├── start.py
│   ├── orders.py
│   └── admin.py
└── keyboards/
    ├── __init__.py
    ├── menu.py
    ├── orders.py
    └── admin.p


## Установка и запуск

```bash
pip install -r requirements.txt
python main.py
```

## Команды

- `/start` — главное меню
- `/admin` — панель администратора (только для ADMIN_IDS)

## Поддержка

@minonnx
