import PySimpleGUI as Interface
import re
Interface.theme('PythonPlus')
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

def DNA_AT_CG_content(DNA_sequence_raw):
    DNA_sequence = DNA_sequence_raw.upper()
    if re.search(r"[^ATGC]", DNA_sequence):
        print("Please re-enter the sequence with the following ambiguous sequences changed:\n")
        for matches in re.finditer(r"[^ATGC]", DNA_sequence):
            base = matches.group()
            position = matches.start()
            print("Ambiguous nucleotide base ", base, " at position ", str(position))
    else:
        AT_total = round(100 * ((DNA_sequence.count("A") + DNA_sequence.count("T")) / len(DNA_sequence)), 2)
        CG_total = round(100 * ((DNA_sequence.count("C") + DNA_sequence.count("G")) / len(DNA_sequence)), 2)
        print("Total AT: ", AT_total, "%\nTotal CG: ", CG_total, "%\nDNA Length: ", len(DNA_sequence))

def RNA_AU_CG_content(RNA_sequence_raw):
    RNA_sequence = RNA_sequence_raw.upper()
    if re.search(r"[^AUGC]", RNA_sequence):
        print("\nPlease re-enter the sequence with the following ambiguous sequences changed:")
        for ambigious_bases in re.finditer(r"[^AUGC]", RNA_sequence):
            base = ambigious_bases.group()
            position = ambigious_bases.start()
            print("Ambiguous nucleotide base ", base, " at position ", str(position), " out of ", len(RNA_sequence))
    else:
        AU_total = 100 * ((RNA_sequence.count("A") + RNA_sequence.count("U")) / len(RNA_sequence))
        CG_total = 100 * ((RNA_sequence.count("C") + RNA_sequence.count("G")) / len(RNA_sequence))
        print("Total AT: ", round(AU_total, 2), "%\nTotal CG: ", round(CG_total, 2), "%\nDNA Length: ", len(RNA_sequence))

#_______________________________________________________________________________________________________________________

def DNA_to_amino_acid(DNA_sequence_raw):
    DNA_strand = DNA_sequence_raw.upper()
    total_length = len(DNA_strand) - 2
    protein = " "
    for triplets in range(0, total_length, 3):
        codon = DNA_strand[triplets:triplets + 3]
        amino_acid = DNA_aa_triplet_dict.get(codon, "X")
        protein = protein + amino_acid
    return(protein)

def RNA_to_amino_acid(RNA_sequence_raw):
    RNA_strand = RNA_sequence_raw.upper()
    total_length = len(RNA_strand) - 2
    protein = " "
    for triplets in range(0, total_length, 3):
        codon = RNA_strand[triplets:triplets + 3]
        amino_acid = RNA_aa_triplet_dict.get(codon, "X")
        protein = protein + amino_acid
    return(protein)

#_______________________________________________________________________________________________________________________

def molecular_weight_daltons(DNA_sequence_raw):
    DNA_strand = DNA_sequence_raw.upper()
    DNA_length = len(DNA_strand) - 1
    molecular_weight_raw = 0
    for nucleotide in range(0, DNA_length, 3):
        triplet = DNA_strand[nucleotide:nucleotide + 3]
        amino_acid = DNA_aa_triplet_dict.get(triplet, "X")
        daltons = daltons_dict.get(amino_acid, 100)
        molecular_weight_raw = (molecular_weight_raw + daltons) - 18.02
    return(molecular_weight_raw + 18.02)

#_______________________________________________________________________________________________________________________

def DNA_to_RNA_conversion(DNA_to_RNA_sequence_raw):
    DNA_to_RNA = DNA_to_RNA_sequence_raw.upper()
    if re.search(r"[^ATGC]", DNA_to_RNA):
        print("\nPlease re-enter the sequence with the following ambiguous sequences changed: ")
        for ambiguous_bases in re.finditer(r"[^ATGC]", DNA_to_RNA):
            base = ambiguous_bases.group()
            position = ambiguous_bases.start()
            print("Ambiguous nucleotide base ", base, " at position", str(position), " out of ", len(DNA_to_RNA))
    else:
        DNA_RNA = DNA_to_RNA.replace("T", "a").replace("A", "u").replace("C", "g").replace("G", "c")
        DNA_RNA_converted = DNA_RNA.upper()
        print("Your RNA sequence is: " + "\n" + DNA_RNA_converted)

#_______________________________________________________________________________________________________________________





