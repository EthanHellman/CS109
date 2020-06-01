# Do NOT add any other import statements.
# Don't remove these import statements.
import numpy as np
import copy
import os

# Name:
# Stanford email:

########### CS109 Problem Set 5, Question 8 ##############
def get_filepath(filename):
    """
    filename is the name of a data file, e.g.,
    "learningOutcomes.csv". You can call this helper
    function in all parts of your code.

    Return a full path to the data file, located in the
    directory datasets, e.g., "datasets/learningOutcomes.csv"
    """
    return os.path.join("datasets", filename)

"""
Assembled by Lisa Yan and Past CS109 TA Anand Shankar
*************************IMPORTANT*************************
For part_a and part_b, do NOT modify the name of 
the functions. Do not add or remove parameters to them
either. Moreover, make sure your return value is exactly as
described in the PDF handout and in the provided function 
comments. Remember that your code is being autograded. 
You are free to write helper functions if you so desire.
Do NOT rename this file.
*************************IMPORTANT*************************
"""

def part_a(filename):
    """
    filename is the name of a data file, e.g. 
    "learningOutcomes.csv". You must use the filename 
    variable. Do NOT alter the filename variable, 
    and do NOT hard-code a filepath; if you do, you'll 
    likely fail the autograder.
    You can use the helper function defined above, get_filepath().

    Return the difference in sample means (float) as 
    described in the handout.
    """
    pass  # TODO: delete this line and implement the function.


def part_b(filename, seed=109):
    """
    filename is the name of a data file, e.g. 
    "learningOutcomes.csv". You must use the filename 
    variable. Do NOT alter the filename variable, 
    and do NOT hard-code a filepath; if you do, you'll 
    likely fail the autograder.

    You MUST use np.random.choice with replace=True
    to draw random samples. You may NOT use any other 
    function to draw random samples. See assignment 
    handout for details.

    Return the p-value (float) as described in the handout.
    """
    np.random.seed(seed)  # DO NOT ALTER OR DELETE THIS LINE

    ### BEGIN YOUR CODE FOR PART (B) ###

    # TODO: write some awesome code here.

    ### END YOUR CODE FOR PART (B) ###


def optional_function():
    """
    We won't autograde anything you write in this function.
    But we've included this function here for convenience. 
    It will get called by our provided main method. Feel free
    to do whatever you want here, including leaving this function 
    blank. We won't read or grade it.
    """
    pass


def main():
    """
    We've provided this for convenience, simply to call 
    the functions above. Feel free to modify this 
    function however you like. We won't grade anything in 
    this function.
    """
    print("****************************************************")
    print("Calling part_a with filename 'learningOutcomes.csv':")
    print("\tReturn value was:", part_a('learningOutcomes.csv'))
    print("****************************************************")

    print("****************************************************")
    print("Calling part_b with filename 'learningOutcomes.csv':")
    print("\tReturn value was:", part_b('learningOutcomes.csv'))
    print("****************************************************")

    print("****************************************************")
    print("Calling optional_function:")
    print("\tReturn value was:", optional_function())
    print("****************************************************")


    print("Done!")


# This if-condition is True if this file was executed directly.
# It's False if this file was executed indirectly, e.g. as part
# of an import statement.
if __name__ == "__main__":
    main()
