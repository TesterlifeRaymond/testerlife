var vue ;
vue = new Vue({
    el:"#login",
    data:{
        username:'',
        password:'',
        result:'',
        apiUrl:'http://127.0.0.1:5000/admin/login'
    },
    methods:{
        click:function() {
            this.$http.get(this.apiUrl)
                .then((response) => {
            if (this.result = 'success'){
                setTimeout(function () {
                    window.location.href = 'http://127.0.0.1:8888'
                },1000)
            }

        })
            .catch(function(response) {
                console.log(response)
            })
        }
    }
})