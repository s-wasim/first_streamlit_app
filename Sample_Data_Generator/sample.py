import pandas as pd
from random import randint, seed
from datetime import datetime
from time import sleep

op_col2 = ['Yes', 'No']
op_col3 = ['Almost everyday', 'Less than once a week','More than once a week','Less than once a month']

temp_df = pd.DataFrame({
    'Timestamp': pd.Series(dtype=object), 
    'Do you like healthy food?': pd.Series(dtype=str), 
    'How often do you eat at our diner?': pd.Series(dtype=str)
    })

seed(datetime.now().microsecond)
for i in range(6):
    op2 = op_col2[randint(0, 1)]
    op3 = op_col3[randint(0, 2)]
    ts = datetime.now()
    sleep(randint(2, 4))
    temp_df.loc[i] = {'Timestamp': ts, 'Do you like healthy food?': op2, 'How often do you eat at our diner?':op3}
    print(f'done iteration {i}')

temp_df.set_index('Timestamp', inplace=True)
temp_df.to_csv('Sample_Data_Generator/Forum_Output.csv')