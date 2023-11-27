# Ingredients calculator

## Presentation

This program automates the process of making a food shopping list. Do you know in advance what meals you want to cook in this week? Then just feed the program with the names of those meals. You will be given the list of ingredients (with their quantities) you need to buy.  
  
For now, the program output is in french, meaning the instructions which the program displays while running are given in french. However, if the meals file is written in english, the meals and the list of needed ingredients will of course be displayed in english.  

## Meals file

The command needed to run the program takes one argument, which is the file that contains all meals the program will know the ingredients of. Any text file should work.  
  
A default file called `meals_and_ingredients.txt` is provided in this repository in order to illustrate the syntax that the program recognizes. The meals it contains can be removed, and new ones can be added. Alternatively, a completely new file can be created. The basic idea is to write the name of the meal followed by the ingredients (with their quantity)  
    
Use whatever names for meals, ingredients and units of measure: the program will automatically store them and keep them in memory while the it is running. Also, if some ingredient doesn't need a unit, then don't write any unit (for example "onions (2)").  
  
Throughout the file, make sure that:
- ingredients are always written the exact same way
    - example: 'potatoe' and 'potatoes' (with an 's') will be considered as two different ingredients
- quantity for an ingredient is always given in the exact same unit
    - example 1: writing 'kg' then 'g' won't work
    - example 2: writing 'teaspoon' then 'teaspoons' (with an 's') won't work
- decimal point quantities are written with a dot (like '0.5') and not a comma ('like '0,5')

## Run the program

Here is the command needed to run the program with the default file (you can replace it with any file):

```
$ python3 main.py meals_and_ingredients.txt
```