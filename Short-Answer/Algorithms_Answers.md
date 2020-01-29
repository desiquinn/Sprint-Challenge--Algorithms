#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) n is our input. If n gets bigger, this program will perform more operations (for loops). Since n is cubed on line 2, as our input gets bigger, the number of operations has a polynomial growth at a worst case scenario of O(n^3). 


b) n is our input. If n gets bigger, this program will perform more operations (for loops). There is also a nested loop that depends on the size of n as well.  So the number of operations will have a polynomial growth at worst case scenario of O(n^2).


c) Bunnies (specifically the amount of bunnies) is our input. This is also a recursive algorithm. So the size of bunnies will affect how many operations it will take to converge this program on it’s base case. The number of operations will have a liner growth at worst case scenario of O(n) because as the growth in inputs is the same as the growth in operations. If I have 10 bunnies, I will have 10 operations, if I have 100 bunnies i will have 100 operations.

## Exercise II

Pseudo Code:

#Assume that all floors are in order from 1 - n_story
#Define a function named broken_egg_floor that takes in one argument: n_story
    # store a count of dropped eggs
    # store true or false in broken egg

    # create an empty variable named f
    # find middle floor and store it in a variable named mid
    # store bottom half of building in a variable named bottom
    # store top half of build in a variable named top

    # while length of bottom half is > 1
        # add 1 count to  dropped eggs
        # if egg breaks
             # store floor in variable f
             # find new middle in bottom half and reassign mid
             # re assign the bottom and top halves to respective halves of the original bottom
        # if egg does not break
             # find a new middle in top half and reassign mid
             # re assign the bottom and top halves to respective halves of the original top
    # return the variable f that tells us which floor is the highest we can go and only break 1 egg
   

Run Time Complexity:

n is the number of floors (n_story) being passed into the function. The size of n affects how many operations we will need to do in this case so we can rule out O(1), the rate of growth will not be the same so we can rule out O(n), and the growth of operations is slower than the growth of inputs n because we do less operations then there are inputs.  Therefore we can rule out everything else except a logarithmic growth O(log n)

