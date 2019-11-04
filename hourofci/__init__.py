from IPython.display import display, clear_output
from IPython.display import HTML
from ipywidgets import widgets, interact, interactive, fixed, interact_manual, Layout
from ipywidgets import Button, HBox, VBox
import time
import datetime
# import psycopg2
import numpy as np
import hashlib
import requests
import random

# Go Button Counting
from string import ascii_lowercase
from collections import Counter
import os
import webbrowser

# Collects user information
import getpass

# Plotting Widgets
# %matplotlib notebook

# Plotting Widgets
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'notebook')
# exec(%matplotlib notebook)

# Answer_Dict is used for the collection of answers from the user. Submit button retrieves the last entered value. 
Answer_Dict = {"Q1":[None], "Q2":[None], "Q3":[None], "Q4":[None], "Q5":[None], "Q6":[None], "Q7":[None], "Q8":[None], "Q9":[None]}

# Submission count for each questions (attempts in the database)
submission_count = {"Q1":0, "Q2":0, "Q3":0, "Q4":0, "Q5":0, "Q6":0,"Q7":0,"Q8":0,"Q9":0}

# Verify that the package has been imported
print("You have imported hourofci")