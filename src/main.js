/**
 * User: weilao
 * Date: 13-10-19
 * Time: 下午3:55
 */
define(['replay'], function (Replay) {

    var handleFileSelect = function () {
        var file, reader;

        reader = new FileReader();
        reader.onload = onload;

        file = this.files[0];
        reader.readAsBinaryString(file);
    };

    var onload = function (e) {
        var replay = new Replay(this.result);
        document.writeln(JSON.stringify(replay));
        console.log(JSON.stringify(replay));
    };

    document.getElementById('files').addEventListener('change', handleFileSelect, false);
});