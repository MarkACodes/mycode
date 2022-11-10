#!/usr/bin/env python3
# coding=utf-8

# pip install countryinfo if needed

from countryinfo import CountryInfo

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

def main():
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
main()

#using imported countryinfo module
#country
print("******************************************************************************************************")
print("GREAT! Now let's try a different way to find the capital of a country, any country, and way more info.")
print("******************************************************************************************************")
print()
country = input('Type in any country (even those not in provided list!) to see all information: ')
#capital
capital = CountryInfo(country).capital()
print(f'The capital of {country} is {capital}')
#alt spellings
alt_spellings = CountryInfo(country).alt_spellings()
print(f'The alt spellings of {country} are {alt_spellings}')
#borders
borders = CountryInfo(country).borders()
print(f'The borders of {country} are {borders}')
#population
population = CountryInfo(country).population()
print(f'The population of {country} is {population}')
#area
area = CountryInfo(country).area()
print(f'The area of {country} is {area}')
#languages
languages = CountryInfo(country).languages()
print(f'The languages of {country} are {languages}')


print("******************************************************************************************************")
print("Thank you for Playing!.")
print("******************************************************************************************************")


