def fibonacci(n):
    """
    First Assign Variables to give the first numbers of the fibonacci 

    We are going to print the variables to give it a start

    Then we are going to loop so we can keep going

    then we are going to assign it to a new variable then flip it so it can keep going

    then return the answer.
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)



if __name__ == "__main__":
    print(fibonacci(3))
