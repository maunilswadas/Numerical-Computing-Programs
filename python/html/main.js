let points = [];
let canvasPoints = [];
let c = document.getElementById("myCanvas");
let degree = document.getElementById("degree");
let ctx = c.getContext("2d");
ctx.translate(250, 250);

const redrawAxis = () => {
    ctx.beginPath();
    ctx.moveTo(-250, 0);
    ctx.lineTo(250, 0);
    ctx.moveTo(0, -250);
    ctx.lineTo(0, 250);
    ctx.closePath();
    ctx.stroke();
    for (let i = -9; i < 10; i++) {
        ctx.fillRect(-3, i * 25, 6, 1);
        ctx.fillRect(i * 25, -3, 1, 6);
        if (i === 0) continue;
        ctx.fillText((i * -1), 10, i * 25);
        ctx.fillText(i, i * 25, 15);
    }
};

const redrawPoints = () => canvasPoints.map(point => ctx.fillRect(point[0], point[1], 5, 5));

const drawRegressionLine = () =>
    fetch(`http://localhost:5000/regression?points=${JSON.stringify(points)}&degree=${degree.value}`)
        .then(data => data.json())
        .then(json => {
            for (let i = 0; i < json.x.length - 1; i++) {
                ctx.moveTo(json.x[i] * 25, json.y[i] * 25);
                ctx.lineTo(json.x[i + 1] * 25, json.y[i + 1] * 25);
                ctx.lineWidth = 0.1;
                ctx.stroke();
            }
        });

const redrawAll = _ => {
    ctx = c.getContext("2d");
    ctx.clearRect(-250, -250, c.width, c.height);
    redrawPoints();
    redrawAxis();
    drawRegressionLine();
};

const addPoint = (x, y) => {
    canvasPoints.push([x, y]);
    points = canvasPoints.map(point => ([point[0] / 25, point[1] / 25]));
};


c.onclick = ((e) => {
    addPoint(e.offsetX - 255, e.offsetY - 255);
    redrawAll();
});

redrawAxis();
redrawPoints();

