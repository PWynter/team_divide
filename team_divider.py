"""create two teams from a list of players"""
from random import choice

#list of all the players to be considered, taken from players.txt
players = []
#create variable and open file as read only
file = open("players.txt","r")
#create variable.open file,read.splitlines every line in file is a new item
players = file.read().splitlines()
print(players)

# emptylists to be populated from append function
teamA = []
teamB = []

#random player selection,appended to teamA and removed from player list
while len(players) > 0:
	playerA = (choice(players))
	#print(playerA)
	teamA.append(playerA)
	players.remove(playerA)
	#print("Players left:",players)

	#when list is empty break loop
	if players == []:
		break

	#random player selection,appended to teamB and removed from player list
	playerB = (choice(players))
	teamB.append(playerB)
	players.remove(playerB)


print("Team A:",teamA)
print("Team B:", teamB)