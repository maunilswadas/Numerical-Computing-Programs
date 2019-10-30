(function () {
    // Create Canvas
    let fractalCanvas = document.getElementById("fractalImage");
    let selectionCanvas = document.getElementById("selectionLayer");
    document.body.appendChild(fractalCanvas);
    let ctx = fractalCanvas.getContext("2d");
    let selectCtx = selectionCanvas.getContext("2d");

    let panX = 2;
    let panY = 1.5;
    let magnificationFactor = 200;

    let drawRectFlag = false;
    let rectPosStart = [0, 0];

    selectionCanvas.addEventListener("mousedown", e => {
        drawRectFlag = true;
        rectPosStart = [e.clientX, e.clientY];
    });
    selectionCanvas.addEventListener("mousemove", e => {
        if (drawRectFlag) {
            selectCtx.clearRect(0, 0, fractalCanvas.width, fractalCanvas.height);
            selectCtx.beginPath();
            selectCtx.setLineDash([5, 3]);
            selectCtx.strokeStyle = '#fff';
            selectCtx.rect(rectPosStart[0], rectPosStart[1], e.clientX - rectPosStart[0], e.clientY - rectPosStart[1]);
            selectCtx.stroke();
        }
    });
    selectionCanvas.addEventListener("mouseup", e => {
        drawRectFlag = false;
        selectCtx.clearRect(0, 0, fractalCanvas.width, fractalCanvas.height);
        console.log(e.clientX - rectPosStart[0]);
        console.log(e.clientY - rectPosStart[1]);
        console.log(600 / Math.min(e.clientX - rectPosStart[0], e.clientY - rectPosStart[1]))
        magnificationFactor = magnificationFactor * (600 / Math.max(e.clientX - rectPosStart[0], e.clientY - rectPosStart[1]));
        console.log(magnificationFactor)
        drawFractal(rectPosStart[0], rectPosStart[1]);
    });


    function checkIfBelongsToMandelbrotSet(x, y) {
        let realComponentOfResult = x;
        let imaginaryComponentOfResult = y;
        let maxIterations = 100;
        for (let i = 0; i < maxIterations; i++) {
            let tempRealComponent = realComponentOfResult * realComponentOfResult
                - imaginaryComponentOfResult * imaginaryComponentOfResult
                + x;
            let tempImaginaryComponent = 2 * realComponentOfResult * imaginaryComponentOfResult
                + y;
            realComponentOfResult = tempRealComponent;
            imaginaryComponentOfResult = tempImaginaryComponent;

            // Return a number as a percentage
            if (realComponentOfResult * imaginaryComponentOfResult > 5)
                return (i / maxIterations * 100);
        }
        return 0;   // Return zero if in set
    }

    function drawFractal(startOffsetX, startOffsetY) {
        // magnificationFactor += 200;
        panX -= startOffsetX / magnificationFactor;
        panY -= startOffsetY / magnificationFactor;

        ctx.clearRect(0, 0, fractalCanvas.width, fractalCanvas.height);
        for (let x = 0; x < fractalCanvas.width; x++) {
            for (let y = 0; y < fractalCanvas.height; y++) {
                let belongsToSet =
                    checkIfBelongsToMandelbrotSet(x / magnificationFactor - panX,
                        y / magnificationFactor - panY);
                if (belongsToSet === 0) {
                    ctx.fillStyle = '#000';
                    ctx.fillRect(x, y, 1, 1); // Draw a black pixel
                } else {
                    ctx.fillStyle = 'hsl(0, 100%, ' + belongsToSet + '%)';
                    ctx.fillRect(x, y, 1, 1); // Draw a colorful pixel
                }
            }
        }
    }

    drawFractal(0, 0);
})();