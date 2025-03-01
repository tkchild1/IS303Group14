#Names: Kimball Berrett, Matt Vance, Devin Holderness, Parker Francis, Tanner Child, Ethan Smith
#This program lets the user choose teams from an menu, then generates scores to simulate a season and reports on how the team performed. 

import random

# Function to introduce the game and get the user's name
def introduction():
    user_name = input("Enter your name: ")
    print(f"\nWelcome {user_name}! This game is simple.")
    print("You will pick a home team and an opponent, then this program will simulate games until you decide to end your season.")
    print("Have fun and good luck!")
    return user_name

# Function to display the menu and get the user's choice
def display_menu():
    print("\nMenu:")
    print("1) Choose your team")
    print("2) Choose opponent and play game")
    print("3) Finish season")
    
    choice = input("Enter your selection: ")
    while choice not in ["1", "2", "3"]:
        print("Invalid option. Please enter 1, 2, or 3.")
        choice = input("Enter your selection: ")
    return choice

# Function to allow the user to select a team
def select_team(teams, prompt):
    print(f"\n{prompt}")
    for i, team in enumerate(teams, 1):
        print(f"{i}. {team}")
    
    selection = input("\nSelect the number next to the team: ")
    while not selection.isdigit() or not (1 <= int(selection) <= len(teams)):
        print(f"Please enter a number between 1 and {len(teams)}.")
        selection = input("Select the number next to the team: ")
    
    return teams.pop(int(selection) - 1)

# Function to simulate a game between the home team and opponent
def play_game(home_team, away_team):
    home_score, away_score = random.randint(0, 10), random.randint(0, 10)
    while home_score == away_score:
        home_score, away_score = random.randint(0, 10), random.randint(0, 10)
    
    result = "W" if home_score > away_score else "L"
    return result, home_score, away_score

# Function to display the final results of the season
def print_results(home_team, wins, losses, total_goals_scored, total_goals_allowed):
    print(f"\nFinal season record for {home_team}: {wins} - {losses}")
    print(f"Total goals scored: {total_goals_scored}, Goals allowed: {total_goals_allowed}")
    
    if wins / (wins + losses) >= 0.75:
        print("\nQualified for the NCAA Women's Soccer Tournament!\n")
    elif wins / (wins + losses) >= 0.5:
        print("\nYou had a good season!\n")
    else:
        print("\nYour team needs to practice\n")

# Main function to run the game loop
def main():
    teams = ["BYU", "Utah", "Baylor", "Arizona", "TCU", "Arizona St", "Kansas", "UCF", "Oklahoma St", "Houston", "Kansas St"]
    wins, losses, total_goals_scored, total_goals_allowed = 0, 0, 0, 0
    user_name = introduction()
    home_team = None
    finished = False
    
    while not finished:
        option = display_menu()
        
        if option == "1":
            if home_team:
                print("You have already selected a team.")
            else:
                home_team = select_team(teams, "Choose your home team:")
        
        elif option == "2":
            if not home_team:
                print("You must select a home team first.")
            else:
                opponent = select_team(teams, "Choose your opponent:")
                result, home_score, away_score = play_game(home_team, opponent)
                print(f"{home_team}: {home_score} - {opponent}: {away_score}")
                if result == "W":
                    wins += 1
                else:
                    losses += 1
                total_goals_scored += home_score
                total_goals_allowed += away_score
        
        elif option == "3":
            if home_team:
                print_results(home_team, wins, losses, total_goals_scored, total_goals_allowed)
            print(f"Thank you {user_name} for playing! Have a great day.")
            finished = True

if __name__ == "__main__":
    main()