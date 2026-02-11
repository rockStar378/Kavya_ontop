import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ───── BASIC ─────
API_ID = int(os.getenv("API_ID", "29448785"))
API_HASH = os.getenv("API_HASH", "599574f6aff0a09ebb76305b58e7e9c2")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7252371475:AAHY_t2H8p2UwoBBfwFYnVLbsOzrVELeE1s")

OWNER_ID = int(os.getenv("OWNER_ID", "8417510906"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "vip_ankit_121")

BOT_USERNAME = os.getenv("BOT_USERNAME", "Hema")
BOT_NAME = os.getenv("BOT_NAME", "˹kavya˼ ♪ [ ᴛᴘʙ ]™")
ASSUSERNAME = os.getenv("ASSUSERNAME", "ALPHA")

# ───── DATABASE ─────
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

# ───── LIMITS ─────
DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", "17000"))

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ───── LOG GROUP ─────
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1002389305159"))

# ───── HEROKU ─────
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "")

# ───── UPDATE (DISABLED – SAFE) ─────
UPSTREAM_REPO = ""
UPSTREAM_BRANCH = ""
GIT_TOKEN = ""

# ───── API / LINKS ─────
API_KEY = os.getenv("API_KEY", "StrangerApia3075f5")
API_BASE_URL = os.getenv("API_BASE_URL", "http://riyabots.site")

PRIVACY_LINK = os.getenv(
    "PRIVACY_LINK",
    "https://telegra.ph/Privacy-Policy-for-YukkiMusic-08-30"
)

SUPPORT_CHANNEL = os.getenv(
    "SUPPORT_CHANNEL", "https://t.me/+gVWf5Y_c5NA5MGY1"
)
SUPPORT_CHAT = os.getenv(
    "SUPPORT_CHAT", "https://t.me/+gVWf5Y_c5NA5MGY1"
)

# ───── ASSISTANT ─────
AUTO_LEAVING_ASSISTANT = (
    os.getenv("AUTO_LEAVING_ASSISTANT", "False").lower() == "true"
)
AUTO_LEAVE_ASSISTANT_TIME = int(os.getenv("ASSISTANT_LEAVE_TIME", "9000"))

# ───── DOWNLOAD LIMITS ─────
SONG_DOWNLOAD_DURATION = int(os.getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    os.getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999")
)

# ───── SPOTIFY ─────
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", "25"))

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# ───── STRING SESSIONS ─────
STRING1 = os.getenv("STRING_SESSION", "")
STRING2 = os.getenv("STRING_SESSION2", "")
STRING3 = os.getenv("STRING_SESSION3", "")
STRING4 = os.getenv("STRING_SESSION4", "")
STRING5 = os.getenv("STRING_SESSION5", "")
STRING6 = os.getenv("STRING_SESSION6", "")
STRING7 = os.getenv("STRING_SESSION7", "")

# ───── MISC ─────
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ───── IMAGES ─────
START_IMG_URL = os.getenv(
    "START_IMG_URL", "https://litter.catbox.moe/y1np46.jpg"
)
PING_IMG_URL = START_IMG_URL
PLAYLIST_IMG_URL = "https://files.catbox.moe/f2s4ws.jpg"
STATS_IMG_URL = "https://files.catbox.moe/z0gh23.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2y5o3g.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2y5o3g.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
SOUNCLOUD_IMG_URL = STREAM_IMG_URL
YOUTUBE_IMG_URL = TELEGRAM_AUDIO_URL
SPOTIFY_ARTIST_IMG_URL = TELEGRAM_AUDIO_URL
SPOTIFY_ALBUM_IMG_URL = TELEGRAM_AUDIO_URL
SPOTIFY_PLAYLIST_IMG_URL = STREAM_IMG_URL

# ───── URL VALIDATION ─────
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit(
        "[ERROR] SUPPORT_CHANNEL must start with https://"
    )

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit(
        "[ERROR] SUPPORT_CHAT must start with https://"
    )
