import os
import tensorflow as tf


tf.gfile.makedir("ram://folder")
with tf.gfile.Gfile("ram://folder/file.txt", mode="w") as f:
    f.write("data")

for root, _, filenames in tf.io.gfile.walk("ram://folder"):
    for filename in filenames:
        assert tf.io.gfile.exists(os.path.join(root, filename))
