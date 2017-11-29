from mxnet.gluon import nn
import sys
sys.path.append('..')
import utils
from mxnet import gluon
from mxnet import init


def vgg_block(num_convs, channels):
    out = nn.Sequential()
    for _ in range(num_convs):
        out.add(
            nn.Conv2D(channels=channels, kernel_size=3,
                      padding=1, activation='relu')
        )

    out.add(nn.MaxPool2D(pool_size=2, strides=2))

    return out


def vgg_stack(architecture):
    out = nn.Sequential()
    for(num_convs, channels) in architecture:
        out.add(vgg_stack(num_convs, channels))

    return out


def main():

    num_outputs = 10
    architecture = ((2, 64), (2, 128), (4, 256), (4, 512), (4, 512))

    net = nn.Sequential()
    with net.name_scope():
        net.add(
            vgg_stack(architecture),
            nn.Flatten(),
            nn.Dense(4096, activation="relu"),
            nn.Dropout(.5),
            nn.Dense(4096, activation="relu"),
            nn.Dropout(.5),
            nn.Dense(num_outputs))

    train_data, test_data = utils.load_data_fashion_mnist(
        batch_size=64, resize=96)

    ctx = utils.try_gpu()

    net.initialize(ctx=ctx, init=init.Xavier())

    loss = gluon.loss.SoftmaxCrossEntropyLoss()

    trainer = gluon.Trainer(net.collect_params(), 'sgd', {
                            'learning_rate': 0.05})
    utils.train(train_data, test_data, net, loss, trainer, ctx, num_epochs=100)
