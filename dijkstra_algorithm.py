graph={}
graph['start']={}
graph['start']["a"]={}
graph['start']['a']=1
graph['start']['b']=3

graph['a']={}
graph['a']['b']=1
graph['a']['c']=5

graph['b']={}
graph['b']['d']=3

graph['c']={}
graph['c']['e']=2

graph['d']={}
graph['d']['f']=1

graph['e']={}
graph['e']['fin']=3

graph['f']={}
graph['f']['fin']=2



infinity = float("inf")

costs={}
costs['a']=1
costs['b']=3
costs['c']=infinity
costs['d']=infinity
costs['e']=infinity
costs['f']=infinity

parents={}
parents['a']="start"
parents['b']="start"
parents['c']=None
parents['d']=None
parents['e']=None
parents['f']=None
parents['fin']=None

processed=[]


def find_lowest_node(cost,processed):
    keys = list(cost.keys())
    values = list(cost.values())

    lowest = float("inf")
    node = None

    for i in range(len(cost)):
        if values[i] < lowest and keys[i] not in processed:
            lowest = values[i]
            node = keys[i]
    
    return node

    
node = find_lowest_node(costs,processed)


while node is not None:
    cost=costs[node]
    
    neighbour = graph.get(node, {})
    for n in neighbour:
        cost_neighbour=cost + neighbour[n]
        
        if n not in costs or cost_neighbour <= costs[n] :
            costs[n]=cost_neighbour
            parents[n]=node
    processed.append(node)
    node=find_lowest_node(costs,processed)
    
    
print(parents)

