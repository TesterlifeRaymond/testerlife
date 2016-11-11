var data = {"a":"1"}

var vue = new Vue({
    el:"#app9",
    data:{
        message:data.a=3,
    }
})

data.a === vue.a;
vue.a = "2";
data.a;
