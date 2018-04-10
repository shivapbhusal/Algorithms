'''
Python implementation of BFS
Created By Shiva Bhusal, BGSU 

Based on explanations in this lecture, By Prof. Erik Demaine
https://www.youtube.com/watch?v=s-CYnVz-uh4&t=7s

'''

def BFS(s, adj):
    '''
    Initialize the level and parent. 
    Since we are starting from S, level will be 0. 
    Parent will be None
    '''
    level={s:0}
    parent={s:None}

    i=1
    frontier=[s]

    while frontier:
        nextNodes=[]
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v]=i
                    parent[v]=u
                    nextNodes.append(v)
        frontier=nextNodes
        i=i+1

    print(level) #Print the results
    print(parent)

adj={'s':['a','c'],'c':['s','b'],'a':['s','b'],'b':['a','c']}

BFS('s',adj)
                    




