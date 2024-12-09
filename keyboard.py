from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Профиль", callback_data="portfolio"), InlineKeyboardButton(text="Заказы", callback_data="data")],
    [InlineKeyboardButton(text="Фото", callback_data="photo"), InlineKeyboardButton(text="Текст", callback_data="text")]

])

setting = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="test", url="https://web.telegram.org/a/")]])

cars = ["BMW", "Tesla", "Matiz", "Lada"]

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for i in cars:
        keyboard.add(InlineKeyboardButton(text=i, url="https://web.telegram.org/a/"))
    return keyboard.adjust(2).as_markup()


start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Регистрация в чате", callback_data="registration in the chat")],
    [InlineKeyboardButton(text="Подписка", callback_data="subscription"), InlineKeyboardButton(text="Pro поиск", callback_data="pro search")],
    [InlineKeyboardButton(text="Задать вопрос", callback_data="question"), InlineKeyboardButton(text="Сотрудничество", callback_data="cooperation")],
    [InlineKeyboardButton(text="Проверенные партнеры", callback_data="trustedpartners")]
])

registration = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Давай", callback_data="go1"), InlineKeyboardButton(text="Нет", callback_data="Start")]])
go1 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Да", callback_data="go2"), InlineKeyboardButton(text="Нет", callback_data="Start")]])
go2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Прочитать оферту", url="https://offer.topeventers.ru/")], [InlineKeyboardButton(text="Да", callback_data="go3"), InlineKeyboardButton(text="Нет", callback_data="Start")]])
trusted_partners = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Написать чудесному мессенжеру", url="https://t.me/eventworkadmin")]])

city_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
        [InlineKeyboardButton(text="Пермь", callback_data='perm'),
        InlineKeyboardButton(text="Екатеринбург", callback_data='ekb'),
        InlineKeyboardButton(text="Тюмень", callback_data='tyumen'),],
        [InlineKeyboardButton(text="Челябинск", callback_data='chelyabinsk'),
        InlineKeyboardButton(text="Ростов-На-Дону", callback_data='rostov'),],
        [InlineKeyboardButton(text="Оренбург", callback_data='orenburg'),
        InlineKeyboardButton(text="Новосибирск", callback_data='novosibirsk'),],
        [InlineKeyboardButton(text="Нижний Новгород", callback_data='nizhny_novgorod'),
        InlineKeyboardButton(text="Самара", callback_data='samara'),],
        [InlineKeyboardButton(text="Казань", callback_data='kazan'),
        InlineKeyboardButton(text="Краснодар", callback_data='krasnodar'),
        InlineKeyboardButton(text="Уфа", callback_data='ufa'),],
        [InlineKeyboardButton(text="Добавить город", callback_data='add_city')]
        ]
    )
