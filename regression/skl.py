from sklearn import datasets

data = datasets.load_iris()

print(data.target)
print(data.data)