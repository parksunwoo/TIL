import numpy as np

class Sigmoid:
    def __init__(self):
        self.params = []

    def forward(self, x):
        return 1 / (1 + np.exp(-x))

class Affine:
    def __init__(self, W, b):
        self.params = [W, b]

    def forward(self, x):
        W, b = self.params
        out = np.matmul(x, W) + b
        return out

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size):
        I, H, O = input_size, hidden_size, output_size

        W1 = np.random.randn(I, H)
        b1 = np.random.randn(H)
        W2 = np.random.randn(H, O)
        b2 = np.random.randn(O)

        self.layers = [
            Affine(W1, b1),
            Sigmoid(),
            Affine(W2, b2)
        ]

        self.params = []
        for layer in self.layers:
            self.params += layer.params

    def predict(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

x = np.random.randn(10, 2)
model = TwoLayerNet(2, 4, 3)
S = model.predict(x)
print(S)
# [[ 5.48669145 -0.3001826  -0.08515097]
#  [ 5.50579445 -0.56834334  0.05421284]
#  [ 3.98796754 -0.91135346 -0.03360283]
#  [ 2.4646512  -0.11995213 -1.00344363]
#  [ 5.74776746 -1.2800679   0.54676293]
#  [ 2.21199205 -0.00945056 -0.9952403 ]
#  [ 3.79936312 -0.54961135 -0.40037853]
#  [ 3.62046151 -0.63909157 -0.33729513]
#  [ 6.8239228  -0.98826012  0.56498186]
#  [ 4.58283448 -1.26237494  0.28180362]]