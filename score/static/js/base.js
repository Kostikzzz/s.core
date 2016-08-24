
function refreshIndicators(){
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
}

$(document).ready(function(){
    refreshIndicators();
});