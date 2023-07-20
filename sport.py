import http.client
import json
import discord
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands,tasks
import os
import requests
import random


#Cool art that displays 

dragon = """

                        /\.
                        ||
                        ||
                        ||
                        ||                                               ~-----~
                        ||                                            /===--  ---~~~
                        ||                   ;'                 /==~- --   -    ---~~~
                        ||                (/ ('              /=----         ~~_  --(  '
                        ||             ' / ;'             /=----               \__~
     '                ~==_=~          '('             ~-~~      ~~~~        ~~~--\~'
     \\                (c_\_        .i.             /~--    ~~~--   -~     (     '
      `\               (}| /       / : \           / ~~------~     ~~\   (
      \ '               ||/ \      |===|          /~/             ~~~ \ \(
      ``~\              ~~\  )~.~_ >._.< _~-~     |`_          ~~-~     )\.
       '-~                 {  /  ) \___/ (   \   |` ` _       ~~         '
       \ -~\                -<__/  -   -  L~ -;   \\    \ _ _/
       `` ~~=\                  {    :    }\ ,\    ||   _ :(
        \  ~~=\__                \ _/ \_ /  )  } _//   ( `|'
        ``    , ~\--~=\           \     /  / _/ / '    (   '
         \`    } ~ ~~ -~=\   _~_  / \ / \ )^ ( // :_  / '
         |    ,          _~-'   '~~__-_  / - |/     \ (
          \  ,_--_     _/              \_'---', -~ .   \.
           )/      /\ / /\   ,~,         \__ _}     \_  "~_
           ,      { ( _ )'} ~ - \_    ~\  (-:-)       "\   ~ 
                  /'' ''  )~ \~_ ~\   )->  \ :|    _,       " 
                 (\  _/)''} | \~_ ~  /~(   | :)   /          }
                <``  >;,,/  )= \~__ {{{ '  \ =(  ,   ,       ;
               {o_o }_/     |v  '~__  _    )-v|  "  :       ,"
               {/"\_)       {_/'  \~__ ~\_ \\_} '  {        /~\.
               ,/!          '_/    '~__ _-~ \_' :  '      ,"  ~ 
              (''`                  /,'~___~    | /     ,"  \ ~' 
             '/, )                 (-)  '~____~";     ,"     , }
           /,')                    / \         /  ,~-"       '~'
       (  ''/                     / ( '       /  /          '~'
    ~ ~  ,, /) ,                 (/( \)      ( -)          /~'
  (  ~~ )`  ~}                   '  \)'     _/ /           ~'
 { |) /`,--.(  }'                    '     (  /          /~'
(` ~ ( c|~~| `}   )                        '/:\         ,'
 ~ )/``) )) '|),                          (/ | \)                
  (` (-~(( `~`'  )                        ' (/ '
   `~'    )'`')                              '
     ` ``

"""
print(dragon)




load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
Key = os.getenv("API_KEY")

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)





@bot.command(name='manutd_live', help='Displays the latest Manchester United result')
async def get_score_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    # Set the headers
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key,
        'Content-Type': 'application/json'
    }

    # Get the latest fixture for Manchester United
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=33&last=1", headers=headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode('utf-8'))
    fixture = data['response'][0]

    # Send the result to the Discord channel
    home_team = fixture['teams']['home']['name']
    away_team = fixture['teams']['away']['name']
    home_score = fixture['goals']['home']
    away_score = fixture['goals']['away']
    result_message = f"{home_team} {home_score} - {away_score} {away_team}\n"
    em11 = discord.Embed(title="Live result for Manchester Utd:\n", description=f"{result_message} ⚽", color=ctx.author.color)
    await ctx.send(embed=em11)


#mancity_live command Displays the latest Manchester City result if they are live, if not live it will give you the previous match result
# this apply's for the other teams with the same command for example lfc_live 

@bot.command(name='mancity_live', help='Displays the latest Manchester City result')
async def get_score_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    # Set the headers
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key,
        'Content-Type': 'application/json'
    }

    # Get the latest fixture for Manchester City
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=50&last=1", headers=headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode('utf-8'))
    fixture = data['response'][0]

    # Send the result to the Discord channel
    home_team = fixture['teams']['home']['name']
    away_team = fixture['teams']['away']['name']
    home_score = fixture['goals']['home']
    away_score = fixture['goals']['away']
    result_message = f"{home_team} {home_score} - {away_score} {away_team}\n"
    em11 = discord.Embed(title="Live result for Manchester City:\n", description=f"{result_message} ⚽", color=ctx.author.color)
    await ctx.send(embed=em11)


# with this live command it will display the live score when the team is playing (LIVE), if the team is NOT playing it will send the last games result into the discord

@bot.command(name='lfc_live', help='Displays the latest Liverpool FC result')
async def get_score_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    # Set the headers
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key,
        'Content-Type': 'application/json'
    }

    # Get the latest fixture for Manchester United
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=40&last=1", headers=headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode('utf-8'))
    fixture = data['response'][0]

    # Send the result to the Discord channel
    home_team = fixture['teams']['home']['name']
    away_team = fixture['teams']['away']['name']
    home_score = fixture['goals']['home']
    away_score = fixture['goals']['away']
    result_message = f"{home_team} {home_score} - {away_score} {away_team}\n"
    em11 = discord.Embed(title="Live result for Liverpool FC:\n", description=f"{result_message} ⚽", color=ctx.author.color)
    await ctx.send(embed=em11)



