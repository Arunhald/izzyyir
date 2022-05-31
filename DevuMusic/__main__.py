#lol

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from DevuMusic import LOGGER, app, userbot
from DevuMusic.core.call import Devu
from DevuMusic.plugins import ALL_MODULES
from DevuMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop_policy().get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("DevuMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("DevuMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module(f"DevuMusic.plugins{all_module}")
    LOGGER("DevuMusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Devu.start()
    try:
        await Devu.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("DevuMusic").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    await Devu.decorators()
    LOGGER("DevuMusic").info("Devu Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("DevuMusic").info("Stopping Devu Music Bot! GoodBye")
