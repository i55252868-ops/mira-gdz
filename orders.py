"""
Клавиатуры для оформления заказов.
"""

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import WORK_TYPES


def work_types_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for key, val in WORK_TYPES.items():
        builder.button(
            text=f"{val['name']} — {val['price']}",
            callback_data=f"type_{key}",
        )
    builder.button(text="🔙 Назад", callback_data="main_menu")
    builder.adjust(1)
    return builder.as_markup()


def confirm_order_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Подтвердить", callback_data="confirm_order")
    builder.button(text="❌ Отмена",      callback_data="cancel")
    builder.adjust(2)
    return builder.as_markup()


def confirm_complaint_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Отправить", callback_data="confirm_complaint")
    builder.button(text="❌ Отмена",    callback_data="cancel")
    builder.adjust(2)
    return builder.as_markup()
