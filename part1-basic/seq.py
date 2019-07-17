"""
A little module for process DNA sequence.
"""

def count_GC_ratio(seq):
    n_gc = 0
    for b in seq:
        B = b.upper()
        if B == 'G' or B == 'C':
            n_gc += 1
    return n_gc / len(seq)

def reverse_complement(seq):
    table = {'c':'g', 'g':'c', 'a':'t', 't':'a', 'n':'n'}
    table_upper = {k.upper():v.upper() for k,v in table.items()}
    table.update(table_upper)
    return "".join(list(map(lambda b: table[b], seq[::-1])))
