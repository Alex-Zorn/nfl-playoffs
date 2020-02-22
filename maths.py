AllTeams = []
AllGames = []
AllDivs = []

#Creates the lists

def Initiate(ts,gs,ds):
    global AllTeams,AllGames,AllDivs
    AllTeams = ts
    AllGames = gs
    AllDivs = ds

                                                ########MATH TYPE STUFF########

#Gets the position of an object in a list

def match(lst,s):
    for i in range(len(lst)):
        if lst[i] == s:
            return i
    return -1

#Gets everything from a list that satisfies a condition

def myfilter(lst,fun):
    rlist = []
    for x in lst:
        if fun(x):
            rlist.append(x)
    return rlist

#Tells you the index of the (first occurrence of) the
#largest element of a numerical list

def largest(lst):
    n = lst[0]
    ind = 0
    for i in range(len(lst)):
        if lst[i] > n:
            ind = i
            n = lst[i]
    return ind

#Combines all things in a list of lists into one list

def smash(lst):
    nlist = []
    for i in lst:
        nlist += i
    return nlist

# Returns highest teams w/r/t a rec, ranked by wins

def CompRecs(teamlist,recname):
    winlist = []
    for x in teamlist:
        if winlist == []:
            winlist = [x]
        else:
            if x.dict[recname] > winlist[0].dict[recname]:
                winlist = [x]
            if x.dict[recname] == winlist[0].dict[recname]:
                winlist.append(x)
    return winlist

#Sorts a list by the fun, best to worst

def SortRecs(lst,fun):
    if lst == []:
        return []
    else:
        w = SortRecs(lst[1:],fun)
        try:
            s = fun(lst[0])
        except IndexError:
            s = 0
        u = []
        add = 0
        for t in w:
            if add == 0:
                try:
                    r = fun(t)
                except IndexError:
                    r = 0
                if s > r:
                    add = 1
                    u.append(lst[0])
                    u.append(t)
                else:
                    u.append(t)
            else:
                u.append(t)
        if add == 0:
            u.append(lst[0])
        return u
    
def Maxrec(team):
    return team.rec + (16 - team.gsplayed)*2

#Comes up with a list of pairs of items from a list

def Pairs(lst):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            pairs.append([lst[i],lst[j]])
    return pairs

def ntuples(lst,n):
    ntups = []
    if n == 1:
        for i in lst:
            ntups.append([i])
        return ntups
    if lst == []:
        return []
    for w in ntuples(lst[1:],n-1):
        ntups.append([lst[0]] + w)
    return ntups + ntuples(lst[1:],n)

def ProperSubsets(lst):
    if len(lst) < 2:
        return []
    else:
        psubs = []
        for n in range(len(lst) - 1):
            psubs += ntuples(lst,n+1)
        return psubs

#Takes a list of lists and returns a list of lists where each thing in the new list is a choice of one thing from the
#first list, one from the second, etc. For instance, Weave([['Blue','Red','Green'],['Shirt','Hat','Tie]]) returns a list
#of 9 items which are clothing option pairs: ['Blue','Shirt'], etc.



def Weave(l):
    s = [[]]
    for n in range(l):
        news = []
        for item in s:
            for o in l[n]:
                news.append(item + [o])
        s = list(news)

def Weave2(l):
    s = [[]]
    for n in range(l):
        news = []
        for item in s:
            for o in l[n]:
                news.append(item + o)
        s = list(news)

def winsnties(lst):
    s = 0
    for j in lst:
        if j == 'W' or j == 'T':
            s += 1
    return s

def wins(lst):
    s = 0
    for j in lst:
        if j == 'W':
            s += 1
    return s

def Qualify(blox,opts):
    k = 0
    for n in range(len(blox)):
        k += max(0,winsnties(opts[n]) - 1)
    if k > 1:
        return True
    else:
        return False
    



                                        ########PROGRAM SPECIFIC UTILITIES#######

#Adds a game's results to all relevant teams. 'Special' is a list
#It effects a teams headrec, comprec, etc.
    

