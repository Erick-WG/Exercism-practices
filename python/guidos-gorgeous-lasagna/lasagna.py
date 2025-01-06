"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(time_in_oven):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    time_remaining = EXPECTED_BAKE_TIME - time_in_oven
    
    return time_remaining


#TODO: Define the 'preparation_time_in_minutes()' function below.

def preparation_time_in_minutes(no_of_layers):
    """Define the preparation_time_in_minutes() function that takes
    the number_of_layers you want to add to the lasagna as an argument
    and returns how many minutes you would spend making them. Assume
    each layer takes 2 minutes to prepare.
    """
    preparation_time = no_of_layers * 2
    return preparation_time



#TODO: define the 'elapsed_time_in_minutes()' function below.
# - function takes one argument (the actual date time object), and returns the elapsed time in minutes
# - you can use the 'datetime' module to get the current time
# - you can use the 'timedelta' class to calculate the difference between two dates

def elapsed_time_in_minutes(no_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.
    """
    layers_time = no_of_layers * 2
    
    elapsed_time = layers_time + elapsed_bake_time
    
    return elapsed_time



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
