# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 07:48:47 2021

@author: lenovo
"""

brand  = {}

print(brand)

brand = {}
major_color = {
    "France" : "blue",
    "Spain" : "red",
    "US" : "pink, green"
  }
keys = ["name","creation_date","creator_name","type_of_clothes","international_competitors","number_stores","major_color"]
values = ["Zara", 1975, "Amancio Ortega Gaona",["men", "women", "children", "home"], ["Gap", "H&M", "Benetton"], 7000, major_color] 

for key, value in zip(keys,values):
    brand.update({key:value})

# Change the number of stores to 2.
brand.update({"number_stores": 2})

# Print a sentence that explains who Zaras clients are.
client = ''
for i in range(len(brand["type_of_clothes"])):
    client +=  brand["type_of_clothes"][i] + '\n'
print(f'The clients of {brand["name"]} are {client}')

# Add a key called country_creation with a value of Spain
brand.update({"country_creation":"Spain"})

# Check if the key international_competitors is in the dictionary.
if "international_competitors" in brand.keys():
    brand["international_competitors"].append("Desigual")
    
#  Delete the information about the date of creation.
brand.pop("creation_date")

# Print the last international competitor.
print(brand["international_competitors"][-1])

# Print the major clothes colors in the US.
clothes_US = ''
for clothes in range(len(brand["major_color"]["US"])):
    clothes_US += brand["major_color"]["US"][clothes]
print(clothes_US)

# Print the amount of key value pairs 
print(len(brand))

# Print the keys of the dictionary.
print(brand.keys())

more_on_zara  = {
    "creation_date": 1975,
    "number_stores": 10000
    }

brand.update({"more_on_zara": more_on_zara})

print(brand["number_stores"]) # he takes the first result