@bot.command(name='Upcoming', help='next 10 upcoming prem games')
async def get_Upcoming_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    conn.request("GET", "/v3/fixtures?league=39&season=2023&next=10", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    matches = json.loads(data)["response"]
    if matches:
        message = "Upcoming matches:\n\n"
        for match in matches:
            home_team = match["teams"]["home"]["name"]
            away_team = match["teams"]["away"]["name"]
            match_date = match["fixture"]["date"].split("T")[0] # Extract match date
            message += f"{home_team} vs {away_team} on {match_date}\n"
        em12 = discord.Embed(title = "Upcoming matches in the premier league:\n", description = f'{message} ⚽',color = ctx.author.color)
        await ctx.send(embed=em12)
    else:
        await ctx.send("No Upcoming matches found.")


#last 10 most recent matches in the premier league then displays results


@bot.command(name='last10', help=' last 10 results of prem games')
async def get_score_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

        # Set the headers
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key,
        'Content-Type': 'application/json'
        }
    conn.request("GET", "/v3/fixtures?league=39&season=2023&last=10", headers=headers)
    response  = conn.getresponse()
  
    data = json.loads(response.read().decode('utf-8'))
    results = data['response'][-10:]

                # Send the results to the Discord channel
    result_message = "Results:\n\n"
    if results:
        for result in results:
            home_team = result['teams']['home']['name']
            away_team = result['teams']['away']['name']
            home_score = result['goals']['home']
            away_score = result['goals']['away']
            result_message += f"{home_team} {home_score} - {away_score} {away_team}\n"
        em11 = discord.Embed(title = "Last 10 results from premier league games:\n", description = f'{result_message} ⚽',color = ctx.author.color)
        await ctx.send(embed=em11)
    else:
        await ctx.send("No Upcoming matches found.")

#Upcoming man united games






@bot.command(name='manutd_games', help='next 10 man utd games')
async def get_Upcoming_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=33&next=10", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    matches = json.loads(data)["response"]
    if matches:
        message = "Upcoming matches:\n\n"
        for match in matches:
            home_team = match["teams"]["home"]["name"]
            away_team = match["teams"]["away"]["name"]
            match_date = match["fixture"]["date"].split("T")[0] # Extract match date
            message += f"{home_team} vs {away_team} on {match_date}\n"
        em12 = discord.Embed(title = "Upcoming matches for manchester united :\n", description = f'{message} ⚽',color = ctx.author.color)
        await ctx.send(embed=em12)
    else:
        await ctx.send("No Upcoming matches found.")



# displays the last 10 manchester united results

@bot.command(name='manutd_results', help=' last 10 Manchester Utd results')
async def get_score_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

        # Set the headers
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key,
        'Content-Type': 'application/json'
        }
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=33&last=10", headers=headers)
    response  = conn.getresponse()
  
    data = json.loads(response.read().decode('utf-8'))
    results = data['response'][-10:]

                # Send the results to the Discord channel
    result_message = "Results:\n\n"
    if results:
        for result in results:
            home_team = result['teams']['home']['name']
            away_team = result['teams']['away']['name']
            home_score = result['goals']['home']
            away_score = result['goals']['away']
            result_message += f"{home_team} {home_score} - {away_score} {away_team}\n"
        em11 = discord.Embed(title = "Last 10 results For Manchester United:\n", description = f'{result_message} ⚽',color = ctx.author.color)
        await ctx.send(embed=em11)
    else:
        await ctx.send("No Upcoming matches found.")



@bot.command(name='lfc_results', help='shows liverpool Last 10 results')
async def get_score_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

        # Set the headers
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key,
        'Content-Type': 'application/json'
        }
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=40&last=10", headers=headers)
    response  = conn.getresponse()
  
    data = json.loads(response.read().decode('utf-8'))
    results = data['response'][-10:]

                # Send the results to the Discord channel
    result_message = "Results:\n\n"
    if results:
        for result in results:
            home_team = result['teams']['home']['name']
            away_team = result['teams']['away']['name']
            home_score = result['goals']['home']
            away_score = result['goals']['away']
            result_message += f"{home_team} {home_score} - {away_score} {away_team}\n"
        em11 = discord.Embed(title = "Last 10 results For Liverpool:\n", description = f'{result_message} ⚽',color = ctx.author.color)
        await ctx.send(embed=em11)
    else:
        await ctx.send("No Upcoming matches found.")


@bot.command(name='lfc_games', help=' shows next 10 liverpool games')
async def get_Upcoming_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=40&next=10", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    matches = json.loads(data)['response']
    if matches:
        message = "Upcoming matches:\n\n"
        for match in matches:
            home_team = match["teams"]["home"]["name"]
            away_team = match["teams"]["away"]["name"]
            match_date = match["fixture"]["date"].split("T")[0] # Extract match date
            message += f"{home_team} vs {away_team} on {match_date}\n"
        em12 = discord.Embed(title = "Upcoming matches for Liverpool :\n", description = f'{message} ⚽',color = ctx.author.color)
        await ctx.send(embed=em12)
    else:
        await ctx.send("No Upcoming matches found.")



   
