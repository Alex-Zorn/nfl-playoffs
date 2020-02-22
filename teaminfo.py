#Team Info- Do not edit!

teamlist = []
teamlist.append(['NE','MIA','BUF','NYJ','AFCE','AFC'])
teamlist.append(['BAL','CIN','PIT','CLE','AFCN','AFC'])
teamlist.append(['HOU', 'IND', 'TEN','JAC','AFCS','AFC'])
teamlist.append(['DEN','SD','OAK','KC','AFCW','AFC'])
teamlist.append(['WAS','NYG','DAL','PHI','NFCE','NFC'])
teamlist.append(['CHI','GB','MIN','DET','NFCN','NFC'])
teamlist.append(['ATL','CAR','NO','TB','NFCS','NFC'])
teamlist.append(['SF','SEA','STL','ARI','NFCW','NFC'])

TeamObjs = []



conflist = ['AFC','NFC']



class Team(object):
    def __init__(self,name,div,conf):
        self.name = name
        self.div = div
        self.conf = conf
        self.gsplayed = 0
        self.rec = 0
        self.divrec = 0
        self.confrec = 0
        self.comrec = 0
        self.headrec = 0
        self.gprec = 0
        self.dict = {'Rec':self.rec,'Div':self.divrec,'Conf':self.confrec,
                     'Com':self.comrec,'Head':self.headrec,'Group':self.gprec}
        self.opps = []
        self.opts = []

    def addwin(self,kinds,add,result):
        for k in kinds:
            self.dict[k] += add*result
            if k == 'Rec':
                self.gsplayed += add
     

    def reset(self):
        self.rec = 0
        self.divrec = 0
        self.confrec = 0
        self.comrec = 0
        self.headrec = 0
        self.gprec = 0
 
class Div(object):
    def __init__(self,name):
        self.name = name
        self.teams = []

divlist = {'AFC':[Div('AFCE'),Div('AFCW'),Div('AFCS'),Div('AFCN')],
           'NFC':[Div('NFCE'),Div('NFCW'),Div('NFCS'),Div('NFCN')]}


for x in teamlist:
    for i in range(4):
        newteam = Team(x[i],x[4],x[5])
        TeamObjs.append(newteam)
        for d in divlist[x[5]]:
            if d.name == x[4]:
                d.teams.append(newteam)

def Catalog(string):
    for t in TeamObjs:
        if t.name == string:
            return t

def Names(lst):
    u = []
    for t in lst:
        u.append(t.name)
    return u

class Game(object):
    def __init__(self,team1,team2,result,week):
        self.team1 = team1
        self.team2 = team2
        self.result = result
        self.week = week

def MakeGames(gamelist):
    GameObjs = []
    for x in gamelist:
        GameObjs.append(Game(Catalog(x[0]),Catalog(x[1]),x[2],x[3]))
    return GameObjs




                                                                        
