'''
Welcome to Homework #2.

This one has a few more methods for you to implement.
When you start implementing a method, remember to delete the line that says "pass", that just exists to stop python
exploding because there's no code within a method!.

When you think you've got a method done, run the automatic tests in test_homework.py. I've tried to include helpful
messages if your method doesn't quite pass a test that might guide you along the way, so pay attention to the text in
the console if the test isn't passing. If you're still struggling after that, ask each other or me for help and I'll do
my best.

If you haven't implemented all of the methods, the tests for the other methods will appear as failed, so don't worry if
you see a lot of red symbols when you run it for the first time, just pay attention to the test for the method you're
currently implementing.

You can delete the comments if they're cluttering the screen for you. Just remember what they say if you need help ;)

I will ask you to submit your homework back up to GitHub once you've done it so I can see the results this time.
I will check everyones answers on the 30th or when everyone says they're done, whichever comes first.
'''




list1 = [1, 2, 3, 4, 5]
list2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
list3 = ['apple', 'banana', 'tomato']

# Write a function here that will add up all the numbers into a list and return the total.
# ie. [4, 7, 12, 16] returns 39
def sum_all_in_list(list):
    return sum(list)
    #or
def sum_all_alt(list):
    total = 0
    for i in list:
        total = total + i
    return total

sum_all_in_list(list1)
sum_all_alt(list1)

# Write a function that will merge a list of lists together. ie. [[4, 2, 6], [2, 4, 7], [9, 2, 6]]
# becomes one list of [4, 2, 6, 2, 4, 7, 9, 2, 6]
def merge_two_lists(list):
    newList =[]
    for i in list:
        for x in i:
            newList.append(x)
    return newList

merge_two_lists(list2)


# Write a function that will find the smallest number in a list and return it.
# ie. [6, 2, 7, 99] returns 2. (There are two main ways you can do this, bonus points if you can find both)
def get_smallest_number_in_list(list):
    # return min(list)
    x = 100
    for i in list:
        if i < x:
            x = i
    return x


# Write a function that will remove all even numbers from a list of numbers.
# You can do this by creating a new list, looping through the old list and adding the odd numbers to the new list
# Don't try and remove numbers from a list you're currently looping through
# ie. [2, 5, 8, 2, 3, 7] becomes [5, 3, 7]
# If there are no odd numbers in the whole list, return an empty list
def return_odd_numbers(list):
    newList =[]
    for i in list:
        if i %2 != 0:
            newList.append(i)
    return newList

return_odd_numbers(list1)


# append a string to all elements in a list and return the list of all.
# ie. append_to_all_elements(["hey", "there", "friend"], "lol") returns ["heylol", "therelol", "friendlol"]
def append_to_all_elements(list, string):
    newList = []
    for i in list:
        newList.append(i + string)
    return newList

append_to_all_elements(list3, "ta-dah")

# return a list of each character in a string
# ie. list_of_characters_in_string("Hello") returns ["H", "e", "l", "l", "o"]
# Hint, doing 'for x in "string":' will loop through each character in the string.
def list_of_characters_in_string(string):
    newList =[]
    for i in string:
        for x in i:
            newList.append(x)
    return newList


# Use the space below this line to call your methods and print out the results to check you've got the answer.
