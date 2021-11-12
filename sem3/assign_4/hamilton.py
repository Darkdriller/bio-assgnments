visited={}
path=[]
def composition(string, k):
    result = []
    for i in range(len(string) - k + 1):
        result.append(string[i:i+k])
    return result

def overlap(patterns):
    n = len(patterns)
    graph={}
    for i in range(n):
        graph[patterns[i]]=[]
        for j in range(n):
            if i != j and patterns[i][1:] == patterns[j][:-1]:
                graph[patterns[i]].append(patterns[j])
    return graph
def init_visited(graph):
    global visited
    for i in graph:
        visited[i]=False

def hamilton(graph,v):
    global visited
    global path
    if len(path)== len(visited):
        return True

    for i in v:
        if visited[i]==False:
            visited[i]=True
            path.append(i)
        if hamilton(graph,graph[i]):
            return True
        visited[i]=False
        path.reverse()
        path.remove(i)
        path.reverse()
    return False

def init_hamilton(graph):
    global visited
    global path
    for i in range(len(graph)):
        path=[]
        init_visited(graph)
        start=list(graph.keys())[i]
        path.append(start)
        visited[start]=True
        if hamilton(graph,graph[start]):
            return path
        else:
            continue
def genome_path(patterns):
    return patterns[0]+"".join([patterns[i][-1] for i in range(1,len(patterns))])
def rearrange(comp):
    return sorted(comp)

#Dhruvjyoti
#AM.EN.U4AIE20023


if __name__ == '__main__':
    string=input("Enter String \n")
    comp=composition(string,3)
    comp=rearrange(comp)
    graph=overlap(comp)
    ans=init_hamilton(graph)
    print("Hamiltonian Path :")
    print(*ans)
    print("Reconstructed string :")
    print(genome_path(ans))