#-------------------------------------------MAIN  INTERFACE-------------------------------------------------------------
def main_window():
      main_layout = [[Interface.Text('This is the Genome Program for evaluating DNA or RNA strands', justification='center', size=(150,1))],
                    [Interface.Text('into their amino acid counterparts, determining the hypothetical', justification='center', size=(150,1))],
                    [Interface.Text('molecular weight, pKA value, and their genomic content.', justification='center', size=(150,1))],
                    [Interface.VPush(), Interface.Text('Please choose whether you have a DNA or RNA sequence below:', justification='center', size=(150,1))],
                    [Interface.VPush(), Interface.Button('DNA', size=(5, 1)), Interface.Button("RNA", size=(5, 1)), Interface.Button('Strand Conversion', size=(15, 1)), Interface.Push(), Interface.Button('Exit', size=(5,1))] ]
      return Interface.Window('Genome Program', main_layout, size=(450,200))

#-------------------------------------------DNA    INTERFACE------------------------------------------------------------

def DNA_window():
    layout_DNA = [[Interface.Text('You have chosen a DNA sequence', justification='center', size=(150,1))],
                  [Interface.Text('Please choose whether you would like to convert this:', justification='center', size=(150,1))],
                  [Interface.Text('to an amino acid or calculate the AT/CG content below:', justification='center', size=(150,1))],
                  [Interface.VPush(), Interface.Button('Amino acid converter', size=(15, 1)), Interface.Button('AT/CG calculator', size=(15, 1)), Interface.Button('Back'), Interface.Push(), Interface.Button('Exit', size=(5,1))]]
    return Interface.Window('DNA Sequence', layout_DNA, size=(450,200))

def DNA_amino_acid_window():
    layout_DNA = [[Interface.Text('DNA to amino acid conversion', justification='center', size=(150,1))],
                  [Interface.Text('Please input your DNA sequence below:', justification='center', size=(150,1))],
                  [Interface.Multiline(size=(60,20))],
                  [Interface.VPush(), Interface.Button('Okay', size=(15, 1)), Interface.Button('Main Menu', size=(15, 1)), Interface.Push(), Interface.Button('Exit', size=(5,1))]]
    return Interface.Window('DNA Sequence', layout_DNA, size=(450,500))

def DNA_ATCG_calculator():
    layout_DNA = [[Interface.Text('AT/CG calculator', justification='center', size=(150,1))],
                  [Interface.Text('Please input your DNA sequence below:', justification='center', size=(150,1))],
                  [Interface.Multiline(size=(60,20))],
                  [Interface.VPush(), Interface.Button('Okay', size=(15, 1)), Interface.Button('Main Menu', size=(15, 1)), Interface.Push(), Interface.Button('Exit', size=(5, 1))]]
    return Interface.Window('ATCG Calculator', layout_DNA, size=(450,500))
#-------------------------------------------RNA    INTERFACE------------------------------------------------------------
def RNA_window():
    layout_DNA = [[Interface.Text('You have chosen an RNA sequence', justification='center', size=(150,1))],
                  [Interface.Text('Please choose whether you would like to convert this:', justification='center', size=(150,1))],
                  [Interface.Text('to an amino acid or calculate the AU/CG content below:', justification='center', size=(150,1))],
                  [Interface.VPush(), Interface.Button('Amino acid converter', size=(15, 1)), Interface.Button('AU/CG calculator', size=(15, 1)), Interface.Button('Back'), Interface.Push(), Interface.Button('Exit', size=(5,1))]]
    return Interface.Window('RNA Sequence', layout_DNA, size=(450,200))

def RNA_amino_acid_window():
    layout_RNA = [ [Interface.Text('RNA to amino acid conversion', justification='center', size=(150,1))],
                   [Interface.Text('Please input your RNA sequence below:', justification='center', size=(150,1))],
                   [Interface.Multiline(size=(60,20))],
                   [Interface.VPush(), Interface.Button('Okay', size=(15, 1)), Interface.Button('Main Menu', size=(15, 1)), Interface.Push(), Interface.Button('Exit', size=(5, 1))]]
    return Interface.Window('RNA Sequence', layout_RNA, size=(450,500))

def RNA_AUCG_calculator():
    layout_RNA = [[Interface.Text('AU/CG calculator', justification='center', size=(150,1))],
                  [Interface.Text('Please input your RNA sequence below:', justification='center', size=(150,1))],
                  [Interface.Multiline(size=(60,20))],
                  [Interface.VPush(), Interface.Button('Okay', size=(15, 1)), Interface.Button('Main Menu', size=(15, 1)), Interface.Push(), Interface.Button('Exit', size=(5, 1))]]
    return Interface.Window('AUCG Calculator', layout_RNA, size=(450,500))

