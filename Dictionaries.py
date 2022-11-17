
#______________________________________________DICTIONARIES_____________________________________________________________
DNA_aa_triplet_dict = {
    "AAA": "F", "AAG": "F",
    "AAT": "L", "AAC": "L", "GAA": "L", "GAG": "L", "GAT": "L", "GAC": "L",
    "AGA": "S", "AGG": "S", "AGT": "S", "AGC": "S", "TCA": "S", "TCG": "S",
    "GGA": "P", "GGG": "P", "GGT": "P", "GGC": "P",
    "TAA": "I", "TAG": "I", "TAT": "I",
    "TAC": "M",
    "TGA": "T", "TGG": "T", "TGT": "T", "TGC": "T",
    "CAA": "V", "CAG": "V", "CAT": "V", "CAC": "V",
    "CGA": "A", "CGG": "A", "CGT": "A", "CGC": "A",
    "ACA": "C", "ACG": "C",
    "ACC": "W",
    "ATA": "Y", "ATG": "Y",
    "ATT": "STOP", "ATC": "STOP", "ACT": "STOP",
    "GCA": "R", "GCG": "R", "GCT": "R", "GCC": "R", "TCT": "R", "TCC": "R",
    "GTA": "H", "GTG": "H",
    "GTT": "Q", "GTC": "Q",
    "TTA": "N", "TTG": "N",
    "TTT": "K", "TTC": "K",
    "CCA": "G", "CCG": "G", "CCT": "G", "CCC": "G",
    "CTA": "D", "CTG": "D",
    "CTT": "E", "CTC": "E"
}
#_______________________________________________________________________________________________________________________
RNA_aa_triplet_dict = {
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "CCU": "P", "CCC": "S", "CCA": "S", "CCG": "S",
    "I": ["AUU", "AUC", "AUA"],
    "M": "AUG",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "!STOP!", "UAG": "!STOP!", "UGA": "!STOP!",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "CAU": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E"
}
#_______________________________________________________________________________________________________________________
daltons_dict = {
    "A": 71.08,
    "R": 156.2,
    "N": 114.11,
    "D": 115.09,
    "C": 103.14,
    "Q": 128.14,
    "E": 129.12,
    "G": 57.06,
    "H": 137.15,
    "I": 113.17,
    "L": 113.17,
    "K": 128.18,
    "M": 131.21,
    "F": 147.18,
    "P": 97.12,
    "S": 87.08,
    "T": 101.11,
    "W": 186.21,
    "Y": 163.18,
    "V": 99.14,
    "H2O": 18.02,
}