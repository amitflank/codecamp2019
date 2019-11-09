// https://plot.ly/javascript/reference/#scatter3d

// can scale marker size if desired
var data


function graph(data) {
    
    var duration = []
    var loudness = []
    var tempo = []
    var hotness = []
    var titles = []
    var artists = []
    
    Object.keys(data).forEach(key => {
        duration.push(data[key]['duration'])
        loudness.push(data[key]['loudness'])
        tempo.push(data[key]['tempo'])
        hotness.push(data[key]['hotttnesss'])
        titles.push(data[key]['title'], data[key]['artist'])
        artists.push(data[key]['artist'])
    });
    
    data = [{
        x: duration,
        y: loudness,
        z: tempo,
        mode: 'markers',
        type: 'scatter3d',
        marker: {
            color: "rgb(250, 100, 150)",
            // color: tempo,
            // colorscale: `[[0, 'rgb(0,0,100)'], [1, 'rgb(255,0,0)']]`,
            size: hotness,
            sizemin: 10,
            sizeref: 0.05,
        },
        text: titles,
        customdata: artists,
        hovertemplate:
            "%{text}: " + "%{customdata}" +
            "<br>Hotness: %{marker.size}"
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
}