def AddGame(g,add = 1,special = 'None'):
    if special == 'None':
        types = ['Rec']
        if g.team1.div == g.team2.div:
            types.append('Div')
        if g.team1.conf == g.team2.conf:
            types.append('Conf')
    else:
        types = special
    if g.result == 1:
        g.team1.addwin(types,add,2)
        g.team2.addwin(types,add,0)
    if g.result == 2:
        g,team1.addwin(types,add,0)
        g.team2.addwin(types,add,2)
    if g.result == 3:
        g.team1.addwin(types,add,1)
        g.team2.addwin(types,add,1)

#Removes a game/games

def RemoveGame(game,special = 'None'):
    AddGame(game,-1,special)
    game.result = 0

def RemoveGames(games,special = 'None'):
    for g in games:
        RemoveGame(g,special)

#Adds all games
            
def MakeRecs(gamelist):
    for g in gamelist:
        g.team1.opps += g.team2.name
        g.team2.opps += g.team1.name
        AddGame(g)

#Computes head-to-head records

def MakeHeadRecs(teamlist):
    teamnames = []
    for t in teamlist:
        t.headrec = 0
        teamnames.append(t.name)
    for g in AllGames:
        if g.team1.name in teamnames and g.team2.name in teamnames:
            AddGame(g,1,['Head'])

#Decides all games according to a key

def Resolve(gs,key):
    for n in range(len(gs)):
        gs[n].result = key[n]
        AddGame(g)

#Computes record in common games among teams

def MakeCommonRecs(teamlist):
    teamnames = []
    for t in teamlist:
        t.comrec = 0
        teamnames.append(t.name)
    opps = []
    for o in AllTeams:
        add = 1
        for t in teamlist:
            if not o.name in t.opps:
                add = 0
        if add == 1:
            opps.append(o.name)
    if len(opps) < 4:
        break
    for g in AllGames:
        if g.team1.name in teamnames and g.team2.name in opps:
            AddGame(g,1,['Com'])
        if g.team1.name in opps and g.team2.name in teamnames:
            AddGame(g,1,['Com'])    

#Finds the winner of a tiebreaker among division teams, winner(s) if SOV

def CompDivTeams(teamlist):
    if len(teamlist) == 1:
        return teamlist
    for T in ['Rec','Head','Div','Com','Conf']:
        if T == 'Head':
            MakeHeadRecs(teamlist)
        if T == 'Com':
            MakeCommonRecs(teamlist)
        listy = CompRecs(teamlist,T)
        if listy != teamlist:
            return CompDivTeams(listy)
    poss = []
    for S in ProperSubsets(teamlist):
        for t in CompDivTeams(S):
            if not t in poss:
                poss += t
    return poss

#Finds all possible orders of division teams with various SOV tiebreakers:

def DivSeeding(teamlist):
    if teamlist == []:
        return []
    else:
        seeds = []
        for t in CompDivTeams(teamlist):
            teamlist.remove(t)
            seeds += [[t] + DivSeeding(teamlist)]
            teamlist.insert(0,t)
        return seeds
    

#Sees if one team has swept all other teams in a list

def Checksweep(team,teamlist):
    winsweep = 1
    losesweep = 1
    for t in teamlist:
        if t != team:
            tcheck = 0
            for g in AllGames:
                if g.team1 == team and g.team2 == t:
                    tcheck = 1
                    if g.result == 1:
                        losesweep = 0
                    if g.result == 2:
                        winsweep = 0
                    if g.result == 3 or g.result == 0:
                        losesweep = 0
                        winsweep = 0
                if g.team2 == team and g.team1 == t:
                    tcheck = 1
                    if g.result == 1:
                        winsweep = 0
                    if g.result == 2:
                        losesweep = 0
                    if g.result == 3 or g.result == 0:
                        losesweep = 0
                        winsweep = 0
            if tcheck == 0:
                winsweep = 0
                losesweep = 0
    return winsweep - losesweep

#Finds the winner of a tiebreaker among conference teams (winners if SOV).

def CompConfTeams(teamlist):
    if len(teamlist) == 1:
        return teamlist
    for T in ['Rec','Head','Conf','Com']:
        listy = []
        if T == 'Head':
            for t in teamlist:
                k = Checksweep(t,teamlist)
                if k == 1:
                    return [t]
                if k == 0:
                    listy.append(t)
                        
        else:
            if T == 'Com':
                MakeCommonRecs(teamlist)
            listy = CompRecs(teamlist,T)
        if listy != teamlist:
            if len(listy) == 1:
                return listy
            else:
                return CompConfTeams(listy)
       poss = []
       for S in ProperSubsets(teamlist):
       for t in CompConfTeams(S):
           if not t in poss:
                poss += t
       return poss


