import midi
from pprint import pprint
# Instantiate a MIDI Pattern (contains a list of tracks)
pattern = midi.Pattern()
# Instantiate a MIDI Track (contains a list of MIDI events)
track = midi.Track()
# Append the track to the pattern
pattern.append(track)
# Instantiate a MIDI note on event, append it to the track
on = midi.NoteOnEvent(tick=0, velocity=20, pitch=midi.G_3)
track.append(on)
# Instantiate a MIDI note off event, append it to the track
off = midi.NoteOffEvent(tick=100, pitch=midi.G_3)
track.append(off)
# Add the end of track event, append it to the track
eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)
# Print out the pattern
# Save the pattern to disk
midi.write_midifile("example.mid", pattern)


import midi
import_song = midi.read_midifile("/Users/finvermehr/Documents/Coding/Python/machine-learning/classical/bwv1052a.mid")


pattern = midi.Pattern()

track_list = list()
count = 0
for item in import_song:
    for note in item:
        if isinstance(note, midi.ProgramChangeEvent):
            count += 1

for i in range(count):
    i = []
    track_list.append(i)

index = -1
current_track = track_list[index]

for item in import_song:
    for note in item:
        if isinstance(note, midi.ProgramChangeEvent):
            index += 1
            print(index)
            current_track = track_list[index]

        if isinstance(note, midi.TrackNameEvent):
            current_track = midi.Track()
            pattern.append(current_track)

            current_track.text = note.text

        if isinstance(note, midi.SetTempoEvent):
            se = midi.SetTempoEvent()
            se.tick = note.tick
            se.data = note.data
            current_track.append(se)

        if isinstance(note, midi.SequencerSpecificEvent):
            sp = midi.SequencerSpecificEvent()
            sp.tick = note.tick
            sp.data = note.data
            current_track.append(sp)

        if isinstance(note, midi.TimeSignatureEvent):
            ti = midi.TimeSignatureEvent()
            ti.tick = note.tick
            ti.data = note.data
            print(track_list)
            current_track.append(ti)

        if isinstance(note, midi.EndOfTrackEvent):
            en = midi.EndOfTrackEvent()
            en.tick = note.tick
            en.data = note.data
            current_track.append(en)

        if isinstance(note, midi.KeySignatureEvent):
            ke = midi.KeySignatureEvent()
            ke.tick = note.tick
            ke.data = note.data
            print(track_list)
            current_track.append(ke)

        if isinstance(note, midi.ControlChangeEvent):
            co = midi.ControlChangeEvent()
            co.tick = note.tick
            co.data = note.data
            co.channel = note.channel
            current_track.append(co)

        if isinstance(note, midi.ProgramChangeEvent):
            pr = midi.ProgramChangeEvent()
            pr.tick = note.tick
            pr.data = note.data
            pr.channel = note.channel
            current_track.append(pr)

        if isinstance(note, midi.NoteOnEvent):
            on = midi.NoteOnEvent()
            on.tick = note.tick
            on.data = note.data
            on.velocity = note.velocity
            on.pitch = note.pitch
            on.channel = note.channel
            current_track.append(on)

        if isinstance(note, midi.NoteOffEvent):
            off = midi.NoteOffEvent()
            off.tick = note.tick
            off.data = note.data
            off.velocity = note.velocity
            off.channel = note.channel
            current_track.append(off)

print(pattern)

midi.write_midifile("/Users/finvermehr/Documents/Coding/Python/machine-learning/classical/bwv1052a_copy.mid", pattern)


        # if isinstance(note, midi.NoteOffEvent) or isinstance(note, midi.NoteOnEvent):
        #     if last_channel is None:

            # if last_channel is not None or last_channel != note.channel:
            #     eot = midi.EndOfTrackEvent(tick=1)
            #     track.append(eot)
            #     print(last_channel)
            # last_channel = note.channel
            #
            # on = midi.NoteOnEvent()
            # on.data = note.data
            # on.pitch = note.pitch
            # on.channel = note.channel
            # on.velocity = note.velocity
            # on.tick = note.tick
            # track.append(on)
            # off = midi.NoteOffEvent(tick=100)
            # off.pitch = note.pitch
            # track.append(off)

# eot = midi.EndOfTrackEvent(tick=1)
# track.append(eot)
# midi.write_midifile("/Users/finvermehr/Documents/Coding/Python/machine-learning/classical/bwv1052a_copy.mid", pattern)
