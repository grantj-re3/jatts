#!/usr/bin/env python3
# License: MIT "Expat" License
#
# Usage:  jatts.py  JAPANESE_TEXT_UTF8.txt
##############################################################################

import pyopenjtalk
import numpy as np
from scipy.io import wavfile

import sys
import os
import json
from pathlib import Path
import subprocess
import pprint

##############################################################################
class ProjectPaths:
    _exe_path = None
    _basename = None
    _stemname = None
    _top_path = None

    # ------------------------------------------------------------------------
    @classmethod
    def init_paths(cls):
        cls._exe_path = Path(__file__).absolute()
        cls._basename = os.path.basename(__file__)
        cls._stemname = Path(__file__).stem	# Script filename without path or file extension
        cls._top_path = Path(__file__).parent.parent.absolute()

    # ------------------------------------------------------------------------
    @classmethod
    def exe(cls):
        return cls._exe_path

    # ------------------------------------------------------------------------
    @classmethod
    def basename(cls):
        return cls._basename

    # ------------------------------------------------------------------------
    @classmethod
    def stemname(cls):
        return cls._stemname

    # ------------------------------------------------------------------------
    @classmethod
    def top(cls):
        return cls._top_path

    # ------------------------------------------------------------------------
    @classmethod
    def json_cfg_default(cls):
        return str(cls._top_path / "etc" / "default.json")

    # ------------------------------------------------------------------------
    @classmethod
    def voices_dir(cls):
        return str(cls._top_path / "etc" / "voices")

    # ------------------------------------------------------------------------
    @classmethod
    def wav_path(cls):
        return str(cls._top_path / "tmp" / ("temp-" + cls.stemname() + ".wav"))	# FIXME

##############################################################################
class CommandLineOptions:

    # ------------------------------------------------------------------------
    def __init__(self):
        self.get_json_cfg()
        self.get_cmd_line_cfg()

    # ------------------------------------------------------------------------
    def get_cmd_line_cfg(self):
        if len(sys.argv) < 2:
            print("Usage:  {}  JAPANESE_TEXT_UTF8.txt".format(ProjectPaths.basename()))
            sys.exit(1)

        else:
            self.text_input_fname = sys.argv[1]

        if os.path.isfile(self.text_input_fname) and os.access(self.text_input_fname, os.R_OK):
            with open(self.text_input_fname, 'r') as f:
                self.text = f.read()

        else:
            print("File {} does not exist or is not readable".format(ProjectPaths.basename()))
            sys.exit(1)

    # ------------------------------------------------------------------------
    def get_json_cfg(self):
        # Load the json file into a dict
        json_path = ProjectPaths.json_cfg_default()
        with open(json_path) as f:
            self.cfg = json.load(f)

        # Put dict values into instance vars
        self.speed		= self.cfg['speed']
        self.add_half_tone	= self.cfg['add_half_tone']
        self.hts_voice_file	= self.cfg['hts_voice_file']

        if self.hts_voice_file.startswith('/'):
            self.hts_voice_path = self.hts_voice_file
        else:
            self.hts_voice_path = ProjectPaths.voices_dir() + "/" + self.hts_voice_file

##############################################################################
class VoiceEngine:
    _audio_player_cmd = "aplay"

    # ------------------------------------------------------------------------
    def __init__(self, opts):
        self.opts = opts
        self.engine = pyopenjtalk.HTSEngine(self.opts.hts_voice_path.encode("utf-8"))
        self.sr = self.engine.get_sampling_frequency()
        self.engine.set_speed(self.opts.speed)
        self.engine.add_half_tone(self.opts.add_half_tone)

    # ------------------------------------------------------------------------
    def write_wavfile(self):
        print("Writing to file:", ProjectPaths.wav_path())
        x = self.engine.synthesize(pyopenjtalk.extract_fullcontext(self.opts.text))
        wavfile.write(ProjectPaths.wav_path(), self.sr, x.astype(np.int16))

    # ------------------------------------------------------------------------
    def play_wavfile(self):
        subprocess.run([VoiceEngine._audio_player_cmd, ProjectPaths.wav_path()]) 

##############################################################################
# Main
##############################################################################
ProjectPaths.init_paths()
opts = CommandLineOptions()

vengine = VoiceEngine(opts)
vengine.write_wavfile()
vengine.play_wavfile()

