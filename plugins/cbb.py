#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    
    if data == "about":
        await query.message.edit_text(
            text=f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://github.com/CodeXBotz/File-Sharing-Bot'>Click here</a>\n○ Channel : @CodeXBotz\n○ Support Group : @CodeXBotzSupport</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🏠 Home", callback_data="home"),
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ]
                ]
            )
        )
        
    elif data == "home":
        # திரும்பவும் மெயின் ஸ்டார்ட் மெசேஜ்க்கு போகும்
        await query.message.edit_text(
            text=f"<b>வணக்கம் {query.from_user.mention}! \n\nநான் உங்களுடைய ஃபைல் ஷேரிங் பாட்.</b>", # இங்க உங்க விருப்பமான ஸ்டார்ட் மெசேஜ் எழுதிக்கலாம்
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ℹ️ About", callback_data="about"),
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ]
                ]
            )
        )
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
