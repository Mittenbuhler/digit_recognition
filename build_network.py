from nn_functions import *

# Import data
train_images, train_labels, test_images, test_labels = pre_processing()

# Build neural network (with two hidden layers of 100 nodes each)
neural_network = NeuralNetwork([784,200,100,10], bias=True)
neural_network.train(train_images, train_labels, epochs=3)
neural_network.evaluate(test_images, test_labels)

# Export neural network
neural_network.save('my_network')