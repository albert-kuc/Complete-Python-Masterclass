from player import Player
from enemy import Enemy, Troll, Vampire

t1000 = Enemy("T1000", 12, 1)
print(t1000)

t1000.take_damage(2)
print(t1000)

t1000.take_damage(112)
print(t1000)

barney = Troll("Barney")
print("Ugly troll - {}".format(barney))

barney.grunt()

gerard = Vampire("Gerard")
print(gerard)

barney.take_damage(15)
print(barney)

gerard.take_damage(10)
print(gerard)