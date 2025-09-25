# Title: Bank Balance
# Author: Dalila Spencer
# Date: 2025-09-24

# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################


    # get the user's budget for the month
    budget = float(input('How much money have you budgeted for this month?: '))

    # get the user's expenses for the month
    while spent > 0:
        spent = float(input('How much have you spent? (enter 0 to continue): '))
        total += spent

    #get the difference
    difference = budget - total

    #print the results
    if difference > 0:
        print(f'You are ${difference:,.2f} under your budget. Good job!')

    elif difference == 0:
        print(f'You are ${total:,.2f} over your budget. Good job!')

    else:
        print(f'You are ${total:,.2f} over your budget.')
    ######################


if __name__ == '__main__':
    main()