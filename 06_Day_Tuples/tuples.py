empty_tuple = ()
tpl = ("sister","brother")

brother_tpl = ("bro1","bro2")
sister_tpl = ("sis1","sis2")
siblings = brother_tpl + sister_tpl
print (len(siblings))

family_members = list(siblings)
family_members.append("father")
family_members.append("mother")
family_members = tuple(family_members)

print (family_members)

siblings = family_members[0:4]
parents = family_members[4:]

fruits = ("apple","banana")
vegetables = ("tomato","onion")
animal_products = ("milk","eggs")
food_stuff_tp = fruits + vegetables + animal_products

food_stuff_lt = list (food_stuff_tp)
print (food_stuff_lt)

if len(food_stuff_lt)%2 == 1:
    print (food_stuff_lt[len(food_stuff_lt)//2])
else:
    print (food_stuff_lt[(len(food_stuff_lt)//2)-1:(len(food_stuff_lt)//2)+1])

    
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-3:]
print (first_three)
print (last_three)

del (food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print ('Estonia' in nordic_countries)
print ('Iceland' in nordic_countries)
