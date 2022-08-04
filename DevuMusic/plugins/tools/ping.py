# Creator Or Dev @HYPER_AD13 | @SHINING_OFF <Found On telegram>
# Found on github < https://github.com/ItsmeHyper13 >.

from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery     

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from DevuMusic import app
from DevuMusic.core.call import Devu
from DevuMusic.utils import bot_sys_stats
from DevuMusic.utils.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


cls = [
    [
        InlineKeyboardButton("✘ •• ❁ ᴄℓοѕє ❁ •• ✘", callback_data="clse")
    ],
]

@app.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Devu.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            MUSIC_BOT_NAME, resp, UP, DISK, CPU, RAM, pytgping
        ),
        reply_markup=InlineKeyboardMarkup(cls)
    )
@app.on_callback_query()
def close(Client, cb: CallbackQuery):
    if cb.data == "clse":
        cb.answer("ϲℓοѕє∂!!🥀")
        cb.message.delete()
