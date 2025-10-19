# Hanzi (kanji) phonetics research

### 1. Create python virtual environments (optional)
* #### Create
````
python3 -m venv venv
````
* #### Activate
````
source venv/bin/activate
````
* #### Deactivate
````
deactivate
````
### 2. Install requirements
````
pip install -r requirements.txt
````

### 3. Usage example
````
python3 phonetics.py 感
````
![漢字音符画像](/docs/sample_image.png?raw=true "漢字音符画像")

### 4. Phonetic Family Tree
Display complete phonetic family trees showing parent-child relationships between characters.

#### Usage
````python
from phonetic_tree import show_phonetic_family

# Show the complete family tree for a character
glyph = "𬩆"
tree = show_phonetic_family(glyph)
print(tree)
````

#### Example output:
````
𡿧(zāi) --
         |
         |災(zāi) --
         |         |
         |         |𨉒(?)
         |
         |甾(zī zāi) --
         |         |
         |         |淄(zī) --
         |         |         |
         |         |         |𬩆(?)
````

#### Run demo:
````
python3 demo_phonetic_tree.py
````

The function automatically:
- Finds the ancestor (root) of the entire family
- Builds a hierarchical tree structure
- Displays pinyin readings from `readings.csv`
- Uses a recursive algorithm to handle multi-level relationships


### Code style and test
* #### Sort the imports
````
isort .
````
* #### Format the code
````
black .
````
* #### Check the code
````
flake8 .
````
* #### Type checking
````
mypy .
````
* #### Unit tests
````
pytest
````
