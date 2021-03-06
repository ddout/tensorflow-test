import tensorflow as tf
import input_data as in_data

mnist = in_data.read_data_sets("../../MNIST_data/", one_hot=True)

print mnist.train.images


x = tf.placeholder("float", [None, 784])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)

y_ = tf.placeholder("float", [None, 10])

cross_entripy = -tf.reduce_sum(y_ * tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entripy)

#init variables
init = tf.initialize_all_variables()

sess = tf.Session()

sess.run(init)

for i in range(1000):
	batch_xs, batch_ys = mnist.train.next_batch(200)
	sess.run(train_step, feed_dict={x: batch_xs, y_ : batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

print correct_prediction

accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

print sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})




