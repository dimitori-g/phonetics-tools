import csv
import sys
from typing import Dict, List


def load_phonetics(filepath: str = "data/phonetics.csv") -> Dict[str, str]:
    """
    Load phonetic relationships from CSV file.
    Returns a dictionary mapping glyph -> parent phonetic.
    """
    phonetics = {}
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            glyph = row["glyph"]
            phonetic = row["phonetic"]
            phonetics[glyph] = phonetic
    return phonetics


def load_readings(filepath: str = "data/readings.csv") -> Dict[str, str]:
    """
    Load pinyin readings from CSV file.
    Returns a dictionary mapping glyph -> pinyin reading.
    """
    readings = {}
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            glyph = row["glyph"]
            pinyin = row["pinyin"].strip()
            if pinyin:
                readings[glyph] = pinyin
    return readings


def find_ancestor(glyph: str, phonetics: Dict[str, str]) -> str:
    """
    Find the root ancestor of a glyph by traversing up the parent chain.
    Returns the ancestor glyph (the one with '0' or '1' as parent).
    """
    current = glyph
    visited = set()

    # Traverse up the parent chain
    while current in phonetics and phonetics[current] not in ("0", "1"):
        if current in visited:
            # Circular reference, return current
            return current
        visited.add(current)
        current = phonetics[current]

    return current


def build_children_map(phonetics: Dict[str, str]) -> Dict[str, List[str]]:
    """
    Build a reverse mapping from parent -> list of children.
    """
    children_map = {}
    for child, parent in phonetics.items():
        if parent not in ("0", "1"):
            if parent not in children_map:
                children_map[parent] = []
            children_map[parent].append(child)

    # Sort children for consistent output
    for parent in children_map:
        children_map[parent].sort()

    return children_map


def render_tree(
    glyph: str,
    readings: Dict[str, str],
    children_map: Dict[str, List[str]],
    prefix: str = "",
    is_root: bool = True,
) -> List[str]:
    """
    Recursively render the family tree for a glyph and its descendants.
    Returns a list of strings representing each line of the tree.
    """
    lines = []

    # Get reading for current glyph
    reading = readings.get(glyph, "?")

    # Format the current glyph with reading
    glyph_str = f"{glyph}({reading})"

    # Get children
    children = children_map.get(glyph, [])

    # Current line
    if is_root:
        # Root node
        if children:
            lines.append(f"{glyph_str} --")
        else:
            lines.append(glyph_str)
    else:
        # Non-root nodes - always start with |
        if children:
            lines.append(f"{prefix}{glyph_str} --")
        else:
            lines.append(f"{prefix}{glyph_str}")

    # Process children
    if children:
        # Determine the child prefix
        if is_root:
            base_prefix = "         "
        else:
            base_prefix = prefix + "         "

        # Render each child
        for child in children:
            # Add vertical line before this child
            lines.append(f"{base_prefix}|")

            # Render the child subtree
            child_lines = render_tree(
                child, readings, children_map, base_prefix + "|", False
            )
            lines.extend(child_lines)

    return lines


def show_phonetic_family(
    glyph: str,
    phonetics_file: str = "data/phonetics.csv",
    readings_file: str = "data/readings.csv",
) -> str:
    """
    Show the complete phonetic family tree for a given glyph.

    Args:
        glyph: The glyph to show the family tree for
        phonetics_file: Path to the phonetics CSV file
        readings_file: Path to the readings CSV file

    Returns:
        A string representation of the family tree
    """
    # Load data
    phonetics = load_phonetics(phonetics_file)
    readings = load_readings(readings_file)

    # Check if glyph exists
    if glyph not in phonetics:
        return f"Error: Glyph '{glyph}' not found in phonetics data."

    # Find the ancestor (root of the family)
    ancestor = find_ancestor(glyph, phonetics)

    # Build children mapping
    children_map = build_children_map(phonetics)

    # Render the tree starting from ancestor
    tree_lines = render_tree(ancestor, readings, children_map)

    return "\n".join(tree_lines)


# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 phonetic_tree.py <glyph>")
        print("Example: python3 phonetic_tree.py 𬩆")
        sys.exit(1)

    glyph = sys.argv[1]
    tree = show_phonetic_family(glyph)
    print(tree)
