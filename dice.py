from random import choices
ntrials = 15000
player1wins = 0
total=0
ndice=2
for i in range(ntrials):
    player2=choices(range(1,7),k=2)
    if player2[0]== player2[1]:
        continue
    player1=choices(range(1,7),k=3)
    player1.sort(reverse=True)
    if player1[0]+player1[1] > player2[0]+player2[1]:
        player1wins += 1
print("Player1Wins=",player1wins/ntrials)

#Since Player1Wins= 0.5299, Player 1's probablity of winning is relatively close to 50%.  Thus, making the game relatively fair.