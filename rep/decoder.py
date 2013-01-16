# -*- coding: utf-8 -*-

import re

#解析回放文件
def decodeFile(fileName):
    replayRawData = __loadReplay(fileName)
    if replayRawData != '':
        return decode(fileName, replayRawData)

#解析回放数据
def decode(fileName, replayRawData):
    replayInfoTmp = __simpleDecode(replayRawData)
    #已经获得初步解析结果，但初步解析后数
    #值的意义还不明确，需进行进一步解析。
    
    players = __decodeAllPalyers(replayInfoTmp)
    map = __decodeMap(replayInfoTmp)
    return {
        'name'     :  __generatorRepName(players, map),
        'filename' :  fileName,
        'map'      :  map,
        'rules'    :  __decodeRules(replayInfoTmp),  
        'players'  :  players
        }

#初步解析
def __simpleDecode(replayRawData):
    result = {}
    for info in replayRawData.split(';'):
        infoArray = info.split('=')
        if(len(infoArray) > 1):
            key = infoArray[0]
            value = infoArray[1]
            result[key] = value #获得key->value格式的数据
    return result

#生成回放名称
def __generatorRepName(players, map):
    repName = '';
    for player in players:
        if player['faction'] not in ['Observer', 'Commentator']:
            repName += player['name'] + '(' + player['faction'][0] +')'+ ' VS '
    repName = repName.rstrip(' S').rstrip('V')
    repName += map['name']
    return repName
    
    
#批量解析玩家
def __decodeAllPalyers(replayInfo):
    palyersResult = []
    playersTmp = replayInfo['S'].split(':')
    for player in playersTmp:
        if player != 'X' and player != '' and not re.search('Hpost Commentator',player):
            palyersResult.append(__decodePlayer(player))
    return palyersResult
    
#解析一个玩家
def __decodePlayer(player):
    #数字对应的阵营意义
    factions = ['None', 'Observer', 'Empire', 'Commentator', 'Allied', 'None', 'None', 'Random', 'Soviet', 'None']
    #数字对应的颜色意义
    colors = ['Blue', 'Yellow', 'Green', 'Orange', 'Purple', 'Red', 'Cyan', 'Random']
    playerTmp = player.lstrip("H").rstrip(",").split(',')
    return {
        'name' : playerTmp[0],
        'color' : colors[int(playerTmp[4])],
        'faction' : factions[int(playerTmp[5])]
        }

#解析地图
def __decodeMap(mapInfo):
    mapName = re.sub(r'(\d)*data/maps/official/', '', mapInfo['M'])
    return {
        'name' : mapName,
        'place_num': mapName.replace('map_mp_', '')[0],
        'image': 'images/' + mapName + '.jpg'
        }

#解析游戏规则
def __decodeRules(gameInfoMap):
    rulesTmp = gameInfoMap['RU'].split(' ')
    return {
        'player_num' : rulesTmp[0],
        'money' : rulesTmp[2]
        }

#读取回放
def __loadReplay(fileName):
    f = open(fileName, 'rb')
    while 1:
        line = f.readline()
        s = re.search(r'M=.*;', str(line))
        if s:
            line = s.group(0)
            f.close()
            return line
    f.close()
