#!/usr/bin/env python3
"""
Simple example showing how to use the phonetic family tree function.
This demonstrates the exact use case from the requirements.
"""

from phonetic_tree import show_phonetic_family


# Example from the user's request:
# Given a glyph like 𬩆, which has the family:
# 𡿧 (ancestor) -> 甾 (parent) -> 淄 (child) -> 𬩆 (grandchild)

# Call the function with any glyph in the family
glyph = "𬩆"  # or use "淄", "甾", or "𡿧" - all show the same family tree

print(f"Phonetic family tree for '{glyph}':\n")
tree = show_phonetic_family(glyph)
print(tree)

print("\n" + "="*60 + "\n")

# You can also use it with any other glyph
another_glyph = "淄"
print(f"Same family tree when querying '{another_glyph}':\n")
tree2 = show_phonetic_family(another_glyph)
print(tree2)

