def fibonacci(n):
    """
    First Assign Variables to give the first numbers of the fibonacci 

    We are going to print the variables to give it a start

    Then we are going to loop so we can keep going

    then we are going to assign it to a new variable then flip it so it can keep going

    then return the answer.

    I got a HUGE help from Code Review and also this youtube video 

    https://www.youtube.com/watch?v=7Sv4NmvdHcw
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """
    This is the Lucas Function
    Takes a number as input
    It will tell you what the number in the lucas it is
    Once again, code review helped me with this
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, parameter1=0, parameter2=1):
    """
    this is the sum series
    it will take three params with the last two being optional
    the first parameter will determine which element in the series to print
    the second will default to 0 and 1 and will come up up with the first two values for the series
    Big help from code review
    """
    if parameter1 == 0:
        return fibonacci(n)
    elif parameter2 == 2:
        return lucas(n)
   
