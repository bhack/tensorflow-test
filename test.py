from tensorflow.io.gfile import GFile

with GFile("ram://test.txt", mode="w") as f:
    f.write("test")
    print(f.size())
