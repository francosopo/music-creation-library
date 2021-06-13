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
number of notes you want to use.

```python
from crafters.scale import TraditionalScale

scale = TraditionalScale(12) # 12 is the number of semitones, it starts in La, according to the method "define_scale"
```

Then, instantiate the melody with the scale you created and choose the notes from that
scale you want to include in your melody. 

```python
from crafters.melody import Melody

melody = Melody(scale)
melody.use_note(index, time_duration)
```
In this case, "index" is the index note according to the "i" parameter you used when you created the scale. For example, the index 0 represents the La note, the 1 represents the La#, and so on.

You can use float in time_duration, the unit represents the quarter note, the number 2 represents the half note, and so on

Then, you have to create an instrument as you want, or use the Basic provided.
It is important to override the "timbre" method, with a periodic wave using the 
parameters specified in the abstract method. Also, you can specify the quarter note duration in miliseconds when you create the instrument.

```python
from crafters.instrument import AbstractInstrument

class Instrument(AbstractInstrument):

    def __init__(self, melody, **kwargs):
        super().__init__(melody, **kwargs)

    def timbre(self, note, armonic_number, time):
        return math.sin(2 * math.pi * note * armonic_number * time)

Instrument(melody,quarter_note_duration=600)
```

Once you have created your instrument with the melody you want to
play, set the render directory you want to save the melody and then, build the melody, give it a name and finally, you can listen the
.wav.

```python
i = Instrument(melody) #the melody object is given as an argument to the constructor
render_directory = "path/to/your/render/directory"
i.set_render_directory(render_directory)
i.build_melody("my_melody")

#or
j = Instrument(melody, quarter_note_duration=1000)
i.build_melody("my_slow_melody")
```

For more info, you can checkout the "docs" folder or see the examples files inside examples folder

Enjoy.