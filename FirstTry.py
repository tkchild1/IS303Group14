import random

wins = 0
losses = 0
totalGoalsScored = 0
totalGoalsAllowed = 0
assurance = 0
teamList = ["BYU", "Utah", "Baylor", "Arizona", "TCU", "Arizona St", "Kansas", "UCF", "Oklahoma St", "Houston", "Kansas St"]

def introduction():
    userName = input("Enter your name: ")
    print(f"Welcome {userName}! This game is simple. You will select a team and simulate their season.")
    print(f"From the following menu, please first select your team. You should only select this option once.")
    print(f"After selecting your team, select an opponent from the list until you desire to end your season.")
    print("Have fun and good luck!")
    return userName
def thankYou(name):
    print(f"Thank you {name} for playing! Have a great day")
def displayMenu():
    print(f"\nMenu:\n1) Choose your team\n2) Choose opponent and play game\n3) Finish season")
    userSelection = input("\nEnter your selection: ")
    return userSelection
def selectHomeTeam(teams=["BYU", "Utah", "Baylor", "Arizona", "TCU", "Arizona St", "Kansas", "UCF", "Oklahoma St", "Houston", "Kansas St"]):
    for i in range(len(teams)):
        message = str((i+1)) + ". " + teams[i] 
        print(message)
    listPlace = int(input("\nSelect the number next to the team you wish to be: "))
    if listPlace < 1 or listPlace > len(teams):
         print(f"Please enter a number between 1 and {len(teams)}. Try again")
    else:
        homeTeam = teams[listPlace - 1]
        teams.pop(listPlace - 1)
        return homeTeam
def selectOpponent(teams=["BYU", "Utah", "Baylor", "Arizona", "TCU", "Arizona St", "Kansas", "UCF", "Oklahoma St", "Houston", "Kansas St"]):
    for i in range(len(teams)):
        message = str((i+1)) + ". " + teams[i] 
        print(message)
    listPlace = int(input("\nSelect the number next to the team you wish to play: "))
    if listPlace < 1 or listPlace > len(teams):
         print(f"Please enter a number between 1 and {len(teams)}. Try again")
    else:
        awayTeam = teams[listPlace - 1]
        teams.pop(listPlace - 1)
        return awayTeam
def playGame(homeTeam, awayTeam):
    homeScore = random.randint(0, 10)
    awayScore = random.randint(0, 10)
    while homeScore == awayScore:
        homeScore = random.randint(0, 10)
        awayScore = random.randint(0, 10)
    #save the results as wins or losses
    if homeScore > awayScore:
        result = "W"
    else:
        result = "L"
    return result, homeScore, awayScore
def printResults(homeTeam, wins, losses):
    print(f"\nFinal season record for {homeTeam}: {wins} - {losses}")
    print(f"You scored {totalGoalsScored} and you allowed {totalGoalsAllowed}")
    numGames = wins + losses
    if wins / numGames >= 0.75:
        print("\nQualified for the NCAA Women's Soccer Tournament\n")
    elif wins / numGames >= 0.5:
        print("\nYou had a good season\n")
    else:
        print("\nYour team needs to practice!\n")


user = introduction()
option = displayMenu()
while option != "3":
    if option == "1":
        if assurance == 1:
            print("You have already selected a team. Try a different option.")
        else:
            homeTeam = selectHomeTeam(teamList)
            assurance = 1
    elif option == "2":
        opponent = selectOpponent(teamList)
        status, myGoals, theirGoals = playGame(homeTeam, opponent)
        print(f"{homeTeam}: {myGoals}\n{opponent}: {theirGoals}")
        if status == "W":
            wins += 1
        else:
            losses += 1
        totalGoalsScored += myGoals
        totalGoalsAllowed += theirGoals
    else:
        print("That is not a valid menu option.")
    option = displayMenu()

printResults(homeTeam, wins, losses)
thankYou(user)