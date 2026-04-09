"""
Клавиатуры админ-панели.
"""

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import STATUS_LABELS


def admin_main_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="📊 Статистика",    callback_data="adm_stats")
    builder.button(text="🆕 Новые заказы", callback_data="adm_orders_new")
    builder.button(text="📋 Все заказы",   callback_data="adm_orders_all")
    builder.button(text="⚠️ Жалобы",       callback_data="adm_complaints")
    builder.adjust(2)
    return builder.as_markup()


def back_admin_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙 Назад", callback_data="adm_back")
    return builder.as_markup()


def orders_list_kb(orders: list, back_cb: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    STATUS_EMOJI = {"new": "🟡", "in_progress": "🔵", "done": "🟢", "rejected": "🔴"}
    for o in orders:
        emoji = STATUS_EMOJI.get(o["status"], "⚪")
        builder.button(
            text=f"{emoji} #{o['id']} {o['work_type']} — {o['full_name']}",
            callback_data=f"adm_order_{o['id']}",
        )
    builder.button(text="🔙 Назад", callback_data="adm_back")
    builder.adjust(1)
    return builder.as_markup()


def order_status_kb(order_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="🔵 В работе", callback_data=f"adm_s_{order_id}_in_progress")
    builder.button(text="🟢 Готово",   callback_data=f"adm_s_{order_id}_done")
    builder.button(text="🔴 Отклонить", callback_data=f"adm_s_{order_id}_rejected")
    builder.button(text="🔙 Назад",    callback_data="adm_orders_all")
    builder.adjust(2, 1, 1)
    return builder.as_markup()


def complaints_list_kb(complaints: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for c in complaints:
        icon = "🆕" if c["status"] == "new" else "✅"
        builder.button(
            text=f"{icon} #{c['id']} {c['full_name'][:20]}",
            callback_data=f"adm_resolve_{c['id']}",
        )
    builder.button(text="🔙 Назад", callback_data="adm_back")
    builder.adjust(1)
    return builder.as_markup()
