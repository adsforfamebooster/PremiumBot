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
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "17107151")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e8ef290caf40133405160fdc0fabcbee") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "")) #Your db channel Id
OWNER = os.environ.get("OWNER", "sewxiy") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "SUPERHERO")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "0"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/CodeflixSupport")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

#--------------------------------------------
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
TUT_VID = os.environ.get("TUT_VID","")

#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>This is a file to link bot work for @Admin\n\n❏ bot commands\n├/start : start the bot\n├/about : our information\n└/help : help related bot\n\n simply click on link and start the bot join both channels and try again thats it.....!\n\n developed by <a href=https://t.me/admin>Admin</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈ Creator: <a href=https://t.me/admin>Admin</a>\n</a></blockquote></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}\n\n<blockquote>I am file store bot, I can store private files in specified channel and other users can access it from special link.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>Join our channels and then click on reload button to get your requested file.</b>")

CMD_TXT = """<blockquote><b>» Admin commands:</b></blockquote>

<b>›› /dlt_time :</b> Set auto delete time
<b>›› /check_dlt_time :</b> Check current delete time
<b>›› /dbroadcast :</b> Broadcast document / video
<b>›› /ban :</b> Ban a user
<b>›› /unban :</b> Unban a user
<b>›› /banlist :</b> Get list of banned users
<b>›› /addchnl :</b> Add force sub channel
<b>›› /delchnl :</b> Remove force sub channel
<b>›› /listchnl :</b> View added channels
<b>›› /fsub_mode :</b> Toggle force sub mode
<b>›› /pbroadcast :</b> Send photo to all users
<b>›› /add_admin :</b> Add an admin
<b>›› /deladmin :</b> Remove an admin
<b>›› /admins :</b> Get list of admins
<b>›› /addpremium :</b> Add a premium user
<b>›› /premium_users :</b> List all premium users
<b>›› /remove_premium :</b> Remove premium from a user
<b>›› /myplan :</b> Check your premium status
<b>›› /count :</b> Count verifications
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Sorry! You are not my owner!!"

#==========================(BUY PREMIUM)====================#

OWNER_TAG = os.environ.get("OWNER_TAG", "admin")
UPI_ID = os.environ.get("UPI_ID", "@admin")
QR_PIC = os.environ.get("QR_PIC", "")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/admin")
#--------------------------------------------
#Time and its price
#15 Days
PRICE1 = os.environ.get("PRICE1", "70 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "120 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "350 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "650 rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "999 rs")

#===================(END)========================#

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
   
