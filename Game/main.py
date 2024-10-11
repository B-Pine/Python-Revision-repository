from enemy import Enemy, Troll, Vampire, VampireKing


steve = Vampire('steve')
print(steve)

# while steve._alive:
#     steve.take_damage(1)
#     # print(steve)

print()
print("-" * 40)
#
# urg = Troll('urg')
# print(urg)
# urg.take_damage(18)
# print(urg)
# urg.take_damage(20)
# print(urg)

vlad = VampireKing('Dracula')
print(vlad)

while vlad._alive:
    vlad.take_damage(55)
