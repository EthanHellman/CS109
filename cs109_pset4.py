# Name:
# Stanford email:

########### CS109 Problem Set 4, Question 10 ##############

# Do NOT add any other import statements.
# Don't remove this import statement.
import numpy as np
from probabilities import *

"""
Starter Code for CS 109 Problem Set 4

*************************IMPORTANT*************************
The file probabilities contains helper functions 
probStress(), probExposure(), probCold(s, e), probFlu(s, e), 
and probSymptom(i, f, c). You should NOT re-implement these
functions; they are imported for you already.

We may additionally test your code with different values
from what is provided to you.

You can call the functions directly from this file:
  x = probFlu() + 5     # not a probability

*************************IMPORTANT*************************
"""


def inferProbFlu(ntrials = 1000000) -> float:

  samples = np.zeros((ntrials, 3))
  exposure = 0
  stress = 0
  cold = 0
  flu = 0
  X_2 = 0

  for i in range(ntrials):

    if np.random.rand() < probExposure():
        exposure = 1
    else:
      exposure = 0

    if np.random.rand() < probStress():
        stess = 1
    else:
      stress = 0
    
    if np.random.rand() < probCold(stress, exposure):
        cold = 1
    else:
      cold = 0

    if np.random.rand() < probFlu(stress, exposure):
        flu = 1
    else:
      flu = 0
    
    if np.random.rand() < probSymptom(2, flu, cold):
        X_2 = 1
    else:
      X_2 = 0
      
    samples[i, 0] = flu
    samples[i, 1] = exposure
    samples[i, 2] = X_2
  
  occurences = samples[samples[:,1] == 1]
  occurences = occurences[occurences[:, 2] == 1]
  flu_occurences = occurences[occurences[:,0] == 1]

  return flu_occurences.shape[0]/occurences.shape[0]




def inferProbFluExact() -> float:
    """
    This is question 10 part (b). This is a REACH problem, meaning 
    that thinking about it will be useful, even if we don't expect
    you to be able to perfectly solve the problem. Show your work.
    If you get stuck (> 15 mins), explain what is hard and
    include your explanation in your writeup, not in your code.

    Computes P(Flu = 1 | Exposure = 1, X_2 = 1) exactly without
    using rejection sampling.
    """
    return -1 # TODO: delete this line and implement the function!


def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    print("***********************************************************")
    print("(a) Calling inferProbFlu():")
    print("\tReturn value was:", inferProbFlu())
    print("***********************************************************\n")

    print("***********************************************************")
    print("(b) Calling inferProbFluExact():")
    print("\tReturn value was:", inferProbFluExact())
    print("***********************************************************\n")

    print("Done!")


########### CS109 Problem Set 4, Question 12 ##############
"""
*********** Article submission **********
If you choose to submit an article for extra credit, it
  should be in a function named article_ec:
  - this function should take 0 arguments
  - edit the string variable sunetid to be your SUNetID,
    e.g., "yanlisa"
  - edit the string variable title to be your article title,
    e.g., "10 Reasons Why Probability Is Great"
  - edit the string variable url to be a URL to your article,
    e.g., "http://cs109.stanford.edu/"
  - you should not modify the return value
"""
def article_ec():
    sunetid = "06343801" # your sunet id here.
    title = "COVID-19 Brings Calculus, Stats, Probability Theory into Our Daily Lives" # your article title here
    url = "https://businessjournaldaily.com/covid-19-brings-calculus-stats-probability-theory-into-our-daily-lives/" # a link to your article here
    return sunetid, title, url


############################################################
# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
