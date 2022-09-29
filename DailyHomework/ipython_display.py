from IPython.display import display
import pandas as pd

states = pd.read_csv('../Data/state_health.csv')
states.set_index('State Name', inplace = True)
display(states)