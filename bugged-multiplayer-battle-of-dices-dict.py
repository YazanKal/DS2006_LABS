import random

num_players = int(input("How many players? "))

player_template = {"name": "", "score": 0}
players = []

for i in range(num_players):
    player_template["name"] = input(f"Enter name of player {i+1}: ")
    players.append(player_template)

rounds = int(input("How many rounds? "))

for r in range(rounds):
    print(f"\n--- Round {r+1} ---")
    for player in players:
        dice = random.randint(1, 6)
        player["score"] += dice
        print(f"{player['name']} rolled {dice}, total score: {player['score']}")

print("\nFinal Results:")
for player in players:
    print(f"{player['name']}: {player['score']}")

