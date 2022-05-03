from tkinter import TOP
import mysql.connector as mc
import gc 

RANG_NAME : str
uuid = []
score = [] 
score0 = []
RANG = []
TOP_RANG = []
uuid_toprangs = []
uuid_allrangs = []
score_toprangs = []
score_allrangs = []

db_main = mc.connect(
    host = "mysql3.joinserver.xyz",
    user = "u77034_L1ZfOAh3wl",
    passwd = "hETSKgyQjb=aYMwmHst+=L0q",
    database = "s77034_BadWars"
)

cursor_main = db_main.cursor()

# cursor.execute("SELECT name, uuid FROM bw_stats_players")

# for x in cursor:
#     print(x)

def naming(rang_score):
    if rang_score >= 0 and rang_score < 1000:
        RANG_NAME = 'Rookie'
    elif rang_score >= 1000 and rang_score < 1500:
        RANG_NAME = 'Newbie I'
    elif rang_score >= 1500 and rang_score < 2000:
        RANG_NAME = 'Newbie II'
    elif rang_score >= 2000 and rang_score < 2500:
        RANG_NAME = 'Newbie III'

    elif rang_score >= 2500 and rang_score < 3000:
        RANG_NAME = 'Bronze I'
    elif rang_score >= 3000 and rang_score < 3500:
        RANG_NAME = 'Bronze II'
    elif rang_score >= 3500 and rang_score < 4000:
        RANG_NAME = 'Bronze III'

    elif rang_score >= 4000 and rang_score < 4500:
        RANG_NAME = 'Iron I'
    elif rang_score >= 4500 and rang_score < 5000:
        RANG_NAME = 'Iron II'
    elif rang_score >= 5000 and rang_score < 5500:
        RANG_NAME = 'Iron III'

    elif rang_score >= 5500 and rang_score < 6000:
        RANG_NAME = 'Silver I'
    elif rang_score >= 6000 and rang_score < 6500:
        RANG_NAME = 'Silver II'
    elif rang_score >= 6500 and rang_score < 7000:
        RANG_NAME = 'Silver III'

    elif rang_score >= 7000 and rang_score < 7500:
        RANG_NAME = 'Gold I'
    elif rang_score >= 7500 and rang_score < 8000:
        RANG_NAME = 'Gold II'
    elif rang_score >= 8000 and rang_score < 8500:
        RANG_NAME = 'Gold III'

    elif rang_score >= 8500 and rang_score < 9000:
        RANG_NAME = 'Diamond I'
    elif rang_score >= 9000 and rang_score < 9500:
        RANG_NAME = 'Diamond II'
    elif rang_score >= 9500 and rang_score < 10000:
        RANG_NAME = 'Diamond III'

    elif rang_score >= 10000:
        RANG_NAME = 'Bed Master'
    
    return RANG_NAME


while True:
    cursor_main = db_main.cursor()
    cursor_main.execute("SELECT score FROM bw_stats_players")

    for x in cursor_main:
        score += x

    # if score != score0:       # Формула Владимира Ведина
    cursor_main = db_main.cursor()
    cursor_main.execute("SELECT uuid FROM bw_stats_players")

    for x in cursor_main:
        uuid += x

    for i in range(len(score)):
        if score[i] >= 10000:
            TOP_RANG.append(naming(int(score[i])))
            uuid_toprangs.append(uuid[i])
            score_toprangs.append(score[i])
        else:
            RANG.append(naming(int(score[i])))
            uuid_allrangs.append(uuid[i])
            score_allrangs.append(score[i])

    max_ind = score_toprangs.index(max(score_toprangs))

    TOP_RANG[max_ind] = 'Bed Grandmaster'

    order67 = 'UPDATE bw_rang_texted SET rang = \'' + TOP_RANG[max_ind] + '\' WHERE uuid = \'' + uuid_toprangs[max_ind] + '\''
    cursor_main.execute(order67)
    db_main.commit()

    TOP_RANG.remove(TOP_RANG[max_ind])
    TOP_RANG.reverse()
    uuid_toprangs.remove(uuid_toprangs[max_ind])
    score_toprangs.remove(score_toprangs[max_ind])
    
    for iInter in range(len(score_toprangs)):
        swapped = False
        for jInter in range(0, len(score_toprangs) - iInter - 1):
            if score_toprangs[jInter] > score_toprangs[jInter + 1]:
                score_toprangs[jInter], score_toprangs[jInter + 1] = score_toprangs[jInter + 1], score_toprangs[jInter]
                uuid_toprangs[jInter], uuid_toprangs[jInter + 1] = uuid_toprangs[jInter + 1], uuid_toprangs[jInter]
                swapped = True
                if swapped == False:
                    break

    uuid_toprangs.reverse()
    score_toprangs.reverse()


    for i in range(len(RANG)):
        order66 = 'UPDATE bw_rang_texted SET rang = \'' + RANG[i] + '\' WHERE uuid = \'' + uuid_allrangs[i] + '\''
        cursor_main.execute(order66)
        db_main.commit()


    for i in range(0, len(TOP_RANG)):
        TOP_RANG[i] += ' [Top-' + str(i+2) + ']'
        order66 = 'UPDATE bw_rang_texted SET rang = \'' + TOP_RANG[i] + '\' WHERE uuid = \'' + uuid_toprangs[i] + '\''
        cursor_main.execute(order66)
        db_main.commit()
        if i > 10:
            break
    
    TOP_RANG.clear()
    RANG.clear()
    score.clear()
    uuid.clear()
    uuid_allrangs.clear()
    uuid_toprangs.clear()
    score_allrangs.clear()
    score_toprangs.clear()
    
    # score0 = score        
                           