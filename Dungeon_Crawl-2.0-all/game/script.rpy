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
        stage1=Stage([
            "111111111111111",
            "100000000100001",
            "100011000010001",
            "100011000000001",
            "100000000000101",
            "111111111111111",
            ],
            enemy)
            
    # The game starts here.
    
    # Place a player position on a dungeon stage (stage,y,x,dy,dx).
    # dx,dy means direction. If dy=1, it's down. If dx=-1, it's left.
    $ here=Coordinate(stage1,2,2,0,1) 
    
    # To start exploring, call or jump to the label dungeon. 
    call dungeon
    
    # To start battling, call the label battle with 2 actor objects: player and enemy.
    call battle(hero,enemy)