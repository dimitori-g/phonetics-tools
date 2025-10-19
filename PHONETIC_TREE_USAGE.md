# Phonetic Family Tree Function

## Overview

The `show_phonetic_family()` function displays complete phonetic family trees for Chinese characters, showing parent-child relationships in a hierarchical tree structure.

## Files Created

1. **phonetic_tree.py** - Main module with the tree generation functionality
2. **demo_phonetic_tree.py** - Demonstration script with usage examples
3. **Updated README.md** - Added documentation section

## How It Works

### Algorithm

1. **Find Ancestor**: Starting from any glyph in a family, traverse up the parent chain to find the root ancestor (the character with `0` as parent)

2. **Build Children Map**: Create a reverse mapping from parents to their children from the `phonetics.csv` file

3. **Recursive Tree Rendering**: Recursively render the tree starting from the ancestor, showing all descendants with proper indentation and visual connectors

4. **Reading Integration**: Load pinyin readings from `readings.csv` and display them in parentheses next to each character

### Data Structure

The function uses two CSV files:

**phonetics.csv** format:
```
glyph,phonetic
𬩆,淄
淄,甾
甾,𡿧
𡿧,0
```

**readings.csv** format:
```
glyph,pinyin,cantonese,on,kun,korean,vietnamese
淄,zī,zi1,SHI,,치,
```

## Usage Examples

### Basic Usage

```python
from phonetic_tree import show_phonetic_family

# Display family tree for any character
tree = show_phonetic_family("𬩆")
print(tree)
```

### With Custom File Paths

```python
tree = show_phonetic_family(
    "甾",
    phonetics_file="data/phonetics.csv",
    readings_file="data/readings.csv"
)
print(tree)
```

### Interactive Usage

```python
# Get user input
glyph = input("Enter a Chinese character: ")
tree = show_phonetic_family(glyph)
print(f"\nPhonetic family tree for '{glyph}':\n")
print(tree)
```

## Output Format

The tree uses the following visual elements:

- `--` indicates a character has children
- `|` shows vertical connections between levels
- Indentation (9 spaces per level) shows hierarchy
- `(?)` indicates no reading found in the database
- Multiple readings are shown separated by spaces

Example output:
```
𡿧(zāi) --
         |
         |災(zāi) --
         |         |
         |         |𨉒(?)
         |         |
         |         |𨓌(?)
         |
         |甾(zī zāi) --
         |         |
         |         |淄(zī) --
         |         |         |
         |         |         |𬩆(?)
```

## Key Features

1. **Automatic Ancestor Detection**: No matter which character you query, the function finds and displays the entire family from the root

2. **Recursive Processing**: Handles multi-level hierarchies of any depth

3. **Sorted Output**: Children are displayed in sorted order for consistency

4. **Circular Reference Protection**: Detects and handles circular references gracefully

5. **Missing Data Handling**: Shows `?` for characters without readings

## Function Reference

### `show_phonetic_family(glyph, phonetics_file='data/phonetics.csv', readings_file='data/readings.csv')`

**Parameters:**
- `glyph` (str): The Chinese character to show the family tree for
- `phonetics_file` (str, optional): Path to the phonetics CSV file
- `readings_file` (str, optional): Path to the readings CSV file

**Returns:**
- `str`: A formatted string representation of the family tree

**Raises:**
- Returns error message if glyph not found in phonetics data

### Helper Functions

- `load_phonetics(filepath)`: Load glyph-parent relationships
- `load_readings(filepath)`: Load pinyin readings
- `find_ancestor(glyph, phonetics)`: Find root ancestor
- `build_children_map(phonetics)`: Build parent-to-children mapping
- `render_tree(glyph, readings, children_map, prefix, is_root)`: Recursively render tree

## Running the Demo

```bash
python3 demo_phonetic_tree.py
```

This will show multiple examples demonstrating different use cases.

## Integration with Existing Code

The function is standalone and can be imported into other scripts:

```python
# In your script
from phonetic_tree import show_phonetic_family

# Use it
result = show_phonetic_family("你的字")
```

## Performance Notes

- First call loads the CSV files (~41K entries in phonetics, ~93K in readings)
- Subsequent trees can reuse loaded data by calling helper functions directly
- Tree rendering is O(n) where n is the number of descendants

## Future Enhancements

Possible improvements:
- Cache CSV data for better performance with multiple queries
- Add support for other reading types (cantonese, on, kun, etc.)
- Export trees to different formats (JSON, XML, SVG)
- Add filtering options (max depth, specific branches)
- Interactive web interface

