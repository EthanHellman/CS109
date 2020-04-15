# Name: Ethan Hellman 
# Stanford email: hellman1@stanford.edu

"""
*************** IMPORTANT ***************
Do NOT rename this file.
Do NOT rename the q14 function or alter its parameters in any way.
Do NOT rename the article_ec function or alter its parameters in any way.

The autograder expects the following:
- Your file should be named cs109_pset1.py
- Your solution to problem 14 should be in a function named q14:
  - it should take 2 arguments as indicated in the provided starter code.
  - it must return a float

Hints:
- Notice the strict inequality in the looping condition
  (until S > 100, and S > 200)
- The function np.random.randint(low, high) is INCLUSIVE of low
  and EXCLUSIVE of high. Hence, we should have low=1 and high=101.
- Player 2 wins if and only if y > x, not when y >= x.
- Player 2 resumes adding from Player 1's sum.
  Player 2 does NOT start over at 0.

Grading:
- The Gradescope autograder will report your problem score
  (i.e., there are no hidden tests). No partial credit will be given
  if you do not pass the autograder.
- You can submit an unlimited number of times. We will only use
  the score from your most recent submission.
"""

# Do NOT add any import statements
import numpy as np

# Instructions:
# Fill in the following function.
# We will be testing your code by setting several random seeds.
# DO NOT ALTER THIS FUNCTION OUTSIDE THE BEGIN/END CODE MARKERS.
# You may add other helper functions if you wish.

def q14(seed: int = 37, ntrials: int = 100000) -> float:
    """
    Plays a game described in q14 ntrials times with a predetermined seed.
    :param seed: seed for the numpy random number generator.
    :param ntrials: the number of trials to run.
    :return: the probability as described in the written pset.
    """
    np.random.seed(seed)
    #################### BEGIN CODE ####################
    player_2_wins = 0
    player_1_number = 0
    player_2_number = 0
    sum = 0

    for i in range(0, 100000):
      sum = 0
      player_1_number = 0
      player_2_number = 0

      while sum < 100 :
        player_1_number = np.random.randint(1, 101)
        sum += player_1_number
      
      while sum < 200 :
        player_2_number = np.random.randint(1, 101)
        sum += player_2_number 
      
      if(player_2_number > player_1_number) :
        player_2_wins+= 1
        
    # You MUST use the function np.random.randint from numpy
    # to generate random numbers, NOT random.randint or
    # any other package.

    return player_2_wins/ntrials
    pass
    ####################  END CODE  ####################

"""
*********** Article submission **********
If you choose to submit an article for extra credit, it should be in
  a function named article_ec:
  - this function should take 0 arguments
  - edit the string variable title to be your article title, e.g.,
    "10 Reasons Why Probability Is Great"
  - edit the string variable url to be a URL to your article, e.g.,
    "http://cs109.stanford.edu/"
  - you should not modify the return value
"""
def article_ec():
    title = "" # your article title here
    url = "" # a link to your article here
    return title, url