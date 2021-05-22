import pybaseball
import numpy as np
import pandas as pd
from pybaseball import statcast
from pybaseball import statcast_pitcher

full_data = statcast(start_dt='2015-02-25', end_dt='2021-11-30') 

left_handed_throwers = full_data[full_data['p_throws'] == 'L'][['game_date','player_name','pitcher']].value_counts().reset_index().drop(columns = 0)
left_handed_throwers.to_csv('left_handed_throwers.csv')

right_handed_throwers = full_data[full_data['p_throws'] == 'R'][['game_date','player_name','pitcher']].value_counts().reset_index().drop(columns = 0)
right_handed_throwers.to_csv('right_handed_throwers.csv')
