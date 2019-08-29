let steps = {'x': [], 'y': []};
let function_points = [];

let x_min = Number(document.getElementById("x_min").value);
let x_max = Number(document.getElementById("x_max").value);

let tolerance = Number(document.getElementById("tolerance").value);
let maximum_iterations = Number(document.getElementById("maximum_iterations").value);

let diff = x_max - x_min;
let unit = 500 / diff;

let c = document.getElementById("myCanvas");
let ctx = c.getContext("2d");
ctx.translate(250, 250);


let interval = null;


const func1 = x => Math.pow(x, 2) - 4;
const func1_diff = x => 2 * x;

const func2 = x => -Math.pow(x, 2) + 4 * x + 5;
const func2_diff = x => 4 - 2 * x;

const func3 = x => Math.pow(x, 3) - 3 * Math.pow(x, 2) - 9 * x - 10;
const func3_diff = x => 3 * Math.pow(x, 2) - 6 * x - 9;

const func4 = x => Math.pow(x, 2) - 2 * x + 3;
const func4_diff = x => 2 * x - 2;

const func5 = x => 2 * Math.pow(x, 3) - 10 * Math.pow(x, 2) + 11 * x - 5;
const func5_diff = x => 6 * Math.pow(x, 2) - 20 * x + 11;

const func6 = x => Math.exp(-x) - x;
const func6_diff = x => -1 - Math.exp(-x);

const func7 = x => x - Math.exp(1 / x);
const func7_diff = x => 1 + Math.exp(1 / x) / Math.pow(x, 2);

let fn = func1;
let fn_diff = func1_diff;

const init = _ => {

    steps = {'x': [], 'y': []};
    function_points = [];

    x_min = Number(document.getElementById("x_min").value);
    x_max = Number(document.getElementById("x_max").value);
    tolerance = Number(document.getElementById("tolerance").value);
    maximum_iterations = Number(document.getElementById("maximum_iterations").value);

    diff = x_max - x_min;
    unit = 500 / diff;

};

const redrawAxis = () => {
    ctx.beginPath();
    ctx.moveTo(-250, 0);
    ctx.lineTo(250, 0);
    ctx.moveTo(0, -250);
    ctx.lineTo(0, 250);
    ctx.closePath();
    ctx.stroke();

    for (let i = -14; i < 15; i++) {
        ctx.fillRect(-3, i * 16.6, 6, 1);
        if (i === 0) continue;
        ctx.fillText((i * -1), 10, i * 16.6);
    }

    for (let i = x_min; i < x_max + 1; i++) {
        ctx.fillRect(i * unit, -3, 1, 6);
        if (i === 0) continue;
        ctx.fillText(i, i * unit, 15);
    }
};

const drawFunctionLine = () => {
    for (let i = 0; i < function_points.length - 1; i++) {
        ctx.moveTo(function_points[i][0] * unit, function_points[i][1] * -16.6);
        ctx.lineTo(function_points[i + 1][0] * unit, function_points[i + 1][1] * -16.6);
        ctx.lineWidth = 0.1;
        ctx.stroke();
    }
};

const drawSteps = async _ => {

    let counter = 0;

    redrawAll();


    interval = setInterval(() => {

        ctx.moveTo(steps.x[counter] * unit, steps.y[counter] * -16.6);
        ctx.lineTo(steps.x[counter + 1] * unit, steps.y[counter + 1] * -16.6);

        ctx.lineWidth = 1;
        ctx.stroke();

        counter++;

        if (counter >= steps.length - 1) clearInterval(interval);

    }, 200);
};


const redrawAll = _ => {
    ctx = c.getContext("2d");
    ctx.clearRect(-250, -250, c.width, c.height);
    redrawAxis();
    drawFunctionLine();
};

const setFunctionLine = func => {
    for (let i = x_min * 100; i < x_max * 100; i++) {
        function_points.push([i / 100, func(i / 100)]);
    }

};

const NewtonMethod = (e) => {
    let x = (e.offsetX - 256) / unit;
    let stepX = [x];
    let stepY = [fn(x)];

    for (let iteration = 0; iteration < maximum_iterations; iteration++) {
        let fxn = fn(x);
        if (Math.abs(fxn) < tolerance) {
            alert(`Found solution after ${iteration} iterations.`);
            steps = {'x': stepX, 'y': stepY}
            drawSteps()
            return null
        }
        let Dfxn = fn_diff(x);

        if (Dfxn === 0) {
            alert('Zero derivative. No solution found.')
            return null
        }

        x = x - fxn / Dfxn;
        stepX.push(x);
        stepY.push(0);

        stepX.push(x);
        stepY.push(fn(x))
    }
    alert('Exceeded maximum iterations. No solution found.')
    steps = {'x': stepX, 'y': stepY};
};

const fetchData = (func) => {
    init();
    ctx.clearRect(-250, -250, c.width, c.height);

    clearInterval(interval);

    fn = eval(`func${func}`);
    fn_diff = eval(`func${func}_diff`);
    setFunctionLine(fn);
    redrawAxis();
    drawFunctionLine();
};

fetchData(1);
c.addEventListener("mousedown", NewtonMethod, false);
