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

use [pyinstaller](https://pyinstaller.org/en/stable/installation.html)

```
pyinstaller --onefile --icon=TerminalNotes.ico TerminalNotes.py
```

Check the 'dist' folder, and you will se 

# Requirements

TinyDB@4.8.0


# Licence

Made by woflmao under the [MIT licence](https://prodicus.mit-license.org/)

You can find a copy of the License at [http://prodicus.mit-license.org/](http://prodicus.mit-license.org/)