#Decides, given a list of relevant teams, if that team will a) Make the playoffs, b) not make the playoffs, c) depends on SOV
#Each 'chunk' is a list of teams in the same division, so chunks is a list of lists
#chunks[0] is the list of teams in the same division as team

def Playoffs(team,chunks):

    chunks[0] += team

    pteams = []

    #First step is to scrape off division winners. At each step you get a list and have to iterate through options.

    seedings = []

    for chunk in chunks:
        seedings += [DivSeeding(chunk)]

    seeds = Weave(seedings)

    for s in seeds:
        mydivcs = []
        mywcs = []
        for n in range(len(s)):
            mydivcs += [s[n][0]]
            del s[n][0]
            s = [x for x in s if x != []]
            fiveseeds = []
            for k in range(len(s)):
                fiveseeds += s[k][0]
            for t in CompConfTeams(fiveseeds):
                sixseeds = []
                j = fiveseeds.index(t)
                news = list(s)
                del news[j][0]
                news = [x for x in news if x != []]
                for k in range(len(news)):
                    sixseeds += news[k][0]
                    for t2 in CompConfTeams(sixseeds):
                        mywcs += [[t,t2]]
        for p in mywcs:
            pteams += [[mydivcs + p]]
                
        
            

    
    


                                    ######THA BEEF#####


def GetScenarios(teamsW,teamsT,teamsL,gs,key,rec):
    #NEEDS WORK FOR TYING TEAMS...
    mywts = list(teamsW)
    mytts = list(teamsT)
    mylts = list(teamsL)
    mykey = list(key)
    mygs = [g for g in gs if g.result == 0]

    while not match(mykey,0) == -1:
        c = 0
        crit = []
        critop = []
        for t in mywts:
            if Maxrec(t) < rec + 2:
                crit.append(t)
        for t in mytts:
            if Maxrec(t) < rec + 1:
                crit.append(t)
            if t.rec == rec:
                critop.append(t)
        for t in mylts:
            if t.rec == rec - 1:
                critop.append(t)
        for n in range(len(gs)):
            g = gs[n]
            if g.result == 0:
                if g.team1 in mywts and not g.team2 in (mytts + mywts):
                    g.result = 1
                    Addgame(g)
                    mykey[n] = 1
                    c = 1
                elif g.team1 in crit:
                    g.result = 1
                    AddGame(g)
                    mykey[n] = 1
                    c = 1
                elif g.team1 in critop:
                    g.result = 2
                    AddGame(g)
                    mykey[n] = 2
                    c = 1
                elif g.team1 in mylts and not g.team2 in (mytts + mylts):
                    g.result = 2
                    AddGame(g)
                    mykey[n] = 2
                    c = 1
                elif g.team2 in mywts and not g.team1 in (mytts + mywts):
                    g.result = 2
                    AddGame(g)
                    mykey[n] = 2
                    c = 1
                elif g.team2 in crit:
                    g.result = 2
                    AddGame(g)
                    mykey[n] = 2
                    c = 1
                elif g.team2 in critop:
                    g.result = 1
                    AddGame(g)
                    mykey[n] = 1
                    c = 1
                elif g.team2 in mylts and not g.team1 in (mytts + mylts):
                    g.result = 1
                    AddGame(g)
                    mykey[n] = 1
                    c = 1
        for t in mywts:
            if t.rec > rec:
                c = 1
        for t in mytts:
            if t.rec > rec:
                RemoveGames(mygs)
                return []
        for t in mylts:
            if t.rec >= rec:
                RemoveGames(mygs)
                return []
        
        mywts = [t for t in mywts if t.rec <= rec]
        
        if c == 0:
            break
    if match(mykey,0) == -1:
        if mywts == []:
            for t in mytts:
                if t.rec < rec:
                    RemoveGames(mygs)
                    return []
            RemoveGames(mygs)
            return [mykey]
        else:
            RemoveGames(mygs)
            return []
    else:
        k = match(mykey,0)
        g = gs[k]
        if not (g.team1 in mytts) and not (g.team2 in mytts):
            g.result = 1
            AddGame(g)
            mykey[n] = 1
            keylist = GetScenarios(mywts,mytts,mylts,gs,mykey,rec)
            if not keylist == []:
                RemoveGames(mygs)
                return keylist
            RemoveGame(g)
            g.result = 2
            AddGame(g)
            mykey[n] = 2
            keylist = GetScenarios(mywts,mytts,mylts,gs,mykey,rec)
            if not keylist == []:
                RemoveGames(mygs)
                return keylist
            Removegame(g)
            g.result = 3
            AddGame(g)
            mykey[n] = 3
            keylist = GetScenarios(mywts,mytts,mylts,gs,mykey,rec)
            RemoveGames(mygs)
            return keylist
        else:
            g.result = 1
            AddGame(g)
            mykey[n] = 1
            keys1 = GetScenarios(mywts,mytts,mylts,gs,mykey,rec)

            RemoveGame(g)
            g.result = 2
            AddGame(g)
            mykey[n] = 2
            keys2 = GetScenarios(mywts,mytts,mylts,gs,mykey,rec)

            Removegame(g)
            g.result = 3
            AddGame(g)
            mykey[n] = 3
            keys3 = GetScenarios(mywts,mytts,mylts,gs,mykey,rec)

            RemoveGames(mygs)
            
            return keys1 + keys2 + keys3

