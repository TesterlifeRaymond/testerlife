/**
 * Created by liujinjia on 2016/11/11.
 */
vue = new Vue({
    el:"#app",
    filter:{
        mustache:function (value) {
            this.message = 1
            if (!value) return this.message;
            alert(value)
            this.message = '111';
            return this.message
        }
    },
    data:{
        message:'111111111'
    }
})