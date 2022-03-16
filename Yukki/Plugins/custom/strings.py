from config import ASSISTANT_PREFIX
from Yukki import BOT_NAME, BOT_USERNAME
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = f"""
✨ **Halo MENTION !**

**Sampeyan bisa nggunakake [{BOT_NAME}](https://t.me/{BOT_USERNAME}) kanggo muter Musik utawa Video ing Obrolan Video Grup.**

💡 **Temokake kabeh printah Bot lan cara kerjane ngeklik ing ➤  Commands button**
"""

COMMANDS_TEXT = f"""
✨ **Hello MENTION !**

**Klik ing tombol ing ngisor iki kanggo ngerti printah sandi.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="Commands", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="Settings", callback_data="settingm"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="Updates Channel", url="https://t.me/synxupdate"
            ),
            InlineKeyboardButton(
                text="Support Group", url="https://t.me/synxsupport"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="➕ Add me to Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),            
        ],
        [   
            InlineKeyboardButton(
                text="Commands", callback_data="command_menu"
            ),                       
        ],
        [
            InlineKeyboardButton(
                text="Updates Channel", url="https://t.me/synxupdate"
            ),
            InlineKeyboardButton(
                text="Support Group", url="https://t.me/synxsupport"
            ),                       
        ],        
    ]
)

COMMANDS_BUTTON_USER = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Admin Commands", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="Bot Commands", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Play Commands", callback_data="play_cmd"
            ),            
            InlineKeyboardButton(
                text="Extra Commands", callback_data="extra_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🗑️ Close", callback_data="close_btn"
            ),            
        ],                
    ]
)

COMMANDS_BUTTON_SUDO = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Admin Commands", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="Bot Commands", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Play Commands", callback_data="play_cmd"
            ),
            InlineKeyboardButton(
                text="Sudo Commands", callback_data="sudo_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Extra Commands", callback_data="extra_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🗑️ Close", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🗑️ Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

SUDO_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="More Sudo Commands", url="https://telegra.ph/SiestaXMusic-Sudo-Commands-02-08"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🗑️ Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)


ADMIN_TEXT = f"""
Here is the help for **Admin Commands:**


--**ADMIN ONLY printah karo ngatur VC tengen:**--

/pause 
- Ngaso muter musik ing obrolan swara.

/resume
- Terusake musik sing ngaso ing obrolan swara.

/skip
- Skip musik sing lagi diputer ing obrolan swara

/end or /stop
- Mungkasi playout.


--**Authorised Users List:**--

**{BOT_NAME} nduweni fitur tambahan kanggo pangguna non-admin sing pengin nggunakake printah admin**
- Pangguna auth bisa ngliwati, ngaso, mandheg, nerusake Obrolan Swara sanajan tanpa Hak Admin.


/auth [Jeneng pangguna utawa Balas Pesen] 
- Tambah pangguna menyang DAFTAR AUTH saka grup.

/unauth [Jeneng pangguna utawa Balas Pesen] 
- Mbusak pangguna saka AUTH LIST saka grup.

/authusers 
- Priksa DAFTAR AUTH saka grup.
"""

BOT_TEXT = """
Here is the help for **Bot Commands:**


/vcstart 
- Miwiti Bot Musik.

/vchelp 
- Entuk Menu Helper Commands kanthi panjelasan rinci babagan printah.

/vcsettings 
- Entuk Dashboard Setelan saka grup. Sampeyan bisa ngatur Mode Pangguna Auth. Mode printah saka kene.

/ping
- Ping Bot lan priksa statistik Ram, Cpu etc saka Music Bot."""

PLAY_TEXT = """
Punika bantuan kanggo **Play Commands:**


--**Youtube and Telegram Files:**--

/play __[Jeneng Musik]__(Bot bakal nggoleki ing Youtube)
/play __[Link Youtube Track utawa Dhaptar lagu]__
/play __[Video, Live, M3U8 Links]__
/play __[Mbales File Audio utawa Video]__
- Stream Video utawa Musik ing Obrolan Swara kanthi milih Tombol inline sing sampeyan entuk


--**Playlists:**--

/playplaylist 
- Miwiti muter Dhaptar lagu sing disimpen.

/playlist 
- Priksa dhaptar lagu sing wis disimpen ing server.

/delmyplaylist
- Busak musik sing disimpen ing dhaptar lagu

/delgroupplaylist
- Busak musik sing disimpen ing dhaptar lagu grup sampeyan [Requires Admin Rights.]
"""

SUDO_TEXT = f"""
Here is the help for **Sudo Commands:**

**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

**<u>BOT COMMANDS:</u>**
/restart - Restart Bot. 
/update - Update Bot.
/stats - Check Bots Stats

**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot

**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast message.
/broadcast_pin [Message or Reply to a Message] - Broadcast message with pin [Disabled Notifications].
/broadcast_pin_loud [Message or Reply to a Message] - Broadcast message with pin [Enabled Notifications].

**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Ban a user globally in Bot's Served Chats and prevents user from using bot commands.
/ungban [Username or Reply to a user] - Remove a user from Bot's GBan List.
"""

EXTRA_TEXT = """
Here is the help for **Extra Commands:**


/lyrics [Music Name]
- Searches Lyrics for the particular Music on web.

/sudolist 
- Check Sudo Users of Music Bot

/song [Track Name] or [YT Link]
- Download any track from youtube in mp3 or mp4 formats via Bot.

/queue
- Check Queue List of Music.
"""

BASIC_TEXT = """
💠 **Basic Commands:**

/start - start the bot
/help - get help message
/play - play songs or videos in vc
/vplay - play videos directly in vc
/spotify - play songs from spotify
/resso - play songs from resso
/lyrics - get lyrics of song
/ping - ping the bot
/playlist - play your playlist
/song - download a song as music or video
/settings - settings of the group
/theme - set theme for your group
/queue - get queued song
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🔍 Basic Commands", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="Advanced Commands", callback_data="advanced_cmd"
            ),
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="🗑️ Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)