def Emptykey(lst):
    key = []
    for n in lst:
        key.append(0)
    return key

def sort(ts,rs):
    tW = []
    tT = []
    tL = []
    for n in range(len(ts)):
        if rs[n] == 'W':
            tW.append(ts[n])
        if rs[n] == 'T':
            tT.append(ts[n])
        if rs[n] == 'L':
            tL.append(ts[n])
    return [tW,tT,tL]
            
        
def chk(ts,rs,gs,rec):
    tlist = sort(ts,rs)
    res = GetScenarios(tlist[0],tlist[1],tlist[2],gs,Emptykey(gs),rec)
    if res == []:
        return False
    else:
        return True

def CheckDefeatable(team):
    M = team.rec
    blox = []
    allts = []
    ind = -1
    
    #FIND ALL RELEVANT TEAMS AND GAMES
    
    for d in AllDivs[team.conf]:
        ts = []
        for t in d.teams:
            if Maxrec(t) > M and t != team:
                ts.append(t)
                allts.append(t)
        blox.append(SortRecs(ts,Maxrec))
    blox = SortRecs(blox,lambda t: Maxrec(t[1]))
    flip = 0
    for n in range(len(blox)):
        try:
            if blox[n][0].div == team.div:
                ind = n
                flip = 1
        except:
            pass
    if flip == 0:
        ind = -1
    gs = [g for g in AllGames if (g.team1 in allts or g.team2 in allts) and g.result == 0)
    
    #CHECK ALL COMBINATIONS
    
    for p in Pairs(range(4)):
        if ind in p:
            for Q in Pairs(blox[p[0]]):
                for R in Pairs(blox[p[1]]):
                    if chk(Q + R,['W','W','W','W'],gs,M):
                        return Q + R
        else:
            for Q in Pairs(blox[p[0]]):
                for R in Pairs(blox[p[1]]):
                    for t in blox[ind]:
                        if chk(Q + R + [t],['W','W','W','W','W'],gs,M):
                            return Q + R + [t]
    for i in range(4):
        if i == ind:
            for Q in ntuples(blox[i],3):
                if chk(Q,['W','W','W'],gs,M):
                    return Q
        else:
            for Q in ntuples(blox[i],3):
                for t in blox[ind]:
                    if chk(Q + [t],['W','W','W','W'],gs,M):
                        return Q + [t]
    return []


                   
