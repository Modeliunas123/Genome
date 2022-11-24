import PySimpleGUI as Interface
import re
import Interface_Layout
import Dictionaries as dict

Interface.theme('PythonPlus')

#------------------------------------------ATCG AND AUCG CONTENT--------------------------------------------------------

def DNA_AT_CG_content(DNA_sequence_raw):
    DNA_sequence = DNA_sequence_raw.upper()
    if re.search(r"[^ATGC]", DNA_sequence):
        base = ''
        position = ''
        for matches in re.finditer(r"[^ATGC]", DNA_sequence):
            base = base + matches.group() + ' '
            position = position + str(matches.start()) + 'p '
        layout_AT_CG_ambiguous = [[Interface.Text('Below are ambiguous bases and their positions', justification='center', size=(150,1))],
                                 [Interface.Text('Ambigious bases: ' + base)],
                                [Interface.Text('At positions: '  + position)],
                                [Interface.VPush(), Interface.Button('Main Menu'), Interface.Button('Exit', size=(5, 1))]]
        return Interface.Window('DNA Sequence', layout_AT_CG_ambiguous, size=(450,200))
    else:
        AT_total = int(round(100 * ((DNA_sequence.count("A") + DNA_sequence.count("T")) / len(DNA_sequence)), 2))
        CG_total = int(round(100 * ((DNA_sequence.count("C") + DNA_sequence.count("G")) / len(DNA_sequence)), 2))
        layout_AT_CG = [[Interface.Text('Below is the total AT and CG content of your DNA sequence:', justification='center', size=(150,1))],
                       [Interface.Text('AT Content: ' + str(AT_total) + '%')],
                       [Interface.Text('CG Content: ' + str(CG_total) + '%')]],\
                       [Interface.Text('With a total length of: ' + str(len(DNA_sequence)))],\
                       [Interface.VPush(), Interface.Button('Main Menu'), Interface.Button('Exit', size=(5,1))]
        return Interface.Window('DNA Sequence', layout_AT_CG, size=(450,200))

def RNA_AU_CG_content(RNA_sequence_raw):
    RNA_sequence = RNA_sequence_raw.upper()
    if re.search(r"[^AUGC]", RNA_sequence):
        base = ''
        position = ''
        for matches in re.finditer(r"[^AUGC]", RNA_sequence):
            base = base + matches.group() + ' '
            position = position + str(matches.start()) + 'p '
        layout_AU_CG_ambiguous = [
            [Interface.Text('Below are ambiguous bases and their positions', justification='center', size=(150, 1))],
            [Interface.Text('Ambigious bases: ' + base)],
            [Interface.Text('At positions: ' + position)],
        [Interface.VPush(), Interface.Button('Main Menu'), Interface.Button('Exit', size=(5, 1))]]
        return Interface.Window('RNA Sequence', layout_AU_CG_ambiguous, size=(450, 200))
    else:
        AU_total = 100 * ((RNA_sequence.count("A") + RNA_sequence.count("U")) / len(RNA_sequence))
        CG_total = 100 * ((RNA_sequence.count("C") + RNA_sequence.count("G")) / len(RNA_sequence))
        layout_AU_CG = [[Interface.Text('Below is the total AT and CG content of your RNA sequence:', justification='center', size=(150,1))],
                       [Interface.Text('AT Content: ' + str(AU_total) + '%')],
                       [Interface.Text('CG Content: ' + str(CG_total) + '%')]],\
                       [Interface.Text('With a total length of: ' + str(len(RNA_sequence)))],\
                       [Interface.VPush(), Interface.Button('Main Menu'), Interface.Button('Exit', size=(5,1))]
        return Interface.Window('RNA Sequence', layout_AU_CG, size=(450,200))

# ______________________________________DNA AND RNA TO AMINO ACID_______________________________________________________

