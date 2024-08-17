from datetime import date
import sys

dateToday = str(date.today())

lift_translation = {
    "S" : "Squat",
    "B" : "Bench",
    "D" : "Deadlift",
}

def safeinput(inp,type):
    while True: 
        try:
            return type(input(inp))         
        except:
            print("Please enter a valid input")

"""
Ask the user if they would like to continue and add another session or end
checks for correct input of Y or N (accepts lowercase)
asks for a correct input if the user inputs anything else
"""         
def cont(): 
    end = safeinput('Would you like to enter another session? (Y/N): ',str)      
    while True:              
        match end.upper():
            case 'Y':
                print()
                break
            case 'N':
                sys.exit()
            case _:
                end = safeinput("Please enter Y or N: ",str)


#Repeat until user selects not to continue
while True:       
        """
        Asks for an input to select the lift to add to
        runs until a correct input is given
        """
        while True:
            lift = safeinput('Enter the chosen lift (' + ",".join(list(lift_translation.keys())) + "): ", str)
            lift_string : str
            try:               
                lift_string = lift_translation[lift.upper()]
                break
            except:
                pass

        sets_input = safeinput('Number of sets:\n',int)
        print()

        """
        Only continue if you the input is greater than 0
        Inputing 0 will ask them if they want to start again or end
        """
        if sets_input > 0:         
            """
            Check to see if the textfile exists
            if it doesnt exist then create the file and print a heading at the top.
            """
            try:
                open(lift_string + ' Sessions.txt')  
            except:
                with open (lift_string + ' Sessions.txt', 'w') as text_file:
                    print(f"Record of all Squat Sessions", file=text_file) 
            """
            Ask for rep and weight inputs
            Add the inputs into the correct textfile
            """         
            reps = [0]*sets_input
            weight = [0]*sets_input
            for i in range(0, sets_input):
                reps[i] = safeinput(f"Reps for set {i+1}:\n",int) 
            print()  
            for i in range(0, sets_input):    
                weight[i] = safeinput(f"Weight for set {i+1}:\n", int) 
            with open(lift_string + ' Sessions.txt', "a") as text_file:
                print(f"\n{lift_string} Session ({dateToday}):", file=text_file)
                for i in range(0,sets_input):
                    print(f"{weight[i]}kg x {reps[i]}", file=text_file)                       
            cont()

        else:
            cont()