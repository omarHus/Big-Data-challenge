import os
import pandas as pd

def files(path):

    for file in os.listdir(path):

        if os.path.isfile(os.path.join(path,file)):
            yield file

L = []
for file in files("Datasets"):
    L.append(file)


