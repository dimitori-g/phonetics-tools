"""
Demonstration script for the phonetic tree function.

This script shows how to use the show_phonetic_family() function
to display phonetic family trees for Chinese characters.
"""

from phonetic_tree import show_phonetic_family


def main():
    """Demonstrate the phonetic tree functionality."""

    # Example 1: Show family tree for 𬩆
    print("=" * 60)
    print("Example 1: Phonetic family tree for '𬩆'")
    print("=" * 60)
    glyph1 = "𬩆"
    tree1 = show_phonetic_family(glyph1)
    print(tree1)
    print()

    # Example 2: Show family tree for any other glyph in the same family
    print("=" * 60)
    print("Example 2: Phonetic family tree for '淄' (same family)")
    print("=" * 60)
    glyph2 = "淄"
    tree2 = show_phonetic_family(glyph2)
    print(tree2)
    print()

    # Example 3: Show family tree for a different family
    print("=" * 60)
    print("Example 3: Phonetic family tree for '一'")
    print("=" * 60)
    glyph3 = "一"
    tree3 = show_phonetic_family(glyph3)
    print(tree3)
    print()

    # Example 4: Custom file paths
    print("=" * 60)
    print("Example 4: Using custom file paths")
    print("=" * 60)
    glyph4 = "甾"
    tree4 = show_phonetic_family(
        glyph4,
        phonetics_file="data/phonetics.csv",
        readings_file="data/readings.csv",
    )
    print(tree4)


if __name__ == "__main__":
    main()

