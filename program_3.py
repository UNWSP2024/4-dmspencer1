# Title: Average Rainfall
# Author: Dalila Spencer
# Date: 2025-09-24

# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################


    #gets number of years
    num_years = int(input('How many years?: '))

    total_rain = 0.0

    #gets rain for each month in each year
    for year in range(num_years):
        for month in range(12):
            total_rain += float(input(f'How many inches of rain were there in month {month + 1} of year {year + 1}?: '))
    total_months = 12 * num_years

    #prints the results
    print(f'Total number of months: {total_months}')
    print(f'Total rain: {total_rain:.1f} inches')
    print(f'Average rain per months: {total_rain / total_months:.1f} inches')

    ######################


if __name__ == '__main__':
    main()