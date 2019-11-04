from hourofci import *
from .valid import valid

# Go button
# CHANGE: add a go button to start timing

# CHANGE in v3: pass the widget function
def gobtn(question, widget_funct, hash_answer_catalog):
    
    # Create a new button
    button = widgets.Button(description="Go!", 
                           button_style='info',)
        
    # Display button
    display(button)

    # Action for the event listener
    def on_button_clicked(b):
        
        # Start time needs to be passed to the Submit button. 
        global start_time
        start_time = time.time()
        
        # CHANGE in v3: generalize the go button to all widgets
        widget_funct(question, hash_answer_catalog)
           
    # Event Listener Called on CLick
    button.on_click(on_button_clicked)

# Submit button

# CHANGE:
# def button(question, start_time = time.time()):  # When the Go button isn't used

# CHANGE in v2: pass the answer catalog (...to valid())
def button(question, hash_answer_catalog): # When the Go button is used
    
    # For checking the state of the button. Specific for each question.
    global button_state
    button_state = []
    
#     # Get the user start time to evaluate how much time is spent on this module. 
#     start_time = start_time
 
    # Submit Button Creation
    
    button_widget = widgets.Button(
                            value=False,
                            description='Submit',
                            disabled=False,
                            button_style='success', # 'success', 'info', 'warning', 'danger' or ''
                            tooltip='Description',
                            icon='check'
                            )
    
    # Display the button
    display(button_widget)
    

    def on_button_clicked(b):
        
        #CHANGE: set start time as global so that it can be changed when the button is clicked
        global start_time 
        
        # Iris: ???
        # Signifies if the button has been pressed to signal to the evaluator that it can run.
        if len(button_state) < 1:
            
            button_state.append(True)
            
        # Checks if the submit button has been clicked.    
        if button_state[0] == True:
            
            # Answer is the last landed on answer in the dictionary. 
            if len(Answer_Dict[question]) > 0:
                # Iris: the value of a key is an array; -1 means getting the last answer
                answer = str(Answer_Dict[question][-1])
            else:
                # Iris: if the user have submnitted once, and do not select any other answer and then click the button again
                print("Try choosing a different answer!")
                return
             
            # Submission Count Incrementing 
            submission_count[question] += 1
            
            # Temp Values --------------------------------------- CHANGE THESE FOR PROD
            lesson = "gateway"
            lesson_level = "beginner"
            #  ------------------------------------------------------------------------
    
            # Iris: the number of submission for this question so far
            # Question attempts
            attempts = str(submission_count[question])
    
            # Call the validation function
            validation = valid(lesson, lesson_level, question, answer, hash_answer_catalog)   
            validation
                 
            # Default
            correct = "N"
            
            # If validation variable == True, the answer becomes "correct"
            if validation == True:
                correct = "Y"
        
            
            # Date 
            date = datetime.datetime.today().strftime('%Y-%m-%d')
            
            # Time
            time_log = time.strftime("%H:%M:%S", time.gmtime(time.time()))
            
            
            # Total time taken (Calculated everytime submit is pressed)
            time_taken = time.time() - start_time
            print(round(time_taken, 2), "Seconds")
            
            # User ID, but we will have to find a way to calculate it dynamically
            userid = getpass.getuser()
            
            # Log information from logging function
            # Answers variable is located in the logging function

            # Iris: not logging to db in test
            #logging(userid, date, time_log, lesson, lesson_level, question, attempts, time_taken, correct)
            
            #CHANGE: move from before "button_status" to here, clear the previous answers after submitting
            #CHANGE: Actually we don't need this one, since the value will be replaced each time (see widget code)
            # Resets the answers list from Answer_Dict so we are not collecting redundant information
            #Answer_Dict[question] = [None]
            
            #CHANGE: reset the start time after a submission
            start_time = time.time()
                   
    # Checks if the button was clicked
    button_widget.on_click(on_button_clicked)