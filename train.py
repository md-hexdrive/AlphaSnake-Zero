from utils.alpha_snake_zero_trainer import AlphaSnakeZeroTrainer
from utils.alphaNNet import AlphaNNet


name = int(input("Enter net family name:\n"))
start = int(input("Enter starting iteration:\n"))
if start == 0:
    net = AlphaNNet(ins = (21, 21, 3))
else:
    net = AlphaNNet(model = "models/" + name + str(start) + ".h5")
a = AlphaSnakeZeroTrainer(name = name, iter = start)
a.train(net)