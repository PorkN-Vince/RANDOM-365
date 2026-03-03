following = {"Mom", "Dad", "Sister", "Crush"}
followers = {"Mom", "Dad", "Brother", "Best Friend"}

traitors = following - followers
mutuals = following & followers
network = following | followers

print(f"{traitors=}")
print(f"{mutuals=}")
print(f"{network=}")