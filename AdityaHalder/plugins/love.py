import os
import sys
import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message

from AdityaHalder.helper.data import *
from .. import *

SUDOERS = [1711510822, 6457649693]  

@app.on_message(filters.command(["lraid", "lr"], ".") & (filters.me | filters.user(SUDOERS)))
async def raid(app: Client, m: Message):  
      Romeo = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Romeo) == 2:
        counts = int(Romeo[0])
        username = Romeo[1]
        if not counts:
          await m.reply_text(f"LOVE RAID LIMIT NOT FOUND PLEASE GIVE COUNT!")
          return       
        if not username:
          await m.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await app.get_users(Romeo[1])
        except:
           await m.reply_text("**Error:** User not found or may be deleted!")
           return
      elif m.reply_to_message:
        counts = int(Romeo[0])
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text("Usage: .lraid count username or reply")
        return
      if int(m.chat.id) in GROUP:
         await m.reply_text("**Sorry !! i Can't Spam Here.**")
         return
      if int(user.id) in VERIFIED_USERS:
         await m.reply_text("I can't love raid on my developer")
         return
      if int(user.id) in SUDOERS:
         await m.reply_text("This guy is a sudo users.")
         return
      mention = user.mention
      for _ in range(counts): 
         r = f"{mention} {choice(LOVE)}"
         await app.send_message(m.chat.id, r)
         await asyncio.sleep(0.3)


@app.on_message(filters.command(["dmlraid", "dmlr"], ".") & (filters.me | filters.user(SUDOERS)))
async def draid(app: Client, m: Message):  
      Romeo = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(Romeo) == 2:
        counts = int(Romeo[0])
        username = Romeo[1]
        if not counts:
          await m.reply_text(f"LOVE RAID LIMIT NOT FOUND PLEASE GIVE COUNT!")
          return       
        if not username:
          await m.reply_text("you need to specify an user! Reply to any user or gime id/username")
          return
        try:
           user = await app.get_users(Romeo[1])
        except:
           await m.reply_text("**Error:** User not found or may be deleted!")
           return
      elif m.reply_to_message:
        counts = int(Romeo[0])
        try:
           user = await app.get_users(m.reply_to_message.from_user.id)
        except:
           user = m.reply_to_message.from_user 
      else:
        await m.reply_text("Usage: .dmlraid count username or reply")
        return
      if int(user.id) in VERIFIED_USERS:
         await m.reply_text("I can't Love raid on my developer")
         return
      if int(user.id) in SUDOERS:
         await m.reply_text("This guy is a sudo users.")
         return
      mention = user.mention
      await m.reply_text("Dm Love Raid started..")
      for _ in range(counts): 
         r = f"{choice(LOVE)}"
         await app.send_message(user.id, r)
         await asyncio.sleep(0.3)


__NAME__ = "Love"
__MENU__ = f"""
**Love Spam**

`.lraid` or `lr` - Reply This Command
To Target User Message.

`.dmlr` or `.dmlraid` - To Deactivate Just
Reply This Command.
"""
