import numpy as np

class Perceptron():
    def __init__(self, example, thresholds=0.5, alpha=0.2, n_iter=100):
        self.thresholds = thresholds
        self.alpha = alpha
        self.n_iter = n_iter
        self.example = example

    def predict(self, x):        
        sum = np.sum(x*self.W)
        out = 1 if sum > self.thresholds else 0
        return out

    def show_weight(self):
        print(self.W)

    def train(self, x, F):
        self.W = np.array([0.1, 0.3])
        
        for i in range(self.n_iter) :
            
            weightSum = 0.0
            for i in range(len(x)):
                Y = self.predict(x[i])
                d = F[i] - Y                
                self.W = self.W + (self.alpha * d * x[i])
                weightSum = weightSum + d

            if weightSum == 0.0:
                break;