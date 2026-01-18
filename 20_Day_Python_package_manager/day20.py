import requests
import statistics
def most_frequent_words (url):
    response = requests.get(url)
    # print (response)
    # print (response.status_code)
    # print (type(response.text))
    # print (response.json)
    lst = response.text.split()
    dt = {}
    for i in lst:
        dt[i] = dt.get(i,0) +1
    lst = [(index,value) for value, index in dt.items()]
    lst_sorted = sorted (lst, key = lambda x:x[0], reverse = True)
    return (lst_sorted[0:10])
print(most_frequent_words('http://www.gutenberg.org/files/1112/1112.txt'))

def weight_compute (url):
    response = requests.get(url)
    js = response.json()
    dt = {}
    for i in js:
        lst = i['weight']['metric'].split()
        lst.remove('-')
        lst_int = [int (j) for j in lst]
        dt[i['name']] = (min(lst_int),max(lst_int),statistics.median(lst_int),statistics.stdev(lst_int) )
    res = [{'name': key,'min': value[0],'max': value[1], 'median': value[2], 'sd':value[3]} for key,value in dt.items()]
    return (res)
print (weight_compute('https://api.thecatapi.com/v1/breeds'))
def lifespan_compute (url):
    response = requests.get(url)
    js = response.json()
    dt = {}
    for i in js:
        lst = i['life_span'].split()
        lst.remove('-')
        lst_int = [int (j) for j in lst]
        dt[i['name']] = (min(lst_int),max(lst_int),statistics.median(lst_int),statistics.stdev(lst_int) )
    res = [{'name': key,'min': value[0],'max': value[1], 'median': value[2], 'sd':value[3]} for key,value in dt.items()]
    return (res)
print (lifespan_compute('https://api.thecatapi.com/v1/breeds'))