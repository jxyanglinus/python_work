# 4-10 切片

players = ["charles", "martina", "michael", "florence", "eli"]

print("The first three players in the list are:")
for player in players[:3]:
    print(player.title())

print("Three players from the middle of the list are:")
for player in players[1:4]:
    print(player.title())

print("The last three players in the list are:")
for player in players[2:]:
    print(player.title())
