import numpy as np
from perceptronClass import Perceptron

example = 'OR'
F = {'AND': np.array([0,0,0,1]), 'OR': np.array([0,1,1,1])}

x = np.array([[0,0], [0,1], [1,0], [1,1]])

F = F[example]
model = Perceptron(alpha=0.2, n_iter=100, example=example)

print('Model Trainning...')
model.train(x, F)

print('Weights: ')
model.show_weight()

for xi in x:
    yi = model.predict(xi)
    print('Prediction: ', xi, yi)

