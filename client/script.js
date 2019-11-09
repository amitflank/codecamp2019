const url = "http://localhost:4200/find"

Vue.use(Vuetify)

var app = new Vue({
    el: '#app',
    vuetify: new Vuetify({}),
    data: {
        colors: ["blue-grey lighten-2", "blue-grey lighten-4", "grey lighten-4"],
        tatums: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096],
        loudness: null,
        tempo: null,
        duration: [120, 240]
    },

    methods: {
        sendQuery: function () {
            console.log(`Loudness: ${this.loudness}`)
            console.log(`Tempo: ${this.tempo}`)
            console.log(`Duration: ${this.duration}`)

            $.ajax({
                url: 'http://localhost:5000/test',
                data: $('form').serialize(),
                type: 'POST',
                success: function (response) {
                    response.json().then(function (data) {
                        console.log(data)
                    })
                },
                error: function (error) {
                    console.log(error);
                }
            });
            // fetch('/smart_Search', {
            //     method: "POST",
            //     headers: {
            //         "Content-type": "application/json"
            //     },
            //     body: JSON.stringify({
            //         loudness: app.loudness,
            //         tempo: app.tempo,
            //         duration: app.duration,
            //     })
            // }).then(function (res) {
            //     res.json().then(function (data) {
            //         console.log(data)
            //     });
            // });
        }
    },

    computed: {
        formatTime: function () {
            var lowMin = Math.floor(this.duration[0] / 60)
            var lowSec = this.duration[0] % 60
            lowSec += 100
            var lowSecString = "" + lowSec
            lowSecString = lowSecString.substring(1, 3)

            var highMin = Math.floor(this.duration[1] / 60)
            var highSec = this.duration[1] % 60
            highSec += 100
            var highSecString = "" + highSec
            highSecString = highSecString.substring(1, 3)

            return `${lowMin}:${lowSecString} - ${highMin}:${highSecString}`
        }
    }
})