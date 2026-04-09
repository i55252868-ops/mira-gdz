"""
Хендлеры: /start, главное меню, о нас, прайс, помощь.
"""

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from config import SHOP_NAME, SHOP_DESCRIPTION, SUPPORT_TEXT, PRICE_TEXT
from keyboards.menu import main_menu_kb, back_to_menu_kb
from keyboards.orders import confirm_complaint_kb

router = Router()


def get_full_name(user) -> str:
    name = (user.first_name or "") + (" " + user.last_name if user.last_name else "")
    return name.strip() or "—"


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(
        f"👋 Привет, <b>{get_full_name(message.from_user)}</b>!\n\n"
        f"Добро пожаловать в <b>{SHOP_NAME}</b>!\n\n"
        "Я помогу вам заказать учебную работу — быстро, удобно и без лишних вопросов.\n\n"
        "Выберите раздел 👇",
        reply_markup=main_menu_kb(),
    )


@router.callback_query(lambda c: c.data == "main_menu")
async def cb_main_menu(call: CallbackQuery) -> None:
    await call.message.edit_text(
        "🏠 <b>Главное меню</b>\n\nВыберите раздел 👇",
        reply_markup=main_menu_kb(),
    )


@router.callback_query(lambda c: c.data == "about")
async def cb_about(call: CallbackQuery) -> None:
    await call.message.edit_text(
        SHOP_DESCRIPTION,
        reply_markup=back_to_menu_kb(),
    )


@router.callback_query(lambda c: c.data == "price")
async def cb_price(call: CallbackQuery) -> None:
    from aiogram.utils.keyboard import InlineKeyboardBuilder
    builder = InlineKeyboardBuilder()
    builder.button(text="📦 Сделать заказ", callback_data="order")
    builder.button(text="🏠 Главное меню",  callback_data="main_menu")
    builder.adjust(1)
    await call.message.edit_text(
        PRICE_TEXT,
        reply_markup=builder.as_markup(),
    )


@router.callback_query(lambda c: c.data == "help")
async def cb_help(call: CallbackQuery) -> None:
    from aiogram.utils.keyboard import InlineKeyboardBuilder
    builder = InlineKeyboardBuilder()
    builder.button(text="📝 Написать жалобу / вопрос", callback_data="complaint")
    builder.button(text="🏠 Главное меню",              callback_data="main_menu")
    builder.adjust(1)
    await call.message.edit_text(
        SUPPORT_TEXT,
        reply_markup=builder.as_markup(),
    )
