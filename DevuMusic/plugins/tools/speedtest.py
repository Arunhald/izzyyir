# Creator Or Dev @HYPER_AD13 | @SHINING_OFF <Found On telegram>
# Found on github < https://github.com/ItsmeHyper13 >.
import asyncio
import os
import speedtest
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from strings import get_command
from DevuMusic import app
from DevuMusic.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("Running Download SpeedTest")
        test.download()
        m = m.edit("Running Upload SpeedTest")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("Sharing SpeedTest Results")    
    except Exception as e:
        return m.edit(e)
    return result





@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    BUTUN = [
        [
            InlineKeyboardButton(
                "◊ ʀᴇᴘᴏ ◊",
                url="https://github.com/ItsmeHyper13/DevuMuxic",
            ),
            InlineKeyboardButton(
                "◊ ᴄʟᴏsᴇ ◊",
                callback_data=f"forceclose abc|{message.from_user.id}",
            ),
        ],
    ]
    m = await message.reply_text("Running Speed test")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    poto = result["share"]
    output = f"""<strong><b><u>♦ 𝄞ᴘᴇᴇᴅᴛᴇsᴛ∮ʀᴇsᴜʟᴛs.</u></b></strong>
    
<strong><i>➥ <u>ᴄʟɪᴇɴᴛ</u> ✨»»»</i></strong>
<b>❍ ɪsᴘ</b> ⇝ <code>{result['client']['isp']}</code>
<b>❍ ᴄᴏᴜɴᴛʀʏ</b> ⇝ <code>{result['client']['country']}</code>
  
<strong><i>➥ <u>sᴇʀᴠᴇʀ</u> 🌟»»»</i></strong>
<b>❍ ɴᴀᴍᴇ</b> ⇝ <code>{result['server']['name']}</code>
<b>❍ ᴄᴏᴜɴᴛʀʏ</b> ⇝ <code>{result['server']['country']},{result['server']['cc']}</code>
<b>❍ sᴘᴏɴsᴏʀ</b> ⇝ <code>{result['server']['sponsor']}</code>
<b>❍ ʟᴀᴛᴇɴᴄʏ</b> ⇝ <code>{result['server']['latency']}</code>
<b>❍ ᴘɪɴɢ</b> ⇝ <code>{result['ping']}</code>"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=poto, caption=output, reply_markup=InlineKeyboardMarkup(BUTUN)
    )
    await m.delete()
    await message.delete()
