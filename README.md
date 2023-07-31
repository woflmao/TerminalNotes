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

Add a symbolic link

```
$ chmod +x TerminalNotes
$ cd ~/bin/
$ ln -s ~/some/path/to/TerminalNotes
```
Replace ``` ~/some/path/to/TerminalNotes ``` with the path where you cloned the repo.

Don't know how to do this on windows


# Licence

Made by woflmao under the [MIT licence](https://prodicus.mit-license.org/)

You can find a copy of the License at [http://prodicus.mit-license.org/](http://prodicus.mit-license.org/)
