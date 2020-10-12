import praw
import discord
from discord.ext import commands
import random
import os
from WebServer import keep_alive
brawl_bot = commands.Bot(command_prefix='brawl ')
TOKEN = os.environ.get('DISCORD_BRAWL_TOKEN')
class meme_post:
  url = ''
  title = ''
  meme_link = ''
  permalink = ''
  def __init__(self, post_url, post_title, meme_urlx, p):
    self.url = post_url
    self.title = post_title
    self.meme_link = meme_urlx
    self.permalink = p
@brawl_bot.event
async def on_ready():
    print('Brawl Memer bot be ready though')

client_id = '-a3rFPB9I37hbw'
client_secret = 'ghA0sWj50nO50FQe4z5hMvFYwFY'
user_agent = 'BrawlMemer'
username = 'BearNo21'
password = 'Prince#2.0'
reddit = praw.Reddit(client_id = client_id, client_secret=client_secret, user_agent=user_agent, username=username, password=password)
subred = reddit.subreddit('brawlstars')

@brawl_bot.command()
async def meme(ctx):
    posts = get_memes()
    post = random.choice(posts)
    print(post.permalink)
    embed = discord.Embed(
      title=post.title,
      colour = discord.Colour.blue(),
      url = 'https://www.reddit.com'+str(post.permalink)
    )
    embed.set_footer(text='Thanks to r/brawlstars for the memes!')
    embed.set_image(url=post.meme_link)
    await ctx.send(embed=embed)

@brawl_bot.command()
async def videomeme(ctx):
    meme_link_list = get_video_memes()
    random_meme_link = random.choice(meme_link_list)
    await ctx.send(random_meme_link)

def get_memes():
    posts = []
    for post in subred.search('flair:"Humor"', limit=50):
        #length-4 to length-1
        meme_url = str(post.url)
        extension = meme_url[len(meme_url)-4:len(meme_url)]
        if (extension == '.jpg' or extension == '.png'):
            post = meme_post(post_url=post.url, post_title = post.title, meme_urlx=meme_url, p=post.permalink)
            posts.append(post)

    return posts

def get_video_memes():
    video_meme_list = []
    for post in subred.search('flair:"Humor"', limit=200):
        #length-4 to length-1
        meme_url = str(post.url)
        extension = meme_url[len(meme_url)-4:len(meme_url)]
        if (extension != '.jpg' and extension != '.png'):
            video_meme_list.append(meme_url)

    return video_meme_list

@brawl_bot.command()
async def info(ctx):
    await ctx.send("Hi there! I am a brawl Memer by Ahaan and I can show you a meme if you type brawl meme. Thanks!")

keep_alive()
brawl_bot.run(TOKEN)
