CaveGame
========
This is a very simple game based on interaction with player to simulate
movement on a map. Player can choose a direction N, S, W, E or Q for
quit.

Two versions of the game exists in this location. One is a complete game
in a single file and second is a group of files working on shelves which
are external files.

cave_game.py
------------
This is the game file.

Depending on players choices it writes players location description and
directions available to move next.

The game file does not contain any text to display for a player.
It reads that data from locations and vocabulary shelve files.

cave_initialise.py
------------------
This is a python file to write shelve files.
It creates and saves content to locations and vocabulary shelves used
in the game.

shelve_challenge.py
-------------------
This is the same initial game file containig whole game in one file.