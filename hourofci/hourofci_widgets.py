from hourofci import *
from .buttons import button
# import buttons

# CHANGE in v2: pass the answer catalog in the notebook to the widget function
def IntSlider(question, hash_answer_catalog):
    # start_time = time.time()
    int_range = widgets.IntSlider()
    display(int_range)
    value = 10
    
    # Iris: where to get change?
    def on_value_change(change):
        
        # CHANGE: append -> replace (only keep the last answers between two submissions)
        Answer_Dict[question]=[change["new"]]
        
    int_range.observe(on_value_change, names='value')
     
    # Button Evaluator with arguments (desired_answer, frmt) | Fmrt is the format to evaluate like single item, list, dict, etc
    # CHANGE in v2: pass the answer catalog to the submit button function to valid
    button(question, hash_answer_catalog)