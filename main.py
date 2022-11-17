import PySimpleGUI as Interface
import re
import InterfaceStuff
import Dictionaries

Interface.theme('PythonPlus')


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
        print("Total AT: ", round(AU_total, 2), "%\nTotal CG: ", round(CG_total, 2), "%\nDNA Length: ",
              len(RNA_sequence))


# _______________________________________________________________________________________________________________________

def DNA_to_amino_acid(DNA_sequence_raw):
    DNA_strand = DNA_sequence_raw.upper()
    total_length = len(DNA_strand) - 2
    protein = " "
    for triplets in range(0, total_length, 3):
        codon = DNA_strand[triplets:triplets + 3]
        amino_acid = Dictionaries.DNA_aa_triplet_dict.get(codon, "X")
        protein = protein + amino_acid
    return protein


def RNA_to_amino_acid(RNA_sequence_raw):
    RNA_strand = RNA_sequence_raw.upper()
    total_length = len(RNA_strand) - 2
    protein = " "
    for triplets in range(0, total_length, 3):
        codon = RNA_strand[triplets:triplets + 3]
        amino_acid = Dictionaries.RNA_aa_triplet_dict.get(codon, "X")
        protein = protein + amino_acid
    return (protein)


# _______________________________________________________________________________________________________________________

def molecular_weight_daltons(DNA_sequence_raw):
    DNA_strand = DNA_sequence_raw.upper()
    DNA_length = len(DNA_strand) - 1
    molecular_weight_raw = 0
    for nucleotide in range(0, DNA_length, 3):
        triplet = DNA_strand[nucleotide:nucleotide + 3]
        amino_acid = Dictionaries.DNA_aa_triplet_dict.get(triplet, "X")
        daltons = Dictionaries.daltons_dict.get(amino_acid, 100)
        molecular_weight_raw = (molecular_weight_raw + daltons) - 18.02
    return (molecular_weight_raw + 18.02)


# _______________________________________________________________________________________________________________________

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


# _______________________________________________________________________________________________________________________


# -------------------------------------------MAIN CODE-------------------------------------------------------------------

def main():
    window = InterfaceStuff.main_window()
    while True:
        event, values = window.read()
        if event == Interface.WIN_CLOSED or event == 'Exit':
            break
        # -------------------------------------------DNA  CODING INTERFACE------------------------------------------------------
        elif event == 'DNA':
            print(1)
            window.close()
            window = InterfaceStuff.DNA_window()
            event, values = window.read()
            if event == Interface.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'Amino acid converter':
                print(2)
                window.close()
                window = InterfaceStuff.DNA_amino_acid_window()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    print('hi')
                elif event == 'Main Menu':
                    window.close()
                    window = InterfaceStuff.main_window()
            elif event == 'AT/CG calculator':
                print(3)
                window.close()
                window = InterfaceStuff.DNA_ATCG_calculator()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    DNA_sequence_raw = values[0]
                    DNA_AT_CG_content(DNA_sequence_raw)
                elif event == 'Main Menu':
                    window.close()
                    window = InterfaceStuff.main_window()
            elif event == 'Back':
                print(4)
                window.close()
                window = InterfaceStuff.main_window()

        # -------------------------------------------RNA  CODING INTERFACE------------------------------------------------------

        elif event == 'RNA':
            print(5)
            window.close()
            window = InterfaceStuff.RNA_window()
            event, values = window.read()
            if event == Interface.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'Amino acid converter':
                print(6)
                window.close()
                window = InterfaceStuff.RNA_amino_acid_window()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    print('hi')
                elif event == 'Main Menu':
                    window.close()
                    window = InterfaceStuff.main_window()
            elif event == 'AU/CG calculator':
                print(7)
                window.close()
                window = InterfaceStuff.RNA_AUCG_calculator()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    print('hi')
                elif event == 'Main Menu':
                    window.close()
                    window = InterfaceStuff.main_window()
            elif event == 'Back':
                print(8)
                window.close()
                window = InterfaceStuff.main_window()

        # -------------------------------------------CONVERSION CODING INTERFACE------------------------------------------------

        elif event == 'Strand Conversion':
            print(9)
            window.close()
            window = InterfaceStuff.DNA_and_RNA_window()
            event, values = window.read()
            if event == Interface.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'DNA -> RNA':
                print(10)
                window.close()
                window = InterfaceStuff.DNA_to_RNA_window()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    print(values[0])
                elif event == 'Main Menu':
                    window.close()
                    window = InterfaceStuff.main_window()
            elif event == 'RNA -> DNA':
                print(11)
                window.close()
                window = InterfaceStuff.RNA_to_DNA_window()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    print(values[0])
                elif event == 'Main Menu':
                    window.close()
                    window = InterfaceStuff.main_window()
            elif event == 'Back':
                window.close()
                window = InterfaceStuff.main_window()


# -----------------------------------------------------------------------------------------------------------------------
main()
