from random import *
import random
import string

def random_user_id(num):
    chars = string.ascii_letters + string.digits
    result = ''.join(random.choice(chars) for i in range(num))
    return (result)
print(random_user_id(6))


def user_id_gen_by_user():
    a = input ('enter no of characters: ')
    b = input ('no of IDs: ')
    res = []
    for i in range(int (b)):
        res.append(random_user_id(int(a)))
    return (res)
print (user_id_gen_by_user())

def rgb_color_gen():
    res = []
    for i in range(3):
        res.append(randint(100,999))
    return (res)
print (rgb_color_gen())

def list_of_hexa_colors(num):
    res = []
    hex = "abcdef0123456789"
    for i in range(num):
        res.append ("#"+"".join(random.choice(hex) for j in range(6)))
    # print (string.ascii_letters(2))
    return (res)
print (list_of_hexa_colors(3))

def list_of_rgb_colors (num):
    res = []
    for i in range(num):
        res.append(randint(100,999))
    return (res)
print (list_of_rgb_colors(3))

def generate_colors (type,num):
    if type == 'hexa':
        return (list_of_hexa_colors(num))
    if type == 'rgb':
        return (list_of_rgb_colors(num))
print(generate_colors('hexa', 3)) 
print (generate_colors('hexa', 1))
print (generate_colors('rgb', 3)) 
print (generate_colors('rgb', 1))

def shuffle_list (lst):
    random.shuffle(lst)
    return (lst)
print (shuffle_list([1, 2, 3, 4, 5]))

def rand():
    res = []
    res.append (randint(0,9))
    i = 1
    while i < 7:
        new = randint (0,9)
        if new not in res:
            res.append (new)
            i +=1
        else: 
            continue
    return (res)
print (rand())