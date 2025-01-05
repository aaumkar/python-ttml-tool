# python-ttml-tool
Python based CLI tool to record TTML Lyrics for Apple Music.

This is a very quick and dirty CLI tool to quickly get a .ttml file based closely on [Apple Music TTML Guide](https://help.apple.com/itc/videoaudioassetguide/?lang=en#/itcd7579a252).


### How to use it?

I am hoping that you can 
- work with `python` (venv preffered for hygene)
- work with a MIDI keyboard
- play your lyrics simultaneously as running this code

#### Getting it running

###### Install the dependancies
```bash
pip3 install -r requirements.txt
```

###### Put lyrics in the `lyrics.txt`
Please have in mind
- The first line should not be blank
- Stanzas should have ONLY single blank line separating
- Follow lyrics guidelines in [Apple Video and Audio Asset Guide](https://help.apple.com/itc/videoaudioassetguide/?lang=en#/itc7e7182942)

###### Running the program
Prepare a media player and run the program. 
Try as best as possible to run them simultaneously. (I know, but this is quick and dirty, remember?)
- When you want to record start time of the line, press any MIDI key.<br/> I am looking for `note_on` event.
- When you want to record end time of the line, release any MIDI key.<br/> I am looking for `note_off` event.



This works for me, but welcome improvements/suggestions.