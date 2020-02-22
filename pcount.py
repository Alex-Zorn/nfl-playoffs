import phistory

yrlist = []
allgames = phistory.biglist

ms = {'W':[[4,5],[3,6]],'D':[[1,3],[1,4],[1,5],[1,6],[2,3],[2,4],[2,5],[2,6]],
      'C':[[1,2],[1,3],[1,4],[1,5],[1,6],[2,3],[2,4],[2,5],[2,6],[3,4],[3,5],[3,6],
           [4,5],[4,6],[5,6]]}

for t in range(1976,2015):
    if not t == 1983:
        yrlist.append(str(t)[2:])

def rec(match,games):
    r = [0,0]
    for g in games:
        if g[:2] == match:
            r[g[2] - 1] += 1
    return r

def Round(rd):
    mygames = [i for i in allgames if i[3] == rd]
    res = []
    for t in ms[rd]:
        res.append([t,rec(t,mygames)])
    return res

def Count(lst):
    mydict = {}
    for t in lst:
        if t in mydict:
            mydict[t] += 1
        else:
            mydict[t] = 1
    return mydict
    
    
def Fullround(rd):
    frs = []
    for y in yrlist:
        mygames = [i for i in allgames if i[3] == rd and i[4] == y]
        r = [0,0]
        for g in mygames:
            r[g[2] - 1] += 1
        frs.append(tuple(r))
    return Count(frs)

def Superbowl(i,j):
    mygames = [i for i in allgames if i[3] == 'S']
    return rec([i,j],mygames)

def Find(i,j,res,rd):
    mygames = [g for g in allgames if g[:4] == [i,j,res,rd]]
    return mygames

