from enum import Enum

class NoteNames(Enum):
    '''
    Notes of the Western musical scale
    C is the lowest note (B sharp is equal lowest)
    s = sharp
    b = flat
    '''

    Bs = 0
    C = 0
    Cs = 1
    Db = 1
    D = 2
    Ds = 3
    Eb = 3
    E = 4
    Fb = 4
    Es = 5
    F = 5
    Fs = 6
    Gb = 6
    G = 7
    Gs = 8
    Ab = 8
    A = 9
    As = 10
    Bb = 10
    B = 11

    SHARP = [Bs, Cs, Ds, Es, Fs, Gs, As]
    FLAT = [Db, Eb, Fb, Gb, Ab, Bb]