def DNA_to_amino_acid(DNA_sequence_raw):
    DNA_strand = DNA_sequence_raw.upper()
    total_length = len(DNA_strand) - 2
    protein = " "
    for triplets in range(0, total_length, 3):
        codon = DNA_strand[triplets:triplets + 3]
        amino_acid = dict.DNA_aa_triplet_dict.get(codon, "X")
        protein = protein + amino_acid
    layout_DNA_amino_acid = [[Interface.Text('Below is the amino acid configuration of the DNA sequence:', justification='center', size=(150,1))],
                             [Interface.Text(protein)],
                             [Interface.VPush(), Interface.Button('Main Menu'), Interface.Button('Exit', size=(5, 1))]]
    return Interface.Window('DNA Amino Acid Sequence', layout_DNA_amino_acid, size=(450,200))


def RNA_to_amino_acid(RNA_sequence_raw):
    RNA_strand = RNA_sequence_raw.upper()
    total_length = len(RNA_strand) - 2
    protein = " "
    for triplets in range(0, total_length, 3):
        codon = RNA_strand[triplets:triplets + 3]
        amino_acid = dict.RNA_aa_triplet_dict.get(codon, "X")
        protein = protein + amino_acid
    layout_RNA_amino_acid = [[Interface.Text('Below is the amino acid configuration of the RNA sequence:', justification='center', size=(150,1))],
                             [Interface.Text(protein)],
                             [Interface.VPush(), Interface.Button('Main Menu'), Interface.Button('Exit', size=(5, 1))]]
    return Interface.Window('RNA Amino Acid Sequence', layout_RNA_amino_acid, size=(450,200))


# __________________________________MOLECULAR WEIGHT____________________________________________________________________

def DNA_molecular_weight_daltons(DNA_sequence_raw):
    DNA_strand = DNA_sequence_raw.upper()
    DNA_length = len(DNA_strand) - 1
    molecular_weight = 0
    for nucleotide in range(0, DNA_length, 3):
        triplet = DNA_strand[nucleotide:nucleotide + 3]
        amino_acid = dict.DNA_aa_triplet_dict.get(triplet, "X")
        daltons = dict.daltons_dict.get(amino_acid, 100)
        molecular_weight = (molecular_weight + daltons) - 18.02
    layout_DNA_molecular_weight = [
        [Interface.Text('Below is the molecular weight of your DNA sequence translated into a protein:', justification='center', size=(150, 1))],
        [Interface.VPush(), Interface.Text('mW: ' + str((molecular_weight + 18.02)))],
        [Interface.VPush(), Interface.Button('Main Menu'), Interface.Button('Exit', size=(5, 1)), Interface.Push()]]
    return Interface.Window('DNA molecular weight', layout_DNA_molecular_weight, size=(500, 200))


def RNA_molecular_weight_daltons(RNA_sequence_raw):
    RNA_strand = RNA_sequence_raw.upper()
    RNA_length = len(RNA_strand) - 1
    molecular_weight = 0
    for nucleotide in range(0, RNA_length, 3):
        triplet = RNA_strand[nucleotide:nucleotide + 3]
        amino_acid = dict.RNA_aa_triplet_dict.get(triplet, "X")
        daltons = dict.daltons_dict.get(amino_acid, 100)
        molecular_weight = (molecular_weight + daltons) - 18.02
    layout_RNA_molecular_weight = [
        [Interface.Text('Below is the molecular weight of your RNA sequence translated into a protein:', justification='center', size=(150, 1))],
        [Interface.VPush(), Interface.Text('mW: ' + str((molecular_weight + 18.02)))],
        [Interface.VPush(), Interface.Button('Main Menu'), Interface.Button('Exit', size=(5, 1)), Interface.Push()]]
    return Interface.Window('RNA molecular weight', layout_RNA_molecular_weight, size=(500, 200))



# ________________________________________DNA <-> RNA CONVERSION________________________________________________________

