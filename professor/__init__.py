

import config
from professor.core.bot import YukkiBot
from professor.core.dir import dirr
from professor.core.git import git
from professor.core.userbot import Userbot
from professor.misc import dbb, heroku, sudo

from .logging import LOGGER

# Pyrogram Client

app = YukkiBot(
    "professor",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    sleep_threshold=240,
    max_concurrent_transmissions=5,
    workers=50,
)

userbot = Userbot()

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()


from .platforms import PlaTForms

Platform = PlaTForms()
HELPABLE = {}
