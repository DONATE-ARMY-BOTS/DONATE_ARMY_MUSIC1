
from DONATE_ARMY_MUSIC.core.bot import YukkiBot
from DONATE_ARMY_MUSIC.core.dir import dirr
from DONATE_ARMY_MUSIC.core.git import git
from DONATE_ARMY_MUSIC.core.userbot import Userbot
from DONATE_ARMY_MUSIC.misc import dbb, heroku, sudo
from .logging import LOGGER

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
# Bot Client
app = YukkiBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}
