# Kimball Berrett
# This program simulates tracking a women's soccer team's scores and record for the season.

#import random to use for number generation
import random

#Have user put in the team name and number of games they played
homeTeam = input("\nEnter the name of your team (the home team): ")
numGames = int(input(f"\nEnter the number of teams that {homeTeam} will play (1-10): "))

#Set all variables
games = {}
wins = 0
losses = 0

#Loop for each of the games
for gameNum in range(1, numGames + 1):
    awayTeam = input(f"\nEnter the name of the away team for game {gameNum}: ")
    
    #Generate the scores and use while statement to avoid ties
    homeScore = random.randint(0, 10)
    awayScore = random.randint(0, 10)
    while homeScore == awayScore:
        homeScore = random.randint(0, 10)
        awayScore = random.randint(0, 10)
    
    #save the results as wins or losses
    if homeScore > awayScore:
        result = "W"
        wins += 1
    else:
        result = "L"
        losses += 1
    
    #Save the data as a dictionary
    games[gameNum] = {
        "homeScore": homeScore,
        "awayTeam": awayTeam,
        "awayScore": awayScore,
        "result": result
    }

#Display the game results and record
print('\n\n\n\n')
for gameNum, gameInfo in games.items():
    print(f"\n{homeTeam}'s score: {gameInfo['homeScore']} {gameInfo['awayTeam']}'s score: {gameInfo['awayScore']}")
print(f"\nFinal season record: {wins} - {losses}")

#Display final message to show how good the team is
if wins / numGames >= 0.75:
    print("\nQualified for the NCAA Women's Soccer Tournament\n")
elif wins / numGames >= 0.5:
    print("\nYou had a good season\n")
else:
    print("\nYour team needs to practice!\n")
