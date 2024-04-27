from insta_bot import InstaBot
from time import sleep
USERNAME='instagram_username'
PASSWORD='instagram_password'

bot=InstaBot()
bot.connect_to_instagram(USERNAME,PASSWORD)
bot.find_follower('caf_online')  # enter the name of the account you wish to follow
bot.follow()