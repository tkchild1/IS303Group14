# Kimball Berrett
# This program simulates tracking a women's soccer team's scores and record for the season.

#import random to use for number generation
import random

# Function to display introduction and get player's name
def get_player_name():
    print("Welcome to the Women's Soccer Team Tracker!")
    print("In this program, you'll record the results of a soccer season.")
    print("After you have played a number of games, the program will:")
    print("1. Generate random scores for the home and away teams.")
    print("2. Determine if the home team wins or loses.")
    print("3. Display the final record of wins and losses.")
    print("4. Evaluate the team's performance based on win percentage.")
    name = input("Please enter your name: ")
    print(f"Welcome, {name}!")
    return name


# Call the function to get player's name
player_name = get_player_name()  # Store player's name

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