@bot.command(name='fa_next', help='displays the next 10 games for the fa cup or less depending on quarter/semi finals etc')
async def get_Upcoming_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    conn.request("GET", "/v3/fixtures?league=45&season=2023&next=10", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    matches = json.loads(data)["response"]
    if matches:
        message = "Upcoming matches:\n\n"
        for match in matches:
            home_team = match["teams"]["home"]["name"]
            away_team = match["teams"]["away"]["name"]
            match_date = match["fixture"]["date"].split("T")[0] # Extract match date
            message += f"{home_team} vs {away_team} on {match_date}\n"
        em12 = discord.Embed(title = "Upcoming matches in the Fa Cup:\n", description = f'{message} ⚽',color = ctx.author.color)
        await ctx.send(embed=em12)
    else:
        await ctx.send("No Upcoming matches found.")



@bot.command(name='uefa_next', help=' displays the next 20 matches in the uefa league')
async def get_Upcoming_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    conn.request("GET", "/v3/fixtures?league=2&season=2023&next=20", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    matches = json.loads(data)["response"]
    if matches:
        message = "Upcoming matches:\n\n"
        for match in matches:
            home_team = match["teams"]["home"]["name"]
            away_team = match["teams"]["away"]["name"]
            match_date = match["fixture"]["date"].split("T")[0] # Extract match date
            message += f"{home_team} vs {away_team} on {match_date}\n"
        em12 = discord.Embed(title = "Upcoming matches in the UEFA champions League:\n", description = f'{message} ⚽',color = ctx.author.color)
        await ctx.send(embed=em12)
    else:
        await ctx.send("No Upcoming matches found.")


@bot.command(name='europa_next', help=' displays the next 10 matches in the europa league')
async def get_Upcoming_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    conn.request("GET", "/v3/fixtures?league=3&season=2023&next=10", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    matches = json.loads(data)["response"]
    if matches:
        message = "Upcoming matches:\n\n"
        for match in matches:
            home_team = match["teams"]["home"]["name"]
            away_team = match["teams"]["away"]["name"]
            match_date = match["fixture"]["date"].split("T")[0] # Extract match date
            message += f"{home_team} vs {away_team} on {match_date}\n"
        em12 = discord.Embed(title = "Upcoming matches in the UEFA europa league:\n", description = f'{message} ⚽',color = ctx.author.color)
        await ctx.send(embed=em12)
    else:
        await ctx.send("No Upcoming matches found.")



@bot.command(name='uefa_last10', help=' displays the last 10 matches in the uefa league')
async def get_score_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

        # Set the headers
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key,
        'Content-Type': 'application/json'
        }
    conn.request("GET", "/v3/fixtures?league=2&season=2023&last=10", headers=headers)
    response  = conn.getresponse()
  
    data = json.loads(response.read().decode('utf-8'))
    results = data['response'][-10:]

                # Send the results to the Discord channel
    result_message = "Results:\n\n"
    if results:
        for result in results:
            home_team = result['teams']['home']['name']
            away_team = result['teams']['away']['name']
            home_score = result['goals']['home']
            away_score = result['goals']['away']
            result_message += f"{home_team} {home_score} - {away_score} {away_team}\n"
        em11 = discord.Embed(title = "Last 10 results from UEFA champions League games:\n", description = f'{result_message} ⚽',color = ctx.author.color)
        await ctx.send(embed=em11)
    else:
        await ctx.send("No Upcoming matches found.")


@bot.command(name='fa_last10', help='displays last 10 results in the fa cup')
async def get_score_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

        # Set the headers
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key,
        'Content-Type': 'application/json'
        }
    conn.request("GET", "/v3/fixtures?league=45&season=2023&last=10", headers=headers)
    response  = conn.getresponse()
  
    data = json.loads(response.read().decode('utf-8'))
    results = data['response'][-10:]

                # Send the results to the Discord channel
    result_message = "Results:\n\n"
    if results:
        for result in results:
            home_team = result['teams']['home']['name']
            away_team = result['teams']['away']['name']
            home_score = result['goals']['home']
            away_score = result['goals']['away']
            result_message += f"{home_team} {home_score} - {away_score} {away_team}\n"
        em11 = discord.Embed(title = "Last 10 results from Fa Cup games:\n", description = f'{result_message} ⚽',color = ctx.author.color)
        await ctx.send(embed=em11)
    else:
        await ctx.send("No Upcoming matches found.")



@bot.command(name='table', help='displays the premier league table')
async def pl_table(ctx):
    connection = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key
        }
    connection.request("GET", "/v3/standings?season=2023&league=39", headers=headers)
    response = connection.getresponse()
    data = response.read()

# Parse response JSON
    table = json.loads(data)['response'][0]['league']['standings'][0]

# Format table data as string
    table_string = ""
    for team in table:
        rank = team['rank']
        name = team['team']['name']
        points = team['points']
        table_string += f"{rank}. {name}: {points}\n"
        em11 = discord.Embed(title = "Premier League Table:\n", description = "\n" + table_string + "" , color = ctx.author.color)
    await ctx.send(embed=em11)



@bot.command(name='mancity_results', help='last 10 mancity results')
async def get_score_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

        # Set the headers
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key,
        'Content-Type': 'application/json'
        }
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=50&last=10", headers=headers)
    response  = conn.getresponse()
  
    data = json.loads(response.read().decode('utf-8'))
    results = data['response'][-10:]

                # Send the results to the Discord channel
    result_message = "Results:\n\n"
    if results:
        for result in results:
            home_team = result['teams']['home']['name']
            away_team = result['teams']['away']['name']
            home_score = result['goals']['home']
            away_score = result['goals']['away']
            result_message += f"{home_team} {home_score} - {away_score} {away_team}\n"
        em11 = discord.Embed(title = "Last 10 results For Manchester City:\n", description = f'{result_message} ⚽',color = ctx.author.color)
        await ctx.send(embed=em11)
    else:
        await ctx.send("No Upcoming matches found.")


@bot.command(name='mancity_games', help=' next 10 mancity games')
async def get_Upcoming_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=50&next=10", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    matches = json.loads(data)['response']
    if matches:
        message = "Upcoming matches:\n\n"
        for match in matches:
            home_team = match["teams"]["home"]["name"]
            away_team = match["teams"]["away"]["name"]
            match_date = match["fixture"]["date"].split("T")[0] # Extract match date
            message += f"{home_team} vs {away_team} on {match_date}\n"
        em12 = discord.Embed(title = "Upcoming matches for Manchester City :\n", description = f'{message} ⚽',color = ctx.author.color)
        await ctx.send(embed=em12)
    else:
        await ctx.send("No Upcoming matches found.")




