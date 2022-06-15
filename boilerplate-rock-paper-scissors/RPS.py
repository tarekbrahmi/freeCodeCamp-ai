import random
import pandas as pd
from _helpers import computer_choice, play_rps
rps_nums = ['Rock', 'Paper', 'Scissors']
global record
# declare variables
record = pd.DataFrame(columns=['p1', 'p2', 'winner', 'model_choice',
                      'model0', 'model1', 'model2', 'model3', 'model4', 'model5'])

def player(prev_play, opponent_history=[]):
    global record
    opponent_history.append(prev_play)
    p2=0
    if len(opponent_history) > 2:
        _p1 =opponent_history[-1]
        p1=0
        if _p1=="P":
            p1=1
        elif _p1=="S":
            p1=2
        p2, model_choice, model_choices = computer_choice(record)
        winner = play_rps(p1, p2)
        record = record.append({'p1': p1, 'p2': p2, 'winner': winner, 'model_choice': model_choice,
                                'model0': model_choices[0], 'model1': model_choices[1], 'model2': model_choices[2],
                                'model3': model_choices[3], 'model4': model_choices[4], 'model5': model_choices[5]}, ignore_index=True)
        opponent_history =list(filter(lambda x:x!="",opponent_history))
    
    return ['R', "P", "S"][p2]

