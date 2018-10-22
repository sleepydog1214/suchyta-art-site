class IndexImage {
    constructor(fragment) {
        this.imageFragment = fragment;
        this.snapObj = Snap(900,900);
    }

    buildColorDisplay() {
        // Load the svg file
        this.snapObj.append(this.imageFragment);

        // Get all paths in the svg
        var paths = this.snapObj.selectAll("path");

        // Build a set of all colors in the svg
        var strokeColors = new Set();
        paths.forEach(function(path) {
            var stroke = path.attr('stroke');
            if (stroke !== null || stroke !== undefined) {
                if (!strokeColors.has(stroke))
                    strokeColors.add(stroke);
            }
        });

        // Draw new svg circles of each color
        var numColorRows = strokeColors.size / 15;

        if (strokeColors.size % 15 > 0)
            numColorRows++;

        var colorHeight = (numColorRows * 45) + 25;
        var colorWidth = 700;
        var colorsSvg = Snap(colorWidth, colorHeight);

        var x = 35, y = 35, idx = 0;
        for (var stroke of strokeColors) {
            if (idx != 0 && idx % 15 == 0) {
                x = 35;
                y += 45;
            }
            else if (idx != 0) {
                x += 45;
            }

            var c = colorsSvg.circle(x, y, 20).attr({ fill: stroke });
            idx++;
        }
    }
}