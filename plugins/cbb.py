#(©)CodeXBotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, START_MSG, START_PIC
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.enums import ParseMode

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    
    if data == "about":
        about_text = f"<b>Nᴏ Iɴғᴏʀᴍᴀᴛɪᴏɴ !?</b>"
        
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ʜᴏᴍᴇ", callback_data="home"),
                    InlineKeyboardButton("• ᴄʟᴏsᴇ", callback_data="close")
                ]
            ]
        )

        # மெசேஜில் போட்டோ இருந்தால் Edit Caption, இல்லை என்றால் Edit Text
        if query.message.photo:
            await query.message.edit_caption(
                caption=about_text,
                parse_mode=ParseMode.HTML,
                reply_markup=reply_markup
            )
        else:
            await query.message.edit_text(
                text=about_text,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )
        
    elif data == "home":
        # உங்க மெயின் Start Message (Photo Caption அல்லது Text)
        start_text = START_MSG.format(
            first=query.from_user.first_name,
            last=query.from_user.last_name,
            username=None if not query.from_user.username else '@' + query.from_user.username,
            mention=query.from_user.mention,
            id=query.from_user.id
        )

        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴀʙᴏᴜᴛ ᴍᴇ", callback_data="about"),
                    InlineKeyboardButton("• ᴄʟᴏsᴇ", callback_data="close")
                ]
            ]
        )

        # Home அழுத்தும்போது திரும்பவும் மெயின் Start Photo/Text-க்கே மாறும்
        if query.message.photo:
            await query.message.edit_caption(
                caption=start_text,
                parse_mode=ParseMode.HTML,
                reply_markup=reply_markup
            )
        else:
            await query.message.edit_text(
                text=start_text,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
                reply_markup=reply_markup
            )
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except Exception:
            pass
