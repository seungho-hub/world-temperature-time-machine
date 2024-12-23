import sys
import pickle

cc = sys.argv[1]
year = sys.argv[2]

with open("models/{}.pkl".format(cc), "rb") as file:
    model = pickle.load(file)

[prediction] = model.predict([[int(year)]])

print(prediction)
