from datetime import date
import sys
import json

dateToday = str(date.today())
lift_string = ""
lift_translation = {
    "S" : "Squat",
    "B" : "Bench",
    "D" : "Deadlift",
}
sessions_dict = {}

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

def continue_checker(): 
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

def rw_input(y):
    x = [0]*sets_input
    for i in range(0, sets_input):
        x[i] = safeinput(f"{y} for set {i+1}: ",int)
    return x

def save_file():
    sessions_dict = {dateToday:[]}
    for i in range(0,sets_input):
        sessions_dict[dateToday].append({"rep"+str(i+1) : reps[i],"weight"+str(i+1)  : weight[i]})
    
    with open(lift_string + ' Sessions.json', "a") as f:
        json.dump(sessions_dict,f)
            

if __name__ == '__main__':
    #Repeat until user selects not to continue
    while True:       

            lift_string = choose_lift()       
            sets_input = safeinput('Number of sets: ',int)
            print()
            """
            Only continue if the input is greater than 0
            Inputing 0 will ask them if they want to start again or end
            """
            if sets_input > 0:         
                """
                Ask for rep and weight inputs
                Add the inputs into the correct textfile
                """         
                reps = rw_input("Reps")
                print()
                weight = rw_input("Weight")
                print()
                save_file()          
                continue_checker()
            else:
                continue_checker()