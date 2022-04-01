# Text based rpg game
import random
import time
import math


# Global variables
name = ""
hp = 0
maxhp = 0
mp = 0
atk = 0
defn = 0
gold = 0
class_ = ""
level = 1
exp = 0
exp_to_next_level = 10
armor_gear = ""
weapon_gear = ""
gearHp = 0
gearMp = 0
gearAtk = 0
gearDefn = 0
geaHp = 0
geaMp = 0
geaAtk = 0
geaDefn = 0
inventory = []
choice = 0
chose = 0
s = 0

def level_up():
    global exp
    global exp_to_next_level
    global level
    global atk
    global defn
    global hp
    global mp

    exp = 0
    exp_to_next_level *= 1.1
    exp_to_next_level = round(exp_to_next_level)
    # CHeck for the highest stat
    if atk > mp:
        # atk is the highest stat
        atk += 2
        defn += 1
        hp += 3
        mp += 0
        # 33% chance to get a +1 to mp
        if random.randint(1, 3) == 1:
            mp += 1
    else:
        # mp is the highest stat
        mp += 4
        defn += 1
        hp += 2
        atk += 0
        # 33% chance to increase atk
        if random.randint(1, 3) == 1:
            atk += 1
    level += 1
    print("You leveled up!")
    time.sleep(1)
    print_stats()

def print_stats():
    global name
    global hp
    global maxhp
    global mp
    global atk
    global defn
    global gold
    global class_
    global level
    global choice
    global exp
    global exp_to_next_level
    global atklist
    global mgclist
    print("Name: " + name)
    print("Class: " + class_)
    print("Level: " + str(level))
    print("Exp: " + str(exp) + "/" + str(exp_to_next_level))
    print("Max HP: " + str(maxhp))
    print("HP: " + str(hp))
    print("MP: " + str(mp))
    print("ATK: " + str(atk))
    print("DEF: " + str(defn))
    print("Gold: " + str(gold))

def gear(name, type, atkbuff, hpbuff, defbuff, mpbuff):
    global hp
    global maxhp
    global mp
    global atk
    global defn
    global armor_gear
    global weapon_gear
    global gearHp
    global gearAtk
    global gearDefn
    global gearMp
    global geaHp
    global geaAtk
    global geaDefn
    global geaMp
    global choice
    global chose
    chose = choice
    print("You have aquired ", name, "!")
    time.sleep(1)
    print("It's stats are:")
    time.sleep(1)
    print("Attack: ", atkbuff, ". Defence: ", defbuff, ". Health: ", hpbuff, ". Mana: ", mpbuff)
    time.sleep(1)
    if type == 1:
        time.sleep(1)
        print("Your current armor stats are: ")
        time.sleep(1)
        print("Attack: ", gearAtk, ". Defence: ", gearDefn, ". Health: ", gearHp, ". Mana: ", gearMp)
        time.sleep(2)
        print("Would you like to replace ", armor_gear, " with ", name, "?")
        print("1. Yes")
        print("2. No")
        choice = input("")
        if choice == "1":
            print("Equipping...")
            time.sleep(1)
            if armor_gear != "":
                maxhp -= gearHp
                mp -= gearMp
                atk -= gearAtk
                defn -= gearDefn
            gearHp = hpbuff
            gearAtk = atkbuff
            gearMp = mpbuff
            gearDefn = defbuff
            maxhp = maxhp + gearHp
            atk += gearAtk
            mp += gearMp
            defn += gearDefn
            print("Equipped!")
        if choice == "2":
            print("Discarded equipment")
    
    if type == 2:
        time.sleep(1)
        print("Your current weapon stats are: ")
        time.sleep(1)
        print("Attack: ", geaAtk, ". Defence: ", geaDefn, ". Health: ", geaHp, ". Mana: ", geaMp)
        time.sleep(2)
        print("Would you like to replace ", weapon_gear, " with ", name, "?")
        print("1. Yes")
        print("2. No")
        choice = input("")
        if choice == "1":
            print("Equipping...")
            time.sleep(1)
            if weapon_gear != "":
                maxhp -= geaHp
                mp -= geaMp
                atk -= geaAtk
                defn -= geaDefn
            geaHp = hpbuff
            geaAtk = atkbuff
            geaMp = mpbuff
            geaDefn = defbuff
            maxhp = maxhp + geaHp
            atk += geaAtk
            mp += geaMp
            defn += geaDefn
            print("Equipped!")
        if choice == "2":
            print("Discarded equipment")

    if hp > maxhp:
        hp = maxhp
    choice = chose

    print_stats()
    time.sleep(3)

