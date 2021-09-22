'''
1. Выполните задание уровня ultra light
2. Создайте csv-файл с данными о машине.
3. Создайте json-файл с данными о машине.
'''
import csv
import json

def getContext( data ):
    rez=[]
    dic = {
        'model': '',
        'volume': '',
        'type': '',
        'power': '',
        'transmission': '',
        'ntransmission': '',
        'drive': '',
        'body': '',
        'country': ''
    }
    i = 0
    with open( data, 'r', encoding='utf8' )  as  f:
        s = f.read()
        lst = s.split('\n')

    for v in dic.keys():
        d = {'character':v, 'val':lst[i] }
        rez.append( d )
        dic[v] = lst[i]
        i += 1

    return rez, dic


lst, dic = getContext(  'dataauto.txt')   # lst для CSV, dic для JSON

#print( lst )

#*********************************************************************** CSV
namField = ['character', 'val']

with open( 'auto.csv','w', newline='', encoding='utf8' ) as f:
    w = csv.DictWriter( f, delimiter=',', fieldnames=namField )
    w.writeheader()

    w.writerows( lst )
    # или
    # for i in range(len(lst)):
    #     w.writerow( lst[i] )
    #     print( lst[i])

#******************************************************* JSON
with open(  'auto.json', 'w', encoding='utf8' )  as f:
    json.dump( dic, f , ensure_ascii=False)   # ensure_ascii=False - для запрета экранирования символов не ASCII