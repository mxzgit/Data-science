import numpy as np
from sklearn import datasets

class LogiticRegression:
    def __init__(self,lr=0.1,num_iter=100,fit_intercept=True,verbose=False):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.verbose = verbose

    def __add_intercept(self,X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis = 1)

    def __sigmoid(self,z):
        return 1/(1+np.exp(-z))

    def __loss(self,h,y):
        return (-y*np.log(h) + (1-y)*np.log(1-h)).mean()

    def fit(self,X,y):
        if self.fit_intercept :
            X = self.__add_intercept(X)

        self.theta = np.zeros(X.shape[1])

        for i in range(self.num_iter):
            z = np.dot(X,self.theta)
            h = self.__sigmoid(z)
            gradient = np.dot(X.T, (h-y)) / y.size
            self.theta -= self.lr * gradient 

            if (self.verbose == True and i % 1000 == 0):
                z = np.dot(X, self.theta)
                h = self.__sigmoid(z)
                print(f'loss : {self.__loss(h,y)} \t')
    
    def predict_prob(self, X):
        if self.fit_intercept:
            X = self.__add_intercept(X)

        return self.__sigmoid(np.dot(X,self.theta))

    def predict(self,X):
        return self.predict_prob(X).round()


if __name__ == "__main__":

    iris = datasets.load_iris()
    X = iris.data[:,:2]
    y = (iris.target != 0) * 1
    
    model = LogiticRegression()
    model.fit(X,y)

    preds = model.predict(X)
    print((preds == y).mean())
