from player import Player
from enemy import Enemy, Troll, Vampire, VampireKing

barney = Troll("Barney")
print("Ugly troll - {0._name}".format(barney))

barney.grunt()

barney.take_damage(15)
print(barney)

print("*" * 40)

gerard = Vampire("Gerard")
print(gerard)

gerard.take_damage(10)
print(gerard)

while gerard._alive:
    gerard.take_damage(1)
    print(gerard)

print("*" * 40)

king = VampireKing("King")
print(king)
king.take_damage(8)
print(king)