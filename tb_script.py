LOG_DIR = 'tb_logs'
import tensorflow as tf

tf.reset_default_graph()

a = tf.constant(2)
b = tf.constant(3)
c = tf.add(a, b)

writer = tf.summary.FileWriter('./tb_logs', tf.get_default_graph())

with tf.Session() as sess:
  print(sess.run(c))
  print(c)  # check what in c

writer.close()
