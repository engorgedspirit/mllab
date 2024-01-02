def astar(start,end):
    open=set(start)
    closed=set()
    g={}
    g[start]=0

    parents={}
    parents[start]=start

    while len(open)>0:
        n=None
        for v in open:
            if n==None or g[v]+heuristic(v)<g[n]+heuristic(n):
                n=v
        
        if n==end or Graph[n]==None:
            pass
        else:
            for (m,weight) in get_nbr(n):
                if m not in open and m not in closed:
                    open.add(m)
                    parents[m]=n
                    g[m]=g[n]+weight
                else:
                   if g[m]>g[n]+weight:
                    g[m]=g[n]+weight
                    parents[m]=n 
                    if m in closed:
                        closed.remove(m)
                        open.add(m)
        if n==None:
            print("Path doesnt exist")
            return None
        if n==end:
            path=[]
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(start)
            path.reverse()
            print('Path found:{}'.format(path))
            return path
        open.remove(n)
        closed.add(n)
    print('path doesnot exist')
    return None

def get_nbr(v):
    if v in Graph:
        return Graph[v]
    else:
        return None
def heuristic(n):
    H_dist={
        'A':11,
        'B':6,
        'C':5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    return H_dist[n]

Graph={
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1),('H', 7)] ,
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)]
}

astar('A','J')