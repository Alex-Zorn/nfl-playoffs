import teaminfo
import gameinfo
import maths

allgames = teaminfo.MakeGames(gameinfo.gamelist)

maths.MakeRecs(allgames)

def fun():
    for t in teaminfo.TeamObjs:
        print(t.name)
        print(t.rec)

def Defeatable(s):
    return maths.CheckDefeatable(teaminfo.Catalog(s),allgames,teaminfo.divlist)

def Defeatable2(s):
    maths.CheckDefeatable2(teaminfo.Catalog(s),allgames,teaminfo.divlist)

def WhosDefeatable():
    for t in teaminfo.TeamObjs:
        print(t.name)
        print(teaminfo.Names(Defeatable(t.name)))

def Def1(s):
    print(maths.DefIn1(teaminfo.Catalog(s),teaminfo.TeamObjs,allgames,teaminfo.divlist,14))

def WhosDef1():
    for t in teaminfo.TeamObjs:
        print(t.name)
        print(teaminfo.Names(maths.DefIn1(t,teaminfo.TeamObjs,allgames,teaminfo.divlist,14)))

def Sweep(s,add = 1):
    maths.WeekSweep(teaminfo.Catalog(s),teaminfo.TeamObjs,allgames,14,add)

for i in range(4):
    print(teaminfo.Names(maths.CompDivTeams(teaminfo.divlist['NFC'][i].teams,teaminfo.TeamObjs,allgames)))
