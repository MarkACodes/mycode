#!/usr/bin/env python3


farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

def print_all_animals(farms):
    for farm in farms:
        for animal in farm["agriculture"]:
            print(animal)
            
# Call the function
print_all_animals(farms)


