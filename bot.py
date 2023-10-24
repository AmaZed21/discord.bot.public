from logging import ERROR, error
from types import MemberDescriptorType
from typing import ContextManager, Sized
import discord
import random
from discord import player
from discord import activity
from discord import message
from discord.ext.commands.core import check
from discord.ext.commands.errors import MissingRequiredArgument
import requests
import json
import time
from discord.utils import get
from discord.ext import commands
import asyncio
from googlesearch import search

TOKEN = ""
client = commands.Bot(command_prefix='i')
puns = ['Why did Adele cross the road? To say hello from the other side.','What kind of concert only costs 45 cents? A 50 Cent concert featuring Nickelback.','What did the grape say when it got crushed? Nothing, it just let out a little wine.','To the guy who invented zero, thanks for nothing.','Can February March? No, but April May.','I don’t trust stairs because they’re always up to something.','Why was Dumbo sad? He felt irrelephant.','A man sued an airline company after it lost his luggage. Sadly, he lost his case.',' I was wondering why the ball was getting bigger. Then it hit me.','Never trust an atom, they make up everything!','Long fairy tales have a tendency to dragon.','I made a pun about the wind but it blows.','Never discuss infinity with a mathematician, they can go on about it forever.','Getting the ability to fly would be so uplifting.','I wasn’t originally going to get a brain transplant, but then I changed my mind.','I hate how funerals are always at 9 a.m. I’m not really a mourning person.','What’s the difference between a poorly dressed man on a bicycle and a nicely dressed man on a tricycle? A tire.','The guy who invented the door knocker got a no-bell prize.','What do you call an alligator in a vest? An investigator.','I bought a boat because it was for sail.','How did the picture end up in jail? It was framed!','I just found out that I’m color blind. The news came completely out of the green!','Why are frogs so happy? They eat whatever bugs them.','My parents said I can’t drink coffee anymore. Or else they’ll ground me!','England doesn’t have a kidney bank, but it does have a Liverpool.','There was a kidnapping at school yesterday. Don’t worry, though – he woke up!','One lung said to another, we be-lung together!','I asked a Frenchman if he played video games. He said Wii.',' What’s America’s favorite soda? Mini soda.','What does a clock do when it’s hungry? It goes back for seconds.','Towels can’t tell jokes. They have a dry sense of humor.','Who is the penguin’s favorite Aunt? Aunt-Arctica!','Why didn’t the cat go to the vet? He was feline fine!','What did the sushi say to the bee? Wasabee!','Sure, I drink brake fluid. But I can stop anytime!','What washes up on tiny beaches? Microwaves.']
nouns = ("puppy", "car", "rabbit", "girl", "monkey")
verbs = ("runs", "hits", "jumps", "drives", "barfs") 
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
adj = ("Adorable", "Clueless", "Dirty", "Odd", "Stupid")
num = random.randrange(0,5)
sentence_old = (adj[num] + ' ' + nouns[num] + ' ' + verbs[num] + ' ' + adv[num])
sentence = str(sentence_old)
winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

def getquote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + '-' + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="iHelp"))
    print("We have logged in as {0.user}".format(client))

@client.command()
async def Message(ctx,member:discord.Member):
    await ctx.send('What do you want to say?')
    def check(m):
        return m.author.id == ctx.author.id
    
    message = await client.wait_for('message', check=check)
    await ctx.send(f'Message has been sent to {member}')

    await member.send(f'{ctx.author.mention} has a message for you:\n{message.content}')

@client.command()
async def Hello(ctx):
    await ctx.send("**Hello!:hand_splayed:**\nI'm iBot! Do iHelp to find out more!")

@client.command()
async def Inspire(ctx):
    quote = getquote()
    await ctx.send(quote)
    await asyncio.sleep(2)
    await ctx.send("Better get inspired kid!")

@client.command()
async def Joke(ctx):
    await ctx.send(random.choice(puns))
    await asyncio.sleep(2)
    await ctx.send('Damn funny!:laughing:')

