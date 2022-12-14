# Creator Or Dev @HYPER_AD13 | @SHINING_OFF <Found On telegram>
# Found on github < https://github.com/ItsmeHyper13 >

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", "11792103"))
API_HASH = getenv("API_HASH", "5a03ee0c82de3e8972dd46a66e039b01")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "2144094143:AAGKN04VmQ2hkXV_DDMJunjIDEFEOp704hA")
# Database to save your chats and stats... Get MongoDB:-  https://telegra.ph/How-To-get-Mongodb-URI-04-06
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Arunkumar:arunhald@cluster0.n5oxsxc.mongodb.net/?retryWrites=true&w=majority")

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.
DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "10080")
)  # Remember to give value in Minutes

# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)  # Remember to give value in Minutes

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001670420638"))

# A name for your Music bot.
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Tessa")

# Your User ID.
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "868753606").split())
)  # Input type must be interger

# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/HYPER-AD13/DevuMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "sree")

# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Only  Links formats are  accepted for this Var value.
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", None
)  # Example:- https://t.me/SILENT_BOTS
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", None
)  # Example:- https://t.me/SilentVerse

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "540000000000")
)  # Remember to give value in Seconds

# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400000000000")
)  # Remember to give value in Seconds

# Set it True if you want to delete downloads after the music playout ends from your downloads folder
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorise command then only your bot will play music in that chat.]
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

# Your Github Repo.. Will be shown on /start Command
GITHUB_REPO = getenv("GITHUB_REPO", None)

# Spotify Client.. Get it from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "99999")
)  # Remember to give value in Seconds


# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(
    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")
)  # Remember to give value in bytes

TG_VIDEO_FILESIZE_LIMIT = int(
    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")
)  # Remember to give value in bytes

# Chceckout https://www.gbmb.org/mb-to-bytes  for converting mb to bytes


# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot @YukkiStringBot
STRING1 = getenv("STRING_SESSION", "BQBz0XIJBw7ICw23dvZwjLqRvSaqL5fJn2nCLMpyfNU0gs_4DFR_B7WOZPEvpbCF7IQy5bn4DeTOPRSgijqVnTEqcRCWDY3crKR-N7riAisx4rLNnbrTzZ63IH59hSBx_Pf6F88Wa_7V-YM-LSVyF2Oyr0n4jp-maWLeXmKyi8bdzGtJDfTuimZMX2R-_EZb5iaWdpXiyPzcXKr_Iz3ftJbtXLEyWV-IMbo3omhK0Nagl19_m12rtTJRAV3wfLnEST-VbvbgtakddT34DbexUDdG__WyvPVqjK6h-EwM-xjcO5pnatgCarW1kk_6U23sGhTNi0AtK5sIT6Reb3ozNPfvAAAAAS2xfIAA")
STRING2 = getenv("STRING_SESSION2","BQCSZHARRaAwcbK0oAb_mwr_BTybySZrNV1UD45LP3Rh8DWr-lnjSxBq1usf64GOnGqkn0HlwkBvP5V2atItHq1awqxami5TCTHFafkUm_T7c5YNyTR71avTecISRYSBnqwtn_jPZqJykC302DEpKEHD3BvorMXol7CDIVzir6hUoKuNmqVJhULHCx4noBR5CpCwu3PRCrl9pKSTEg2dxN5XVHnBUJzgjBlakr8TEdNw_FVIzmVY-tQEeL9FJcRP_80o2pB-sVLUrFZhOtTmF3fjG2idiy3_TfGG4CbfQrUQr_R0DBQrLVSRFOlig40YgAVrGQuc9ZoPwggd3HZ3TD13U1QFhQA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


'''
██████╗░███████╗██╗░░░██╗██╗░░░██╗
██╔══██╗██╔════╝██║░░░██║██║░░░██║
██║░░██║█████╗░░╚██╗░██╔╝██║░░░██║
██║░░██║██╔══╝░░░╚████╔╝░██║░░░██║
██████╔╝███████╗░░╚██╔╝░░╚██████╔╝
╚═════╝░╚══════╝░░░╚═╝░░░░╚═════╝░
'''

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "Yukkilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


# Images
START_IMG_URL = getenv("START_IMG_URL", None)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/ac9b523a50a77f6b7e555.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://telegra.ph/file/134cfcb9a758ce0fc77a3.jpg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "assets/Global.jpeg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "assets/Stats.jpeg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "assets/Audio.jpeg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "assets/Video.jpeg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "assets/Stream.jpeg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "assets/Soundcloud.jpeg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "assets/Youtube.jpeg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "assets/SpotifyArtist.jpeg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "assets/SpotifyAlbum.jpeg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "assets/SpotifyPlaylist.jpeg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    print(
        "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if SUPPORT_GROUP and not re.match("(?:http|https)://", SUPPORT_GROUP):
    print(
        "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if UPSTREAM_REPO and not re.match("(?:http|https)://", UPSTREAM_REPO):
    print(
        "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if GITHUB_REPO and not re.match("(?:http|https)://", GITHUB_REPO):
    print(
        "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    PING_IMG_URL
    and PING_IMG_URL != "assets/Ping.jpeg"
    and not re.match("(?:http|https)://", PING_IMG_URL)
):
    print(
        "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if (
    PLAYLIST_IMG_URL
    and PLAYLIST_IMG_URL != "assets/Playlist.jpeg"
    and not re.match("(?:http|https)://", PLAYLIST_IMG_URL)
):
    print(
        "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if (
    GLOBAL_IMG_URL
    and GLOBAL_IMG_URL != "assets/Global.jpeg"
    and not re.match("(?:http|https)://", GLOBAL_IMG_URL)
):
    print(
        "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    STATS_IMG_URL
    and STATS_IMG_URL != "assets/Stats.jpeg"
    and not re.match("(?:http|https)://", STATS_IMG_URL)
):
    print(
        "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    TELEGRAM_AUDIO_URL
    and TELEGRAM_AUDIO_URL != "assets/Audio.jpeg"
    and not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL)
):
    print(
        "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    STREAM_IMG_URL
    and STREAM_IMG_URL != "assets/Stream.jpeg"
    and not re.match("(?:http|https)://", STREAM_IMG_URL)
):
    print(
        "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    SOUNCLOUD_IMG_URL
    and SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg"
    and not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL)
):
    print(
        "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if (
    YOUTUBE_IMG_URL
    and YOUTUBE_IMG_URL != "assets/Youtube.jpeg"
    and not re.match("(?:http|https)://", YOUTUBE_IMG_URL)
):
    print(
        "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    TELEGRAM_VIDEO_URL
    and TELEGRAM_VIDEO_URL != "assets/Video.jpeg"
    and not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL)
):
    print(
        "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if not MUSIC_BOT_NAME:
    print(
        "[ERROR] - You've defined MUSIC_BOT_NAME wrong. Please don't use any special characters or Special font for this... Keep it simple and small."
    )
    sys.exit()
