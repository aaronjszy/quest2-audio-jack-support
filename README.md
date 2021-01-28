# quest2-audio-jack-support
SolidPython / OpenSCAD model to "fix" broken right side audio for broken quest 2 audio jack.

## How is this supposed to help?
If you unfortunate enough to accidentally pull down hard on your headphone cord while playing, one of the solder joints for a pin on your audio jack may have popped loose. This would cause one of the speakers (probably the right side) to stop working. If you find that pushing up on the plug while you have it plugged in causes it to work than this print might help. It can be hot glued into place and will hold your headphone jack in the "correct" <.< position to make it work.

## Configuration  
Measure the diameter of your headphone plug and set `AUDIO_JACK_DIAMETER` in audio-jack-support.py. Optionally, you can try increasing the `SUPPORT_ANGLE` value a little if you find that it needs to be pushed up a bit further.

## Build the scad file
```
pip install solidpython
python ./audio-jack-support.py
```

## Installation
1. Insert audio jack into support and plug it into the quest, it should fit snugly
2. Hold it all in place and test the audio to see if its held in the right position
3. Unplug it, apply some hot glue to the support, and plug it back in
4. Hold it in place and try to test the audio at the same time to ensure its in the right position
5. Cross your fingers and hope that it keeps working

## Removal
If this doesnt work for you or you need to re-glue it, you can remove it with a pair of pliers. Just carefully pull it off. The glue should peel away without leaving and marks or damage.🤞
