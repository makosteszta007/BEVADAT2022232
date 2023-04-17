import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from NJCleaner import NJCleaner
from DecisionTreeClassifier import DecisionTreeClassifier

nj = NJCleaner('./2018_03.csv')
nj.prep_df()

column_names = ['stop_sequence', 'from_id', 'to_id', 'status', 'line', 'type', 'day', 'part_of_the_day', 'delay']
data = pd.read_csv('./data/NJ.csv', skiprows=1, header=None, names=column_names)

X = data.iloc[:,:-1].values
Y = data.iloc[:,-1].values.reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=.2, random_state=41)

classifier = DecisionTreeClassifier(min_samples_split=2, max_depth=4)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)
print(accuracy_score(Y_test, Y_pred))

"""
A feladat leírása alapján megcsináltam a .py fájlokat, HAZI06.ipynb-ben teszteltem, ahol a következõ eredményeket is kaptam.
Sajnos a DecisionTree törlõdött a gépemrõl, ezért azt a moodle-be feltöltött alapján újra létrehoztam, a Node-al együtt, majd megkapta a paramétereket.
Nehézségek:
    Figyelmetlenségbõl adódó hibák: rossz elnevezések, elírások, data mappa hiánya -> nem tudta elmenteni a NJ.csv-t
    A python néha szeret errort adni teljesen egyértelmûen jó példákra.
Eredmények:
i/    min_samples_split:  max_depth:  accuracy:
1/            1               1       0.7828333333333334
2/            1               2       0.7843333333333333
3/            2               3       0.7869166666666667
4/            2               4       0.7884166666666667
5/            3               5       0.79075
6/            3               1       0.7828333333333334
7/            4               2       0.7843333333333333
8/            4               3       0.7869166666666667
9/            5               4       0.7884166666666667
10/           5               5       0.79075
"""