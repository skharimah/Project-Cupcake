# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
# The game starts here.

### Choice menu ###
label start:
    "A monster appeared!"
    menu:
     "What should I do?"

     "Drink coffee.":
         "I drink the coffee, and it's good to the last drop."

     "Drink tea.":
         $ drank_tea = True

         "I drink the tea, trying not to make a political statement as I do."

     "Genuflect.":
         jump after_menu

label after_menu:
    "After having my drink, I got on with my morning."

### Prompt user-typed input ###
define mainChar = Character("[charName]")
python:
    charName = renpy.input("What's your name?")
    charName = charName.strip()
    if not charName:
        charName = "John Smith"
mainChar "My name is [charName]!"