def DNA_to_RNA_conversion(DNA_to_RNA_sequence_raw):
    DNA_to_RNA = DNA_to_RNA_sequence_raw.upper()
    if re.search(r"[^ATGC]", DNA_to_RNA):
        base = ''
        position = ''
        for matches in re.finditer(r"[^ATGC]", DNA_to_RNA):
            base = base + matches.group() + ' '
            position = position + str(matches.start()) + 'p '
        DNA_to_RNA_ambiguous = [Interface.Text('Below are ambiguous bases and their positions in the conversion of DNA to RNA:', justification='center', size=(150, 1))],\
                                [Interface.Text('Ambigious bases: ' + base)],\
                                [Interface.Text('At positions: ' + position)],\
                               [Interface.VPush(), Interface.Button('Main Menu'), Interface.Button('Exit', size=(5, 1))]
        return Interface.Window('DNA Sequence', DNA_to_RNA_ambiguous, size=(500, 200))
    else:
        DNA_RNA = DNA_to_RNA.replace("T", "a").replace("A", "u").replace("C", "g").replace("G", "c")
        DNA_RNA_converted = DNA_RNA.upper()
    layout_DNA_to_RNA = [[Interface.Text('Below is the amino acid configuration of the DNA sequence:', justification='center', size=(150,1))],
                             [Interface.Text(DNA_RNA_converted)],
                         [Interface.VPush(), Interface.Button('Main Menu'), Interface.Button('Exit', size=(5, 1))]]
    return Interface.Window('DNA Amino Acid Sequence', layout_DNA_to_RNA, size=(500,200))

def RNA_to_DNA_conversion(RNA_to_DNA_sequence_raw):
    RNA_to_DNA = RNA_to_DNA_sequence_raw.upper()
    if re.search(r"[^AUGC]", RNA_to_DNA):
        base = ''
        position = ''
        for matches in re.finditer(r"[^AUGC]", RNA_to_DNA):
            base = base + matches.group() + ' '
            position = position + str(matches.start()) + 'p '
        RNA_to_DNA_ambiguous = [Interface.Text('Below are ambiguous bases and their positions in the conversion of RNA to DNA', justification='center', size=(150, 1))],\
                                [Interface.Text('Ambigious bases: ' + base)],\
                                [Interface.Text('At positions: ' + position),
                                 [Interface.VPush(), Interface.Button('Main Menu'), Interface.Button('Exit', size=(5, 1))]]
        return Interface.Window('RNA Sequence', RNA_to_DNA_ambiguous, size=(500, 200))
    else:
        RNA_DNA = RNA_to_DNA.replace("U", "a").replace("A", "t").replace("C", "g").replace("G", "c")
        RNA_to_DNA_converted = RNA_DNA.upper()
    layout_RNA_to_DNA = [[Interface.Text('Below is the amino acid configuration of the RNA sequence:', justification='center', size=(150, 1))],
                         [Interface.Text(RNA_to_DNA_converted)],
                         [Interface.VPush(), Interface.Button('Main Menu'), Interface.Button('Exit', size=(5, 1))]]
    return Interface.Window('RNA Amino Acid Sequence', layout_RNA_to_DNA, size=(500, 200))



# -------------------------------------------MAIN CODE-------------------------------------------------------------------

def main():
    window = Interface_Layout.main_window()
    while True:
        event, values = window.read()
        if event == Interface.WIN_CLOSED or event == 'Exit':
            break
