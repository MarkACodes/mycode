#!/usr/bin/env python3


countries = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "China": "Beijing",
    "Japan": "Tokyo",
    "India": "New Delhi",
    "Australia": "Canberra",
    "South Africa": "Pretoria",
    "Egypt": "Cairo",
    "Greece": "Athens",
    "Iceland": "Reykjavik",
    "Norway": "Oslo",
    "Sweden": "Stockholm",
    "Finland": "Helsinki",
    "Denmark": "Copenhagen",
    "Ireland": "Dublin",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Switzerland": "Bern",
    "Austria": "Vienna",
    "Poland": "Warsaw",
    "Czech Republic": "Prague",
    "Slovakia": "Bratislava",
    "Hungary": "Budapest",
    "Slovenia": "Ljubljana",
    "Croatia": "Zagreb",
    "Serbia": "Belgrade",
    "Bosnia and Herzegovina": "Sarajevo",
    "Macedonia": "Skopje",
    "Albania": "Tirana",
    "Montenegro": "Podgorica",
}

# create a welcome message
print("Welcome to the Capital of the World program.")

# Game loop:
while True:
    # add a number to each country in dictionary
    for i, country in enumerate(countries):
        # print the number and country
        print(f"{i + 1}. {country}")
    # prompt user for country
    country = input("Please enter a number from the list above to see the capital of the country: ")
    print()
    # check if country is in dictionary
    if int(country) in range(1, len(countries) + 1):
        print(f"The capital of {list(countries.keys())[int(country) - 1]} is {list(countries.values())[int(country) - 1]}.")
        print()
        break
    else:
        country = input("Please enter a VALID number from list provided: ")
        if int(country) in range(1, len(countries) + 1):
            print(f"The capital of {list(countries.keys())[int(country) - 1]} is {list(countries.values())[int(country) - 1]}.")
            print()
            break
        else:
            print("You have entered an invalid number. Goodbye.")
            # ask if user wants to play again
            if input("Would you like to play again (y/n)? ").lower() == "n":
                print("Thanks for playing the Capital of the World program. Goodbye.")
                break
