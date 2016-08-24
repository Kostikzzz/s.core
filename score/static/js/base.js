/*
var navbarNotifier = new Vue({
    el:'#navbar',
    data: {
        hasMessages: 0
    },
    ready: function(){
        this.hasMessages = serverHasMessages;
    }
});*/

$(document).ready(function(){
    $('.serverMsgIndicator').hide();
    if (serverHasMessages){
        $('.serverMsgCount').html(serverHasMessages);
        $('.serverMsgIndicator').show();
    }

    $('.serverNotsIndicator').hide();
    if (serverHasNotifications){
        $('.serverNotsCount').html(serverHasNotifications);
        $('.serverNotsIndicator').show();
    }
});