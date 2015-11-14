// Script used to draw data graph

var graph = {};

(function() {
    var canvas;
    var ctx;
    var width;
    var height;

    var bgColor = '#f5f5f5';
    var barColor = '#2196f3';
    var highlightColor = '#ff8f00';

    // Initial graph
    graph.init = function(c) {
        canvas = c;
        ctx = canvas.getContext('2d');
        width = canvas.offsetWidth;
        height = canvas.offsetHeight;
    };

    // Draw bars on graph
    graph.draw = function(highlightIndexes, values) {
        ctx.fillStyle = bgColor;
        ctx.fillRect(0, 0, width, height);
        var idx1 = highlightIndexes[0];
        var idx2 = highlightIndexes[1];

        var size = values.length;
        var barWidth = (width - size + 1) / size;
        var barHeightUnit = height / size;

        var x = 0;
        var h = 0;
        ctx.fillStyle = barColor;
        for(var i = 0; i < values.length; i++) {
            h = values[i] * barHeightUnit;
            if(i === idx1 || i === idx2) {
                ctx.fillStyle = highlightColor;
                ctx.fillRect(x, height- h, barWidth, h);
                ctx.fillStyle = barColor;
            } else {
                ctx.fillRect(x, height- h, barWidth, h);
            }
            x = x + barWidth + 1;
        }
    };
})();

