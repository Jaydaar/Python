from player import Player

kevin = Player("Kevin")

print(kevin.name)
print(kevin.lives)
kevin.lives -= 1
print(kevin)
kevin.lives -= 1
print(kevin)
kevin.lives -= 1
print(kevin)
kevin.lives -= 1
print(kevin)

kevin.level = 2
print(kevin)

kevin.level += 5
print(kevin)

kevin.level = 3
print(kevin)

kevin.score = 500
print(kevin)
