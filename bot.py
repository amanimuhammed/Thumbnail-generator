from pyrogram import Client, filters

from pyrogram.types import CallbackQuery, ChatPermissions, InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

import os 

TOKEN = os.environ.get("TOKEN","")
API_ID =int(os.environ.get("API_ID",12345))
API_HASH =os.environ.get("API_HASH","")
CHANNEL = os.environ.get("CHANNEL","")



app= Client("Thumbot",bot_token=TOKEN,api_hash=API_HASH,
            api_id=APP_ID)

@app.on_message(filters.command(['start']))
def start(client, message):
            message.reply_text(text =f"**Hello {message.from_user.first_name }** \n\n **I am simple YouTube Thumbnail link Generator** \n\n **Send me Youtube link and get Thumbnail link** \n\n 🏷 **Maintained By: @Amani_m_h_d**",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📜 Updates Channel" ,url="https://t.me/My_Test_Botz") ],
                 [InlineKeyboardButton("Developer 👨‍💻", url="https://t.me/Amani_m_h_d") ]
           ]
        ) )


@app.on_message(filters.regex("^https?:\/\/?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/).{11}"))
def gyt(client,message):
      update_channel = CHANNEL
      user_id = message.from_user.id
      if update_channel :
        try:
	      client.get_chat_member(update_channel, user_id)
        except UserNotParticipant:
	      message.reply_text("**You Must Join My Updates Channel to use ME 😎 🤭** ",parse_mode="markdown", reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([ [ InlineKeyboardButton("Join My Updates Channel" ,url="https://t.me/My_Test_Botz") ]]))
	      return

	try:
		ms = message.reply_text("```checking valid link or not ```",reply_to_message_id = message.message_id )
		url =message.matches[0].group(0)
		video = YouTube(url)
		thumb = video.thumbnail_url
		app.send_photo(message.chat.id ,photo = thumb, reply_markup=InlineKeyboardMarkup([    [ InlineKeyboardButton("🔗 link" ,url=thumb) ]]))
		ms.delete()
        
	except VideoUnavailable:
		ms.edit("**Invalid video link!**")


		


app.run()
	
