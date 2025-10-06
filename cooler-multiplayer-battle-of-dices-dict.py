# cooler-multiplayer-battle-of-dices-dict.py
import random

num_players = int(input("How many players? "))

# Use a dictionary to store each player's info
players = {}

for i in range(num_players):
    name = input(f"Enter name of player {i+1}: ")
    players[name] = {"score": 0, "rolls": []}  # each player has their own dict

rounds = int(input("How many rounds? "))

for r in range(rounds):
    print(f"\n--- Round {r+1} ---")
    for name in players:
        dice = random.randint(1, 6)
        players[name]["score"] += dice
        players[name]["rolls"].append(dice)
        print(f"{name} rolled {dice}, total score: {players[name]['score']}")

print("\nFinal Results:")
for name, data in players.items():
    print(f"{name}: {data['score']} points | Rolls: {data['rolls']}")

# Find winner
winner = max(players, key=lambda p: players[p]["score"])
print(f"\n🏆 Winner is {winner} with {players[winner]['score']} points!")

