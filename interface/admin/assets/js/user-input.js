var app5 = new Vue({
    el:"#app5",
    data:{
        message: "123456"
    },
    methods:{
        click:function() {
            this.message = this.message.split('').reverse().join('')
        }
    }
})