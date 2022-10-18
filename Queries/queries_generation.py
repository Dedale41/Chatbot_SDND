import os
import pandas as pd
import numpy as np
import re
from nltk import word_tokenize 
import string
from random import randint, uniform, choice, sample

docs = ['CriticalRole','xQcOW','summit1g','Tfue','NICKMERCS','ludwig','TimTheTatman','Altoar','auronplay','LIRIK','__unknown__','Gaules','HasanAbi','Asmongold','loltyler1','RanbooLive','MontanaBlack88','ibai','Castro_1021','MOONMOON','TheRealKnossi','moistcr1tikal','Mizkif','CohhCarnage','shroud','AdmiralBahroo','Pestily','Sykkuno','ESL_CSGO','LVNDMARK','DrLupo','AdinRoss','Clix','TeePee','Rubius','PaymoneyWubby','alanzoka','Trainwreckstv','pokimane','tommyinnit','Maximilian_DOOD','GRONKH','sodapoppin','ZeratoR','BobbyPoffGaming','Ninja','Philza','Amouranth','BruceGreene','Odablock','RayNarvaezJr','Symfuhny','dakotaz','ZanoXVII','SypherPK','Trymacs','TheGrefg','Papaplatte','JohnPitterTV','RATIRL','RocketLeague','NoWay4u_Sir','GamesDoneQuick','GernaderJake','fps_shaka','EsfandTV','buddha','Locklear','stylishnoob4','ANGRYPUG','Sintica','Fresh','Quackity','RonnieRadke','Riot','KYR_SP33DY','Gladd','juansguarnizo','Bugha','NickEh30','Tubbo','Pikabooirl','RatedEpicz','Swagg','Shotz','CDNThe3rd','Tumblurr','Aydan','ops1x','scump','BarbarousKing','julien','mang0','Kitboga','chocoTaco','alexelcapo','Anomaly','Jerma985','The8BitDrummer','TSM_ImperialHal','Northernlion','ChilledChaos','Kamet0','lilypichu','daltoosh','mistermv','HusKerrs','OgamingLoL','nl_Kripp','Cellbit','cloakzy','Syndicate','Quin69','ELoTRiX','imaqtpie','Gotaga','Nick28T','forsen','JASONR','Ramee','chowh1','PietSmiet','LosPollosTV','POW3Rtv','Shlorox','GMHikaru','Lord_Kebun','Myth','chessbrah','SmallAnt','AnthonyZ','slEEPy','AvoidingThePuddle','LCS','Sardoche','Dhalucard','Nmplol','CaptainSparklez','fl0m','DougisRaw','Domingo','IlloJuan','UberHaxorNova','Baiano','dasMEHDI','Hitchariide','Hungrybox','Nagzz21','lilsimsie','TSM_Viss','GameAttack','Rallied','TheBubbaArmy','Repullze','aceu','aDrive','GeorgeNotFound','KingGeorge','kennybeats','Yassuo','Beaulo','Yogscast','ironmouse','JoshOG','Mews','GrandPOObear','MiltonTPike1','Kyle','Otzdarva','JLTomy','Pieface23','Solary','itsHafu','Ponce','LuluLuvely','ã‚‰ã£ã','Agraelus','richwcampbell','JERICHO','Limmy','Jelty']
X = []
Y = []

def create_query_print() :
    pages = randint(1, 500)
    doc = choice(docs)
    query_type = ["Je veux imprimer doc de number pages", 
                  "Imprime doc number pages", 
                  "doc number pages imprime", 
                  "print doc de number pages", 
                  "print doc de number pages", 
                  "Peux-tu imprimer doc, number pages"]
    query = choice(query_type)
    query = query.replace("number", str(pages))
    query = query.replace("doc", doc)

    X.append(query)
    Y.append(1)


def create_query_no_print() :
    query_type = ["Bonjour", 
                  "Comment ça va ?", 
                  "Quel est le planning ?"]
    query = choice(query_type)

    X.append(query)
    Y.append(0)


def create_queries(path_to_file, n = 50000) :
    for i in range (0, n//2) : 
        create_query_print()
        create_query_no_print()
    data = pd.DataFrame(list(zip(X,Y)),columns=["Query", "Label"])
    data.to_csv("Queries/"+path_to_file, index=False)


if __name__ == "__main__":
    create_queries("queries.csv", 10000)
