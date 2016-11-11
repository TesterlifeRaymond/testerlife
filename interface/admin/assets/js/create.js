/**
 * Created by liujinjia on 2016/11/11.
 */
var abc;
abc = 2
var vue = new Vue({
    el:"#app",
    data:{
        false:abc ===this.a,
        true: !(abc === this.a)
    },
    created:function () {
        console.log(abc ===this.a)
        console.log(!(abc ===this.a))
    }
})