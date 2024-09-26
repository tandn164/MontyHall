import random

try_count = 1000

def create_random_doors():
    items = ["car", "goat", "goat"]    
    random.shuffle(items)    
    doors = {i + 1: items[i] for i in range(3)}
    
    return doors

def select_door(doors, door_number, option):
    available_doors = [key for key in doors if key != door_number]
    if len(doors) > 2:
        # MC select
        goat_doors = [key for key in available_doors if doors[key] != "car"]
        random_door = random.choice(goat_doors)
        new_doors = {key: value for key, value in doors.items() if key != random_door}
        return select_door(new_doors, door_number, option)
    else:
        if (option == 1):
            # User change
            changed_door = random.choice(available_doors)
            if doors[changed_door] == 'car':
                return 1
            return 0
        if (option == 2):
            # Assumpt that we play again
            new_door = random.choice([key for key in doors])
            if doors[new_door] == 'car':
                return 1
            return 0

win = 0
for _ in range(try_count):
    win += select_door(create_random_doors(), random.randint(1, 3), 1)
print(win/try_count*100)

win = 0
for _ in range(try_count):
    win += select_door(create_random_doors(), random.randint(1, 3), 2)
print(win/try_count*100)