piano_notes=['C4', 'C4#', 'D4', 'D4#', 'E4', 'F4', 'F4#', 'G4', 'G4#',
            'A4', 'A4#', 'B4', 'C5', 'C5#', 'D5', 'D5#', 'E5', 'F5', 'F5#', 'G5', 'G5#',
            'A5', 'A5#', 'B5']
white_notes=['C4', 'D4', 'E4', 'F4', 'G4',
            'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5',
            'A5', 'B5']
black_notes=['C4#','D4#','F4#','G4#','A#4','C5#','D5#','F5#','G5#','A5#']

keybord_input ='A W S E D R F T G Y H U J I '
input_list=keybord_input.split()

pos=[i*98.1 for i in range(14)]

black_pos=pos[:2]+pos[3:6]+pos[7:9]+pos[10:13]

def ranges(start):
    octave=piano_notes[start:start+12]
    return octave

def search(k_input,start):
    octave=piano_notes[start:start+12]
    if k_input.upper() in setting(start):
        a=setting(start).index(k_input.upper())
        return octave[a]

def setting(start):
    key_input = keybord_input.split()
    removal = []
    if start==0:
        removal.append(['R','I'])
    elif start==1:
        removal.append(['E','U'])
    elif start==3:
        removal.append(['W','Y'])
    elif start==4:
        removal.append(['I', 'T'])
    elif start == 5:
        removal.append(['U', 'R'])
    elif start == 6:
        removal.append(['Y', 'E'])
    elif start == 7:
        removal.append(['T', 'W'])
    for i in removal[0]:
        key_input.remove(i)
    return key_input