@client.command()
async def Bye(ctx):
    await ctx.send('Not very nice of you !:rage:')
    await asyncio.sleep(2)

@client.command()
async def Play(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver
    global board
    if ctx.author == p1:
        await ctx.send(f'{p2.mention} do you want to play? Please answer with yes/no within 30 seconds.')
        def check(m):
            return m.author == p2
        try:
            message_old = await client.wait_for('message',check=check,timeout=30)
            message = str(message_old.content)
            message = message.lower()
        except asyncio.TimeoutError:
            await ctx.send(f':x:Sorry {p2.mention} did not reply in time!')
        if 'y' in message:
            await ctx.send(f'Game started, get ready {p1.mention} and {p2.mention}!:thumbsup:')
            if gameOver:
                
                board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                         ":white_large_square:", ":white_large_square:", ":white_large_square:",
                         ":white_large_square:", ":white_large_square:", ":white_large_square:"]
                turn = ""
                gameOver = False
                count = 0

                player1 = p1
                player2 = p2

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

            # determine who goes first
            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
            elif num == 2:
                turn = player2
                await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
            else:
                await ctx.send("A game is already in progress! Finish it before starting a new one.")
        elif 'n' in message:
            await ctx.send('Alright no game started!:thumbsup:')
            
    elif ctx.author == p2:
        await ctx.send(f'{p1.mention} do you want to play? Please answer with yes/no within 30 seconds.')
        def check(m):
            return m.author == p1
        try:
            message_old = await client.wait_for('message',check=check,timeout=30)
            message = str(message_old.content)
            message = message.lower()
        except asyncio.TimeoutError:
            await ctx.send(f':x:Sorry {p1.mention} did not reply in time!')
        if 'y' in message:
            await ctx.send(f"Game started, get ready {p1.mention} and {p2.mention}!:thumbsup:")
            if gameOver:
                board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                         ":white_large_square:", ":white_large_square:", ":white_large_square:",
                         ":white_large_square:", ":white_large_square:", ":white_large_square:"]
                turn = ""
                gameOver = False
                count = 0

                player1 = p1
                player2 = p2

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

            # determine who goes first
            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
            elif num == 2:
                turn = player2
                await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
            else:
                await ctx.send("A game is already in progress! Finish it before starting a new one.")
        elif 'n' in message:
            await ctx.send('Alright no game started!:thumbsup:')

@client.command()
async def Place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " **wins**!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("**It's a tie**!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the iPlay command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@Play.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please do 'iPlay [user] [user]'.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@user>).")

@Place.error
async def Place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

