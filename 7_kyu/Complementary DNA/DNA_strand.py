"""Complementary DNA
"""


def DNA_strand(dna):
    dna_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return "".join(dna_dict[key] for key in dna)
