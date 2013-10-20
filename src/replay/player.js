/**
 * User: weilao
 * Date: 13-10-20
 * Time: 上午10:22
 */
define(['underscore', 'util', 'faction', 'clan'], function (_, util, Faction, Clan) {
    var Player = function (strPlayer) {
        var tmp, rawName;

        tmp = strPlayer.split(',');
        rawName = tmp[0].substr(1);

        switch (strPlayer[0]) {
            case 'H': //Human
                this.name = rawName;
                this.faction = new Faction(tmp[5]);
                this.color = this.getColor(tmp[4]);
                this.team = parseInt(tmp[7]) + 1;
                this.clan = tmp[11];
                break;

            case 'C': //Computer
                this.name = this.getComputerName(rawName);
                this.color = this.getColor(tmp[1]);
                this.faction = new Faction(tmp[2]);
                this.team = parseInt(tmp[4]) + 1;
                break;
        }

        this.name = util.ascii2utf8(this.name);
        this.clan = new Clan(this.name);
    };

    Player.prototype.getColor = function (colorId) {
        // 无法解析随机颜色
        switch (colorId) {
            case "0":
                return 'Blue';
            case "1":
                return 'Yellow';
            case "2":
                return 'Gray';
            case "3":
                return 'Orange';
            case "4":
                return 'Purple';
            case "5":
                return 'Red';
            case "6":
                return 'Cyan';
            default:
            case "7":
                return 'Azure';
        }
    };

    Player.prototype.getComputerName = function (level) {
        switch (level) {
            case "E": // Easy
                return "简单的电脑";
            case "M": // Middle
                return "中等的电脑";
            case "H": // Hard
                return "困难的电脑";
            case "B": // Brutal
                return "凶残的电脑";
            default:
                return "这不可能吧。。。录像坏了？";
        }
    };

    var isPlayerStr = function (rawPlayer) {
        return rawPlayer != "X" && rawPlayer != "" && rawPlayer.search("Hpost Commentator") < 0;
    };

    Player.getPlayers = function (strPlayers) {
        var players, player, rawPlayers;

        players = [];
        rawPlayers = strPlayers.split(':');

        _.each(rawPlayers, function (rawPlayer, i) {
            if (!isPlayerStr(rawPlayer)) return;

            if (rawPlayer.split(',').length > 1) {
                player = new Player(rawPlayer);
            } else {
                //卧槽，有人ID里竟然包含冒号。
                player = new Player(rawPlayer + ":" + rawPlayers[i + 1]);
            }
            players.push(player);
        });

        return players;
    };

    return Player;
});