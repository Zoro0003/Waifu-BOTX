import logging
from pyrogram import Client
from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger("name")

OWNER_ID = "6138142369"
sudo_users = ["6138142369", "6143079414"]
GROUP_ID = "-1002083898719"
TOKEN = "7287151907:AAGg_ub-omJkMG7k5jb6wGhLIOQPGHjw-V4"
mongo_url = "mongodb+srv://Srikanta:srikanta@cluster0.xzbil3m.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL = ["https://graph.org/file/cafd84de9c790da6ce770.jpg", "https://graph.org/file/407a498548a0f4c6881b3.jpg"]
SUPPORT_CHAT = "https://t.me/Midexoz"
UPDATE_CHAT = "https://t.me/MidexozBotUpdates"
BOT_USERNAME = "@Snatch_Your_Waifu_Robot"
CHARA_CHANNEL_ID = ""
api_id = "20457610"
api_hash = "b7de0dfecd19375d3f84dbedaeb92537"

application = Application.builder().token(TOKEN).build()
Grabberu = Client("Grabber", api_id, api_hash, bot_token=TOKEN)
client = AsyncIOMotorClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters']
user_totals_collection = db['user_totals']
user_collection = db["user_collection"]
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']
