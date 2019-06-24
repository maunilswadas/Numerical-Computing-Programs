let steps = [];
let function_points = [];

let x_min_query = Number(document.getElementById("x_min").value);
let x_min = Math.floor(x_min_query - 1);

let x_max_query = Number(document.getElementById("x_max").value);
let x_max = Math.ceil(x_max_query + 1);


let tolerance = Number(document.getElementById("tolerance").value);
let maximum_iterations = Number(document.getElementById("maximum_iterations").value);

let diff = x_max - x_min;
let unit = 500 / diff;

let c = document.getElementById("myCanvas");
let ctx = c.getContext("2d");
ctx.translate(250, 250);

let interval = null;


const init = _ => {

    steps = [];
    function_points = [];

    x_min_query = Number(document.getElementById("x_min").value);
    x_min = Math.floor(x_min_query - 1);

    x_max_query = Number(document.getElementById("x_max").value);
    x_max = Math.ceil(x_max_query + 1);


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

        //secant
        ctx.moveTo(steps[counter].p1[0] * unit, steps[counter].p1[1] * -16.6);
        ctx.lineTo(steps[counter].p2[0] * unit, steps[counter].p2[1] * -16.6);

        //middle
        ctx.moveTo(steps[counter].p_middle[0] * unit, 0);
        ctx.lineTo(steps[counter].p_middle[0] * unit, steps[counter].p_middle[1] * -16.6);

        ctx.lineWidth = 1;
        ctx.stroke();

        counter++;

        if (counter >= steps.length) clearInterval(interval);

    }, 1000);
};


const redrawAll = _ => {
    ctx = c.getContext("2d");
    ctx.clearRect(-250, -250, c.width, c.height);
    redrawAxis();
    drawFunctionLine();
};

const fetchData = (func) => {
    init();
    clearInterval(interval)
    fetch(`http://localhost:5000/program_5_2?func=${func}&a=${x_min_query}&b=${x_max_query}&maximum_iterations=${maximum_iterations}&tolerance=${tolerance}`)
        .then(data => data.json())
        .then(json => {
            function_points = json.function_points;
            steps = json.steps;
        }).then(drawSteps);
};

fetchData(1);

