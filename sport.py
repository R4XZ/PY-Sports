import http.client
import json
import discord
from discord.utils import get
from dotenv import load_dotenv
from discord.ext import commands,tasks
import os
import requests
import random




load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
Key = os.getenv("API_KEY")

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)





#standard commands


@bot.command(name='Upcoming', help='next 10 upcoming prem games')
async def get_Upcoming_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    conn.request("GET", "/v3/fixtures?league=39&season=2024&next=10", headers=headers)
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
    conn.request("GET", "/v3/fixtures?league=39&season=2024&last=10", headers=headers)
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




#new function for a more user friendly manner Example: !matches 33

@bot.command(name='matches', help='Get the next 10 matches for a specific team by ID')
async def get_Upcoming_matches(ctx, team_id: int):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    conn.request("GET", f"/v3/fixtures?league=39&season=2024&team={team_id}&next=10", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    matches = json.loads(data)["response"]
    
    if matches:
        message = "Upcoming matches:\n\n"
        for match in matches:
            home_team = match["teams"]["home"]["name"]
            away_team = match["teams"]["away"]["name"]
            match_date = match["fixture"]["date"].split("T")[0]  # Extract match date
            message += f"{home_team} vs {away_team} on {match_date}\n"
        
        team_name = matches[0]["teams"]["home"]["id"] == team_id and matches[0]["teams"]["home"]["name"] or matches[0]["teams"]["away"]["name"]
        em12 = discord.Embed(title=f"Upcoming matches for {team_name}:\n", description=f'{message} ⚽', color=ctx.author.color)
        await ctx.send(embed=em12)
    else:
        await ctx.send("No upcoming matches found.")

#new function works the same way: !scores 33

@bot.command(name='scores', help='Get the last 10 results for a specific team by ID')
async def get_score_matches(ctx, team_id: int):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    # Set the headers
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key,
        'Content-Type': 'application/json'
    }
    conn.request("GET", f"/v3/fixtures?league=39&season=2024&team={team_id}&last=10", headers=headers)
    response = conn.getresponse()

    data = json.loads(response.read().decode('utf-8'))
    results = data['response']

    # Send the results to the Discord channel
    result_message = "Results:\n\n"
    if results:
        for result in results:
            home_team = result['teams']['home']['name']
            away_team = result['teams']['away']['name']
            home_score = result['goals']['home']
            away_score = result['goals']['away']
            result_message += f"{home_team} {home_score} - {away_score} {away_team}\n"

        team_name = results[0]["teams"]["home"]["id"] == team_id and results[0]["teams"]["home"]["name"] or results[0]["teams"]["away"]["name"]
        em11 = discord.Embed(title=f"Last 10 results for {team_name}:\n", description=f'{result_message} ⚽', color=ctx.author.color)
        await ctx.send(embed=em11)
    else:
        await ctx.send("No recent results found.")


#Neww function for the user to display prem team id's 


@bot.command(name='premid', help='Displays all Premier League team IDs for the 2024 season')
async def get_premier_league_team_ids(ctx):
    url = "https://api-football-v1.p.rapidapi.com/v3/teams"
    querystring = {"league": "39", "season": "2024"}

    headers = {
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        teams = data['response']
        
        team_message = ""
        for team in teams:
            team_id = team['team']['id']
            team_name = team['team']['name']
            team_message += f"{team_name}: {team_id}\n"
        
        # Embed the message in red
        embed = discord.Embed(title="Premier League Teams and their IDs for the 2024 season", description=team_message, color=0xff0000)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"Failed to fetch data. Status code: {response.status_code}")




@bot.command(name='fa_last10', help='displays last 10 results in the fa cup')
async def get_score_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

        # Set the headers
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key,
        'Content-Type': 'application/json'
        }
    conn.request("GET", "/v3/fixtures?league=45&season=2024&last=10", headers=headers)
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








@bot.command(name='fa_next', help='displays the next 10 games for the fa cup or less depending on quarter/semi finals etc')
async def get_Upcoming_matches(ctx):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        "X-RapidAPI-Key": Key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    conn.request("GET", "/v3/fixtures?league=45&season=2024&next=10", headers=headers)
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
    conn.request("GET", "/v3/fixtures?league=2&season=2024&next=20", headers=headers)
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
    conn.request("GET", "/v3/fixtures?league=3&season=2024&next=10", headers=headers)
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
    conn.request("GET", "/v3/fixtures?league=2&season=2024&last=10", headers=headers)
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






@bot.command(name='table', help='displays the premier league table')
async def pl_table(ctx):
    connection = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': Key
        }
    connection.request("GET", "/v3/standings?season=2024&league=39", headers=headers)
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


@bot.command(name='link', help='sends a link for football')
async def link(ctx):
    link2 = 'https://vipleague.im/football-schedule-streaming-links'
    em11 = discord.Embed(title="Oh You want to watch some football :) ?", description=f"I can Reccomend this site:\n {link2}\n but i also reccomend a VPN too ⚽", color=ctx.author.color)
    await ctx.send(embed=em11)




@bot.command(name='Starting11', help='Displays the lineup for the next fixture of a specific team by ID')
async def display_team_lineup(ctx, team_id: int):
    conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': Key,
        'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

    # Get the next upcoming fixture ID for the specified team in the Premier League
    conn.request("GET", f"/v3/fixtures?league=39&season=2024&team={team_id}&next=1&timezone=UTC", headers=headers)
    res = conn.getresponse()
    fixture_data = res.read()
    fixtures_response = json.loads(fixture_data.decode("utf-8"))['response']

    if not fixtures_response:
        await ctx.send("No upcoming fixtures found.")
        return

    fixture_id = fixtures_response[0]['fixture']['id']

    # Get the lineup data for the upcoming fixture
    conn.request(f"GET", f"/v3/fixtures/lineups?fixture={fixture_id}&team={team_id}", headers=headers)
    res = conn.getresponse()
    lineup_data = res.read()
    lineup_response = json.loads(lineup_data.decode("utf-8"))['response']

    # Check if there is any response from the API
    if not lineup_response:
        await ctx.send("No lineup data available. Try again 20 minutes before the match.")
    else:
        # Parse the lineup data into a Discord embed
        team_name = lineup_response[0]['team']['name']
        embed = discord.Embed(title=f'{team_name} Lineup', color=0xff0000)
        for item in lineup_response:
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


bot.run(TOKEN)