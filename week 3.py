#%%
#

'''

Welcome to week 3!

Please review and run the following code to see how conditionals and loops work!

You can play around with the value(s) to have hte program show different branches!

'''

#%%
# Looping Function

def loop_function(x):

    # Here is an example of a "for" loop
    for i in range(x):

        # Here is an example of a conditional statement
        # If hte remainder of i divided by 2 is 0, then it is an even number
        if i % 2 == 0:
            print(i, "is even!")
        else:
            print(i, "is an odd number!")

    print("Done!")


number_of_loops = 10

loop_function(number_of_loops)
# %%
# Looping Function

def loop_function(x):
    # Here is an example of a "for" loop
    for i in range(x):
        # Here is an example of a conditional statement
        # If the remainder of i divided by 2 is 0, then it is an even number
        if i % 2 == 0:
            print(i, "is even!")
        else:
            print(i, "is odd!")

    print("Done!")

# Define the number of loops
number_of_loops = 10

# Call the function with the specified number of loops
loop_function(number_of_loops)
# %%
#%% Intro
#%% Intro
#%% Intro

'''
Please The following code SHOULD run and FINISH...but doesn't

This is an example of an infinite loop.  This is NOT a good thing to 
have in your code.  It will cause your code to run forever and never
finish.  This is a problem because it will cause your code to use up
all of the resources on your computer and cause it to crash.

Please fix the code so that it runs and finishes.

You should only need to change two lines of code to fix this problem!
'''


#%%
# Code

finished_program = False

# Count to 10 Program

while finished_program == False:

    i = 0

    print(f'Testing i = {i}')

    if i == 10:
        finished_program = True

    i += 1
# %% 
# Code 

finished_program = False
i = 0 # Move i outside the loop

while finished_program == False:
    
    print(f'Testing i = {i}')

    i += 1 # Increment before checking the condition   

    if i == 10:
        finished_program = True
# %%
# Objective: Write a program that takes a list of numbers and prints out the sum, average, and largest number in the list.



# Problem 1: Write a program that takes a list of numbers and prints out the sum of all the numbers in the list.



# Problem 2: Write a program that takes a list of numbers and prints out the average of all the numbers in the list.



# Problem 3: Write a program that takes a list of numbers and prints out the largest number in the list.

#%%
# Define  a list of numbers
numbers = [10,20,30,40,50] 

# Problem 1: Calculate and print the sum of all the numbers 
total_sum = sum(numbers)
print(f'The sum of the numbers is: {total_sum}')

# Problem 2: Calculate and print the average of all the numbers
average = total_sum / len(numbers) if numbers else 0
print(f'The average of the numbers is: {average}')

# Problem 3: Find and print the largest number in the list
largest_number = max(numbers) if numbers else None  
print(f'The largest number in the list is: {largest_number}')
# %%