votes = {}

while True:
    name = input("Enter the candidate's last name (or '/stop' to finish): ")
    if name == "/stop":
        break
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1

print("\n--- voting results ---")
for candidate, count in votes.items():
    print(f"{candidate}: {count} votes")
winner = max(votes, key=votes.get)
print(f"\nWinner: {winner}!")
