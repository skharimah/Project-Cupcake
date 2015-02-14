# This file is in the public domain.
label start:
  
    # Initializing data
    python:
        
        import random  
      # Create skills (name, type, hit, power)
        attack = Skill("Attack", "attack", 100, 40)
        escape = Skill("Escape", "escape")
        
        # Create battle actors (name, max_hp, skills)
        hero = Actor("Hero",1000, [attack,escape])
        goblin = Actor("Goblin",20, [attack])
        fireSprite = Actor("Fire Sprite",50, [attack])
        orc = Actor("Joseph", 40, [attack])
        dog = Actor("Stephen", 5, [escape])
        adorableKitten = Actor("Feline",1,[attack])


        enemySet = [goblin, fireSprite, orc, dog]
        enemy = random.choice(enemySet)
        # Create a dungeon stage (map,enemy)
        # "1" means wall, "0" means path.
        #create random dungeon
        array = [0,1]
        array1 = [1]
        array2 = [1]
        array3 = [1]
        array4 = [1]
        array5 = [1]
        array6 = [1]
        array7 = [1]
        array8 = [1]
        array9 = [1]
        array10 = [1]

        for y in range(1,21):
            number = random.choice(array)
            array1.append(number)
            number = random.choice(array)
            array2.append(number)
            number = random.choice(array)
            array3.append(number)
            number = random.choice(array)
            array4.append(number)
            number = random.choice(array)
            array5.append(number)
            number = random.choice(array)
            array6.append(number)
            number = random.choice(array)
            array7.append(number)
            number = random.choice(array)
            array8.append(number)
            number = random.choice(array)
            array9.append(number)
            number = random.choice(array)
            array10.append(number)
            number = random.choice(array)

        array1.append(1)
        array2.append(1)
        array3.append(1)
        array4.append(1)
        array5.append(1)
        array6.append(1)
        array7.append(1)
        array8.append(1)
        array9.append(1)
        array10.append(1)

        array1 = map(str,array1)
        array2 = map(str,array2)
        array3 = map(str,array3)
        array4 = map(str,array4)
        array5 = map(str,array5)
        array6 = map(str,array6)
        array7 = map(str,array7)
        array8 = map(str,array8)
        array9 = map(str,array9)
        array10 = map(str,array10)

        arrayStageTest = [
            "1111111111111111111111",
            array1,
            array2,
            array3,
            array4,
            array5,
            array6,
            array7,
            array8,
            array9,
            array10,
            "1111111111111111111111"
            ]

        arrayStage = [
            "111111111111111",
            "100000000100001",
            "100011000010001",
            "100011000000001",
            "100000000000101",
            "111111111111111",
            ]
        stage1=Stage(arrayStageTest,
            enemy)
            
    # The game starts here.
    
    # Place a player position on a dungeon stage (stage,y,x,dy,dx).
    # dx,dy means direction. If dy=1, it's down. If dx=-1, it's left.
    $ here=Coordinate(stage1,2,2,0,1) 
    
    # To start exploring, call or jump to the label dungeon. 
    call dungeon
    
    # To start battling, call the label battle with 2 actor objects: player and enemy.
    call battle(hero,enemy)
