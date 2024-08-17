from datetime import date
import sys

dateToday = str(date.today())
lift_string = ""
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

def choose_lift():
    """
    Ask for an input to select the lift
    runs until a correct input is given
    """
    while True:
        lift = safeinput('Enter the chosen lift (' + ",".join(list(lift_translation.keys())) + "): ", str)     
        lift_string:str 
        try:               
            lift_string = lift_translation[lift.upper()]
            return lift_string
        except:
            pass

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

def checkfile():
    """
    Check to see if the textfile exists
    if it doesnt exist then create the file and print a heading at the top.
    """
    try:
        open(lift_string + ' Sessions.txt')  
    except:
        with open (lift_string + ' Sessions.txt', 'w') as text_file:
            print(f"Record of all Squat Sessions", file=text_file) 
def rw_input(y):
    x = [0]*sets_input
    for i in range(0, sets_input):
        x[i] = safeinput(f"{y} for set {i+1}: ",int)
    return x

def output():
    with open(lift_string + ' Sessions.txt', "a") as text_file:
        print(f"\n{lift_string} Session ({dateToday}):", file=text_file)
        for i in range(0,sets_input):
            print(f"{weight[i]}kg x {reps[i]}", file=text_file) 


#Repeat until user selects not to continue
while True:       

        lift_string = choose_lift()       
        sets_input = safeinput('Number of sets: ',int)
        print()
        """
        Only continue if you the input is greater than 0
        Inputing 0 will ask them if they want to start again or end
        """
        if sets_input > 0:         
            checkfile()
            """
            Ask for rep and weight inputs
            Add the inputs into the correct textfile
            """         
            reps = rw_input("Reps")
            print()
            weight = rw_input("Weight")
            print()
            output()          
            cont()
        else:
            cont()