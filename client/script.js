const url = "http://localhost:4200/find"

Vue.use(Vuetify)

var app = new Vue({
    el: '#app',
    vuetify: new Vuetify({}),
    data: {
        colors: ["blue-grey lighten-2", "blue-grey lighten-4", "grey lighten-4"],
        loudness: 10,
        tempo: 25,
        duration: 180,

    },

    created() {
        fetch('http://localhost:5000/initialize', {
            method: "GET",
            headers: {
                "Content-type": "application/json"
            },
        }).then(function (response) {
            response.json().then(function (data) {
                console.log(data)
                graph(data)
            })
        });
        // $.ajax({
        //     url: 'http://localhost:5000/initialize',
        //     type: 'GET',
        //     success: function (response) {
        //         console.log("porn")
        //         response.json().then(function (data) {
        //             console.log(data)
        //             graph(data)
        //         })
        //     },
        // });
    },

    methods: {
        sendQuery: function () {
            console.log(`Loudness: ${this.loudness}`)
            console.log(`Tempo: ${this.tempo}`)
            console.log(`Duration: ${this.duration}`)

            $.ajax({
                url: 'http://localhost:5000/find_song',
                data: $('form').serialize(),
                type: 'POST',
                success: function (response) {
                    response.json().then(function (data) {
                        console.log(data)
                    })
                },
            });
        }
    },

    computed: {
        formatTime: function () {
            var min = Math.floor(this.duration / 60)
            var sec = this.duration % 60
            sec += 100
            var secString = "" + sec
            secString = secString.substring(1, 3)

            return `${min}:${secString}`
        }
    }
})