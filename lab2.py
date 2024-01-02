class Graph:
    def __init__(self,graph,HNList,startN):
        self.graph=graph
        self.H=HNList
        self.start=startN
        self.parent={}
        self.status={}
        self.SolnGraph={}
    def applyAOstar(self):
        self.AOstar(self.start,False)
    def getNBR(self,v):
        return self.graph.get(v,'')
    def getStatus(self,v):
        return self.status.get(v,0)
    def setStatus(self,v,val):
        self.status[v]=val
    def getHNodeVal(self,n):
        return self.H.get(n,0)
    def setHNodeVal(self,n,val):
        self.H[n]=val
    def printSoln(self):
        print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:",self.start)
        print("------------------------------------------------------------")
        print(self.SolnGraph)
        print("------------------------------------------------------------")
    def computeChild(self,v):
        minCost=0
        childNList={}
        childNList[minCost]=[]
        flag=True
        for NTupleList in self.getNBR(v):
            cost=0
            nodeList=[]
            for c,weight in NTupleList:
                cost= cost + self.getHNodeVal(c)+weight
                nodeList.append(c)
            if flag==True:
                minCost=cost
                childNList[minCost]=nodeList   
                flag = False
            else :
                if minCost >  cost:
                    minCost= cost
                    childNList[minCost] = nodeList
        return minCost,childNList[minCost]
    def AOstar(self,v,backTracking):
        print("HEURISTIC VALUES :",self.H)
        print("SOLUTION GRAPH :", self.SolnGraph)
        print("PROCESSING NODE :", v)
        print("-----------------------------------------------------------------------------------------")

        if self.getStatus(v)>=0:
            minCost,childNList=self.computeChild(v)
            print(minCost,childNList)
            self.setHNodeVal(v,minCost)
            self.setStatus(v,len(childNList))
            solved=True
            for childNode in childNList:
                self.parent[childNode]=v
                if self.getStatus(childNode)!=-1:
                    solved=solved & False
            if solved ==True:
                self.setStatus(v,-1)
                self.SolnGraph[v]=childNList
            if v!=self.start:
                self.AOstar(self.parent[v],True)
            if backTracking==False:
                for childNode in childNList:
                    self.setStatus(childNode,0)
                    self.AOstar(childNode,False)

h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1}
graph1 = {
'A': [[('B', 1), ('C', 1)], [('D', 1)]],
'B': [[('G', 1)], [('H', 1)]],
'C': [[('J', 1)]],
'D': [[('E', 1), ('F', 1)]],
'G': [[('I', 1)]]
}
G1= Graph(graph1, h1, 'A')
G1.applyAOstar()
G1.printSoln()
