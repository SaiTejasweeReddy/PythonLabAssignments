import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

day = []
opening_price = []

# data from Paris CAC 40 (^FCHI Yahoo Finance) at https://finance.yahoo.com/quote/%5EFCHI/history?p=%5EFCHI
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            #print(', '.join(row))
            day.append(int(row[0]))
            opening_price.append(float(row[1]))
    return


def show_plot(day, opening_price):
    linear_mod = linear_model.LinearRegression()
    day = np.reshape(day, (len(day), 1))
    opening_price = np.reshape(opening_price, (len(opening_price), 1))
    linear_mod.fit(day, opening_price)
    plt.scatter(day, opening_price, color='red')
    plt.title('Linear prediction model')
    plt.xlabel('Dates')
    plt.ylabel('Opening Prices')
    plt.plot(day, linear_mod.predict(day), color='blue', linewidth=3)
    plt.show()
    return


def predict_price(day, opening_price, x):
    linear_mod = linear_model.LinearRegression()
    day = np.reshape(day, (len(day), 1))
    opening_price = np.reshape(opening_price, (len(opening_price), 1))
    linear_mod.fit(day, opening_price)
    predicted_price = linear_mod.predict(x)
    return predicted_price[0][0], linear_mod.coef_[0][0], linear_mod.intercept_[0]


get_data('data.csv')
print
day
print
opening_price
print
"\n"

show_plot(day, opening_price)

(predicted_price, coefficient, constant) = predict_price(day, opening_price, 1)
print("The regression coefficient is ", str(coefficient), ", and the constant is ", str(constant))
print("the relationship equation between a day and the opening price on that day is: price = ", str(coefficient), "* day + ", str(constant))