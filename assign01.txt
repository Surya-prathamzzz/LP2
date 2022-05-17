from collections import deque

class Graph:
    def __init__(self, edges, n):
        
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
def DFS(graph, v, visited):
 
    visited[v] = True           
    print(v, end=' ')             
 
    for u in graph.adjList[v]:
        if not visited[u]:      
            DFS(graph, u, visited)
 
 
def recursiveBFS(graph, q, visited):
 
    if not q:
        return
    v = q.popleft()
    print(v, end=' ')
    for u in graph.adjList[v]:
        if not visited[u]:
            visited[u] = True
            q.append(u)
    recursiveBFS(graph, q, visited)
 

if __name__ == '__main__':


     vx= int(input("Enter the no of vertices=>"))
     edge= int(input("Enter the no of edges=>"))
     print("\nEnter the vertices of edges: ")
     edges= list(tuple(map(int,input().split())) for r in range(edge))
     #print(edges)

     graph = Graph(edges, vx)
     visited = [False] * vx
     loopVar=True
     while(loopVar!=False):
        print("\n--------MENU-------")
        print("\n1.DFS\n2.BFS\n3.Exit")
        ch=int(input("Enter ur chocie: "))
        if(ch==1):
            for i in range(vx):
                if not visited[i]:
                    DFS(graph, i, visited)

        elif(ch==2):
            q = deque() 
            visited = [False] * vx
            for i in range(vx):
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
                    recursiveBFS(graph, q, visited)

        elif(ch==3):
            loopVar=False
            print("End!")
            
        else:
            print("\nEnter valid choice!!")

''' 
Output:

Enter the no of vertices=>5
Enter the no of edges=>5

Enter the vertices of edges:
0 1
0 2
0 3
1 2
1 4

--------MENU-------

1.DFS
2.BFS
3.Exit
Enter ur chocie: 1
0 1 2 4 3 
--------MENU-------

1.DFS
2.BFS
3.Exit
Enter ur chocie: 2
0 1 2 3 4 
--------MENU-------

1.DFS
2.BFS
3.Exit
Enter ur chocie: 3
End!

OutputCase2:
Enter the no of vertices=>6
Enter the no of edges=>6

Enter the vertices of edges: 
0 1
0 2
0 3
1 4
1 5
2 5

--------MENU-------

1.DFS
2.BFS
3.Exit
Enter ur chocie: 1 
0 1 4 5 2 3 
--------MENU-------

1.DFS
2.BFS
3.Exit
Enter ur chocie: 2
0 1 2 3 4 5 
--------MENU-------

1.DFS
2.BFS
3.Exit
Enter ur chocie: 3
End!
'''