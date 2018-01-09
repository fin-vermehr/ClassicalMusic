import midi

import_song = midi.read_midifile("/Users/finvermehr/Documents/Coding/Python/machine-learning/classical/Bach_Chorale_Piano_original.mid")

pattern = midi.Pattern()
index = 0

pattern.format = import_song.format
pattern.resolution = import_song.resolution

count = len(import_song)
note_list = []

track_list = []

for i in range(count):
    i = []
    track_list.append(i)


for track in import_song:
    track_list[index] = midi.Track()
    for note in track:
        if isinstance(note, midi.TrackNameEvent):
            track_list[index] = midi.Track()
            pattern.append(track_list[index])

            track_list[index].text = note.text

        if isinstance(note, midi.SetTempoEvent):
            se = midi.SetTempoEvent()
            se.tick = note.tick
            se.data = note.data
            track_list[index].append(se)

        if isinstance(note, midi.SequencerSpecificEvent):
            sp = midi.SequencerSpecificEvent()
            sp.tick = note.tick
            sp.data = note.data
            track_list[index].append(sp)

        if isinstance(note, midi.TimeSignatureEvent):
            ti = midi.TimeSignatureEvent()
            ti.tick = note.tick
            ti.data = note.data
            track_list[index].append(ti)

        if isinstance(note, midi.EndOfTrackEvent):
            en = midi.EndOfTrackEvent()
            en.tick = note.tick
            en.data = note.data
            track_list[index].append(en)
            index += 1


        if isinstance(note, midi.KeySignatureEvent):
            ke = midi.KeySignatureEvent()
            ke.tick = note.tick
            ke.data = note.data
            track_list[index].append(ke)

        # if isinstance(note, midi.ControlChangeEvent):
        #     co = midi.ControlChangeEvent()
        #     co.tick = note.tick
        #     co.data = note.data
        #     co.channel = note.channel
        #     track_list[index].append(co)

        if isinstance(note, midi.ProgramChangeEvent):
            pr = midi.ProgramChangeEvent()
            pr.tick = note.tick
            pr.data = note.data
            pr.channel = note.channel
            track_list[index].append(pr)

        if isinstance(note, midi.NoteOnEvent):
            on = midi.NoteOnEvent()
            on.tick = note.tick + 20
            on.data = note.data
            on.velocity = note.velocity
            on.pitch = note.pitch
            on.channel = note.channel
            track_list[index].append(on)
            note_list.append(note)

        if isinstance(note, midi.NoteOffEvent):
            off = midi.NoteOffEvent()
            off.tick = note.tick + 100
            off.data = note.data
            off.velocity = note.velocity
            off.channel = note.channel
            off.pitch = note.pitch
            track_list[index].append(off)
            note_list.append(note)

midi.write_midifile("/Users/finvermehr/Documents/Coding/Python/machine-learning/classical/final_copy.mid", pattern)


final_list = []
s = []
for note in note_list:
    if type(note) == midi.NoteOnEvent:
        new_note = dict()
        new_note["start"] = note.tick
        new_note["note"] = note.pitch
        new_note["end"] = None
        final_list.append(new_note)

    if type(note) == midi.NoteOffEvent:
        for dict_ in final_list:
            if dict_["note"] == note.pitch and dict_["end"] == None:
                dict_["end"] = note.tick
    #     for dict_ in final_list:
    #         if dict_[""]
f = open("/Users/finvermehr/Documents/Coding/Python/machine-learning/classical/classical_data.txt", "a")

for item in final_list:
    f.write(str(item))
    print(item)

# class Midi_note:
#     def __init__(self, start, end, velocity, channel, tick):
#         (self.start, self.end, self.velocity, self.channel, self.tick =
#          start, end, velocity, channel, tick)
#
#     def __eq__(self, other):
#         return(type(self) == type(other) and self.start == other.start and
#                self.end == other.end and self.velocity == other.velocity and
#                self.channel == other.channel and self.tick == other.tick)
#
#     def __repr__(self):

last_end = None
last_start = None


for item in final_list:

    if last_end is None and last_start is None:
        last_start, last_end = item['start'], item['end']

    else:
        if item['start'] == 0 and last_start != 0:
            item['start'] = last_start

        elif item['start'] != 0:
            last_start = item['start'] + last_end
            item['start'] == last_start

        if item['end'] == 0:
            item['end'] = last_end

        if item['end'] != 0:
            item['end'] = item['start'] + item['end'] + last_end



print(final_list)
