module.exports = function (grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        requirejs: {
            compile: {
                options: {
//                    appDir: '.',
//                    dir: "./dist",
//                    modules: [
//                        {name: 'replay'}
//                    ],
                    name: 'replay',
                    out: 'dist/replay.min.js',

                    mainConfigFile: 'src/configs.js',

                    baseUrl: 'src',
                    removeCombined: true,
                    fileExclusionRegExp: /(node_modules|Gruntfile\.js|\.idea|package\.json)/
                },
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-requirejs');
    grunt.registerTask('default', ['requirejs']);

};