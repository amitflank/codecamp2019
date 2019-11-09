// https://plot.ly/javascript/reference/#scatter3d

// can scale marker size if desired

var randomData = [
    [3, 2, 6, 1],
    [1, 7, 9, 4],
    [4, 1, 5, 2],
    [2, 20, 11, 25],
    [2, 3, 15, 6]
]

var duration = []
var loudness = []
var tempo = []
var hotness = []

randomData.forEach(song => {
    duration.push(song[0])
    loudness.push(song[1])
    tempo.push(song[2])
    hotness.push(song[3])
});

var data = [{
    x: duration,
    y: loudness,
    z: tempo,
    mode: 'markers+text',
    type: 'scatter3d',
    marker: {
        color: "rgb(250, 100, 150)",
        // color: tempo,
        // colorscale: `[[0, 'rgb(0,0,100)'], [1, 'rgb(255,0,0)']]`,
        size: hotness,
        sizemin: 10,
        sizeref: 2,
    },
    text: ["A", "B", "C", "D", "E"],
    hovertemplate:
        "%{text}" +
        "<br>Duration: %{x}"
    ,
}];

var layout = {
    autosize: true,
    height: 550,
    scene: {
        aspectratio: {
            x: 1,
            y: 1,
            z: 1
        },
        camera: {
            center: {
                x: 0,
                y: 0,
                z: 0
            },
            eye: {
                x: 1.25,
                y: 1.25,
                z: 1.25
            },
            up: {
                x: 0,
                y: 0,
                z: 1
            }
        },
        xaxis: {
            type: 'linear',
            zeroline: false
        },
        yaxis: {
            type: 'linear',
            zeroline: false
        },
        zaxis: {
            type: 'linear',
            zeroline: false
        }
    },
    title: 'Musical Landscape',
    width: 800,
};

Plotly.newPlot('myDiv', data, layout);

