/**
 * User: weilao
 * Date: 13-10-20
 * Time: 上午10:15
 */
define(['underscore', 'util', 'map', 'player'], function (_, util, Map, Player) {
    var Replay = function (rep) {
        var raw;

        raw = rep.match(/M=.*;/);
        if (raw.length <= 0) return;

        raw = raw[0].split(';');
        raw = _.invoke(raw, 'split', '=');
        raw = _.object(raw);

        this.map = new Map(raw.M);
        this.players = Player.getPlayers(raw.S);
        this.date = decodeDate(rep);
        this.length = decodeLength(rep);
    };

    var decodeLength = function (raw) {
        var i, length, rawLength;
        rawLength = raw.slice(-1000);

        i = rawLength.search('FOOTER') + 6;
        length = util.getInt32At(rawLength, i) / 15;
        length = Math.floor(length);

        return length;
    };

    var decodeDate = function (raw) {
        var i, timeOffset, baseTime;
        baseTime = Date.UTC(1970, 0, 1, 0, 0, 0);

        i = raw.search('CNC3RPL\0RA3') + 10 + 20;
        timeOffset = util.getInt32At(raw, i) * 1000;

        return new Date(baseTime + timeOffset);
    };

    return Replay;
});
