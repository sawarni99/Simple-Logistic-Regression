
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("Social_Network_Ads.csv")
X = dataset.iloc[:, 3:4].values
y = dataset.iloc[:, 4:5].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/4, random_state = 0)

from sklearn.preprocessing import StandardScaler
var = StandardScaler()
X_train = var.fit_transform(X_train)
X_test = var.transform(X_test)

m = X_train.shape[0]

# sigmoid function 
def sigmoid(Z):
	Exp = np.exp(-1*Z)
	sig = 1/(1 + Exp)
	return sig

# Cost Function
def costFunction(y, a, m):
	cost = 1/m*np.sum(-1 * (y*(np.log(a)) + (1-y)*(np.log(1-a))))
	return cost

# Prediction
def predict(w, b, X, thres = 0.5):
	Z = np.dot(X, w.T) + b
	A = sigmoid(Z)
	ar = np.zeros((A.shape[0], 1))
	
	for i in range(A.shape[0]):
		if (A[i, 0] >= thres ):
			ar[i, 0] = 1
	return ar

# Accuracy
def accuracy(y_pred, y_test):
	max_num = y_test.shape[0]
	num = 0
	for i in range(max_num):
		if y_test[i, 0] == y_pred[i, 0]:
			num+=1
	acc = num/max_num*100
	lst = (acc, max_num, num)
	return lst


# Building Logistic regression

# Initializations 
w = np.zeros((1,1))
b = 0
iteration = 16000
alpha = 0.01

for i in range(iteration):
	# Computing hypothesis
	Z = np.dot(X_train, w.T) + b
	A = sigmoid(Z)
	
	# Printing costFunction
	print("Cost Function at iteration " + str(i) + ": " + str(costFunction(y_train, A, m)))
	
	# Optimizing by gradient decsent
	dZ = A - y_train
	dB = 1/m*np.sum(dZ)
	dW = 1/m*(np.dot(dZ.T, X_train))
	
	# Updating weights
	w = w - alpha*dW
	b = b = alpha*dB

# Predicting on X_test
y_pred = predict(w, b, X_test, thres = 0.65)

lst = accuracy(y_pred, y_test)

print("------------------------------------------------"+
	  "\n Number of test sets : " + str(lst[1]) +
	  "\n Number of correct prediction : " + str(lst[2]) +
	  "\n Accuracy : " + str(lst[0]) + "%")


