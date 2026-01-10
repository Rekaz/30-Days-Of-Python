numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_zero = [x for x in numbers if x<=0]
print (neg_zero)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat = [num for lst in list_of_lists for l in lst for num in l]
print (flat)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
def data_tuple (country):
    lst = []
    c, city = country
    lst.append (str(c).upper())
    lst.append (str(c[0:3]).upper())
    lst.append (str(city).upper())
    return lst
segregate = [data_tuple(country) for lst in countries for country in lst]
print (segregate)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
def change_to_dict(tup):
    d ={}
    country, city = tup
    d["country"] = str(country).upper()
    d["city"] = str(city).upper()
    return d
flat = [change_to_dict(tup) for lst in countries for tup in lst]
print (flat)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

def constr (tup):
    first, last = tup
    st = str(first) + " " + str(last)    
    return st
concat = [constr(tup) for lst in names for tup in lst]
print (concat)

slope = lambda m,x,c: m*x +c
print (slope(2,2,3))