import PySimpleGUI as Interface

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