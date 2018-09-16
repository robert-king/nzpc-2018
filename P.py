import sys
sys.setrecursionlimit(100000000)
from collections import defaultdict

def read_vals():
    return [int(x) for x in input().strip().split()]


while True:

    N,=read_vals()
    if N == 0:
        break
    
    start, target  = input().split()


    
    G = defaultdict(list)

    for _ in range(N):
        toks  = input().split()
        toks = [sys.intern(t) for t in toks]
        node = toks[0]
        toks = toks[2:-1]
        cost  = len(list(filter(lambda x: x[0] == '"', toks)))
        ch = list(filter(lambda x: x[0] != '"', toks))
        goal = target in toks
        G[node].append((cost,ch,goal))

    #print("G", G)
    mincosts = {n:-2 for n in G}
    gcosts = {n:-2 for n in G}

    visited = set()#start]

    def visit(n,visited_,mincosts_):
        ##print("visit", n,  "visited=", visited)
        if n in mincosts_ and mincosts_[n] != -2:
            return mincosts_[n]
        if n in visited_:
            return 10000000000
        visited_.add(n)

        mcost = 10000000000
        for cost, ch,goal in G[n]:
            for child in ch:
                cost += visit(child,visited_, mincosts_)    
            mcost = min(mcost, cost)

        mincosts_[n] = mcost
        visited_.remove(n)
        return mcost

    visit(start, visited,mincosts)

    visited = set()#start]

    #print("mincosts:", mincosts)

    def visit2(n):
        #print(" " * len(visited), "visit2",n)
        if gcosts[n] != -2:
            #print(" " * len(visited), "cached", gcosts[n])
            return gcosts[n]
        if n in visited:
            #print(" " * len(visited), "loop")
            return 10000000000
        visited.add(n)

        mcost = 10000000000
        for cost, ch,goal in G[n]:
            if goal:
                #temp = cost + sum(mincosts[child] for child in ch)
                tempvisited = set()
                tempmincost = {}
                for child in ch:
                    cost += visit(child, tempvisited, tempmincost)
                #print(" " * len(visited), "reach goal w ch", ch, "cost", temp)
                mcost = min(mcost, cost)
            else:
                temp1 = [visit2(c) for c in ch]
                temp2 = [mincosts[c] for c in ch]
                total = cost + sum(temp2)
                for i1 in range(len(ch)):
                    rcost = total - temp2[i1] + temp1[i1]
                    mcost = min(mcost, rcost)

                # for i1,child in enumerate(ch):
                #     rcost = cost
                #     for i2,c2 in enumerate(ch):
                #         if i1 == i2:
                #             rcost += visit2(c2)
                #         else:
                #             rcost += mincosts[c2]
                #     #print(" " * len(visited), "try", child,"rcost", rcost)
                #     mcost = min(mcost, rcost)

        gcosts[n] = mcost
        visited.remove(n)
        return mcost

    x=visit2(start)

    #print("gcosts:", gcosts)
    if x >= 1e9:
        print(-1)
    else:
        print(x)
    #print()
    input()




