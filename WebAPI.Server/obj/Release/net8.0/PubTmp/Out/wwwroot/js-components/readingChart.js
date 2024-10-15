
function drawGraph(canvasId, jsonDatasets, wavelengths, minX, maxX, type) {
    const ctx = document.getElementById(canvasId).getContext('2d');

    // Destroy any existing chart to avoid overlapping
    if (ctx.chart) {
        ctx.chart.destroy();
    }

    // Parse the inputted JSON dataset(s)
    const datasets = JSON.parse(jsonDatasets);

    // Check if datasets is an array (multiple datasets) or a single object (single dataset)
    const parsedDatasets = Array.isArray(datasets) ? datasets : [datasets];

    // Default labels and chart type
    let setXLabel = 'Wavelength (nm)';
    let setYLabel = 'Intensity (counts)';
    let chartType = 'line';
    let xFontSize = 14;
    let xTickFont = 10;
    let yFontSize = 14;
    let yTickFont = 10;

    // Text colors all white
    let axisTitleColor = 'white';
    let tickColor = 'white';
    let legendTextColor = 'white';

    // Calculate tick positions for the x-axis
    const numberOfTicks = 10;
    const tickInterval = Math.floor(wavelengths.length / numberOfTicks);
    const xLabels = [];

    if (type === 'PredictAbsorbance') {
        setYLabel = 'Absorbance';
    }

    for (let i = 0; i < wavelengths.length; i += tickInterval) {
        xLabels.push(wavelengths[i]);
    }
    xLabels.push(wavelengths[wavelengths.length - 1]);

    const xScaleOptions = {
        title: {
            display: true,
            text: setXLabel,
            font: {
                size: xFontSize
            },
            color: axisTitleColor
        },
        ticks: {
            autoSkip: false,
            callback: function (value, index, values) {
                const tickIndex = values[index].value;
                if (xLabels.includes(wavelengths[tickIndex])) {
                    return Math.round(wavelengths[tickIndex]);
                } else {
                    return '';
                }
            },
            font: {
                size: xTickFont
            },
            color: tickColor
        },
        grid: {
            display: false,
            // Show grid lines only for the specified tick values
            drawTicks: true,
            tickColor: function (context) {
                const tickIndex = context.tick.value;
                if (xLabels.includes(wavelengths[tickIndex])) {
                    return tickColor;
                } else {
                    return 'rgba(0, 0, 0, 0)'; // Hide grid lines for other values
                }
            },
            tickBorderDash: [2, 2], // Make hidden grid lines dashed
        }
    };

    const yScaleOptions = {
        title: {
            display: true,
            text: setYLabel,
            font: {
                size: yFontSize
            },
            color: axisTitleColor
        },
        ticks: {
            font: {
                size: yTickFont
            },
            color: tickColor
        }
    };

    // Initialize chartData object
    const chartData = {
        labels: wavelengths, // Use the full wavelengths array for labels
        datasets: []
    };

    // Populate datasets array using a loop
    parsedDatasets.forEach(ds => {
        chartData.datasets.push({
            label: ds.Label,
            data: ds.Data,
            borderColor: ds.BorderColor,
            borderWidth: ds.BorderWidth,
            fill: ds.Fill,
            pointRadius: ds.PointRadius
        });
    });

    if (parsedDatasets[0]?.Data && parsedDatasets.length > 0) {
        ctx.chart = new Chart(ctx, {
            type: chartType,
            data: chartData,
            options: {
                scales: {
                    x: xScaleOptions,
                    y: yScaleOptions
                },
                plugins: {
                    legend: {
                        labels: {
                            color: legendTextColor
                        }
                    }
                }
            }
        });
    }
}