@bot.command(name='link', help='sends a link for football')
async def link(ctx):
    link2 = 'https://vipleague.im/football-schedule-streaming-links'
    em11 = discord.Embed(title="Oh You want to watch some football :) ?", description=f"I can Reccomend this site:\n {link2}\n but i also reccomend a VPN too ⚽", color=ctx.author.color)
    await ctx.send(embed=em11)




@bot.command(name='manutd_lineup', help='Displays the lineup for the previous Manchester United match')
async def get_lineup(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    # Set the headers
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key,
        'Content-Type': 'application/json'
    }

    # Get the latest fixture for Manchester United
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=33&last=2", headers=headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode('utf-8'))

    # Check if there is at least one previous match
    if len(data['response']) < 2:
        await ctx.send("No previous matches found.")
        return

    # Get the details for the previous match
    previous_fixture = data['response'][-2]
    home_team = previous_fixture['teams']['home']['name']
    away_team = previous_fixture['teams']['away']['name']

    # Check if the previous match has lineups available
    if 'lineups' not in previous_fixture:
        await ctx.send(f"No lineups found for the previous match between {home_team} and {away_team}\n please note Lineups are only available between 20 and 40 minutes before the fixture.")
        return

    # Get the lineups for the previous match
    home_lineup = previous_fixture['lineups']['home']['startXI']
    away_lineup = previous_fixture['lineups']['away']['startXI']

    # Create an embed message with the lineups
    em = discord.Embed(title=f"Lineups for the previous match between {home_team} and {away_team}.", color=ctx.author.color)
    em.add_field(name=f"{home_team} lineup", value='\n'.join([player['player'] for player in home_lineup]), inline=True)
    em.add_field(name=f"{away_team} lineup", value='\n'.join([player['player'] for player in away_lineup]), inline=True)

    await ctx.send(embed=em)




