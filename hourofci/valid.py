from hourofci import *

# CHANGE in v2: move the answer to each notebook
# hash answer
# hash_answer_catalog = {'gateway': {'beginner': {'Q1': 'c62040943e0d0d3ba840788f89c68a6bf839c408209c578ed0af37733713b522', 'Q2': 'ac88c6e3452c7540d7df76d079ebff7b99752a3a4407f4def2961c22d14e503f', 'Q3': 'e73b2bc4043553b458eaa713735ba7a25190d747ee6f4db2dabac00817070db8', 'Q4': '3fdba35f04dc8c462986c992bcf875546257113072a909c162f7e470e581e278', 'Q5': '8b940be7fb78aaa6b6567dd7a3987996947460df1c668e698eb92ca77e425349', 'Q6': '62d7a6b1211d627650e2bf0c869b69b564e2cd74290ae1dd78ae4b5e20b0cfe7', 'Q7': '3fdba35f04dc8c462986c992bcf875546257113072a909c162f7e470e581e278', 'Q8': 'b530f329d65f246114bd293232aa31ec383289b020059c7628942ee9dcd55f9b', 'Q9': '7d2857159e3091222d89dc3a870f741fa522997ee31f6557fc29a7cd4387ddac'}}, 'parallel_programming': {'beginner': {'Q1': 'f5baf0e4336fd53b4c82b453ece859868475160d36f22e9551a0e9b10ac9cc00', 'Q2': '4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5', 'Q3': '7391b1eb195e2636fb66215bd7e893c665c6c00f2d4f4b2e68ecd6675db3492c', 'Q4': 'cf9dcf6da8a82be1335c398a4005def7ee3a53d4698c59dbc6b2b14e72d1263c', 'Q5': 'f91c5ef3017e7339963efb516609bc580cdd5c8ecf2714ff77dfcac07e4e5117'}, 'advanced': {'Q1': '8d51addd113608ec37781c46eb2aad4d81cc6ccab48fd047410f098fe45e97f0', 'Q2': '9f14025af0065b30e47e23ebb3b491d39ae8ed17d33739e5ff3827ffb3634953', 'Q3': '7391b1eb195e2636fb66215bd7e893c665c6c00f2d4f4b2e68ecd6675db3492c', 'Q4': 'e06a321148a8ed1ab42a0653286ddf1f752689f0d2fa4d449afab0baa6006136', 'Q5': 'f91c5ef3017e7339963efb516609bc580cdd5c8ecf2714ff77dfcac07e4e5117'}}}

# CHANGE in v2: pass the answer catalog to the function (user's answer vs. the answer catalog)
def valid(lesson, lesson_level, question, answer, hash_answer_catalog):
    # Lowercase answer to make it non-case sensitive
    answer = answer.lower()  
    # Hash answer to send over to the Flask API for validation
    answer = answer.encode('utf-8')
    hash_object = hashlib.sha256(answer)
    hash_answer = hash_object.hexdigest()  

    if str(hash_answer_catalog[lesson][lesson_level][question]) == str(hash_answer):
        valid_widget = widgets.Valid(
                            value=True,
                            description='Valid!',
                            )
        display(valid_widget)
        print("Congrats!!")
        return True
    else:
        valid_widget = widgets.Valid(
                      value=False,
                      description='',
                      )
        
        display(valid_widget)
        print("Try Again!")
        return False