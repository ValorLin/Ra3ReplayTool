/**
 * User: weilao
 * Date: 13-10-20
 * Time: 下午1:27
 */
define(['underscore'], function (_) {

    return {

        str2bytes: function (str) {
            return  _.invoke(str.split(''), 'charCodeAt', 0);
        },

        bytes2int32: function (bytes) {
            return ( (bytes[0]) |
                (bytes[1] << 8) |
                (bytes[2] << 16) |
                (bytes[3] << 24));
        },

        getInt32At: function (str, i) {
            var bytes = this.str2bytes(str.slice(i, i + 4));
            return this.bytes2int32(bytes);
        },

        ascii2utf8: function (asciiText) {
            var i, c, c2, c3, string;
            i = c = c2 = c3 = 0;
            string = "";

            while (i < asciiText.length) {

                c = asciiText.charCodeAt(i);

                if (c < 128) {
                    string += String.fromCharCode(c);
                    i++;

                } else if ((c > 191) && (c < 224)) {
                    c2 = asciiText.charCodeAt(i + 1);
                    string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                    i += 2;

                } else {
                    c2 = asciiText.charCodeAt(i + 1);
                    c3 = asciiText.charCodeAt(i + 2);
                    string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                    i += 3;
                }

            }

            return string;
        }
    };
});