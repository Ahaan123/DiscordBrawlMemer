import praw
import discord
from discord.ext import commands
import random
import os
from WebServer import keep_alive
brawl_bot = commands.Bot(command_prefix='brawl ')
TOKEN = "TOKEN IS HIDDEN"
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

client_id = 'Hidden'
client_secret = 'Hidden'
user_agent = 'Hidden'
username = 'Hidden'
password = 'Hidden'
reddit = praw.Reddit(client_id = client_id, client_secret=client_secret, user_agent=user_agent, username=username, password=password)
subred = reddit.subreddit('brawlstars')
brawl_bot.remove_command('help')
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
    embed = discord.Embed(
      colour=0xf1c40f,
      title = "**BrawlMemer | Info**"
    )
    embed.add_field(name="**BrawlMemer | Version**", value="v1.1", inline=False)
    embed.add_field(name="**BrawlMemer | Developer**", value="Ahaan Pandya", inline=False)
    embed.add_field(name="**Disclaimer**", value="This material is unofficial and is not endorsed by Supercell. For more information see Supercell's Fan Content Policy: www.supercell.com/fan-content-policy.")
    await ctx.send(embed=embed)

@brawl_bot.command()
async def help(ctx):
  auth = ctx.message.author
  embed = discord.Embed(
    title='**COMMANDS HELP**',
    colour = 0xf1c40f
  )
  embed.add_field(name=":laughing:`brawl meme`", value="Displays a Brawl Stars meme (image)")
  embed.add_field(name=":video_camera:`brawl videomeme`", value="Displays a Brawl Stars meme (video)")
  embed.add_field(name=":information_source:`brawl info`", value="Shows you information about the Bot")
  embed.add_field(name=":question:`brawl help`", value="Gives Command Help")
  embed.add_thumbnail(url='https://upload.wikimedia.org/wikipedia/en/thumb/1/18/Brawl_Stars_logo.png/220px-Brawl_Stars_logo.png')
  new_embed = discord.Embed(
    colour = 0xf1c40f,
    description = "**A DM containing the help message has been sent to you!**"
  )
  await ctx.send(embed=new_embed)
  await auth.send(embed=embed)
keep_alive()
brawl_bot.run(TOKEN)
