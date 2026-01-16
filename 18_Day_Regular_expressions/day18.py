import re
import keyword
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
reg = r'[.*]'
clean_para = re.sub(reg, '',paragraph)
print (clean_para)
words = clean_para.split()
d = {}
for word in words:
    d[word] = d.get (word,0) +1
print (d)
lst = [(index, word) for word, index in d.items()]
lst_sorted = sorted(lst,key = lambda x: x[0], reverse=True)
print (lst_sorted)

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
points_int = [int(point) for point in points]
points_int_sort = sorted(points_int)
distance = points_int_sort[len(points_int_sort)-1]-points_int_sort[0]
print (f"distance = {distance}")

def is_valid_variable(var):
    reg = r'^[a-zA-Z_][a-zA-Z0-9]*$'
    if re.match(reg,var):
        print("True")
    else:
        print("False")
is_valid_variable('f3232') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True

def clean_text(sentence):
    reg = r'[^a-zA-Z ]*'
    sentence = re.sub(reg,'',sentence)
    return sentence
def most_frequent_words(cleaned_text):
    words = cleaned_text.split()
    dt = {}
    for word in words:
        dt[word] = dt.get(word,0) + 1
    lst = [(index,word) for word, index in dt.items()]
    sorted_lst = sorted (lst, key = lambda x:x[0], reverse=True)
    return (sorted_lst[0:3])
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
print(clean_text(sentence))
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
cleaned_text = clean_text(sentence)
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]