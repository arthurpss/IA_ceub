import pandas as pd
nameColumns= ['SeppalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Class']
dataFrame = pd.read_csv('./data/iris.csv', names=nameColumns)
print('linhas: {}, colunas: {}'.format(len(dataFrame), len(dataFrame.columns)))
print(dataFrame.head())