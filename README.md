# Ingredients calculator


## Contents

- [Ingredients calculator](#ingredients-calculator)
  - [Contents](#contents)
  - [Presentation](#presentation)
  - [Configure the meals file](#configure-the-meals-file)
  - [Requirements](#requirements)
  - [Run the program](#run-the-program)


<a name="Presentation"></a>
## Presentation

Do you know in advance what meals you want to cook this week? Then just feed the program with the names of those meals. You will be given the list of ingredients (with their quantities) you need to buy.  
  
For now, the instructions that the program displays are given in french. However, if the meals file is written in english, the meals and the list of needed ingredients will of course be displayed in english.  


<a name="ConfigureTheMealsFile"></a>
## Configure the meals file

The program takes in argument the name of the file that contains the selectable meals with their ingredients.
This file must be a YAML file and follow a specific syntax. An example file (`meals_and_ingredients.yaml`) is provided. The syntax is the following :

```yaml
- meal: the name of a meal
  ingredients:
    an ingredient:
      quantity: 3
      unit: kg
    another ingredient:
      quantity: 1
      unit: unit
- meal: the name of another meal
  ingredients:
    an ingredient:
      quantity: 2
      unit: kg
    yet another ingredient:
      quantity: 5
      unit: pinch
```

If some ingredient doesn't have a unit, then type `unit` in the `unit` field (as shown in the example above).  

Throughout the file, make sure that:
- a given ingredient or unit is always written the exact same way
    - example 1: `potatoe` & `potatoes` (with an 's') will be considered as two different ingredients
    - example 2: `teaspoon` & `teaspoons` (with an 's') too
- the quantity for an ingredient is always given in the exact same unit
    - example: using `kg` then `g` for `flour` won't work


<a name="Requirements"></a>
## Requirements

Install the requirements:

```sh
pip install -r requirements.txt
```

<a name="RunTheProgram"></a>
## Run the program

To run the program with the default file (you can replace it with any file), type:

```sh
python3 src/main.py meals.yaml
```