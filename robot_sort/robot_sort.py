class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # THE PLAN - Start by using seleciton sort
        # define a method called sort() ** Already done for us **
            # turn on light

            # while the light is on
                # pick up the item at starting position 0 / current position
                # loop through all the elements in self.list by checking if you can move right
                   # compare the item being held to each item at postion to see if it's smaller
                       #if smaller swap the items
                # when the robot can no longer move right but he is holding an item
                    # move left to the empty position
                    # swap item again
                # if robot cannot move right and there he is not holding any item
                    # turn off light
            # return self.list
        pass


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


"""
Understand:
This robot has been given abilities to pick up items, compare it to another item
and swap these items if need be.  This is really everything you need to sort a list.
I have to tell the robot step by step instructions to sort this list by calling it's
built in methods. To further understand i'm going to sort playing cards.

DO NOT:
1. Modify any other robot method other than sort()
2. Store any variables
3. Access instance variables
4. Use any python libraroes or methods

YOU CAN:
1. Use pre-defined robot methods
2. Use logical operators - (`if`, `and`, `or`, `not`)
3. Use comparison operators - (`>`, `>=`, `<`, `<=`, `==`, `is`)
4. Use iterators - (`while`, `for`, `break`, `continue`)
5. Define robot helper method that still follow the rules

Start with 1st pass solution then..
Make sure to do Step 4 of Polya to optimize solution so it's not to slow 
and so that it runs in less that 1 second.

Questions:
* Which sorting method should I use? - 1st pass will be selection sort... optimized
may be Merge Sort.. Divide and conquor...Sounds fitting for a robot..

* Can I use len()? - no 

* Why is it important that the robot only has one bit of memory and that memory
    is it's light? - I assume this means the robot cannot store anything in memory
    which will affect what time of algorithm we use.

Why does the robot need a light to sort items?
Which of it's methods will help me in sorting the list?
Which of the methods if any can i ignore?

* What does it mean when the robot "swaps" something?  - this means that it will
pick up the item in front of it, and put down the item is was holding in the same position.
This results in it holding a new item.

* What is the signifcance or importance of the timer counter? - Maybe it can tell me
how long the list is if the robot moves right until it can't move any more

* What are my inputs - using self.list inside the sort() method, do not have to
pass it in

* What should I be returning - the newly sorted list

* Is it ok to mutate the list? - Should probably never mutate the original collection

PLAN: *** See the sort() method for note and comments on the plan ***
"""