import csv
import sys

from prettytable import PrettyTable

ptable = PrettyTable()

args = sys.argv

readings_path = 'data/readings.csv'
phonetics_path = 'data/phonetics.csv'

def search_pair(glyph):
  with open(phonetics_path, encoding='utf-8') as f_obj:
    reader = csv.reader(f_obj, delimiter=',')
    for line in reader:
        if glyph in str(line[0]):
          return line

def search_readings(glyph):
  with open(readings_path, encoding='utf-8') as f_obj:
      reader = csv.reader(f_obj, delimiter=',')
      for line in reader:
        if glyph in str(line[0]):
          return line

def search_glyph_list(phonetic):
  res = []
  with open(phonetics_path, encoding='utf-8') as f_obj:
    reader = csv.reader(f_obj, delimiter=',')
    for line in reader:
      if phonetic in str(line[1]):
        res.append(line[0])
    return res

def search_glyph_family(glyph):
  sym = glyph
  res = [glyph]
  while (True):
    phonetic = search_pair(sym)
    if phonetic:
      sym = phonetic[1]
      res.append(sym)
    else:
      break
    return res

def search_group(kanji):
  glyph_list = [kanji] + search_glyph_list(kanji)
  res = []
  with open(readings_path, encoding='utf-8') as f_obj:
    reader = csv.reader(f_obj, delimiter=',')
    for line in reader:
      for glyph in glyph_list:
        if glyph in str(line[0]):
          res.append(line)
    return res

if (len(args) > 1):
  family = search_glyph_family(args[1])
  print('phonetic family: ', family)
  for phonetic in family[:-1]:
    ptable.add_rows(search_group(phonetic))
    ptable.field_names = ['glyph', 'pin',
                          'cant', 'on', 'kun', 'kr', 'viet']
    ptable.del_column('kun')
    ptable.sort_key([1, 2])
    ptable.align = 'l'
    print(phonetic)
    print(ptable)
    ptable.clear()
else:
    print('argument required')
