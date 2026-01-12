import sys
print(sys.path)
import os
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "countries_data.json")

from functools import reduce
from data.countries import countries as cd
with open(file_path, "r", encoding="utf-8") as f:
    countries1 = json.load(f)
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s = """
map: it takes two parameters, function and iterable and it iterates over the items in parallel and returns an iterable.
filter: it takes function and iterable, and it returns boolean value for each item of iterable. it is used to filter the objects based on filtering criteria.
reduce: it takes two parameters, function and iterable but it doesn't return iterable, it returns a single value
""" 
print (s)

s = """
higher order function: there are few conditions: 
    1. it can takes multiple functions as parameter
    2. it can return a function 
    3. enhances the functionality of a function
    4. assign a function to a variable
    
closure: a nested function can have the access to the outer scope of enclosing function.

decorators: a decorator is used to enhance the functionality of the base function. The base function goes as a parameter to the decorator function.  
"""
print (s)

m = map (lambda x: x*x, numbers)
print (list (m))

def long_names (name):
    if len (name) > 7:
        return True
    else:
        return False
f = filter (long_names, names )
print (list(f))

f_lambda = filter (lambda c: len(c)>7, names)
print (list (f_lambda))

def add_two_nums (x,y):
    return int(x) + int (y)
total = reduce (add_two_nums, numbers)
print(total)

for c in countries:
    print (c)
for n in names:
    print (n)
for no in numbers:
    print (no)

c_upper = map (lambda x: x.upper(), countries)
print (list(c_upper))

n_square = map (lambda x: x*x, numbers)
print (list(n_square))

n_upper = map (lambda  n: n.upper(), names)
print (list (n_upper))

f_land = filter (lambda country: 'land' in country, countries)
print (list (f_land))

f_6_char = filter (lambda country: len(country)==6, countries)
print (list (f_6_char))

f_6_more = filter (lambda country: len(country) >=6, countries)
print (list(f_6_more))

f_start_e = filter (lambda country: country.startswith('E'),countries)
print (list (f_start_e))

map_filter = map(lambda x: x.upper(),filter(lambda country: 'land' in country,countries))
print (list(map_filter)) 

lst = [1,2,"dfsd","dfvgfg",23,23.45]
f_str_lst = filter (lambda x: isinstance(x,str),lst)
print (list(f_str_lst))

red_sum = reduce (lambda x,y: x+y, numbers)
print (red_sum)

concat_red = reduce (lambda x,y: f"{x}, {y}", countries[:-1]) + f" and {countries[-1]} are north European countries"
print (concat_red)

cat_country_land = filter (lambda x: 'land' in x,cd)
print (list (cat_country_land))

def categorize_countries (pattern):
    return list (filter (lambda x: pattern.lower() in x.lower(), cd))
print (categorize_countries("land"))
print (categorize_countries("ia"))
print (categorize_countries("island"))
print (categorize_countries("stan"))

def dic_country (character):
    c = 0
    return list (filter (lambda x: x.lower().startswith(character)  ,cd))
s = "abcdefghijklmnopqrstuvwxyz"
for i in s:
    print (dic_country(i))

count_countries_by_starting_letter = lambda cd: {
    letter: list(map(lambda c: c[0].upper(), cd)).count(letter)
    for letter in set(map(lambda c: c[0].upper(), cd))
}
print(count_countries_by_starting_letter(cd))


def get_first_ten_countries():
    return list (map(lambda x: x['name'], countries1[:10]))
print (get_first_ten_countries())

def get_last_ten_countries():
    return list (map(lambda x: x['name'], countries1[-10:]))
print (get_last_ten_countries())

get_country_by_name = list(map (lambda x:x['name'],countries1))
get_country_by_name_sorted = sorted(get_country_by_name)
dic_get_country_by_name_sorted = []
for i in get_country_by_name_sorted:
    for c in countries1:
    
        if i == c['name']:
            dic_get_country_by_name_sorted.append(c)
print (dic_get_country_by_name_sorted)

get_capital_by_name = list(map (lambda x:x['capital'],countries1))
get_capital_by_name_sorted = sorted(get_capital_by_name)
dic_get_capital_by_name_sorted = []
for i in get_capital_by_name_sorted:
    for c in countries1:
    
        if i == c['capital']:
            dic_get_capital_by_name_sorted.append(c)
print (dic_get_capital_by_name_sorted)

get_country_by_population = list(map (lambda x:x['population'],countries1))
get_country_by_population_sorted = sorted(get_country_by_population)
dic_get_country_by_population_sorted = []
for i in get_country_by_population_sorted:
    for c in countries1:    
        if i == c['population']:
            dic_get_country_by_population_sorted.append(c)
print (dic_get_country_by_population_sorted)

def msl (lst):
    d = {}
    for l in lst:
        if l not in d:
            # count = 0
            d[l] = 1
        else:
            d[l] += 1
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return(list(sorted_dict)[:10])
    
most_spoken_language =  [lst for c in countries1 for lst in c['languages']]
print (msl(most_spoken_language))