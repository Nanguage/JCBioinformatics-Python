"""
cut each line to it's first half

usage:
    cat input.txt | python cut_half.py > output.txt
"""

import sys

for line in sys.stdin:
    line = line.strip()
    print(line[:len(line)//2])
