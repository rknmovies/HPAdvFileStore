# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#


import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8156814961:AAFaR0uGkpQswbyYlGMq8lnUkRuD7E0VM1E")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "28269435"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "839f282133fe8ee79b4a946095cf4360")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002752916849"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Kicchanayaka")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7508245094"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Hanuman:hanuman@cluster0.l5toshc.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Hanuman")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "600"))


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1003317580141"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "50"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/c534870ef7fbdfd81e701-66149a3c2b466e5eeb.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/c534870ef7fbdfd81e701-66149a3c2b466e5eeb.jpg")

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
TOKEN = True if os.environ.get('TOKEN', "False") == "True" else False  #For Enable Token 

#TOKEN = False if os.environ.get('TOKEN', "FALSE") == 'FALSE' else False # For disable Token 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "Shortxlinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "7f4785525dda19ff748e7f92f1ad4fc7cac85a43")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "False")
TUT_VID = os.environ.get("TUT_VID","https://t.me/hwdownload/3")


HELP_TXT = "<b><blockquote>ꜱᴏʀʀʏ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ\n\n×͜× ᴩᴏᴡᴇʀᴇᴅ ʙʏ : @RKN_MOVIEZ1</b>"

ABOUT_TXT = "<b><blockquote>◈ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/RKNFileStorezbot>RKNFileStorezbot</a>\n◈ ᴅᴇᴠʟᴏᴘᴇʀ : <a href=https://t.me//HP_Raj_Support_Bot>ӇƤ Ʀƛʆ</a>\n◈ ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org/>ᴩʏᴛʜᴏɴ</a>\n◈ ʟɪʙʀᴀʀʏ : <a href=https://docs.pyrogram.org/>ᴩʏʀᴏɢʀᴀᴍ</a>\n◈ ʜᴏsᴛᴇᴅ ᴏɴ: <a href=https://t.me/HP_Raj_MOVIES>ʜᴇʀᴏᴋᴜ</a>\n◈ ᴏᴡɴᴇʀ : <a href=https://t.me/CallmeNayak>_RKN_</a>\n◈ ꜱᴜᴩᴩᴏʀᴛ : <a href=https://t.me/RKN_MOVIEZ1>RKN MOVIEZ1</a></b>"


START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\nɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</b>")
try:
    ADMINS=[8005648537]
    for x in (os.environ.get("ADMINS", "8005648537").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>{filename}\n\n×͜×  ᴊᴏɪɴ ꜰᴏʀ ᴍᴏʀᴇ:- @RKN_MOVIEZ1</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
