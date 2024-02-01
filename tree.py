import csv
import sys

from rich import print
from rich.tree import Tree

args = sys.argv

if len(args) == 1:
    print("argument required")
    exit(0)
else:
    input_glyph = args[1]

phonetics_path = "data/glyphs.csv"


def find_parent_phonetic(glyph):
    with open(phonetics_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            if row[0] == glyph:
                return row[2]
        return None


phonetic = find_parent_phonetic(input_glyph)

if phonetic is None:
    print("Data not founded")
    exit(0)


def find_phonetics(unphonetics, phonetic):
    result = {}
    temp_unph = unphonetics.get(phonetic)
    if temp_unph is None:
        return result
    else:
        for sub_unph in temp_unph:
            result[sub_unph] = find_phonetics(unphonetics, sub_unph)
    return result


with open(phonetics_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=",")
    phonetics_full_revers = {}
    count = 0
    for row in reader:
        if count > 0:
            if phonetics_full_revers.get(row[1]) is None:
                phonetics_full_revers[row[1]] = row[0]
            elif row[1] != "0":
                phonetics_full_revers[row[1]] = (
                    phonetics_full_revers.pop(row[1]) + row[0]
                )
        count += 1
    phonetic_tree = {phonetic: find_phonetics(phonetics_full_revers, phonetic)}


def make_tree(node, tree):
    for child in node.keys():
        branch = tree.add(child)
        make_tree(node[child], branch)


tree = Tree(phonetic)
make_tree(phonetic_tree[phonetic], tree)
print(tree)
