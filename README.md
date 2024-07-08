# TerminalNotes

The lightest weight command line notes app I could think of building, no security, no fluff. Uses tinydb and a couple lines of python.

Inspired by [tnote](https://github.com/tasdikrahman/tnote/tree/master), I just forgot my password and got frustrated one day and wanted to build something without authentication.

# Dependencies

``` 
$ git clone https://github.com/woflmao/TerminalNotes.git
$ cd TerminalNotes && pip install -r requirements.txt
```

made with python3 so you might have to use pip3 install instead

# Running the app
If you downloaded from the releases page, I would suggest putting the .exe in it's own folder, as the db.json will just be created in whatever root folder the .exe is in.

click the exe!

# Installing the app

If you want to build it yourself, follow these steps:

1. pip install pip install pyinstaller

2.
```
pyinstaller --onefile --icon=TerminalNotes.ico TerminalNotes.py
```

*NOTE: I don't know why, but chances are if you build the .exe, in the dist folder you will see NOT the icon you added in the step above, you can copy to another directory which will solve this.
It's something to do with windows caching, but I don't know if it's really important enough. If you know a fix, please PR!*

The exe will be in the newly created 'dist' folder (icon may not be present, see note above)

# Requirements

TinyDB@4.8.0

# Resources

Would have been much worse to use without [pyinstaller](https://pyinstaller.org/en/stable/installation.html), this is a phenomenal program that took very little learning/effort to make it work!

# Licence

Made by woflmao under the [MIT licence](https://prodicus.mit-license.org/)

You can find a copy of the License at [http://prodicus.mit-license.org/](http://prodicus.mit-license.org/)