def battle(name, ehp, edef, eatk, emp, expgain, goldgain, isboss):
    global hp
    global mp
    global atk
    global defn
    global gold
    global class_
    global level
    global exp
    global exp_to_next_level
    global choice
    global chose
    global s
    chose = choice
    print("You have encountered a " + name + "!")
    time.sleep(1)
    while ehp > 0 and hp > 0:
        print("Your HP: ", hp, ". Enemy HP: ", ehp)
        time.sleep(1)
        print("What do you want to do?")
        print("1. Attack")
        print("2. Magic")
        print("3. Run")
        print("4. Items")
        choice = input("Choice: ")
        if choice == "1":
            print("You have decided to attack the ", name, ".")
            s = ehp
            ehp += edef
            ehp -= atk
            if ehp > s:
                ehp = s
                message("The enemy's defense was too strong to penetrate!")
            time.sleep(1)
            print("The enemy has ", ehp, " health remaining.")
            time.sleep(1)
            
        if choice == "2":
            print("You have decided to cast a spell on the ", name, ".")
            s = ehp
            ehp += edef
            ehp -= mp / 2
            if ehp > s:
                ehp = s
            time.sleep(1)
            print("The enemy has ", ehp, " health remaining.")
            time.sleep(1)

        if choice == "3":
            if isboss == 0:
                print("You ran away")
                time.sleep(1)
                print("You lost half your health")
                hp -= hp / 2
                hp = round(hp)
                ehp = 0
            else:
                print("You can't run from a boss!")
                time.sleep(1)

        if choice == "4":
            print("You have chosen to use an item.")
            print("What item in your inventory do you want to use?")
            for i in range(len(inventory)):
                print(str(i + 1) + ". " + inventory[i])
                time.sleep(1)
            choice = input("")
            use_inventory_item(choice)

        if ehp > 0:
            print("The enemy begins it's turn...")
            time.sleep(2)
            print("The enemy attacks for", eatk + emp, "!")
            s = hp
            hp += defn
            hp -= (emp / 2) + eatk
            if hp > s:
                hp = s
                message("Your defence was too strong to penetrate!")
            time.sleep(1)
    if hp < 1:
        print("Game over!")
        exit()
    else:
        print("You won the battle!")
        time.sleep(1)
        exp += expgain
        gold += goldgain
        print("You gained ", expgain, " exp and ", goldgain, " gold.")
        time.sleep(1)
        if exp >= exp_to_next_level:
            level_up()
            time.sleep(1)
        choice = chose


def shop(item1, item2, item3, item4, item5, i1p, i2p, i3p, i4p, i5p):
    global gold
    global chose
    global choice
    chose = choice
    print("In this shop there are 5 items.")
    time.sleep(1)
    print(item1)
    time.sleep(1)
    print(item2)
    time.sleep(1)
    print(item3)
    time.sleep(1)
    print(item4)
    time.sleep(1)
    print(item5)
    time.sleep(1)
    print(item1, " costs ", i1p)
    time.sleep(1)
    print(item2, " costs ", i2p)
    time.sleep(1)
    print(item3, " costs ", i3p)
    time.sleep(1)
    print(item4, " costs ", i4p)
    time.sleep(1)
    print(item5, " costs ", i5p)
    time.sleep(1)
    print("Which one do you want to buy?")
    time.sleep(1)
    print("1. ", item1)
    print("2. ", item2)
    print("3. ", item3)
    print("4. ", item4)
    print("5. ", item5)
    print("6. Leave")
    print("Enter a number, eg. 1, 2, 3, 4, 5 or 6:")
    choice = input()

    if choice == "1":
        if gold >= i1p:
            gold -= i1p
            print("You bought ", item1, " for ", i1p, " gold.")
            inventory.append(item1)
            time.sleep(1)
        else:
            print("You don't have enough gold!")
            time.sleep(1)
            print("You have ", gold, " gold.")
            time.sleep(1)
    if choice == "2":
        if gold >= i2p:
            gold -= i2p
            print("You bought ", item2, " for ", i2p, " gold.")
            inventory.append(item2)
            time.sleep(1)
        else:
            print("You don't have enough gold!")
            time.sleep(1)
            print("You have ", gold, " gold.")
            time.sleep(1)
    if choice == "3":
        if gold >= i3p:
            gold -= i3p
            print("You bought ", item3, " for ", i3p, " gold.")
            inventory.append(item3)
            time.sleep(1)
        else:
            print("You don't have enough gold!")
            time.sleep(1)
            print("You have ", gold, " gold.")
            time.sleep(1)
    if choice == "4":
        if gold >= i4p:
            gold -= i4p
            print("You bought ", item4, " for ", i4p, " gold.")
            inventory.append(item4)
            time.sleep(1)
        else:
            print("You don't have enough gold!")
            time.sleep(1)
            print("You have ", gold, " gold.")
            time.sleep(1)
    if choice == "5":
        if gold >= i5p:
            gold -= i5p
            print("You bought ", item5, " for ", i5p, " gold.")
            inventory.append(item5)
            time.sleep(1)
        else:
            print("You don't have enough gold!")
            time.sleep(1)
            print("You have ", gold, " gold.")
            time.sleep(1)
    if choice == "6":
        print("You left the shop.")
        time.sleep(1)
    choice = chose

