import pandas as pd

data = {'Student Number':  ['1', '2', '3', '4', '5','6', '7', '8', '9', '10'],
        'Average Grade': ['A', 'A', 'B', 'E', 'D','C', 'B', 'A', 'B', 'C'],
        'Total Points': ['342', '351', '314', '25', '87','123', '242', '379', '267', '150'],
        'Number of assignments submitted': ['15', '15', '14', '3', '9','11', '13', '15', '14', '10'],
        'Current streak': ['10', '9', '6', '1', '3','4', '6', '11', '7', '5'],
        'Number of questions answered': ['3', '4', '1', '1', '1','1', '1', '7', '3', '1']}

df = pd.DataFrame (data, columns = ['Student Number','Average Grade', 'Total Points','Number of assignments submitted', 'Current streak','Number of questions answered'])

df.to_csv('MOCK_STUDENT_DATA.csv')

print(df)
