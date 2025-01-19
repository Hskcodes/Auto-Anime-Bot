# Bot Configs
API_ID="25582726"
API_HASH="558df3cdc4820fd2de0950656e8112f3"
BOT_TOKEN="8041132355:AAHyYuoDmlGd6t7l-0k7VGf-CXH4c6e5zCs"

# Database ( Mandatory )
MONGO_URI="mongodb+srv://auto:auto@autoanime.990ey.mongodb.net/?retryWrites=true&w=majority&appName=autoanime"


# Channels Configs
FSUB_CHATS= ""  #Multiple Separated By Space ( Optional ) ( Upto 80 )
BACKUP_CHANNEL= "" # Multiple Separated By Space ( Optional )
MAIN_CHANNEL= "-1002024030760"
LOG_CHANNEL="" # ( Optional )
FILE_STORE= "-1001627911624"
ADMINS= "831859341"

# Bot Settings
RSS_ITEMS="https://nyaa.si/?page=rss&u=varyg1001"
SEND_SCHEDULE="False"

BRAND_UNAME="@zblivebot" # Username of Channel with @ or Text as Footer of Every Post
FFCODE_1080 = ffmpeg -i """{}""" -progress "{}" -c:v libx264 -crf 34 -c:s copy -pix_fmt yuv420p -s 1920x1080 -b:v 150k -c:a libopus -b:a 35k -preset ultrafast -metadata title='Team Warlords' -metadata author='Team @zblivebot' -metadata:s:s title='Team @zblivebot' -metadata:s:a title='Team @zblivebot' -metadata:s:v title='Team @zblivebot' '{}' -y
FFCODE_720 = ffmpeg -i """{}""" -progress "{}" -c:v libx264 -crf 32 -c:s copy -pix_fmt yuv420p -s 1280x720 -b:v 150k -c:a libopus -b:a 35k -preset ultrafast -metadata title='Team Warlords' -metadata author='Team @zblivebot' -metadata:s:s title='Team @zblivebot' -metadata:s:a title='Team @zblivebot' -metadata:s:v title='Team @zblivebot' '{}' -y
FFCODE_480 = ffmpeg -i """{}""" -progress "{}" -c:v libx264 -crf 34 -c:s copy -pix_fmt yuv420p -s 854x480 -b:v 150k -c:a libopus -b:a 35k -preset ultrafast -metadata title='Team Warlords' -metadata author='Team @zblivebot' -metadata:s:s title='Team @zblivebot' -metadata:s:a title='Team @zblivebot' -metadata:s:v title='Team @zblivebot' '{}' -y
FFCODE_360 = ffmpeg -i """{}""" -progress "{}" -c:v libx264 -crf 36 -c:s copy -pix_fmt yuv420p -s 640x360 -b:v 150k -c:a libopus -b:a 35k -preset ultrafast -metadata title='Team Warlords' -metadata author='Team @zblivebot' -metadata:s:s title='Team @zblivebot' -metadata:s:a title='Team @zblivebot' -metadata:s:v title='Team @zblivebot' '{}' -y
QUALS="360 480 720 1080" # Qualities Separated by Space without 'p' ( Sequence Specific )

# Customisation
THUMB="https://telegra.ph/file/d6665dc98be1c27228f0c.jpg"
"
AUTO_DEL="True"
DEL_TIMER="1800"
START_PHOTO="https://telegra.ph/file/d6665dc98be1c27228f0c.jpg"
"
START_MSG="<b><blockquote><bold>𝙷𝚎𝚢</bold> {first_name}</blockquote></b>\n\n<b><blockquote><bold>𝙸 𝙰𝚖 𝙰𝚞𝚝𝚘 𝙰𝚗𝚒𝚖𝚎 𝙵𝚒𝚕𝚎 𝚂𝚑𝚊𝚛𝚒𝚗𝚐 𝙱𝚘𝚝 & 𝙰𝚞𝚝𝚘𝚖𝚊𝚝𝚒𝚌 𝙴𝚗𝚌𝚘𝚍𝚎 𝙱𝚘𝚝 𝙼𝚊𝚍𝚎 𝙱𝚢 『𝚈𝚊𝚎 𝙼𝚒𝚔𝚘』❋𝄗⃝🦋 ⌞𝚆𝚊𝚛𝚕𝚘𝚛𝚍𝚜⌝ ㊋⚡⚡</blockquote></bold></b>" # Available Fillings : first_name, last_name, mention, user_id 
START_BUTTONS="𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕|https://t.me/zballupdatws 𝚂𝚞𝚙𝚙𝚘𝚛𝚝|https://t.me/zblivebot"

# Update 
UPSTREAM_REPO=""
UPSTREAM_BRANCH="main"
