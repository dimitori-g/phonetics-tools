import csv
import sys

from prettytable import PrettyTable

ptable = PrettyTable()

args = sys.argv

def search_kanji(kanji):
    with open('data/phonetics.csv', encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj, delimiter=',')
        for line in reader:
            if kanji in str(line[0]):
                return line

def search_readings(kanji):
    with open('data/readings.csv', encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj, delimiter=',')
        for line in reader:
            if kanji in str(line[0]):
                return line

def search_phonetic(phonetic):
    res = []
    with open('data/phonetics.csv', encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj, delimiter=',')
        for line in reader:
            if phonetic in str(line[1]):
                res.append(line[0])
    return res

def search_family(kanji):
  sym = kanji
  res = [kanji]
  while(True):
    phonetic = search_kanji(sym)
    if phonetic:
      sym = phonetic[1]
      res.append(sym)
    else:
      break
  return res

def search_group(kanji):
    kanji_list = [kanji] + search_phonetic(kanji)
    res = []
    with open('data/readings.csv', encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj, delimiter=',')
        for line in reader:
            for kanji in kanji_list:
                if kanji in str(line[0]):
                    res.append(line)
    return res

if (len(args) > 1):
    family = search_family(args[1])
    print('phonetic family: ', family)
    for phonetic in family[:-1]:
      ptable.add_rows(search_group(phonetic))
      ptable.field_names = ['glyph', 'pin', 'cant', 'on', 'kun', 'kr', 'viet']
      ptable.del_column('kun')
      ptable.sort_key([1, 2])
      ptable.align = 'l'
      print(phonetic)
      print(ptable)
      ptable.clear()
else:
    print('argument required')
