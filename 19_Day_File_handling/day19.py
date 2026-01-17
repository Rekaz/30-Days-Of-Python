import json
import re
from data.stop_words import stop_words
import csv
# import data.stop_words
with open ("data\obama_speech.txt", mode = 'r') as f:
    lst_lines = f.readlines()
    print (len(lst_lines))
    count = 0
    for line in lst_lines:
        words = line.split()
        count += len(words)
    print (count)
    
with open ("data\michelle_obama_speech.txt", mode = 'r') as f:
    lst_lines = f.readlines()
    print (len(lst_lines))
    count = 0
    for line in lst_lines:
        words = line.split()
        count += len(words)
    print (count)

with open ("data\donald_speech.txt", mode = 'r') as f:
    lst_lines = f.readlines()
    print (len(lst_lines))
    count = 0
    for line in lst_lines:
        words = line.split()
        count += len(words)
    print (count)

with open ("data\melina_trump_speech.txt", mode = 'r') as f:
    lst_lines = f.readlines()
    print (len(lst_lines))
    count = 0
    for line in lst_lines:
        words = line.split()
        count += len(words)
    print (count)
    
def most_spoken_languages (filename, top):
    with open (filename, mode = 'r',encoding='utf-8') as f:
        dtry = json.loads(f.read())
        d_lang = {}
        for item in dtry:
            for i in item['languages']:
                    d_lang[i] = d_lang.get (i,0)+1
        list_lang = [(index, item) for item, index in d_lang.items()]
        list_lang_sorted = sorted(list_lang, key = lambda x: x[0], reverse = True)
        return (list_lang_sorted[0:top])
print(most_spoken_languages(filename='./data/countries_data.json',top= 10))  
print(most_spoken_languages(filename='./data/countries_data.json', top=3))  

def most_populated_countries (filename, top):
    with open (filename,mode = 'r', encoding='utf-8') as f:
        dt = json.loads(f.read())
        res = {}
        for item in dt:
            # res ['country'] = item['name']
            # res ['population'] = item ['population'] 
            res [item['name']] = item ['population'] 
        res_lst = [{"country": country,"population":population} for country,population in res.items()]
        res_lst_sorted = sorted(res_lst, key = lambda x:x['population'], reverse= True)
        return (res_lst_sorted[0:top])  
print(most_populated_countries(filename='./data/countries_data.json', top = 10)) 
print(most_populated_countries(filename='./data/countries_data.json',top= 3)) 

def find_most_common_words(filename, top):
    with open (filename, mode = 'r', encoding = 'utf-8')  as f:
        lines = f.readlines()
        dt = {}
        for line in lines:
            words = line.split()
            for word in words:
                dt[word] = dt.get(word,0) +1
        lst = [(value, word) for word, value in dt.items()]
        lst_sorted = sorted (lst, key = lambda x:x[0], reverse=True)
        return (lst_sorted[0:top])
print(find_most_common_words('data\obama_speech.txt', 10))  
print(find_most_common_words('data\michelle_obama_speech.txt', 10))
print(find_most_common_words('data\donald_speech.txt', 10))
print(find_most_common_words('data\melina_trump_speech.txt', 10))

def clean_text (filename):
    with open (filename, mode = 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
        reg = r'[^a-zA-Z0-9 ]'
        clean_text = [re.sub (reg,'',line) for line in lines]
        return (clean_text)
def support_words_rm (lst):
        lst_rm_support_word = []
        for line in lst:
            filter_words = [word for word in line.split() if word not in stop_words]
            lst_rm_support_word.append(' '.join(filter_words))
        # print (lst_rm_support_word)
        return (lst_rm_support_word) 
# def check_text_similarity(rm_support):
     
clean_michelle = clean_text("data\michelle_obama_speech.txt")
clean_melina = clean_text("data\melina_trump_speech.txt")
rm_support_melina = support_words_rm(clean_melina)
rm_support_michelle = support_words_rm(clean_michelle)

print (find_most_common_words('data/romeo_and_juliet.txt',10))

def count_lines (*args):
    with open ('data\hacker_news.csv') as f:
        csv_reader = csv.reader (f, delimiter=',')
        line_count = 0 
        for row in csv_reader:
            for words in row:
                word_lst = words.split()
                for arg in args:
                    if arg in word_lst:
                        line_count+=1
        return (line_count)
print (count_lines('python','Python'))
print (count_lines('JavaScript','javascript','Javascript'))
print (count_lines('Java'))