import os
import tensorflow as tf


tf.io.gfile.makedirs("ram://folder")
with tf.io.gfile.GFile("ram://folder/file.txt", mode="w") as f:
    f.write("data")

for root, _, filenames in tf.io.gfile.walk("ram://folder"):
    print(root)
    print(filenames)
    for filename in filenames:
        print(filename)
        print(os.path.join(root, filename))
        assert tf.io.gfile.exists("ram://folder/file.txt")
        assert tf.io.gfile.exists(os.path.join(root, filename))