def add_to_inventory(item):
    global inventory
    global choice
    global chose
    chose = choice
    print("Would you like to add ", item, " to your inventory?")
    time.sleep(1)
    print("1. Yes")
    print("2. No")
    choice = input()
    if choice != "1" and choice != "2":
        print("Invalid choice.")
        exit()
    if choice == "1":
        inventory.append(item)
        print("You have added ", item, " to your inventory.")
        time.sleep(1)
    if choice == "2":
        print("You have not added ", item, " to your inventory.")
        time.sleep(1)

def message(msg):
    global choice
    global chose
    chose = choice
    print(msg)
    time.sleep(1)
    choice = chose

def choose_class(class1, class2, class3, class4, c1hp, c1mp, c1atk, c1def, c2hp, c2mp, c2atk, c2def, c3hp, c3mp, c3atk, c3def, c4hp, c4mp, c4atk, c4def):
    global chose
    global choice
    global hp
    global maxhp
    global mp
    global atk
    global defn
    global class_
    chose = choice
    print("Which class do you want to choose?")
    time.sleep(1)
    print("1. ", class1)
    print("2. ", class2)
    print("3. ", class3)
    print("4. ", class4)
    print("Enter a number, eg. 1, 2, 3, 4:")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("Invalid choice.")
        exit()
    if choice == "1":
        hp = c1hp
        maxhp = c1hp
        mp = c1mp
        atk = c1atk
        defn = c1def
        class_ = class1
        print("You chose ", class1, ".")
        time.sleep(1)
        print_stats()
        time.sleep(1)
    if choice == "2":
        hp = c2hp
        maxhp = c2hp
        mp = c2mp
        atk = c2atk
        defn = c2def
        class_ = class2
        print("You chose ", class2, ".")
        time.sleep(1)
        print_stats()
        time.sleep(1)
    if choice == "3":
        hp = c3hp
        maxhp = c3hp
        mp = c3mp
        atk = c3atk
        defn = c3def
        class_ = class3
        print("You chose ", class3, ".")
        time.sleep(1)
        print_stats()
        time.sleep(1)
    if choice == "4":
        hp = c4hp
        maxhp = c4hp
        mp = c4mp
        atk = c4atk
        defn = c4def
        class_ = class4
        print("You chose ", class4, ".")
        time.sleep(1)
        print_stats()
        time.sleep(1)
    choice = chose

def options_menu():
    global inventory
    global choice
    global chose
    global weapon_gear
    global armor_gear
    chose = choice
    print("What do you want to do?")
    time.sleep(1)
    print("1. Check your inventory")
    print("2. Check your stats")
    print("3. Check your equipment")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3":
        print("Invalid choice.")
        exit()
    if choice == "1":
        print("Your inventory contains:")
        for item in inventory:
            print(item)
        time.sleep(1)
    if choice == "2":
        print_stats()
        time.sleep(1)
    if choice == "3":
        print("Your weapon is ", weapon_gear, ".")
        time.sleep(1)
        print("Your armor is ", armor_gear, ".")
        time.sleep(1)
    choice = chose

