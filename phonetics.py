import csv
import sys
from prettytable import PrettyTable
ptable = PrettyTable()

args = sys.argv

def search_kanji(kanji):
    with open('phonetics.csv', encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj, delimiter=',')
        for line in reader:
            if kanji in str(line[0]):
                return line

def search_readings(kanji):
    with open('readings.csv', encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj, delimiter=',')
        for line in reader:
            if kanji in str(line[0]):
                return line

def search_phonetic(phonetic):
    res = []
    with open('phonetics.csv', encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj, delimiter=',')
        for line in reader:
            if phonetic in str(line[1]):
                res.append(line[0])
    return res

def search_group(kanji):
    kanji_list = [kanji] + search_phonetic(kanji)
    # res = []
    with open('readings.csv', encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj, delimiter=',')
        for line in reader:
            for kanji in kanji_list:
                if kanji in str(line[0]):
                    ptable.add_row(line)
                    # print(line)
                    # res.append(line)
    # return res

if(len(args) > 1):
    print(search_kanji(args[1]))
    # print(search_readings(args[1]))
    # print(search_phonetic(args[1])) 
    search_group(args[1])
    ptable.field_names = ['gliph', 'pin', 'cant', 'jp_on', 'jp_kun', 'kr', 'viet']
    ptable.del_column('jp_kun')
    ptable.sort_key([1,2])
    ptable.align = 'l'
    print(ptable)
else:
    print('argument requred')