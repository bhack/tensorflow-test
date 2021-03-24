import tensorflow as tf


tf.io.gfile.makedirs("ram://test/inner")

with tf.io.gfile.GFile("ram://test/inner/test.txt", mode="w") as f:
    f.write("test")

with tf.io.gfile.GFile("ram://test/inner/test.txt", mode="rb") as f:
    print(f.size())




# import os
# import tensorflow as tf


# model = tf.keras.Sequential(tf.keras.Input((10,)), tf.keras.layers.Dense(1))

# model.save("ram://test")

# for root, _, filenames in tf.io.gfile.walk("ram://test"):
#     for filename in filenames:
#         dest_path = os.path.join(root, filename)
#         with tf.io.gfile.GFile(dest_path, mode="rb") as f:
#             f.write("test")
#             assert f.size() == 4