def use_inventory_item(item):
    global hp
    global maxhp
    global mp
    global atk
    global defn
    global inventory
    global choice
    global chose
    chose = choice
    if item == "Potion":
        hp += 10
        if hp > maxhp:
            hp = maxhp
        print("You used a potion.")
        time.sleep(1)
        print("You have ", hp, " HP.")
        time.sleep(1)
        inventory.remove(item)
    if item == "Ether":
        atk += 1
        print("You used an ether.")
        time.sleep(1)
        print("You have ", atk, " ATK.")
        time.sleep(1)
        inventory.remove(item)
    if item == "Elixir":
        defn += 1
        print("You used an elixir.")
        time.sleep(1)
        print("You have ", defn, " DEFN.")
        time.sleep(1)
        inventory.remove(item)
    if item == "Phoenix Down":
        hp = maxhp
        mp += 3
        atk += 3
        defn += 3
        print("You used a phoenix down.")
        time.sleep(1)
        print("You have full HP, MP, ATK and DEFN.")
        time.sleep(1)
        inventory.remove(item)
    else:
        print("You can't use that item.")
        time.sleep(1)
    choice = chose

def upgrade_class(upgraded_class, ucHp, ucAtk, ucDefn, ucMp):
    global hp
    global maxhp
    global atk
    global defn
    global mp
    global class_
    global choice
    global chose
    chose = choice
    print("Do you want to upgrade your class from ", class_, " to ", upgraded_class, "?")
    time.sleep(1)
    print("1. Yes")
    print("2. No")
    choice = input()
    if choice != "1" and choice != "2":
        print("Invalid choice.")
        exit()
    if choice == "1":
        maxhp += ucHp
        hp = maxhp
        atk += ucAtk
        defn += ucDefn
        mp += ucMp
        class_ = upgraded_class
        print("You have upgraded your class to ", upgraded_class, ".")
        time.sleep(1)
        print_stats()
        time.sleep(1)
    if choice == "2":
        print("You have not upgraded your class.")
        time.sleep(1)
    choice = chose

def get_name():
    global name
    global choice
    global chose
    chose = choice
    print("What is your name?")
    choice = input()
    name = choice
    choice = chose

def inn(price):
    global hp
    global maxhp
    global choice 
    global chose
    chose = choice
    print("You have arrived at the inn.")
    time.sleep(1)
    print("The innkeeper says, 'Welcome to the inn, ", name, ".'")
    time.sleep(1)
    print("The innkeeper says, 'Do you want to stay for ", price, " gold?'")
    time.sleep(1)
    print("1. Yes")
    print("2. No")
    choice = input()
    if choice != "1" and choice != "2":
        print("Invalid choice.")
        exit()
    if choice == "1":
        print("The innkeeper says, 'Here you are, ", name, ".'")
        time.sleep(1)
        print("The innkeeper says, 'You have been healed for ", maxhp, " HP and your MP has been restored.'")
        time.sleep(1)
        hp = maxhp
        choice = "1"
    if choice == "2":
        print("The innkeeper says, 'Okay, come again when you are ready.'")
        time.sleep(1)

def trap(damage):
    global hp
    global maxhp
    global mp
    global atk
    global defn
    global choice
    global chose
    chose = choice
    print("You have encountered a trap.")
    time.sleep(1)
    print("The trap deals ", damage, " damage to you.")
    time.sleep(2)
    hp -= damage
    if hp <= 0:
        print("You have died.")
        time.sleep(1)
        exit()
    print("You have ", hp, " HP.")
    time.sleep(3)
    choice = chose
    
def npc(npc, dialogue):
    global choice
    global chose
    chose = choice
    time.sleep(2)
    print(npc, ": ", dialogue)
    time.sleep(2)
    choice = chose

# This is a list of all functions that can be used in the game.
# level_up()
# print_stats()
# gear("name", type [1 = armor, 2 = weapon], atkbuff, hpbuff, defbuff, mpbuff)
# battle("name", ehp, eatk, edefn, emp, expgain, goldgain, isboss)
# shop(item1, item2, item3, item4, item5, i1p, i2p, i3p, i4p, i5p)
# add_to_inventory(item)
# message(msg)
# choose_class(class1, class2, class3, class4, c1hp, c1mp, c1atk, c1def, c2hp, c2mp, c2atk, c2def, c3hp, c3mp, c3atk, c3def, c4hp, c4mp, c4atk, c4def)
# options_menu()
# use_inventory_item(item)
# upgrade_class(upgraded_class, ucHp, ucAtk, ucDefn, ucMp)
# get_name()
# inn(price)
# trap(damage)
# npc(npc, dialogue)

get_name()
choose_class("Warrior", "Mage", "Beserker", "Rouge", 15, 0, 8, 4, 13, 15, 2, 3, 10, 0, 12, 2, 11, 4, 6, 4)
npc("NPC", "Hello, I am an NPC.")