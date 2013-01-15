# -*- coding: utf-8 -*-

#按阵营进行筛选
def byFactions(factions, reps):
    if isinstance(factions, str):
        factions = [factions] #将factions处理成数组

    #内战
    if factions[0] in factions[1:]:
        return filter(lambda rep : __onlyFaction(rep, factions[0]), reps)

    #非内战
    for faction in factions:
       reps = filter(lambda rep : __hasFaction(rep, faction), reps)
    return reps
    
#所有玩家阵营都为faction时返回True
def __onlyFaction(rep, faction):
    for player in rep['players']:
        if player['faction'] != faction:
            return False
    return True

#有玩家阵营为faction时返回True
def __hasFaction(rep, faction):
    for player in rep['players']:
        if player['faction'] == faction:
            return True
    return False

