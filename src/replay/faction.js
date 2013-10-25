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

    var FACTIONS = ["Observer", "Empire", "Commentator",
        "Allied", "Random", "Soviet"];

    var decodeName = function (factionId) {
        return FACTIONS[factionId] || "None";
    };

    return Faction;
});