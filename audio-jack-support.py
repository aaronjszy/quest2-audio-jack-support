#! /usr/bin/env python

# python audio-jack-support.py

from solid import *
from solid.utils import *

AUDIO_JACK_DIAMETER = 6.5
SUPPORT_ANGLE = 2 # Angle the support UP a little bit

config = {
    "height": 18,
    "support": {
        "diameter": 10,
        "xAngle": -SUPPORT_ANGLE,
    },
    "base": {
        "height": 10,
        "diameter": 20,
    },
    "hole": {
        "diameter": AUDIO_JACK_DIAMETER,
    },
    "enclosure": {
        "diameter": 109,
        "xOffset": 8.9,
        "yOffset": 9,
        "visible": False,
        "enabled": True,
    },
}

# -----------------------

class AudioJackSupport():
    def __init__(self, config):
        self.config = config

    def assemble(self):
        jack_support = rotate([0,self.config["support"]["xAngle"],0])(
            cylinder(h = self.config["height"], d=self.config["support"]["diameter"]))
        jack_support_hole = rotate([0,self.config["support"]["xAngle"],0])(
            translate([0, 0, -10])(
                cylinder(h = self.config["height"]+20, d=self.config["hole"]["diameter"])))
        base = cylinder(h = self.config["base"]["height"], d=self.config["base"]["diameter"])

        enclosure_depth = 100
        enclosure = rotate([90,0,0])(
            translate([-self.config["enclosure"]["xOffset"],-(self.config["enclosure"]["diameter"]/2) + self.config["enclosure"]["yOffset"],-enclosure_depth/2])(
                cylinder(h = enclosure_depth, d=self.config["enclosure"]["diameter"])))

        assembly = ((base + jack_support) - jack_support_hole)

        if(self.config["enclosure"]["enabled"]):
            if(self.config["enclosure"]["visible"]):
                assembly += enclosure
            else:
                assembly -= enclosure
        
        return  assembly

if __name__ == '__main__':
    a = AudioJackSupport(config).assemble()
    scad_render_to_file(a, "audio-jack-support.scad", file_header='$fn = 100;', include_orig_code=True)
