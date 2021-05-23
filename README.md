# MUSIC CREATION LIBRARY
This library is for creating custom musical scales, melodies and instruments so far.
In the next versions, we are planning to add features for creating armonies.
# INSTALL
```shell
git clone https://github.com/francosopo/music-creation-library.git
```
Or download the zip

# USAGE
For basic usage, instantiate the Traditional Scale (Do menor relative) with the
amount of notes you want to use.

Then, instantiate the melody with the scale you created and choose the notes from that
scale you want to include in your melody. 

```python
melody.use_note(index, time_duration)
```
Use integers for time_duration, the unit represents the quarter note. 


You also have to create an instrument you want, or use the Basic provided.
It is important to override the timbre method, with a periodic wave using the 
parameters. Also, you can specify the quarter note duration in miliseconds when you create the instrument.

```python
class Instrument(AbstractInstrument):

    def __init__(self, melody, **kwargs):
        super().__init__(melody, **kwargs)

    def timbre(self, note, armonic_number, time):
        return math.sin(2 * math.pi * note * armonic_number * time)

Instrument(melody,quarter_note_duration=600)
```

Once you have created your instrument with the melody you want to
play, build the melody and give it a name. Then, you can listen the
.wav.

```python
i = Instrument(melody) #the melody object
i.build_melody("my_melody")

#or
j = Instrument(melody, quarter_note_duration=1000)
i.build_melody("my_slow_melody")
```

For more info, see the example.py file

Enjoy.