Ra3ReplayTool
=============

An javascript libray for decode *Command & Conquer: Red Alert 3* game replay.

Example Usage
-------------------------------------------------------------------------------------
	
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

Then you would get a replay objcet which contains attributes of the replay.

Don't use `readAsText()` since it would cause some problems with date decode and length decode. 