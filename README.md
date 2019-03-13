# Project Log Analysis 
This is a machine learning project made in python using pandas and sklearn libraries.The details for the dataset used in this project can be found here [Dataset](http://archive.ics.uci.edu/ml/datasets/Bank+Marketing).In this project we aim to build a classifier with good accuracy to maximize acquire percentage(Y%) and minimize marketing cost(X%)

# Prerequisites
- [Python](https://www.python.org/)
- Dataset [bank-full.csv](http://archive.ics.uci.edu/ml/datasets/Bank+Marketing).
- [Pandas library](https://pandas.pydata.org/)
- [Sklearn](https://scikit-learn.org/stable/)
- [Matplotlib](https://matplotlib.org/)
- [Git](https://git-scm.com/)

# Usage
- Download and unzip or clone this repository.Clonning can be done with following command.
```
$ git clone https://github.com/Nsharma96/Ml-Bank.git
```
- Go to the directory and run the Ml.py file using python.


### Run The tool
- To See the output of tool type.
```
$ python3 Ml.py
```

# Output
- Selecting important features.Using feature importance.
![Screenshot](https://github.com/Nsharma96/Ml-Bank/blob/master/Figure_1.png)

- correlation matrix.

- Accuracy Matrix .
  - Accuracy for Random Forest :0.8937299568727193
  - Accuracy for KNN :0.8752626340816101
  - Accuracy for Neural Nets :0.8521508348999226
  
# Goals achieved

As we can see Random Forest classifier gave the best accuracy. So, to reduce marketing cost and increase acquire percentage 
(Y%) we can make use of this classifier. This classifier requires 5 inputs that is ‘age’, ‘duration’, ‘month’, ‘day’ and
‘balance’ after which the classifier will predict the probability of ‘yes’ from a customer. Thus, this way we can make a list
with much more accuracy and thereby reducing marketing cost (as there will be less number of calls to be made) and increasing
Y%.
We can also make this classifier recurrent which with time will keep getting better and better. Thereby reducing human resource, time and money expenditure.
