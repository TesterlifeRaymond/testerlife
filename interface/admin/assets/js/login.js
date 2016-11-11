var vue ;
vue = new Vue({
    el:"#login",
    data:{
        result:'',
        username:'',
        password:''
    },
    methods:{
        click:function() {
            console.log("this.username :"+this.username);
            console.log("this.password :"+this.password);
        }
    }
})