def GetLogs(team):

    #Returns a pair [List of Lists,List of List of Lists]. The first list could be empty, the second would then be a list
    #containing an empty list. The first argument is a list of teams, sorted by division. The second list is, for each
    #division in the first list, a list of possible results those teams could achieve. For example, the first list could be
    #[[chi,gb],[nyg,phi]] and the second would be a list consisting of , indicating that chi and gb could either both win or win/tie,
    #and nyg/phi must win/win.
    
    M = team.rec

    #MAKE THE TEAM LOSE OUT (tgs is so we can remove these games later)
    
    tgs = []
    for g in AllGames:
        if g.result == 0:
            if g.team1 == team:
                tgs.append(g)
                g.result = 2
                AddGame(g)
            elif g.team2 == team:
                tgs.append(g)
                g.result = 1
                AddGame(g)
    
    #FIND ALL RELEVANT TEAMS
    
    allts = []
    blox = []
    divopps = 0
    for d in AllDivs[team.conf]:
        ts = []
        for t in d.teams:
            if Maxrec(t) >= M and t != team:
                ts.append(t)
                allts.append(t)
        if not ts == []:
            if d == team.div:
                divopps = 1
                blox.append(SortRecs(ts,Maxrec))
            elif len(ts) > 1:
                blox.append(SortRecs(ts,Maxrec))
    blox = SortRecs(blox,lambda t: Maxrec(t[1]))
    for n in range(len(blox)):
        try:
            if blox[n][0].div == team.div and n > 0:
                blox.insert(0,blox.pop(n))
        except:
            pass

    if divopps == 0:
        RemoveGames(tgs)
        return [[],[[]],gs]

    gs = [g for g in AllGames if (g.team1 in allts or g.team2 in allts) and g.result == 0]

    #CATEGORIZE TEAMS AND CREATE ALL CHUNKS

    for t in allts:
        t.opts = []
        if Maxrec(t) > M:
            t.opts += 'W'       
        if M > t.rec:
            t.opts += 'L'
        if Maxrec(t) == M:
            t.opts += 'T'
        elif t.rec == M:
            t.opts += 'T'
        elif 'W' in t.opts and 'L' in t.opts:
            t.opts += 'T'
            
    nublox = []
    presets = []
    for ind in range(len(blox)):

        #ind goes through the divisions
        
        s = [[]]
        for t in blox[ind]:
            news = []
            for item in s:
                for o in t.opts:
                    news.append(item + [o])
            s = list(news)

        #Checks if those division teams can actually achieve the result
            
        s = [item for item in s if chk(blox[ind],item,gs,M)]

        if ind == 0:
            s = [item for item in s if winsnties(item) > 0]

        #Checks if there is actually a wildcard threat from this division

        add = 0
        if ind == 0:
            add = 1
        else:
            for item in s:
                if winsnties(item) > 1:
                    add = 1

        if add == 1:
            nublox.append(blox[ind])
            presets.append(s)
    sets = Weave(presets)

    sets = [item for item in sets if Qualify(nublox,item)]
    
    RemoveGames(tgs)        
    return [nublox,sets,gs]

def Clinch(team):
    beat = CheckDefeatable(team)
    if not beat == []:
        return beat
    else:
        log = GetLogs(team)
        myts = smash(log[0])
        mygs = log[2]

        tgs = []
        for g in AllGames:
            if g.result == 0:
                if g.team1 == team:
                    tgs.append(g)
                    g.result = 2
                    AddGame(g)
                elif g.team2 == team:
                    tgs.append(g)
                    g.result = 1
                    AddGame(g)

        SOV = []

        for pos in log[1]:
            pos2 = smash(pos)
            tlist = sort(myts,pos2)
            keys = GetScenarios(tlist[0],tlist[1],tlist[2],mygs,Emptykey(mygs),team.rec)
            for key in keys:
                Resolve(mygs,key)
                res = Playoffs(team,log[0])
                if res == 'No Clinch':
                    ans = Parse(mygs)
                    RemoveGames(mygs)
                    return ans
                if res == 'SOV':
                    SOV += [key]
                RemoveGames(mygs)
        if SOV == []:
            return 'Clinched!'
        else:
            return 'SOV Clinch...?'
                

        
    




def DivPos(team,ts):
    newts = [t for t in ts if t.div == team.div]
    lst = CompDivTeams([team] + ts)
    if team in lst:
        return 1
    else:
        return 0

def PlayoffPos(team,ts):
    pass

def WeekSweep(team,week,add = 1):
    mygs = [g for g in AllGames if g.week == week]
    teams = []
    for g in mygs:
        teams += [g.team1,g.team2]
        g.result = add + 1
    myts = [t for t in AllTeams if t in teams and t != team]
    for t in myts:
        t.rec[1] += add
    team.rec[0] += add

def DefIn1(team,week):
    WeekSweep(team,week)
    val = CheckDefeatable(team)
    WeekSweep(team,week,-1)
    return val
    

    
        
                        
    
    
    
