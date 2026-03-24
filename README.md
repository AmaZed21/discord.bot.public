# Discord Bot (Scyther)

iBot is a multifunctional Discord bot built with Python and `discord.py`. It includes entertainment commands, moderation tools, direct messaging utilities, Google search support, role management, inspirational quotes, and an interactive Tic-Tac-Toe game between server members.

## Features

- Inspirational quote command
- Joke and pun generator
- Private messaging command
- Google search command
- Coin flip command
- Random phone affordability joke command
- Tic-Tac-Toe game for two users
- User profile display
- Suggestion submission command
- Moderation commands such as kick, mute, unmute, ban
- Role management commands such as add role, remove role, create role, delete role, and change role colour
- Custom help menu using embeds


## Technologies Used

- Python
- discord.py
- requests
- googlesearch-python
- asyncio
- json


## Installation

1. Clone or download the project.
2. Create and activate a virtual environment if desired.
3. Install the required packages:

```bash
pip install -r requirements.txt
```


## Running the Bot

Run the script using:

```bash
python main.py
```

Make sure the bot has been invited to your Discord server before running it.


## Command Prefix

The bot uses the following prefix for all commands:

```text
i
```

Example:
- `iHello`
- `iJoke`
- `iPlay @user1 @user2`


## Commands

### General Commands

- `iHello` — Greets the user
- `iInspire` — Sends an inspirational quote
- `iJoke` — Sends a random pun or joke
- `iBye` — Sends a farewell response
- `iFlip` — Flips a coin
- `iPhone` — Randomly decides whether you can afford an iPhone
- `iHelp` — Displays the full command list
- `iSearch <query>` — Searches the internet and returns the top result
- `igoogle <query>` — Returns the top 3 Google search results

### Messaging Commands

- `iMessage @user` — Sends a direct message to another user
- `iSuggest` — Sends your suggestion privately to the bot owner

### Game Commands

- `iPlay @user1 @user2` — Starts a Tic-Tac-Toe game
- `iPlace <position>` — Places your mark on the board in positions 1 to 9

### Profile Commands

- `iProfile @user` — Displays a user's profile and roles

### Moderation Commands

- `iKick @user` — Kicks a user from the server
- `iBan @user` — Bans a user from the server after confirmation
- `iMute @user` — Mutes a user
- `iUnmute @user` — Unmutes a user

### Role Management Commands

- `iAddrole @role @user` — Adds a role to a user
- `iRemoverole @role @user` — Removes a role from a user
- `iCreaterole <name>` — Creates a new role
- `iDeleterole @role` — Deletes a role
- `iColour @role <colour>` — Changes a role's colour


## Example Usage

```text
iHello
iJoke
iInspire
iPlay @User1 @User2
iPlace 5
iMessage @User
iAddrole @Member @User
iBan @User
iSearch python discord bot tutorial
```


## Notes

- Administrative commands require the appropriate Discord server permissions.
- The bot must be invited with sufficient permissions to manage roles, mute users, kick users, and ban users.
- The suggestion command sends feedback to a specific user ID configured in the code.
- The quote command uses the ZenQuotes API.
- Search commands depend on internet access.

---

## Author
Built as a Python Discord bot project with moderation, utility, entertainment, and game features.
