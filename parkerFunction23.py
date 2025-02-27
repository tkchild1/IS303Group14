def chooseTeam(team = True) :
    lstTeams = ["BYU", "UofU", "USU", "UVU", "WSU"]
    if team == True :
        for index, team in enumerate(lstTeams):
            print(f"{index+1}) {team}")
        iSelectTeam = int(input("Select your team: "))
        team = lstTeams[iSelectTeam-1]
        return team
    else :
        if team in lstTeams :
            lstTeams.remove(team)
        for index, team in enumerate(lstTeams):
            print(f"{index+1}) {team}")
        iSelectTeam = int(input("Select your opponent: "))
        team = lstTeams[iSelectTeam-1]
        return team