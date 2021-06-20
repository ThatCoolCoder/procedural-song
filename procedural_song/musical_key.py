from procedural_song import NoteNames

class MusicalKey:
    def __init__(self, notes:list):
        # Notes should be a list of length 12 containing notes in ascending order
        self.notes = notes.copy()
    
    @property
    def sharps(self):
        return [note for note in self.notes if note in NoteNames.SHARP]
    
    @property
    def flats(self):
        return [note for note in self.notes if note in NoteNames.FLAT]