@Message.error
async def Message_error(ctx,error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please include a user by pinging them after the iMessage!')

@client.command()
async def Phone(ctx):
    num = random.randint(1, 2)
    if num == 1:
        await ctx.send("**You can afford an iphone!**:money_mouth:")
    elif num == 2:
        await ctx.send("**Imagine being poor!** You are too poor and can't afford an iphone:cry:")
    
@client.command()
async def Addrole(ctx, role: discord.Role, user: discord.Member):
        if role in user.roles:
            await ctx.send(f":x:{user.mention} already has {role.mention}!")
        elif role not in user.roles:
            if ctx.author.guild_permissions.manage_roles:
                await user.add_roles(role)
                await ctx.send(f"Successfully given {role.mention} to {user.mention}!:thumbsup:")
            elif ctx.author.guild_permissions.manage_roles == False:
                await ctx.send(":x:You are not an administrator!")

@client.command()
async def Removerole(ctx, role: discord.Role, user: discord.Member):
    if role in user.roles:    
        if ctx.author.guild_permissions.manage_roles == True:
            await user.remove_roles(role)
            await ctx.send(f"Successfully removed {role.mention} from {user.mention}!:thumbsup:")
        elif ctx.author.guild_permissions.manage_roles == False:
            await ctx.send(":x:You are not an administrator!")
    if role not in user.roles:
        await ctx.send(f":x:{user.mention} does not have {role.mention}!")

@Addrole.error
async def Addrole_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please do 'iAddrole [role] [user]'")

@Removerole.error
async def Removerole_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please do 'iRemoverole [role] [user]'")

@client.command()
async def Suggest(ctx):
    member = await client.fetch_user("832597324290195466")
    await ctx.send('What do you want to say?')
    def check(m):
        return m.author.id == ctx.author.id
    message = await client.wait_for('message', check=check, timeout=30)
    await ctx.send('Thank you for your suggestion!')
    await member.send(f' Suggestion: \n{message.content}')
    print(message.content)

@client.command()
async def Flip(ctx):
    numb = random.randint(1, 2)
    message = await ctx.send("`Flipping...`")
    await asyncio.sleep(2)
    if numb == 1:
        await message.edit(content = "**Tails!**")
    elif numb == 2:
        await message.edit(content = "**Heads!**")

@client.command()
async def Help(ctx):
    embed = discord.Embed(title="Commands:", description="Commands for you to use!", color=discord.Color.random())
    embed.add_field(name= "**iInspire**", value="Gives an inspirational quote!", inline=False)
    embed.add_field(name="**iPlay**",value="Play tictactoe with another player!", inline=False)
    embed.add_field(name= "**iBye**", value="Says bye?", inline=False)
    embed.add_field(name= "**iSuggest**", value="Give suggestions to improve the bot!", inline=False)
    embed.add_field(name= "**iJoke**", value="Tells a joke!", inline=False)
    embed.add_field(name= "**iAddrole**", value="Adds a role to a user!(ONLY ADMIN)", inline=False)
    embed.add_field(name= "**iRemoverole**", value="Removes a role from a user!(ONLY ADMIN)", inline=False)
    embed.add_field(name= "**iMessage**", value="Messages a user for you!", inline=False)
    embed.add_field(name= "**iFlip**", value="Flips a coin!", inline=False)
    embed.add_field(name="**iProfile**", value="Shows the profile of a user!", inline=False)
    embed.add_field(name="**iKick**", value="Kicks a user!(ONLY ADMIN)", inline=False)
    embed.add_field(name="**iMute**", value="Mutes a user!(ONLY ADMIN)", inline=False)
    embed.add_field(name= "**iCreaterole**", value="Creates a role!(ONLY ADMIN)", inline=False)
    embed.add_field(name="**iUnmute**", value="Unmutes a user!(ONLY ADMIN)", inline=False)
    embed.add_field(name="**iSearch**", value="Searches the internet for the best result!", inline=False)
    embed.add_field(name="**iBan**", value="Bans selected memeber!", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Search(ctx, *args):
    query = str(args)

    for i in search(query, tld="co.in", num=1, stop=1, pause=1):
        await ctx.send(f"The best result for your search is: \n {i}")
    
@client.command()
async def Profile(ctx, user:discord.Member):
    mention = []
    pfp = user.avatar_url
    for role in user.roles:
        if role.name != "@everyone":
            mention.append(role.mention)

    roles = ", ".join(mention)

    embed = discord.Embed(title=f"Profile:", description=user.mention, color=discord.Color.random())
    embed.set_thumbnail(url=pfp)
    embed.add_field(name="Top role:", value=user.top_role.mention, inline=False)
    embed.add_field(name="Roles:", value=roles, inline=False)

    await ctx.send(embed=embed)

@Profile.error
async def Profile_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please include a user to see their profile!")

@client.command()
async def Kick(ctx, member:discord.Member):
    if ctx.author.guild_permissions.kick_members == False:
        await ctx.send(":x:You are not an administrator!")
    elif ctx.author.guild_permissions.kick_members == True:
        await member.kick()
        await ctx.send(f"{member} has been kicked!:thumbsup:")
        await member.send(f"You have been kicked from {ctx.message.guild.name}")

@Kick.error
async def Kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please include a user to kick!")

@client.command()
async def Createrole(ctx, *,name):
    if ctx.author.guild_permissions.manage_roles == True:
        guild = ctx.guild
        await guild.create_role(name=name)
        await ctx.send(f'Role {name} has been created')
    elif ctx.author.guild_permissions.manage_roles == False:
        await ctx.send(':x:You are not an administrator!')

@client.command()
async def Mute(ctx, member:discord.Member):
    if ctx.author.guild_permissions.kick_members or ctx.author.guild_permissions.ban_members == True:
        role = discord.utils.get(ctx.guild.roles, name = "Muted")
        guild = ctx.guild
        if role not in guild.roles:
            perms = discord.Permissions(send_messages=False, speak=False)
            await guild.create_role(name="Muted",permissions=perms)
            await member.add_roles(role)
            await ctx.send(f"{member.mention} has been muted!:thumbsup:")
        elif role in guild.roles:
            if role in member.roles:
                await ctx.send(f":x:{member.mention} has already been muted!")
            elif role not in member.roles:
                await member.add_roles(role)
                await ctx.send(f'{member.mention} has been muted!:thumbsup:')
    elif ctx.author.guild_permissions.kick_members or ctx.author.guild_permissions.ban_members == False:
        await ctx.send(':x:You are not an administrator!')
    
@Mute.error
async def Mute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x:Please include a user to mute!")

@client.command()
async def Unmute(ctx, member:discord.Member):
    if ctx.author.guild_permissions.kick_members or ctx.author.guild_permissions.ban_members == True:
        role = get(ctx.guild.roles, name = "Muted")
        if role not in member.roles:
            await ctx.send(f":x:{member.mention} has not been muted!")
        elif role in member.roles:
            await member.remove_roles(role)
            await ctx.send(f'{member.mention} has been unmuted!:thumbsup:')
    elif ctx.author.guild_permissions.kick_members or ctx.author.guild_permissions.ban_members == False:
        await ctx.send(':x:You are not an administrator!')

@Unmute.error
async def Unmute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x:Please include a user to unmute!")

@client.command()
async def Colour(ctx, role:discord.Role, colour:discord.Colour):
    server = ctx.guild
    if ctx.author.guild_permissions.manage_roles == True:
        await role.edit(colour=colour)
        await ctx.send(f"{role.mention} has a new colour, {colour}!:thumbsup:")
    elif ctx.author.guild_permissions.manage_roles == False:
        await ctx.send(':x:You are not an administrator!')
@Colour.error
async def Colour_error(ctx, error):
    if isinstance(error, commands.BadColourArgument):
        await ctx.send("Sorry the colour does not exist!")
@client.command()
async def Deleterole(ctx, role:discord.Role):
    if ctx.author.guild_permissions.manage_roles == True:
        await role.delete()
        await ctx.send(f"{role} has been deleted!:thumbsup:")
        if role not in ctx.guild.server:
            await ctx.send(":x:You cannot delete a role that does not exist!")
    elif ctx.author.guild_permissions.manage_roles == False:
        await ctx.send(":x:You are not an administraor!")

@Deleterole.error
async def Deleterole_missing(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x:Please include a role to delete!")
    if isinstance(error, commands.RoleNotFound):
        await ctx.send(":x:You cannot delete a role that does not exist!")
@client.command()
async def Ban(ctx, member:discord.Member):
    if ctx.author.guild_permissions.ban_members == False:
        await ctx.send(":x:You are not an administrator!")
    elif ctx.author.guild_permissions.ban_members == True:
        await ctx.send('Are you sure? Please reply with yes or no.')
        def check(m):
            return m.author.id == ctx.author.id
        try:
            message_old = await client.wait_for('message',check=check,timeout=30)
            message = str(message_old.content)
            message = message.lower()
        except asyncio.TimeoutError:
            await ctx.send('Due to the time out, no actions have been done.')
        if 'y' in message:
            await member.ban()
            await ctx.send(f"{member} has been banned!:thumbsup:")
            await member.send(f"You have been banned from {ctx.message.guild.name}")
        elif 'n' in message:
            await ctx.send(f"{member} has not been banned as action was cancelled!:x:")
client.run(TOKEN)
