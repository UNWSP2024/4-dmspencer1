# Title: Movie Tix
# Author: Dalila Spencer
# Date: 2025-09-24

# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################

    # Loop until n
    #   Show movie list
    #   Prompt movie
    #   Prompt number of tickets
    #   Add num_tickets to movie variable
    #   Prompt for another movie
    # Print total tickets for each movie
    # Print total tickets


    doomsday = 0
    jaws = 0
    httyd = 0
    hunger_games = 0
    pirates = 0
    repeat = 'y'

    while repeat == 'y':

        movie_list = '''1. Avengers: Doomsday 
2. Jaws 50th Anniversary
3. How to Train Your Dragon
4. The Hunger Games
5. Pirates of the Caribbean: Curse of the Black Pearl '''

        #gets what movie the user wants to see
        movie = int(input(f'''What movie would you like to see?
{movie_list}
Please enter the number of the movie you would like to see: '''))

        if movie <= 0 or movie > 5: # validation loop
            print ('Error: Please enter a valid movie number.')
            movie = int(input(f'''What movie would you like to see? 
{movie_list}
Please enter the number of the movie you would like to see: '''))

        #gets how many tickets the user wants
        num_tickets = int(input('How many tickets would you like?: '))

        if num_tickets <= 0 or num_tickets > 100: # validation loop
            print ('Error: Please enter a valid number.')
            num_tickets = int(input('How many tickets would you like?: '))

        #counts how many tickets for each movie
        if movie == 1:
            doomsday += num_tickets
        elif movie == 2:
            jaws += num_tickets
        elif movie == 3:
            httyd += num_tickets
        elif movie == 4:
            hunger_games += num_tickets
        elif movie == 5:
            pirates += num_tickets

        # asks if the user wants to see another movie
        repeat = str(input('Would you like to see another movie? y/n: '))

    #prints tickets
    print(f'''Here are your tickets:
Avenger's Doomsday: {doomsday}
Jaws 50th Anniversary: {jaws}
How to Train Your Dragon: {httyd}
The Hunger Games: {hunger_games}
Pirates of the Caribbean: {pirates}
Total tickets: {doomsday + jaws + httyd + hunger_games + pirates}''')

    ######################


if __name__ == '__main__':
    main()