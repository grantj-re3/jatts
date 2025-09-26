# jaTTS

jaTTS (pronounced 'Jatz') is a simple Japanese Language TTS (Text-To-Speech) program built
using the Python pyopenjtalk package.


## Usage

```
$ cd path/to/jatts			# jatts project dir
$ source venv/bin/activate		# If required, activate your python virtual environment
$ bin/jatts.py tmp/japanese-test.txt	# Read and speak the content the file in the Japanese language
```

## Configuration

### HTS voice files

Put your XXXX.htsvoice files in the directory etc/voices within the jatts project directory.

I prefer to unzip .htsvoice files into their own subdirectories under etc, then put symlinks
within etc/voices which point to them. E.g. Assuming you have several .htsvoice files within
etc/MMDAgent, then:

```
$ cd etc/voices
$ ln -s ../MMDAgent/*.htsvoice  .	# Symlink to each voice file (using the same filename for the link)
```


### JSON voice configuration file

The voice configuration is stored at etc/default.json within the jatts project directory.
It allows you to select which voice to use, the speaking speed and the speaking pitch.

I prefer to save one or more json configuration files with descriptive names in the etc
directory, then make default.json a symlink to my favourite one.


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

