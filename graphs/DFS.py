'''
Python implementation of DFS
Created By Shiva Bhusal, BGSU 

Based on explanations in this lecture, By Prof. Erik Demaine
https://www.youtube.com/watch?v=s-CYnVz-uh4&t=7s

'''

def DFS(s, adj):
    '''
    Initialize the level and parent. 
    Since we are starting from S, level will be 0. 
    Parent will be None
    '''
    parent={s:None}
    for v in adj[s]:
        if v not in parent:
            parent[v]=s
            DFS(v,adj)
    print(parent)

adj={'s':['a','c'],'c':['s','b'],'a':['s','b'],'b':['a','c']}
DFS('s',adj)





