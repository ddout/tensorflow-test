import tensorflow as tf

hello = tf.constant('Hello, tensorflow!')

sess = tf.Session()

print sess.run(hello)

a = tf.constant(100) 

b = tf.constant(32) 

print sess.run(a + b)
