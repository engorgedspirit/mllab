import numpy as np
import pandas as pd

data=pd.read_csv("training_examples.csv")
table=np.array(data)[:,1:-1]
print("Concepts to be learned")
print(table)
target=np.array(data)[:,-1]
print("Labels of the concepts")
print(target)
def learn(concept,target):
    S=concept[0].copy()
    G=[['?' for i in range(len(S))] for i in range(len(S))]

    for i,h in enumerate(concept):
        if target[i]=='Yes':
            for j in range(len(S)):
                if h[j]!=S[j]:
                    S[j]='?'
                    G[j][j]='?'
        elif target[i]=='No':
            for j in range(len(S)):
                if h[j]!=S[j]:
                    G[j][j]=S[j]
                else:
                    G[j][j]='?'
    indices=[i for i,val in enumerate(G) if val==['?' for i in range(len(S))]]
    for i in indices:
        G.remove(['?' for i in range(len(S))])
    return S,G

S,G=learn(table,target)
print("Specific hypothesis",S)
print("General hypothesis",G)