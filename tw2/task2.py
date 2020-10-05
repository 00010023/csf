"""
Teaching Week 1
Blanker Program
"""

# Created new line function does print
# new line
def new_line():
    print(">", "|")
    pass


# A function that does print 3 lines
def three_lines():
    for lines in range(3):
        new_line()
        pass
    pass


# A function that print 3 three lined
# blank lines
def nine_lines():
    for lines in range(3):
        three_lines()
        pass
    pass


# A function that prints 25 lines of
# empty blank lines and cleans space
def clear_screen():
    for lines in range(2):
        nine_lines()
        pass
    for lines in range(2):
        three_lines()
        pass
    for lines in range(1):
        new_line()
        pass
    pass


# Initiating new program and running
# it
if __name__ == '__main__':
    # Nine lines of empty space
    nine_lines()

    # Just a line
    print()

    clear_screen()
    pass
