/**
 * User: weilao
 * Date: 13-10-20
 * Time: 上午9:54
 */
define(['underscore'], function (_) {
    var CLEAN_REGEXP = new RegExp('^.*data/maps/official/');
    var MAPS_NAME = {
        "map_mp_2_black1b": "原始神庙-TP",
        "map_mp_2_feasel1": "卡巴那共和国-CR",
        "map_mp_2_feasel2": "血流成河",
        "map_mp_2_feasel3": "秘密圣地",
        "map_mp_2_feasel4": "战斗实验平台-BB",
        "map_mp_2_feasel5": "雪梨-SP",
        "map_mp_2_feasel6": "工业区-IS",
        "map_mp_2_feasel7": "休闲聚会-",
        "map_mp_2_feasel8": "火山岛-FI",
        "map_mp_2_rao1": "无限岛-II",
        "map_mp_3_feasel2": "混乱火山湖",
        "map_mp_3_feasel3": "隐藏要塞",
        "map_mp_3_feasel4": "火山断层",
        "map_mp_4_black_xslice": "敌对旅馆-HH",
        "map_mp_4_feasel1": "圆屋",
        "map_mp_4_feasel2": "岩石岭",
        "map_mp_4_feasel3": "疯狂暗礁",
        "map_mp_4_feasel5": "八角作战基地",
        "map_mp_4_feasel6": "池塘聚会-PP",
        "map_mp_4_feasel7": "交火圈-FR",
        "map_mp_4_ssmith2_remix": "死亡水域",
        "map_mp_4_stewart_1": "严寒对决",
        "map_mp_5_feasel2": "山顶杀戮",
        "map_mp_5_feasel3": "大型竞技场",
        "map_mp_6_feasel1": "殆尽的天堂",
        "map_mp_6_feasel3": "零下时刻-SZ",
        "map_mp_6_feasel4": "麦格马格登",
        "map_mp_6_ssmith2": "卡维利",
        "083data/maps/internal/(new_star)_map-1v1_1.3": "第二届EEC比赛图",
        "081data/maps/internal/1v1_pool_party_made_by_maniek": "池塘派对1v1版"
    };

    return function (strMap) {
        var key = strMap.replace(CLEAN_REGEXP, '');

        this.name = MAPS_NAME[key];
        this.image = key + '.jpg';
        this.playerNum = key.replace('map_mp_', '')[0];
    };
});