@bot.command(name='manutd_stats', help='Displays Manchester United statistics')
async def manu_stats(ctx):
    url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

    querystring = {"league":"39","team":"33","season":"2023"}

    headers = {
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # Format the JSON response
    data = json.loads(response.text)

    # Save data to file
    with open('data.json', 'w') as f:
        json.dump(data, f,indent=4)

    # Load the JSON data from file
    with open('data.json') as f:
        data = json.load(f)

    # Extract the data
    get = data['get']
    params = data['parameters']
    league = data['response']['league']
    team = data['response']['team']
    form = data['response']['form']
    fixtures = data['response']['fixtures']
    cards = data['response']['cards']
    lineups = data['response']['lineups']

    # Create the embed message
    embed = discord.Embed(title="Manchester United Statistics", color=0xff0000)
    embed.add_field(name="API Endpoint", value=get, inline=False)
    embed.add_field(name="Parameters", value="\n".join([f"{key} {value}" for key, value in params.items()]), inline=False)
    embed.add_field(name="Team", value="\n".join([f"{key} {value}" for key, value in team.items()]), inline=False)
    embed.add_field(name="Form", value=form, inline=False)
    for lineup in lineups:
        embed.add_field(name="Lineups", value=f"{lineup['formation']} played {lineup['played']} times", inline=False)
    for key, value in fixtures.items():
        embed.add_field(name=key.capitalize(), value="\n".join([f"{subkey} {subvalue}" for subkey, subvalue in value.items()]), inline=False)
    for key, value in cards.items():
        embed.add_field(name=key.capitalize(), value="\n".join([f"{subkey} {subvalue}" for subkey, subvalue in value.items()]), inline=False)


    # Send the message to Discord
    await ctx.send(embed=embed)





@bot.command(name='manutd_topscorers', help='Displays top 3 goal scorers for Manchester United')
async def display_manutd_topscorers(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': Key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    conn.request("GET", "/v3/players/topscorers?league=39&season=2023", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    #save the data into a json format
    with open('top_scorers.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("Data saved to top_scorers.json")

    # Load the data from the JSON file
    with open("top_scorers.json", "r") as f:
        data = json.load(f)

    # Get the man utd players
    man_city_players = [player for player in data["response"] if player["statistics"][0]["team"]["name"] == "Manchester United"]

    # Sort the man utd players by number of goals scored (in descending order)
    sorted_players = sorted(man_city_players, key=lambda x: x["statistics"][0]["goals"]["total"], reverse=True)

    # Create an embed to display the top 3 goal scorers for man utd, along with their number of assists
    embed = discord.Embed(title="Top goal scorers for Manchester United", color=discord.Color.red())
    for i in range(min(3, len(sorted_players))):
        player_name = sorted_players[i]["player"]["name"]
        goals_scored = sorted_players[i]["statistics"][0]["goals"]["total"]
        assists = sorted_players[i]["statistics"][0]["goals"]["assists"]
        embed.add_field(name=f"{i+1}. {player_name}", value=f"{goals_scored} goals, {assists} assists", inline=False)

    await ctx.send(embed=embed)





@bot.command(name='lfc_topscorers', help='Displays top 3 goal scorers for Liverpool')
async def display_manutd_topscorers(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': Key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    conn.request("GET", "/v3/players/topscorers?league=39&season=2023", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    #save the data into a json format
    with open('top_scorers.json', 'w') as f:
        json.dump(data, f, indent=4)

    #print("Data saved to top_scorers.json")  Debugging the json

    # Load the data from the JSON file
    with open("top_scorers.json", "r") as f:
        data = json.load(f)

    # Get the Liverpool  players
    man_city_players = [player for player in data["response"] if player["statistics"][0]["team"]["name"] == "Liverpool"]

    # Sort the Liverpool players by number of goals scored (in descending order)
    sorted_players = sorted(man_city_players, key=lambda x: x["statistics"][0]["goals"]["total"], reverse=True)

    # Create an embed to display the top 3 goal scorers for Liverpool, along with their number of assists
    embed = discord.Embed(title="Top goal scorers for Liverpool", color=discord.Color.red())
    for i in range(min(3, len(sorted_players))):
        player_name = sorted_players[i]["player"]["name"]
        goals_scored = sorted_players[i]["statistics"][0]["goals"]["total"]
        assists = sorted_players[i]["statistics"][0]["goals"]["assists"]
        embed.add_field(name=f"{i+1}. {player_name}", value=f"{goals_scored} goals, {assists} assists", inline=False)

    await ctx.send(embed=embed)






@bot.command(name='mancity_topscorers', help='Displays top 3 goal scorers for City')
async def display_manutd_topscorers(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': Key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    conn.request("GET", "/v3/players/topscorers?league=39&season=2023", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    #save the data into a json format
    with open('top_scorers.json', 'w') as f:
        json.dump(data, f, indent=4)

    #print("Data saved to top_scorers.json")  Debugging the json

    # Load the data from the JSON file
    with open("top_scorers.json", "r") as f:
        data = json.load(f)

    # Get the Manchester City players
    man_city_players = [player for player in data["response"] if player["statistics"][0]["team"]["name"] == "Manchester City"]

    # Sort the Manchester City players by number of goals scored (in descending order)
    sorted_players = sorted(man_city_players, key=lambda x: x["statistics"][0]["goals"]["total"], reverse=True)

    # Create an embed to display the top 3 goal scorers for Manchester City, along with their number of assists
    embed = discord.Embed(title="Top goal scorers for Manchester City", color=discord.Color.red())
    for i in range(min(3, len(sorted_players))):
        player_name = sorted_players[i]["player"]["name"]
        goals_scored = sorted_players[i]["statistics"][0]["goals"]["total"]
        assists = sorted_players[i]["statistics"][0]["goals"]["assists"]
        embed.add_field(name=f"{i+1}. {player_name}", value=f"{goals_scored} goals, {assists} assists", inline=False)

    await ctx.send(embed=embed)



@bot.command(name='mancity_injuries', help='Displays most recent injuries and suspensions for Manchester City')
async def liv_injuries(ctx):

    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': Key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    conn.request("GET", "/v3/injuries?league=39&season=2023", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    with open('injuries.json', 'w') as f:
        json.dump(data, f, indent=4)

    #print("Data saved to injuries.json") debugging the json

    with open("injuries.json", "r") as f:
        data = json.load(f)

    # Get all the injuries and suspensions
    injuries = data["response"]

    # Filter the injuries and suspensions for Liverpool
    liv_injuries = [injury for injury in injuries if injury["team"]["name"] == "Manchester City"]

    # Sort the injuries and suspensions by fixture date (in descending order)
    sorted_injuries = sorted(liv_injuries, key=lambda x: x["fixture"]["date"], reverse=True)

    # Create the embed message to send to Discord
    embed = discord.Embed(title="Most recent injuries and suspensions for Manchester City:")
    embed.color = discord.Color.blue()

    num_injuries = len(sorted_injuries)
    if num_injuries == 0:
        embed.description = "No injuries or suspensions found for Manchester City."
    else:
        for i in range(num_injuries):
            if i >= 5:
                break
            player_name = sorted_injuries[i]["player"]["name"]
            fixture_date = sorted_injuries[i]["fixture"]["date"]
            injury_type = sorted_injuries[i]["player"]["type"]
            injury_reason = sorted_injuries[i]["player"]["reason"]
            embed.add_field(name=f"{i+1}. {player_name}", value=f"{injury_type}, {injury_reason} ({fixture_date})", inline=False)

        if num_injuries > 5:
            embed.set_footer(text=f"Showing the most recent 5 out of {num_injuries} injuries and suspensions.")

    await ctx.send(embed=embed)




@bot.command(name='lfc_injuries', help='Displays most recent injuries and suspensions')
async def liv_injuries(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': Key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    conn.request("GET", "/v3/injuries?league=39&season=2023", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    with open('injuries.json', 'w') as f:
        json.dump(data, f, indent=4)

    #print("Data saved to injuries.json") debugging the json
    
    with open("injuries.json", "r") as f:
        data = json.load(f)

    # Get all the injuries and suspensions
    injuries = data["response"]

    # Filter the injuries and suspensions for Liverpool
    liv_injuries = [injury for injury in injuries if injury["team"]["name"] == "Liverpool"]

    # Sort the injuries and suspensions by fixture date (in descending order)
    sorted_injuries = sorted(liv_injuries, key=lambda x: x["fixture"]["date"], reverse=True)

    # Create the embed message to send to Discord
    embed = discord.Embed(title="Most recent injuries and suspensions for Liverpool FC:")
    embed.color = discord.Color.red()

    num_injuries = len(sorted_injuries)
    if num_injuries == 0:
        embed.description = "No injuries or suspensions found for Liverpool FC."
    else:
        for i in range(num_injuries):
            if i >= 5:
                break
            player_name = sorted_injuries[i]["player"]["name"]
            fixture_date = sorted_injuries[i]["fixture"]["date"]
            injury_type = sorted_injuries[i]["player"]["type"]
            injury_reason = sorted_injuries[i]["player"]["reason"]
            embed.add_field(name=f"{i+1}. {player_name}", value=f"{injury_type}, {injury_reason} ({fixture_date})", inline=False)

        if num_injuries > 5:
            embed.set_footer(text=f"Showing the most recent 5 out of {num_injuries} injuries and suspensions.")

    await ctx.send(embed=embed)




@bot.command(name='manutd_injuries', help='Displays most recent injuries and suspensions for Manchester United')
async def liv_injuries(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': Key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    conn.request("GET", "/v3/injuries?league=39&season=2023", headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))

    with open('injuries.json', 'w') as f:
        json.dump(data, f, indent=4)

    #print("Data saved to injuries.json") debugging the json
    
    with open("injuries.json", "r") as f:
        data = json.load(f)

    # Get all the injuries and suspensions
    injuries = data["response"]

    # Filter the injuries and suspensions for Liverpool
    liv_injuries = [injury for injury in injuries if injury["team"]["name"] == "Manchester United"]

    # Sort the injuries and suspensions by fixture date (in descending order)
    sorted_injuries = sorted(liv_injuries, key=lambda x: x["fixture"]["date"], reverse=True)

    # Create the embed message to send to Discord
    embed = discord.Embed(title="Most recent injuries and suspensions for Manchester United:")
    embed.color = discord.Color.red()

    num_injuries = len(sorted_injuries)
    if num_injuries == 0:
        embed.description = "No injuries or suspensions found for Manchester United."
    else:
        for i in range(num_injuries):
            if i >= 5:
                break
            player_name = sorted_injuries[i]["player"]["name"]
            fixture_date = sorted_injuries[i]["fixture"]["date"]
            injury_type = sorted_injuries[i]["player"]["type"]
            injury_reason = sorted_injuries[i]["player"]["reason"]
            embed.add_field(name=f"{i+1}. {player_name}", value=f"{injury_type}, {injury_reason} ({fixture_date})", inline=False)

        if num_injuries > 5:
            embed.set_footer(text=f"Showing the most recent 5 out of {num_injuries} injuries and suspensions.")

    await ctx.send(embed=embed)


@bot.command(name='manutd_odds', help='Displays Man Utd odds')
async def upcoming_fixture(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': Key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    # Get the next upcoming fixture ID for Manchester United in the Premier League
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=33&next=1&timezone=UTC", headers=headers)

    res = conn.getresponse()
    fixture_data = res.read()

    fixture_id = json.loads(fixture_data.decode("utf-8"))['response'][0]['fixture']['id']

    # Save the fixture data to a JSON file
    with open('fixture.json', 'w') as f:
        json.dump(json.loads(fixture_data.decode("utf-8")), f, indent=4)

    # Get the odds for the upcoming fixture
    conn.request("GET", f"/v3/odds?fixture={fixture_id}", headers=headers)

    res = conn.getresponse()
    odds_data = res.read()

    # Save the odds data to a JSON file
    with open('upcoming_fixture_odds.json', 'w') as f:
        json.dump(json.loads(odds_data.decode("utf-8")), f, indent=4)
        
    # Read the fixture data and odds data from the JSON files
    with open('fixture.json') as f:
        fixture_data = json.load(f)

    with open('upcoming_fixture_odds.json') as f:
        odds_data = json.load(f)
        
    home_team = fixture_data['response'][0]['teams']['home']['name']
    away_team = fixture_data['response'][0]['teams']['away']['name']
    
    # Create an embed with the fixture information and odds
    embed = discord.Embed(title=f"{home_team} vs {away_team}", color=discord.Color.blue())
    
    for bookmaker in odds_data['response'][0]['bookmakers']:
        bookmaker_name = bookmaker['name']
        if bookmaker_name == "William Hill":
            embed.add_field(name=bookmaker_name, value="", inline=False)
            
            for bet in bookmaker['bets']:
                bet_name = bet['name']
                bet_odds = ""
                
                for value in bet['values']:
                    bet_odds += f"{value['value']}: {value['odd']}\n"
                    
                embed.add_field(name=bet_name, value=bet_odds, inline=False)
            
    # Send the embed to the Discord channel
    await ctx.send(embed=embed)





@bot.command(name='manutd_XI', help='Displays the previous starting XI')
async def display_manutd_lineup(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': Key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    # Get the next upcoming fixture ID for Manchester United in the Premier League
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=33&last=1&timezone=UTC", headers=headers)

    res = conn.getresponse()
    fixture_data = res.read()

    fixture_id = json.loads(fixture_data.decode("utf-8"))['response'][0]['fixture']['id']

    # Get the lineup data for the upcoming fixture
    conn.request(f"GET", f"/v3/fixtures/lineups?fixture={fixture_id}&team=33", headers=headers)

    res = conn.getresponse()
    lineup_data = res.read()



    # Parse the lineup data into a Discord embed
    embed = discord.Embed(title='Manchester United Lineup', color=0xff0000)
    for item in json.loads(lineup_data.decode("utf-8"))['response']:
        embed.add_field(name='Team', value=item['team']['name'], inline=False)
        embed.add_field(name='Coach', value=item['coach']['name'], inline=False)
        embed.add_field(name='Formation', value=item['formation'], inline=False)
        starting_xi_str = ''
        for player in item['startXI']:
            starting_xi_str += f"{player['player']['name']} ({player['player']['number']}) - {player['player']['pos']}\n"
        embed.add_field(name='Starting XI', value=starting_xi_str, inline=False)
        substitute_str = ''
        for player in item['substitutes']:
            substitute_str += f"{player['player']['name']} ({player['player']['number']}) - {player['player']['pos']}\n"
        embed.add_field(name='Substitutes', value=substitute_str, inline=False)

    # Send the embed as a message in Discord
    await ctx.send(embed=embed)





@bot.command(name='manutdlive_XI', help='Displays the lineup for the next Manchester United fixture')
async def display_manutd_lineup(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': Key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    # Get the next upcoming fixture ID for Manchester United in the Premier League
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=33&next=1&timezone=UTC", headers=headers)

    res = conn.getresponse()
    fixture_data = res.read()

    fixture_id = json.loads(fixture_data.decode("utf-8"))['response'][0]['fixture']['id']

    # Get the lineup data for the upcoming fixture
    conn.request(f"GET", f"/v3/fixtures/lineups?fixture={fixture_id}&team=33", headers=headers)

    res = conn.getresponse()
    lineup_data = res.read()

    # Check if there is any response from the API
    if not json.loads(lineup_data.decode("utf-8"))['response']:
        await ctx.send("No lineup data available try again 20 minutes before the match.")
    else:
    # Parse the lineup data into a Discord embed
        embed = discord.Embed(title='Manchester United Lineup', color=0xff0000)
    for item in json.loads(lineup_data.decode("utf-8"))['response']:
        embed.add_field(name='Team', value=item['team']['name'], inline=False)
        embed.add_field(name='Coach', value=item['coach']['name'], inline=False)
        embed.add_field(name='Formation', value=item['formation'], inline=False)
        starting_xi_str = ''
        for player in item['startXI']:
            starting_xi_str += f"{player['player']['name']} ({player['player']['number']}) - {player['player']['pos']}\n"
        embed.add_field(name='Starting XI', value=starting_xi_str, inline=False)
        substitute_str = ''
        for player in item['substitutes']:
            substitute_str += f"{player['player']['name']} ({player['player']['number']}) - {player['player']['pos']}\n"
        embed.add_field(name='Substitutes', value=substitute_str, inline=False)

    # Send the embed as a message in Discord
    await ctx.send(embed=embed)






@bot.command(name='manutd_prediction', help='Displays the prediction for the next Manchester United fixture')
async def predict(ctx, fixture_id=None):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': Key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    # Get the next upcoming fixture ID for Manchester United in the Premier League
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=33&next=1&timezone=UTC", headers=headers)

    res = conn.getresponse()
    fixture_data = res.read()

    fixture_id = json.loads(fixture_data.decode("utf-8"))['response'][0]['fixture']['id']

    conn.request("GET", f"/v3/predictions?fixture={fixture_id}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # Decode the response data from bytes to a string and parse it as JSON
    json_data = json.loads(data.decode('utf-8'))


    with open('prediction.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


    with open('prediction.json', 'r') as f:
        data = json.load(f)

# Get the prediction details from the response data
    for prediction in data['response']:
        home_team = prediction['teams']['home']['name']
        away_team = prediction['teams']['away']['name']
        winner = prediction['predictions']['winner']['name']
        advice = prediction['predictions']['advice']
        percent_home = prediction['predictions']['percent']['home']
        percent_draw = prediction['predictions']['percent']['draw']
        percent_away = prediction['predictions']['percent']['away']
        home_logo = prediction['teams']['home']['logo']
        away_logo = prediction['teams']['away']['logo']
        home_form = prediction['teams']['home']['last_5']['form']
        away_form = prediction['teams']['away']['last_5']['form']
        home_goals_for_total = prediction['teams']['home']['league']['goals']['for']['total']['total']
        home_goals_for_home = prediction['teams']['home']['league']['goals']['for']['total']['home']
        home_goals_for_away = prediction['teams']['home']['league']['goals']['for']['total']['away']
        away_goals_for_total = prediction['teams']['away']['league']['goals']['for']['total']['total']
        away_goals_for_home = prediction['teams']['away']['league']['goals']['for']['total']['home']
        away_goals_for_away = prediction['teams']['away']['league']['goals']['for']['total']['away']



    
        embed = discord.Embed(title=f"{home_team} vs {away_team}", color=discord.Color.dark_red())
        embed.add_field(name="Winner", value=winner, inline=False)
        embed.add_field(name="Advice", value=advice, inline=False)
        embed.add_field(name="Percentages", value=f"Home: {percent_home}%, Draw: {percent_draw}%, Away: {percent_away}%", inline=False)
        embed.add_field(name=f"{home_team} Form", value=home_form, inline=True)
        embed.add_field(name=f"{away_team} Form", value=away_form, inline=True)
        embed.add_field(name=f"{home_team} Total Goals Scored", value=home_goals_for_total, inline=True)
        embed.add_field(name=f"{home_team} Goals Scored at Home", value=home_goals_for_home, inline=True)
        embed.add_field(name=f"{home_team} Goals Scored Away", value=home_goals_for_away, inline=True)
        embed.add_field(name=f"{away_team} Total Goals Scored", value=away_goals_for_total, inline=True)
        embed.add_field(name=f"{away_team} Goals Scored at Home", value=away_goals_for_home, inline=True)
        embed.add_field(name=f"{away_team} Goals Scored Away", value=away_goals_for_away, inline=True)
        embed.set_thumbnail(url=home_logo)
        embed.set_thumbnail(url=away_logo)
    
    await ctx.send(embed=embed)



@bot.command(name='lfc_prediction', help='Displays the prediction for the next Liverpool fixture')
async def predict(ctx, fixture_id=None):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': Key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    # Get the next upcoming fixture ID for Manchester United in the Premier League
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=40&next=1&timezone=UTC", headers=headers)

    res = conn.getresponse()
    fixture_data = res.read()

    fixture_id = json.loads(fixture_data.decode("utf-8"))['response'][0]['fixture']['id']

    conn.request("GET", f"/v3/predictions?fixture={fixture_id}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # Decode the response data from bytes to a string and parse it as JSON
    json_data = json.loads(data.decode('utf-8'))


    with open('prediction.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


    with open('prediction.json', 'r') as f:
        data = json.load(f)

# Get the prediction details from the response data
    for prediction in data['response']:
        home_team = prediction['teams']['home']['name']
        away_team = prediction['teams']['away']['name']
        winner = prediction['predictions']['winner']['name']
        advice = prediction['predictions']['advice']
        percent_home = prediction['predictions']['percent']['home']
        percent_draw = prediction['predictions']['percent']['draw']
        percent_away = prediction['predictions']['percent']['away']
        home_logo = prediction['teams']['home']['logo']
        away_logo = prediction['teams']['away']['logo']
        home_form = prediction['teams']['home']['last_5']['form']
        away_form = prediction['teams']['away']['last_5']['form']
        home_goals_for_total = prediction['teams']['home']['league']['goals']['for']['total']['total']
        home_goals_for_home = prediction['teams']['home']['league']['goals']['for']['total']['home']
        home_goals_for_away = prediction['teams']['home']['league']['goals']['for']['total']['away']
        away_goals_for_total = prediction['teams']['away']['league']['goals']['for']['total']['total']
        away_goals_for_home = prediction['teams']['away']['league']['goals']['for']['total']['home']
        away_goals_for_away = prediction['teams']['away']['league']['goals']['for']['total']['away']

        # Example score prediction
        predicted_home_goals = random.randint(0, 3)
        predicted_away_goals = random.randint(0, 3)
        predicted_score = f"{predicted_home_goals}-{predicted_away_goals}"

    
        embed = discord.Embed(title=f"{home_team} vs {away_team}", color=discord.Color.dark_red())
        embed.add_field(name="Winner", value=winner, inline=False)
        embed.add_field(name="Advice", value=advice, inline=False)
        embed.add_field(name="Percentages", value=f"Home: {percent_home}%, Draw: {percent_draw}%, Away: {percent_away}%", inline=False)
        embed.add_field(name=f"{home_team} Form", value=home_form, inline=True)
        embed.add_field(name=f"{away_team} Form", value=away_form, inline=True)
        embed.add_field(name=f"{home_team} Total Goals Scored", value=home_goals_for_total, inline=True)
        embed.add_field(name=f"{home_team} Goals Scored at Home", value=home_goals_for_home, inline=True)
        embed.add_field(name=f"{home_team} Goals Scored Away", value=home_goals_for_away, inline=True)
        embed.add_field(name="Predicted Score", value=predicted_score, inline=False)
        embed.add_field(name=f"{away_team} Total Goals Scored", value=away_goals_for_total, inline=True)
        embed.add_field(name=f"{away_team} Goals Scored at Home", value=away_goals_for_home, inline=True)
        embed.add_field(name=f"{away_team} Goals Scored Away", value=away_goals_for_away, inline=True)
        embed.set_thumbnail(url=home_logo)
        embed.set_thumbnail(url=away_logo)
    
    await ctx.send(embed=embed)







@bot.command(name='mancity_prediction', help='Displays the prediction for the next Manchester city fixture')
async def predict(ctx, fixture_id=None):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': Key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    # Get the next upcoming fixture ID for Manchester United in the Premier League
    conn.request("GET", "/v3/fixtures?league=39&season=2023&team=50&next=1&timezone=UTC", headers=headers)

    res = conn.getresponse()
    fixture_data = res.read()

    fixture_id = json.loads(fixture_data.decode("utf-8"))['response'][0]['fixture']['id']

    conn.request("GET", f"/v3/predictions?fixture={fixture_id}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # Decode the response data from bytes to a string and parse it as JSON
    json_data = json.loads(data.decode('utf-8'))


    with open('prediction.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)


    with open('prediction.json', 'r') as f:
        data = json.load(f)

# Get the prediction details from the response data
# Get the prediction details from the response data
    for prediction in data['response']:
        home_team = prediction['teams']['home']['name']
        away_team = prediction['teams']['away']['name']
        winner = prediction['predictions']['winner']['name']
        advice = prediction['predictions']['advice']
        percent_home = prediction['predictions']['percent']['home']
        percent_draw = prediction['predictions']['percent']['draw']
        percent_away = prediction['predictions']['percent']['away']
        home_logo = prediction['teams']['home']['logo']
        away_logo = prediction['teams']['away']['logo']
        home_form = prediction['teams']['home']['last_5']['form']
        away_form = prediction['teams']['away']['last_5']['form']
        home_goals_for_total = prediction['teams']['home']['league']['goals']['for']['total']['total']
        home_goals_for_home = prediction['teams']['home']['league']['goals']['for']['total']['home']
        home_goals_for_away = prediction['teams']['home']['league']['goals']['for']['total']['away']
        away_goals_for_total = prediction['teams']['away']['league']['goals']['for']['total']['total']
        away_goals_for_home = prediction['teams']['away']['league']['goals']['for']['total']['home']
        away_goals_for_away = prediction['teams']['away']['league']['goals']['for']['total']['away']



    
        embed = discord.Embed(title=f"{home_team} vs {away_team}", color=discord.Color.dark_red())
        embed.add_field(name="Winner", value=winner, inline=False)
        embed.add_field(name="Advice", value=advice, inline=False)
        embed.add_field(name="Percentages", value=f"Home: {percent_home}%, Draw: {percent_draw}%, Away: {percent_away}%", inline=False)
        embed.add_field(name=f"{home_team} Form", value=home_form, inline=True)
        embed.add_field(name=f"{away_team} Form", value=away_form, inline=True)
        embed.add_field(name=f"{home_team} Total Goals Scored", value=home_goals_for_total, inline=True)
        embed.add_field(name=f"{home_team} Goals Scored at Home", value=home_goals_for_home, inline=True)
        embed.add_field(name=f"{home_team} Goals Scored Away", value=home_goals_for_away, inline=True)
        embed.add_field(name=f"{away_team} Total Goals Scored", value=away_goals_for_total, inline=True)
        embed.add_field(name=f"{away_team} Goals Scored at Home", value=away_goals_for_home, inline=True)
        embed.add_field(name=f"{away_team} Goals Scored Away", value=away_goals_for_away, inline=True)
        embed.set_thumbnail(url=home_logo)
        embed.set_thumbnail(url=away_logo)

    await ctx.send(embed=embed)


bot.run(TOKEN)