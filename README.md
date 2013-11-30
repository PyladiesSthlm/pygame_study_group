## BUILDING A DATABASE 

Download these files: 

ftp://ftp.sunet.se/pub/tv+movies/imdb/actresses.list.gz

ftp://ftp.sunet.se/pub/tv+movies/imdb/actors.list.gz

And start on some study material: 

http://en.wikibooks.org/wiki/Think_Python/Files


## BUILDING A GAME 

* Install dependencies with pip:
pip install -r requirements.txt

* Check that you can run the skeleton game
python skeleton.py

* Put any images you want to load in the 'images' folder

More info:
The pygame docs can be found at: http://www.pygame.org/docs/ref/index.html

## INSTALLING PYGAME ON OSX

If you have issues installing the pygame depency on OSX, try: 

* Install homebrew (if you don't already have it): http://brew.sh/

* Open a terminal and run:
brew install sdl sdl_image sdl_mixer sdl_ttf portmidi hg
sudo pip install hg+http://bitbucket.org/pygame/pygame

* Then install the rest of the dependencies:
pip install -r requirements.txt

