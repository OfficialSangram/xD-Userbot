from .. import *

@app.on_message(commandx(["alive"]))
async def alive_check(client, message):
    await message.reply_text("**🥀 𝙄 𝙖𝙢 𝙖𝙡𝙞𝙫𝙚 𝙢𝙮 𝙙𝙚𝙖𝙧 𝙢𝙖𝙨𝙩𝙚𝙧....**")



__NAME__ = "Alive"
__MENU__ = f"""
**🥀 Check Userbot Working
Or Not ..**

**Example:** `.alive`
"""
