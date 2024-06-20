# PY-Sports Discord Bot


# Introduction

PY-Sports is an open-source Discord bot developed by DwrldDev, that provides real-time statistics and information for sports enthusiasts, specifically focusing on football (soccer). The bot fetches data from an external API and presents it in a user-friendly embedded format on Discord.

Inspired by the renowned sports network Sky Sports

# Features

Manchester United Statistics:

Display detailed statistics for Manchester United football club.

Real-Time Updates: 

Access up-to-date information from the external API.
Caching: 

Optimized data retrieval using local JSON caching for improved performance.

PY-Sports is fully open-source under the MIT License, allowing the community to contribute and customize the bot.


# New features for 2024
Implemented new functions so we can use commands with the team id. also removed some code. user can now call ```!premid``` to get the id's of every prem team then use the command below to view upcoming fixtures.

EXAMPLE:
```
!matches 33 - Manchester United
!matches 50 - Manchester City
```
please note that the ```!starting11``` command will work the same way to view starting 11 players with each time via id (20 minutes or so before match)

```
!starting11 33 - Manchester United
!starting11 50 - Manchester City
```

# How I Started PY-Sports

Originally, I developed PY-Sports as a private Discord bot for my personal server to keep track of Manchester United statistics. The bot's success and the positive feedback I received from friends and fellow server members motivated me to take it to the next level. I decided to make PY-Sports open-source to engage the wider community and enable sports enthusiasts to benefit from the bot's features.


# How to Use PY-Sports

Create a Discord Application:

Go to the Discord Developer Portal and create a new application.
Navigate to the "Bot" tab within your application and click "Add Bot" to create a bot for your application.
Copy the bot token, which will be used to authenticate your bot with Discord.
Invite PY-Sports to Your Server:

Generate an invite link for your bot by navigating to the "OAuth2" tab in the Discord Developer Portal.
Select the "bot" scope and any required permissions for your bot (e.g., "Read Messages" and "Send Messages").
Copy the generated invite link and paste it into your web browser. Follow the instructions to add the bot to your Discord server.
Obtain an API Key from api-football:

Visit the [api-football](https://rapidapi.com/api-sports/api/api-football) website and create an account if you haven't already.
After logging in, obtain an API key from the dashboard.
This API key will be required to fetch sports data from the api-football API.

# Set Up Your Environment File:

Create a new file named .env in the root directory of the PY-Sports project or you can use the one provided.
Inside the .env file, add the following lines:
makefile


```js
DISCORD_BOT_TOKEN=your_discord_bot_token_here
API_FOOTBALL_KEY=your_api_football_key_here
```


Replace your_discord_bot_token_here with your Discord bot token and your_api_football_key_here with your api-football API key.


Make sure you have Python installed on your system (Python 3.7 or later is recommended).
Install the required dependencies using pip install -r requirements.txt.
Run the bot using python bot.py or the start.bat.

The bot is now active on your Discord server.


# Why PY-Sports Uses JSON Files
PY-Sports utilizes JSON files as a simple yet effective caching mechanism for data fetched from the external API. Here are the reasons behind this choice.


Efficient Data Retrieval:

JSON is a lightweight and easily parseable data format. Storing the API response in JSON allows for efficient data retrieval and manipulation when constructing the embedded message for Discord.

Easy Management:

JSON files are human-readable and straightforward to manage. Developers can easily inspect the cached data and ensure its accuracy, as well as manually refresh the cache if needed.

# 2024 Team id's updated 06/20/2024
if you want to change the ids of premier league teams 
```
Team Name: Manchester United, Team ID: 33
Team Name: Newcastle, Team ID: 34
Team Name: Bournemouth, Team ID: 35
Team Name: Fulham, Team ID: 36
Team Name: Wolves, Team ID: 39
Team Name: Liverpool, Team ID: 40
Team Name: Southampton, Team ID: 41
Team Name: Arsenal, Team ID: 42
Team Name: Everton, Team ID: 45
Team Name: Leicester, Team ID: 46
Team Name: Tottenham, Team ID: 47
Team Name: West Ham, Team ID: 48
Team Name: Chelsea, Team ID: 49
Team Name: Manchester City, Team ID: 50
Team Name: Brighton, Team ID: 51
Team Name: Crystal Palace, Team ID: 52
Team Name: Brentford, Team ID: 55
Team Name: Ipswich, Team ID: 57
Team Name: Nottingham Forest, Team ID: 65
Team Name: Aston Villa, Team ID: 66
```


# Contributing

I welcome contributions from the community to enhance PY-Sports and make it one of the best sports bots on Discord. If you have ideas for new features, improvements, or bug fixes, please follow the contribution guidelines and feel free to submit pull requests.

# Feedback and Support

If you encounter any issues, have suggestions, or need assistance, please create an issue on GitHub. I value your feedback and will do my best to address any concerns.

# License

PY-Sports is licensed under the MIT License. Feel free to use, modify, and distribute the bot following the terms of the license.

# Preview


![ezgif-1-2186b8f46a](https://github.com/DwrldDev/PY-Sports/assets/116701630/302eb2b9-ff7b-4fc2-8513-f578c24741ea)

