/**
 * User: weilao
 * Date: 13-10-20
 * Time: 下午10:44
 */
require.config({
    baseUrl: './src',
    paths: {
        'underscore': 'libs/underscore',
        'replay': 'replay/replay',
        'map': 'replay/map',
        'player': 'replay/player',
        'faction': 'replay/faction',
        'clan': 'replay/clan',
        'util': 'replay/util'
    },
    shim: {
        underscore: {exports: '_'}
    }
});

requirejs(["main"]);