#-------------------------------------------DNA <-> RNA   INTERFACE-----------------------------------------------------

def DNA_and_RNA_window():
    layout_DNA_and_RNA = [ [Interface.Text('You have selected strand conversion', justification='center', size=(150,1))],
                    [Interface.Text('Would you like to convert DNA -> RNA or RNA -> DNA?', justification='center', size=(150,1))],
                    [Interface.VPush(), Interface.Button('DNA -> RNA', size=(10,1)), Interface.Button('RNA -> DNA', size=(10,1)), Interface.Push(), Interface.Button('Back', size=(5,1)), Interface.Button('Exit', size=(5,1))]]
    return Interface.Window('DNA and RNA Selection', layout_DNA_and_RNA, size=(450,150))

def DNA_to_RNA_window():
    layout_DNA_to_RNA = [ [Interface.Text('DNA to RNA conversion', justification='center', size=(150,1))],
                    [Interface.Text('Please input your sequence below:', justification='center', size=(150,1))],
                    [Interface.Multiline(size=(60,20))],
                    [Interface.VPush(), Interface.Button('Okay', size=(15, 1)), Interface.Button('Main Menu', size=(15, 1)), Interface.Push(), Interface.Button('Exit', size=(5, 1))]]
    return Interface.Window('DNA to RNA', layout_DNA_to_RNA, size=(450,500))

def RNA_to_DNA_window():
    layout_RNA_to_DNA = [ [Interface.Text('RNA to DNA conversion', justification='center', size=(150,1))],
                    [Interface.Text('Please input your sequence below:', justification='center', size=(150,1))],
                    [Interface.Multiline(size=(60,20))],
                    [Interface.VPush(), Interface.Button('Okay', size=(15, 1)), Interface.Button('Main Menu', size=(15, 1)), Interface.Push(), Interface.Button('Exit', size=(5, 1))]]
    return Interface.Window('RNA to DNA', layout_RNA_to_DNA, size=(450,500))

def ATCG_content_window():
    layout_ATCG_content = [ [Interface.Text('AT/CG content calculation', justification='center', size=(150,1))],
                            [Interface.Text('Please enter your ')]]

#-------------------------------------------MAIN CODE-------------------------------------------------------------------

def main():
    window = main_window()
    while True:
        event, values = window.read()
        if event == Interface.WIN_CLOSED or event == 'Exit':
            break
# -------------------------------------------DNA  CODING INTERFACE------------------------------------------------------
        elif event == 'DNA':
            window.close()
            window = DNA_window()
            event, values = window.read()
            if event == Interface.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'Amino acid converter':
                window.close()
                window = DNA_amino_acid_window()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    print('hi')
                elif event == 'Main Menu':
                    window.close()
                    window = main_window()
            elif event == 'AT/CG calculator':
                window.close()
                window = DNA_ATCG_calculator()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    DNA_sequence_raw = values[0]
                    DNA_AT_CG_content(DNA_sequence_raw)
                elif event == 'Main Menu':
                    window.close()
                    window = main_window()
            elif event == 'Back':
                window.close()
                window = main_window()

# -------------------------------------------RNA  CODING INTERFACE------------------------------------------------------

        elif event == 'RNA':
            window.close()
            window = RNA_window()
            event, values = window.read()
            if event == Interface.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'Amino acid converter':
                window.close()
                window = RNA_amino_acid_window()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    print('hi')
                elif event == 'Main Menu':
                    window.close()
                    window = main_window()
            elif event == 'AU/CG calculator':
                window.close()
                window = RNA_AUCG_calculator()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    print('hi')
                elif event == 'Main Menu':
                    window.close()
                    window = main_window()
            elif event == 'Back':
                window.close()
                window = main_window()

# -------------------------------------------CONVERSION CODING INTERFACE------------------------------------------------

        elif event == 'Strand Conversion':
            window.close()
            window = DNA_and_RNA_window()
            event, values = window.read()
            if event == Interface.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'DNA -> RNA':
                window.close()
                window = DNA_to_RNA_window()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    print(values[0])
                elif event == 'Main Menu':
                    window.close()
                    window = main_window()
            elif event == 'RNA -> DNA':
                window.close()
                window = RNA_to_DNA_window()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    print(values[0])
                elif event == 'Main Menu':
                    window.close()
                    window = main_window()
            elif event == 'Back':
                window.close()
                window = main_window()
#-----------------------------------------------------------------------------------------------------------------------
main()