import asyncio
import logging
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import keyboard as kb

router = Router()

class Reg(StatesGroup):
    full_name = State()
    city = State()
    chat_city = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    user = message.from_user.username
    print(message.from_user.id, message.from_user.username)
    await message.answer("Выберите раздел👇", reply_markup=kb.start_kb)



@router.callback_query(F.data == "trustedpartners")
async def cmd_trustedpartners(Callback: CallbackQuery):
    await Callback.answer()
    await Callback.message.edit_text(
        "Bы хотели бы поделиться информацией о\nсвоих услугах и стать нашим проверенным\nпартнером?\n<b>Отличная идея!<b>\nНапишите нашему менеджеру\n@eventworkadmin. Она у нас чудесная и\nпроконсультирует вас лучше, чем я.\n\nПо вопросам сотрудничества и рекламы\nнажмите на кнопку ..."
    , reply_markup=kb.trusted_partners)

@router.callback_query(F.data == "registration in the chat")
async def cmd_registration(Callback: CallbackQuery):
    await Callback.answer()
    await Callback.message.edit_text(
        """Чтобы работа в чате была более продуктивной, давайте познакомимся с вами поближе!
Для этого вам нужно будет ответить на несколько вопросов, которые помогут мне быть более эффективным для вас"""
    , reply_markup=kb.registration)

@router.callback_query(F.data == "Start")
async def start(Callback: CallbackQuery):
    await Callback.answer()
    await Callback.message.edit_text("Выберите раздел👇", reply_markup=kb.start_kb)

@router.callback_query(F.data == "go1")
async def cmd_go1(Callback: CallbackQuery):
    await Callback.answer()
    await Callback.message.edit_text("Вы спец?", reply_markup=kb.go1)


@router.callback_query(F.data == "go2")
async def cmd_go2(Callback: CallbackQuery):
    await Callback.answer()
    await Callback.message.edit_text("""Ваши данные попадут в общую базу и будут доступны по запросу на специалистов вашего профиля. Для. вас это может стать дополнительной рекламой.
Мы с удовольствием делимся контактами профессионалов.
Вы согласны?""", reply_markup=kb.go2)

@router.callback_query(F.data == "go3")
async def cmd_go3(Callback: CallbackQuery, state: FSMContext):
    await state.set_state(Reg.full_name)
    await Callback.answer()
    await Callback.message.edit_text("Напишите своё имя и фамилию (именно в таком порядке)")


@router.message(Reg.full_name)
async def cmd_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await state.set_state(Reg.city)
    await message.answer("Напишите город вашего проживания")

@router.message(Reg.city)
async def cmd_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await state.set_state(Reg.chat_city)
    await message.answer("Чат какого города вас интересует(можно выбрать несколько)", reply_markup=kb.city_keyboard)

@router.message(Reg.chat_city)
async def cmd_chat_city(message: Message, state: FSMContext):
    pass
