
function cloneSVG() {
    if(!document.getElementById("main2")){
        return;
    }
    if(!document.getElementById("bird")){
        return;
    }
    const sourceSVG = d3.select(main2);
    const targetSVG = d3.select(bird);
    var containerWidth = document.getElementById("svg-container").clientWidth;
    var containerHeight = document.getElementById("svg-container").clientHeight;

    // Set up SVG canvas
    targetSVG.attr("viewBox", "0 0 " + containerWidth + " " + containerHeight); // Outline width
    const svgContent = sourceSVG.node().innerHTML;
    targetSVG.html(svgContent);
    const rectX = -currentTranslateX *0.6;
    const rectY = -currentTranslateY*0.6;
   const x = 0; // x-coordinate of the top-left corner
    const y = 0; // y-coordinate of the top-left corner
    const viewBox = targetSVG.attr("viewBox").split(" ");
    const width = parseFloat(viewBox[2]);
    const height = parseFloat(viewBox[3]);
    const strokeWidth = 2; // Stroke width of the outline
    const strokeColor = "red"; // Stroke color of the outline
    targetSVG.append("rect")
        .attr("x", rectX)
        .attr("y", rectY)
        .attr("width", width/currentScale)
        .attr("height", height/currentScale)
        .attr("fill", "none") // No fill
        .attr("stroke", strokeColor) // Outline color
        .attr("stroke-width", strokeWidth)
        .attr('id', "redLine"); // Outline width
    const rect = d3.select("redLine");
}

if(document.getElementById("main")){
    var svgElement = d3.select("#main");
    var currentTranslateX = 0;
    var currentTranslateY = 0;
    var currentScale = 1;
    svgElement.on('zoomChange', function(event) {
        currentScale = d3.event.detail.scale;
        currentTranslateX = d3.event.detail.translateX;
        currentTranslateY = d3.event.detail.translateY;
    });
    setInterval(cloneSVG, 50);

}





