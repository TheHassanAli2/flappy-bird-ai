# flappy-bird-ai
Create an ai for the popular game flappy bird to learn neural networks and basic reinforcement learning with games.

We'll be expanding on what we've learned from Hassan in this slideshow on the Introduction to Machine Learning: https://docs.google.com/presentation/d/1ySxGJUtw_h__lznZO3IgjoEH2n5dlvtBip-fLgNjAFw/edit?usp=sharing

## Development:

### Setting Up a Python Virtual Environment

- Create a Python virtual environment by typing `python3 -m venv venv` 
  - You may need to use a different command instead of `python3` such as `python` or `py` (this can be tested by simply typing this command alone and seeing if it opens the Python interpreter which says your Python version and includes `>>>` at the bottom to indicate where you're supposed to code)
  - the last term in this command `venv` can be changed to whichever name you'd like to give it
- To activate this virtual environment:
  - Type `source venv/bin/activate` on a UNIX system such as MacOS or Linux
  - Type `venv\Scripts\activate` on Windows
- Once you'd like to deactivate it, type `venv\Scripts\deactivate` on Windows or `deactivate` on a UNIX-based OS


## Create Game:

Chrome dinosaur game in pygame: https://www.youtube.com/watch?v=lcC-jiCuDnQ (first video in a series) 

We can extrapolate from this video and others about making pygames to make Flappy Bird rather than copying directly so we learn more from this experience.  

- Create canvas using pygame
- Create Player class for the flappy bird (Jump)
- Create pipes (paired up, move to the left from the right)
  - Use coordinates of the pipes and the bird to check collisions
- Add a score
- Add the game over sequence

Try not to use videos of this exact project because then you're not trying to apply something you've learned, you're just copying.

## Create AI:


- Change config.txt
- Import NEAT library
  - Setup the NEAT algorithm
Modify Game to work with the algorithm

Resource: https://youtu.be/CKFCIzPSBjE (same playlist as video from before used to make the game itself, just the 3rd of the series)
