import numpy as np
import chainer
from chainer import cuda, Function, gradient_check, Variable, optimizers, serializers, utils
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L

import data
mnist = data.load_mnist_data()
x_all = mnist['data'].astype(np.float32) / 255
y_all = mnist['target'].astype(np.int32)
x_train, x_test = np.split(x_all, [60000])
y_train, y_test = np.split(y_all, [60000])

model = L.Classifier(MLP())
optimizer = optimizers.SGD()
optimizer.setup(model)
batchsize = 100
datasize = 60000
loss_over_time = []
acc = []
for epoch in range(20):
    print('epoch %d' % epoch)
    indexes = np.random.permutation(datasize)
    for i in range(0, datasize, batchsize):
        x = Variable(x_train[indexes[i : i + batchsize]])
        t = Variable(y_train[indexes[i : i + batchsize]])
        model.zerograds()
        loss = model(x, t)
        loss.backward()
        optimizer.update()
        loss_over_time.append(loss.data)
        acc.append(model.accuracy.data)
sum_loss, sum_accuracy = 0, 0
for i in range(0, 10000, batchsize):
    x = Variable(x_test[i : i + batchsize])
    t = Variable(y_test[i : i + batchsize])
    loss = model(x, t)
    sum_loss += loss.data * batchsize
    sum_accuracy += model.accuracy.data * batchsize
mean_loss = sum_loss / 10000
mean_accuracy = sum_accuracy / 10000