# -------------------------------------------DNA CODING INTERFACE------------------------------------------------------
        elif event == 'DNA':

            window.close()
            window = Interface_Layout.DNA_window()
            event, values = window.read()
            if event == Interface.WIN_CLOSED or event == 'Exit':
                break

            elif event == 'Amino Acid Converter':
                window.close()
                window = Interface_Layout.DNA_amino_acid_window()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    DNA_sequence_raw = values[0]
                    window.close()
                    window = DNA_to_amino_acid(DNA_sequence_raw)
                    event, values = window.read()
                    if event == Interface.WIN_CLOSED or event == 'Exit':
                        break
                    elif event == 'Main Menu':
                        window.close()
                        window = Interface_Layout.main_window()
                elif event == 'Main Menu':
                    window.close()
                    window = Interface_Layout.main_window()

            elif event == 'AT/CG Calculator':
                window.close()
                window = Interface_Layout.DNA_ATCG_calculator()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    DNA_sequence_raw = values[0]
                    window.close()
                    window = DNA_AT_CG_content(DNA_sequence_raw)
                    event, values = window.read()
                    if event == Interface.WIN_CLOSED or event == 'Exit':
                        break
                    elif event == 'Main Menu':
                        window.close()
                        window = Interface_Layout.main_window()
                elif event == 'Main Menu':
                    window.close()
                    window = Interface_Layout.main_window()

            elif event == 'Molecular Weight':
                window.close()
                window = Interface_Layout.DNA_molecular_weight()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    DNA_sequence_raw = values[0]
                    window.close()
                    window = DNA_molecular_weight_daltons(DNA_sequence_raw)
                    event, values = window.read()
                    if event == Interface.WIN_CLOSED or event == 'Exit':
                        break
                    elif event == 'Main Menu':
                        window.close()
                        window = Interface_Layout.main_window()
                elif event == 'Main Menu':
                    window.close()
                    window = Interface_Layout.main_window()

            elif event == 'Back':
                window.close()
                window = Interface_Layout.main_window()


        # -------------------------------------------RNA  CODING INTERFACE------------------------------------------------------

        elif event == 'RNA':
            window.close()
            window = Interface_Layout.RNA_window()
            event, values = window.read()
            if event == Interface.WIN_CLOSED or event == 'Exit':
                break

            elif event == 'Amino Acid Converter':
                window.close()
                window = Interface_Layout.RNA_amino_acid_window()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    RNA_sequence_raw = values[0]
                    window.close()
                    window = RNA_to_amino_acid(RNA_sequence_raw)
                    event, values = window.read()
                    if event == Interface.WIN_CLOSED or event == 'Exit':
                        break
                    elif event == 'Main Menu':
                        window.close()
                        window = Interface_Layout.main_window()
                elif event == 'Main Menu':
                    window.close()
                    window = Interface_Layout.main_window()

            elif event == 'AU/CG Calculator':
                window.close()
                window = Interface_Layout.RNA_AUCG_calculator()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    RNA_sequence_raw = values[0]
                    window.close()
                    window = RNA_AU_CG_content(RNA_sequence_raw)
                    event, values = window.read()
                    if event == Interface.WIN_CLOSED or event == 'Exit':
                        break
                    elif event == 'Main Menu':
                        window.close()
                        window = Interface_Layout.main_window()
                elif event == 'Main Menu':
                    window.close()
                    window = Interface_Layout.main_window()

            elif event == 'Molecular Weight':
                window.close()
                window = Interface_Layout.RNA_molecular_weight()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    RNA_sequence_raw = values[0]
                    window.close()
                    window = RNA_molecular_weight_daltons(RNA_sequence_raw)
                    event, values = window.read()
                    if event == Interface.WIN_CLOSED or event == 'Exit':
                        break
                    elif event == 'Main Menu':
                        window.close()
                        window = Interface_Layout.main_window()
                elif event == 'Main Menu':
                    window.close()
                    window = Interface_Layout.main_window()

            elif event == 'Back':
                window.close()
                window = Interface_Layout.main_window()

        # -------------------------------------------CONVERSION CODING INTERFACE------------------------------------------------

        elif event == 'Strand Conversion':

            window.close()
            window = Interface_Layout.DNA_and_RNA_window()
            event, values = window.read()
            if event == Interface.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'DNA -> RNA':
                window.close()
                window = Interface_Layout.DNA_to_RNA_window()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    DNA_sequence_raw = values[0]
                    window.close()
                    window = DNA_to_RNA_conversion(DNA_sequence_raw)
                    event, values = window.read()
                    if event == Interface.WIN_CLOSED or event == 'Exit':
                        break
                    elif event == 'Main Menu':
                        window.close()
                        window = Interface_Layout.main_window()
                elif event == 'Main Menu':
                    window.close()
                    window = Interface_Layout.main_window()

            elif event == 'RNA -> DNA':
                window.close()
                window = Interface_Layout.RNA_to_DNA_window()
                event, values = window.read()
                if event == Interface.WIN_CLOSED or event == 'Exit':
                    break
                elif event == 'Okay':
                    RNA_sequence_raw = values[0]
                    window.close()
                    window = RNA_to_DNA_conversion(RNA_sequence_raw)
                    event, values = window.read()
                    if event == Interface.WIN_CLOSED or event == 'Exit':
                        break
                    elif event == 'Main Menu':
                        window.close()
                        window = Interface_Layout.main_window()
                elif event == 'Main Menu':
                    window.close()
                    window = Interface_Layout.main_window()
            elif event == 'Back':
                window.close()
                window = Interface_Layout.main_window()

# -----------------------------------------------------------------------------------------------------------------------

main()

