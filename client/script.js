Vue.use(Vuetify)

var app = new Vue({
    el: '#app',
    vuetify: new Vuetify({}),
    data: {
        colors: ["blue-grey lighten-2", "blue-grey lighten-4", "grey lighten-4"],
        tatums: [1,2,4,8,16,32,64,128,256,512,1024,2048,4096],
        tatum: null,
        timeSig: null,
        beats: null,
        duration: [120,240]
    },
    
    created() {
    
    },
    
    methods: {
    
    },
    
    computed: {
        formatTime: function() {
            var lowMin = Math.round(this.duration[0] / 60)
            var lowSec = this.duration[0] % 60
            lowSec += 100
            var lowSecString = "" + lowSec
            lowSecString = lowSecString.substring(1,3)
            
            var highMin = Math.round(this.duration[1] / 60)
            var highSec = this.duration[1] % 60
            highSec += 100
            var highSecString = "" + highSec
            highSecString = highSecString.substring(1,3)

            return `${lowMin}:${lowSecString} - ${highMin}:${highSecString}`
        }
    }
})