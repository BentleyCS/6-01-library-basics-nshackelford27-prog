#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)

import analytics
import CSP_5_01_Searching

# Modify the below function such that it takes in a list of prices and returns that list with 15% added value
def process_expenses(rawPrices):
    percentage = []
    for i in rawPrices:
        a = analytics.apply_markup(i, 15)
        percentage.append(a)

    return percentage

# Modify the below function such that it asks the user for n scores and then returns the highest score and the average score of the list.
def analyze_scores(n):
    score = []
    for i in range(n):
        b = int(input("Enter score:"))
        score.append(b)
    c = analytics.get_average(score)
    d = analytics.get_highest(score)

    return c, d



# Modify the below function such that it takes in a list of strings and returns that list with all spaces removed
#and all letters lower case.
def sanitize_usernames(qwerty):
    uiop = analytics.clean_text(qwerty)

    return uiop

# Modify the list such that it takes in a list as an argument and returns a version of the list with all values over 100.
def identify_outliers(wasd):
    dsaw = analytics.filter_threshold(wasd, 100)

    return dsaw


# Modify the below function such that it takes in a list of items and asks the user for an item to search for.
#Sanitize the list to only be lower case words with no extra spaces
#Then return the location of the word using binary search if the list is in order and linear search if it is not.
#example items = ["  Apple", "Banana ", "  CHERRY  ", " date "]
def search_and_report(qwert):
    iop = analytics.clean_text(qwert)
    a = input("Search for item:")
    for i in range(1, len(iop)):
        if iop[i - 1] > iop[i]:
            return CSP_5_01_Searching.linearSearch(iop, a)

    return CSP_5_01_Searching.binarySearch(iop, a)



