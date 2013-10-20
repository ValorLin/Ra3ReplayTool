/**
 * User: weilao
 * Date: 13-10-20
 * Time: 上午10:37
 */
define(function () {
    var Faction = function (strFaction) {
        this.id = strFaction;
        this.name = decodeName(this.id);
        this.shortName = this.name[0];
    };

    var decodeName = function (factionId) {
        switch (factionId) {
            case '1':
                return "Observer";
            case '2':
                return "Empire";
            case '3':
                return "Commentator";
            case '4':
                return "Allied";
            case '7':
                return "Random";
            case '8':
                return "Soviet";
            default:
                return "None";
        }
    };
    return Faction;
});