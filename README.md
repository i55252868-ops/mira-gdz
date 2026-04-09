# Miras_gdz Bot

Telegram-бот для приёма заказов на учебные работы.

## Структура проекта

```
student_bot/
├── main.py                  # Точка входа
├── config.py                # Токен, настройки, прайс
├── requirements.txt
├── database/
│   ├── db.py                # Подключение к БД, init_db
│   └── models.py            # CRUD функции
├── handlers/
│   ├── start.py             # /start, главное меню, о нас, прайс, помощь
│   ├── orders.py            # Оформление заказов и жалоб (FSM)
│   └── admin.py             # Админ-панель (/admin)
└── keyboards/
    ├── menu.py              # Главное меню
    ├── orders.py            # Клавиатуры заказов
    └── admin.py             # Клавиатуры админки
```

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
