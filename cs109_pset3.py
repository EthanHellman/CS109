# Name: Ethan Hellman
# Stanford email: hellman1@stanford.edu

########### CS109 Problem Set 3, Question 1 ##############
"""
************************IMPORTANT************************
For all parts, do NOT modify the names of the functions.
Do not add or remove parameters to them either.
Moreover, make sure your return value is exactly as 
described in the PDF handout and in the provided function 
comments. Remember that your code is being autograded. You
are free to write helper functions if you so desire.
Do NOT rename this file.
************************IMPORTANT************************
"""

# Do not add import statements.
# Do not remove this import statement either.
from numpy.random import rand

# part (a) - completed for you
def simulate_bernoulli(p=0.4):
    if rand() < p:
        return 1
    return 0


# part (b)
def simulate_binomial(n=20, p=0.4):
  successes = 0
  for i in range(n):
    successes += simulate_bernoulli(p)

  return successes


# part (c)
def simulate_geometric(p=0.03):
  trials = 0
  while(simulate_bernoulli(p) == 0):
    trials += 1

  return trials+1


# part (d)
def simulate_neg_binomial(r=5, p=0.03):
  trials = 0
  for i in range(r):
    trials += simulate_geometric(p)

  return trials


# Note for parts (e) and (f):
# Since `lambda` is a reserved word in Python, we've used
# the variable name `lamb` instead. Do NOT use the word
# `lambda` in your code. It won't do what you want!


# part (e)
def simulate_poisson(lamb=3.1):
  new_lambda = lamb/60000
  events = 0
  for i in range(60000):
    events += simulate_bernoulli(new_lambda)

  return events



# part (f)
def simulate_exponential(lamb=3.1):
  new_lambda = lamb/60000
  time = 0
  while(simulate_bernoulli(new_lambda) == 0):
      time += 1

  return time/60000

def main():
    """
    We've provided this for convenience.
    Feel free to modify this function however you like.
    We won't grade anything in this function.
    """
    print("Bernoulli:", simulate_bernoulli())
    print("Bernoulli:", simulate_binomial())
    print("Bernoulli:", simulate_geometric())
    print("Bernoulli:", simulate_neg_binomial())
    print("Bernoulli:", simulate_poisson())
    print("Bernoulli:", simulate_exponential())
    __, title, __ = article_ec()
    print(title)

########### CS109 Problem Set 3, Question 13 ##############
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
    title = "Machine learning cracks quantum chemistry conundrum" # your article title here
    url = "https://phys.org/news/2020-05-machine-quantum-chemistry-conundrum.html" # a link to your article here
    return sunetid, title, url


############################################################
# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()