
cities = {
    'Singapore' : {
        'country' : 'Singapore',
        'population' : '5.541 million',
        'fact' : 'Locals speak singlish not english',
    },
    'Los Angeles' : {
        'country' : 'United States',
        'population' : '3.849 million',
        'fact' : 'Los Angeles hosted the olympics twice',
    },
    'Frankfurt' : {
        'country' : 'Germany',
        'population' : '753,056',
        'fact' : "It's called Mainhattan",
    },
}

for city, city_info in cities.items():
    print(f"{city} is located in {city_info['country']}.\nIt has a population of {city_info['population']} people and {city_info['fact']}.\n")