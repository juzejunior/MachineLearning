"""
   Exemplo de uso machine learning para reconhecer uma fruta
"""
from sklearn import tree
#coletando dados para treinamento
features = [[140, 1], [140, 1], [150,2], [170, 2]]
labels = ["apple", "apple", "orange", "orange"]
#criando um classificador
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(features, labels)
#agora colocamos um input para teste do algoritmo
print "I think it is: "+str(classifier.predict([[160, 0]]))
