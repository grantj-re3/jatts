# jaTTS

jaTTS (pronounced 'Jatz') is a simple Japanese Language TTS (Text-To-Speech) program built
using the Python pyopenjtalk package.

This program does not yet handle errors gracefully.


## Usage

```
$ cd path/to/jatts			# jatts project dir
$ source venv/bin/activate		# If required, activate your python virtual environment
$ bin/jatts.py tmp/japanese-test.txt	# Read and speak the content the file in the Japanese language
```

## Configuration

### JSON jatts configuration file

The jatts configuration is stored at etc/default.json within the jatts project directory.
It allows you to select which voice to use, the speaking speed and the speaking pitch.

I prefer to save one or more json configuration files with descriptive names in the etc
directory, then make default.json a symlink to my favourite one.


### HTS voice files

Put your XXXX.htsvoice files in the directory etc/voices within the jatts project directory.

I prefer to unzip .htsvoice files into their own subdirectories under etc, then put symlinks
within etc/voices which point to them. E.g. Assuming you have several .htsvoice files within
etc/MMDAgent, then:

```
$ cd etc/voices
$ ln -s ../MMDAgent/*.htsvoice  .	# Symlink to each voice file (using the same filename for the link)
```

### Where did the voice-file used in this repository come from?

The voice-file used in this repository is at
etc/pyopenjtalk/htsvoice/mei_normal.htsvoice. The symlink at
etc/voice/pyopenjtalk_mei_normal.htsvoice points to it. This file
(with CC-BY-3.0 license) was sourced from the pyopenjtalk package.
I have included it so you don't have to find the copy that comes
with your own pyopenjtalk package.

You should be able to run jatts.py without this voice-file by pointing
to your own copy in one of the following ways.

Let's assume you can find your own pyopenjtalk package copy, and the path
to it is /MY/PATH/TO/pyopenjtalk/htsvoice/mei_normal.htsvoice.


**Alternative 1: Symlink to it from the etc/voices folder**

The symlink created below with the "ln" command can be a relative path
(not starting with "/") or absolute (starting with "/").

```
$ cd etc/voices
$ ln -s /MY/PATH/TO/pyopenjtalk/htsvoice/mei_normal.htsvoice  my_mei_normal.htsvoice
```

Now you have a copy in the etc/voices folder which you can reference
inside your json file with:

```
  "hts_voice_file": "my_mei_normal.htsvoice",
```


**Alternative 2: Point to it directly from your json file**

You don't need a copy within your etc/voices folder at all. Simply
point to the voice-file directly with an absolute path starting
with "/".

```
  "hts_voice_file": "/MY/PATH/TO/pyopenjtalk/htsvoice/mei_normal.htsvoice",
```


## Environment

I have successfully run this script in the following environment.

```
Linux 6.1.0-21-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.90-1 (2024-05-03) x86_64 GNU/Linux
MX Linux        23.3
Python          3.11.2
python3-venv    3.11.2

pip             23.0.1
pyopenjtalk     0.4.1
scipy           1.16.2
```

