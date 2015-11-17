// Helper script, providing function for other scripts

var helper = {
    range: function(min, max) {
        var res = [];
        for(var i = min; i < max; i++) {
            res.push(i);
        }
        return res;
    },

    shuffle: function(ary, typeNum) {
        for(var i = ary.length - 1; 0 <= i; i--) {
            if (typeNum == 'pretty'){
                var rnd = Math.random() * (i + 1) | 0;
                helper.swap(ary, i, rnd);
            } else {
                var rnd = Math.random() * i + 1 | 0;
                ary[i] = rnd;
            }
        }
    },

    swap: function(ary, a, b) {
        if(a < 0 || b < 0 || ary.length <= a || ary.length <= b) {
            throw new Error('IndexError ' + a + " - " + b);
        }
        var temp = ary[a];
        ary[a] = ary[b];
        ary[b] = temp;
    },

    insert: function(ary, from, to) {
        while(from != to) {
            if(from < to) {
                helper.swap(ary, from, from + 1);
                from += 1;
            } else {
                helper.swap(ary, from, from - 1);
                from -= 1;
            }
        }
    },

    median3: function(a, b, c) {
        if(b <= a)
            if (a <= c)
                return a;
            else if(c <= b)
                return b;
            else
                return c;
        else if(c <= a)
            return a;
        else if(c <= b)
            return c;
        else
            return b;
    },

    getCanvas: function(id) {
        var canvas = document.getElementById(id);
        if(canvas === null || canvas.nodeName.toLowerCase() !== 'canvas') {
            return document.createElement('canvas');
        }
        return canvas;
    }
};

