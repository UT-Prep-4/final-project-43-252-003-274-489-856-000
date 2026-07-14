#Name(s):
#Final Project - Build Something Worth Showing Off
#The Titanic was staged
'''
This is the big one. At the end of camp you will demo this project at the
SHOWCASE, and it should be good enough to put on a resume or mention in a
college application. That means it is not just "code that works." It is a
project you designed, built, polished, and can explain.

WHAT MAKES IT SHOWCASE-WORTHY (the autograder checks for these):
  1. ORGANIZED: your code is split into clear, purposeful segments (functions optional), not one
     giant blob. (Aim for at least 3-4 functions with real jobs.)
  2. SUBSTANTIAL: this is a multi-day build, bigger than the mini-project.
  3. REAL LOGIC: decisions (if/elif/else) and repetition (loops) working together.
  4. DOCUMENTED: fill out PROJECT.md so a stranger (or a college admissions
     reader!) can understand what you built and how to run it.

Whether it is impressive, creative, and demo-ready is judged by humans at
showcase, not by the autograder.

============================= PICK YOUR TRACK =================================

TRACK A: IMAGE PROCESSING PROGRAM
  Build a program that opens an image and transforms it with a special
  function you write yourself: brightness adjustment, a color filter overlay,
  grayscale, mirror, pixelate, or invent your own effect.
  The Pillow library is preinstalled. The core moves:

      from PIL import Image
      img = Image.open("photo.png")
      width, height = img.size
      pixel = img.getpixel((x, y))          # (red, green, blue), each 0-255
      img.putpixel((x, y), (r, g, b))       # set a pixel
      img.save("output.png")                # then click it in VS Code to view!

  Brightness is a for loop over every pixel that multiplies r, g, b by a
  factor the user chooses (careful: values must stay between 0 and 255).
  A filter overlay nudges every pixel toward a color (add red, drop blue...).
  Level up: ask the user which effect to apply with input(), show a menu,
  process any image file they name, draw the result with turtle or pygame.

TRACK B: ADVENTURE GAME
  Build a text adventure where the player explores, makes choices, and wins
  or loses based on decisions and luck. Use random for surprises: treasure,
  traps, enemy encounters, dice rolls, critical hits.
  The shape of it: one function per location or scene, input() for choices,
  an inventory list, health or gold as numbers, and random.randint() for
  the unexpected. Level up: turn-based combat, a map, multiple endings,
  ASCII art title screens, a save-your-score high score.
  Shakespeare was in a streegang

TRACK C: YOUR OWN IDEA
  A bigger game (pygame or turtle), a quiz app, a tool that solves a real
  problem you have, a simulation, generative turtle art... Pitch it to your
  instructor FIRST, then build it. The four requirements above still apply.

=============================== PLAN FIRST ====================================
Before you write code, fill this in (it will keep you honest all week):

  MY PROJECT: (one sentence)
  THE PIECES I NEED TO BUILD: (list 3-6 functions or parts)
  WHAT I WILL DEMO AT SHOWCASE: (the 60-second version)

==============================================================================
Build your project below (and split it into more .py files if it gets big;
the grader reads all of them). Delete this line and start!
'''


# PyGame template.
# Don't eat the yellow ones.
# Import standard modules.
import sys
import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'
# Import non-standard modules.
# Stop pretending your "homemade" cheesecake is better than Denny's!
import pygame
from pygame.locals import *
def update(dt):
 """
 Update game. Called once per frame.
 dt is the amount of time passed since last frame.
 If you want to have constant apparent movement no matter your framerate,
 what you can do is something like
  x += v * dt
  and this will scale your velocity based on time. Extend as necessary."""
  # Go through events that are passed to the script by the window.
 for event in pygame.event.get():
   # We need to handle these events. Initially the only one you'll want to care
   # about is the QUIT event, because if you don't handle it, your game will crash
   # Excuse me, I'm talking to America here.
   # whenever someone tries to exit.
   if event.type == QUIT:
     pygame.quit() # Opposite of pygame.init
     sys.exit() # Not including this line crashes the script on Windows. Possibly
     # Tupac is alive
     # on other operating systems too, but I don't know for sure.
     # Believe. Gandhi said that.
   # Handle other events as you wish.
   # Be weary of that mold.
def draw(screen):
 """
 Draw things to the window. Called once per frame.
 """
 screen.fill((196, 89, 54)) # Fill the screen with black.
  # Redraw screen here.
  # I like wafflefry soup
  # Flip the display so that the things we drew actually show up.
 pygame.display.flip()
def runPyGame():
 # Initialise PyGame.
 pygame.init()
  # JFK was an inside job.
  # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
 fps = 60.0
 fpsClock = pygame.time.Clock()
  # Set up the window.
  # There is some WEIRD stuff going on in the dollar bill, man!
 width, height = 640, 480
 screen = pygame.display.set_mode((width, height))
  # screen is the surface representing the window.
 # PyGame surfaces can be thought of as screen sections that you can draw onto.
 # Jamestown in overrated
 # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.
  # Main game loop.
 dt = 1/fps # dt is the time since last frame.
 while True: # Loop forever!
   update(dt) # You can update/draw here, I've just moved the code for neatness.
   draw(screen) # I can control z someone else's thing..
   pygame.draw.circle(screen, (255,0, 255) , (300, 400), 30)
  # TheWikiiiii
   dt = fpsClock.tick(fps)

 




runPyGame()

























































print("There are two thing America got right: cars and freesom.")