# multiplayer-battle-of-dices-dict.py
import random

num_players = int(input("How many players? "))

players = {}

for i in range(num_players):
    name = input(f"Enter name of player {i+1}: ")
    players[name] = {"score": 0}

rounds = int(input("How many rounds? "))

for r in range(rounds):
    print(f"\n--- Round {r+1} ---")
    for name in players:
        dice = random.randint(1, 6)
        players[name]["score"] += dice
        print(f"{name} rolled {dice}, total score: {players[name]['score']}")

print("\nFinal Results:")
for name, data in players.items():
    print(f"{name}: {data['score']}")

winner = max(players, key=lambda p: players[p]["score"])
print(f"\nWinner is {winner} with {players[winner]['score']} points!")
