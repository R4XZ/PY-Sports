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


# New features for 2023

Will there be more teams Implemented into PY-Sports? The answer is YES!!

- [x] updated for the 23/24 season
- [x] Implemented LiverpoolFC
- [x] Implemented ManchesterCity
- [x] Implemented FA Cup
- [x] Implemented UEFA Europa

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




# Contributing

I welcome contributions from the community to enhance PY-Sports and make it one of the best sports bots on Discord. If you have ideas for new features, improvements, or bug fixes, please follow the contribution guidelines and feel free to submit pull requests.

# Feedback and Support

If you encounter any issues, have suggestions, or need assistance, please create an issue on GitHub. I value your feedback and will do my best to address any concerns.

# License

PY-Sports is licensed under the MIT License. Feel free to use, modify, and distribute the bot following the terms of the license.

# Screenshots

![manUtdUpcoming](https://github.com/DwrldDev/PY-Sports/assets/116701630/5bb66557-b3e1-4b9b-b12f-4bd2ce417a4a)


# Predictions

![prediction](https://github.com/DwrldDev/PY-Sports/assets/116701630/24f8f5a7-3b07-4006-8abe-1619c4fa3bc6)



# Live Results

![liveresult](https://github.com/DwrldDev/PY-Sports/assets/116701630/0a600fb4-2cc0-4a5b-9b67-d5ec9887dafc)



# Next 10 upcoming matches

![upcoming](https://github.com/DwrldDev/PY-Sports/assets/116701630/97072ce0-91bd-45ab-87f9-247d223637fb)



