def to_rna(dna_strand):
    rna = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }
    return "".join(map(lambda nuc: rna[nuc], list(dna_strand)))
