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
    repName += '\r\n' + map['name']
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
    factions = [
        'None',
        'Observer',
        'Empire',
        'Commentator',
        'Allied',
        'None',
        'None',
        'Random',
        'Soviet',
        'None'
    ]
    #数字对应的颜色意义
    colors = [
        'Blue', 
        'Yellow',
        'Green', 
        'Orange', 
        'Purple', 
        'Red', 
        'Cyan', 
        'Random'
    ]
    playerTmp = player.lstrip("H").rstrip(",").split(',')
    return {
        'name' : playerTmp[0],
        'color' : colors[int(playerTmp[4])],
        'faction' : factions[int(playerTmp[5])]
        }

#解析地图
def __decodeMap(mapInfo):
    #地图对应的地图名
    maps = {
        'map_mp_2_black1b'      : '原始神庙-TP',
        'map_mp_2_feasel1'      : '卡巴那共和国-CR',
        'map_mp_2_feasel2'      : '血流成河',
        'map_mp_2_feasel3'      : '秘密圣地',
        'map_mp_2_feasel4'      : '战斗实验平台-BB',
        'map_mp_2_feasel5'      : '雪梨-SP',
        'map_mp_2_feasel6'      : '工业区-IS',
        'map_mp_2_feasel7'      : '休闲聚会-',
        'map_mp_2_feasel8'      : '火山岛-FI',
        'map_mp_2_rao1'         : '无限岛-II',
        'map_mp_3_feasel2'      : '混乱火山湖',
        'map_mp_3_feasel3'      : '隐藏要塞',
        'map_mp_3_feasel4'      : '火山断层',
        'map_mp_4_black_xslice' : '敌对旅馆-HH',
        'map_mp_4_feasel1'      : '圆屋',
        'map_mp_4_feasel2'      : '岩石岭',
        'map_mp_4_feasel3'      : '疯狂暗礁',
        'map_mp_4_feasel5'      : '八角作战基地',
        'map_mp_4_feasel6'      : '池塘聚会-PP',
        'map_mp_4_feasel7'      : '交火圈-FR',#FR？
        'map_mp_4_ssmith2_remix': '死亡水域',
        'map_mp_4_stewart_1'    : '严寒对决',
        'map_mp_5_feasel2'      : '山顶杀戮',
        'map_mp_5_feasel3'      : '大型竞技场',
        'map_mp_6_feasel1'      : '殆尽的天堂',
        'map_mp_6_feasel3'      : '零下时刻-SZ',
        'map_mp_6_feasel4'      : '麦格马格登',
        'map_mp_6_ssmith2'      : '卡维利'
    }
    mapName = re.sub(r'(\d)*data/maps/official/', '', mapInfo['M'])
    return {
        'name' : maps[mapName].decode('utf-8'),
        'place_num': mapName.replace('map_mp_', '')[0],
        'image': mapName + '.jpg'
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
