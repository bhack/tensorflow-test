import os
import tensorflow as tf


model = tf.keras.Sequential([tf.keras.Input((1,)), tf.keras.layers.Dense(1)])
model.compile(loss="mse")
model.fit(x=[[1]], y=[1])

model.save("ram://test")

for root, _, filenames in tf.io.gfile.walk("ram://test"):
    for filename in filenames:
        if filename[0] == "\\":
            # on windows
            print("STRIPPING LEADING \\")
            filename = filename[1:]
        path = os.path.join(root, filename)
        print(f"root: {root}")
        print(f"filename: {filename}")
        print(f"path: {path}")
        print("exists: ", tf.io.gfile.exists(path))
        with tf.io.gfile.GFile(path, mode="rb") as f:
            print(f.size())


# import tensorflow as tf


# tf.io.gfile.makedirs("ram://test")
# with tf.io.gfile.GFile("ram://test/test.txt", mode="w") as f:
#     f.write("test")
# print(tf.io.gfile.walk("ram://test"))
