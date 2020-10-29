import sys
import constants
import copy

# Creates a copy of the constants.py PLAYERS list
copy_players = copy.deepcopy(constants.PLAYERS)

# Empty list for the three teams to be populated with data
panthers = []
bandits = []
warriors = []


# clean_data() will convert players height to inches and set experience
# to a boolean
def clean_data():
    for player in copy_players:
        new_height = int(player['height'][:2])
        player['height'] = new_height
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False


# team_balance will balance out the teams by importing the clean_data()
# then it will separate the experience players and count them, then it
# will take the experience players and divide them equally among the team.
# The second for will take the remaining players and divide them equally
# among the teams
def team_balance():
    clean_data()

    exp_player_count = 0

    for player in copy_players:
        if player['experience']:
            exp_player_count += 1

    for player in copy_players:
        if player['experience']:
            if len(panthers) < exp_player_count / 3:
                panthers.append(player)
            elif len(bandits) < exp_player_count / 3:
                bandits.append(player)
            elif len(warriors) < exp_player_count / 3:
                warriors.append(player)

    for player in copy_players:
        if not player['experience']:
            if len(panthers) < len(copy_players) / 3:
                panthers.append(player)
            elif len(bandits) < len(copy_players) / 3:
                bandits.append(player)
            elif len(warriors) < len(copy_players) / 3:
                warriors.append(player)


# players_on_team() will take the players on the team and display them
# when the team is selected
def players_on_team(team_name):
    new_list = []  # list to store players names to be printed as one string
    team_height = []  # list to store players height to be averaged
    guardians = []  # list to display gaurdians to the screen as one string
    exp = 0  # variable to store the total experience players total
    non = 0  # variable to store the total non experience players total

    # for loop to loop over team and store the correct value its intended list
    for name in team_name:
        new_list.append(name['name'])
        team_height.append(name['height'])
        guardians.append(name['guardians'])
        if name['experience']:
            exp += 1
        else:
            non += 1

    list_to_str = ', '.join(map(str, new_list))  # takes new list and coverts to string
    guardian_str = ', '.join(map(str, guardians))  # takes guardian list and converts to string

    # the following prints display the team and info to the screen
    print(f"Total players: {len(team_name)}")
    print("Total experienced: {}".format(exp))
    print("Total inexperienced: {}".format(non))
    print("Average height: {}".format(sum(team_height) / len(team_name)))
    print("\nPlayers on Team:")
    print('\t' + list_to_str)
    print("\nGuardians:")
    final_guardian = guardian_str.replace(' and', ',')
    print('\t' + final_guardian)


# choice() displays the choice menu and ask which team the user would like to select
# it also features try/except to catch any errors
def choice():
    try:
        print("\tHere are your choices:")
        print("\t\t1) Display Team Stats")
        print("\t\t2) Quit\n")
        team_choice = int(input("Enter an option >"))

        if team_choice == 1:
            print("\n1) Panthers")
            print("2) Bandits")
            print("3) Warriors\n")
        elif team_choice == 2:
            sys.exit()
        else:
            print("\nInvalid choice try again: ")
            choice()
    except ValueError:
        print("You need to enter only numbers to guess...")
        choice()


if __name__ == "__main__":
    team_balance()  # calls the team balance function

print("\nBASKETBALL TEAM STATS TOOL\n")
print("\t\t---- MENU ----\n")

# The code below is placed in a while loop will give the user options and call and
# print the function of the team they select, it will also ask if the user would
# like to go again, all of this is placed in try/except blocks to catch any error
while True:
    choice()
    try:
        team = int(input("Enter an option >"))
        if 1 < team > 3:
            print("Only numbers between from 1 and 3, \nPlease Try Again...")
            print("\n1) Panthers")
            print("2) Bandits")
            print("3) Warriors\n")
            team = int(input("Enter an option >"))
    except:
        print("\nInvalid input please start over...")

    else:
        if team == 1:
            print("\nTeam: Panthers stats")
            print("--------------------")
            players_on_team(panthers)

        elif team == 2:
            print("\nTeam: Bandits stats")
            print("-------------------")
            players_on_team(bandits)

        elif team == 3:
            print("\nTeam: Warriors stats")
            print("--------------------")
            players_on_team(warriors)

    try:
        again = input("\nWould you like to go again [Y]es or [N]o >>>")
        if again[0].lower() == 'y':
            continue
        elif again[0].lower() == 'n':
            print("\nThanks for using our stats tool!")
            sys.exit()
        else:
            print("Invalid entry try again")
            again = input("\nWould you like to go again [Y]es or [N]o >>>")
    except ValueError:
        print("Invalid Entry try again")
