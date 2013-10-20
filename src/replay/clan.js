/**
 * User: weilao
 * Date: 13-10-20
 * Time: 下午7:51
 */
define(['underscore'], function (_) {
    var CLAN_LIST = [
        {
            shortName: 'CCZD',
            name: '传承战队'
        },
        {
            shortName: 'yzzd',
            name: '野战战队'
        },
        {
            shortName: 'RTJT',
            name: 'RT军团'
        }
    ];

    var findClan = function (playerName) {
        return _.find(CLAN_LIST, function (clan) {
            return playerName.indexOf(clan.shortName) > -1;
        });
    };

    var Clan = function (playerName) {
        var tmpClan;

        tmpClan = findClan(playerName);
        if (!tmpClan) return;

        this.shortName = tmpClan.shortName;
        this.name = tmpClan.name;
    };

    return Clan;
})
;