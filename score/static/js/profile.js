$(document).ready(function(){
	$('#add-nickname-button').removeAttr('disabled');
	$('#add-nickname-input').on('keyup', function(){
		if ($(this).val().length<30) {
			getResults('/check-nick','json',{val: $(this).val()}, function(res){
				if (res.val == 1){
					$('#nickname-group').removeClass('has-success');
					$('#nickname-group').addClass('has-error');
					$('#add-nickname-button').attr('disabled','disabled');
					$('#nickname-status').html('<span style="color:red">This nickname has already taken</span>');
				} else if (res.val==0){
					$('#nickname-group').removeClass('has-error');
					$('#nickname-group').addClass('has-success');
					$('#add-nickname-button').removeAttr('disabled');
					$('#nickname-status').html('<span style="color:green">This nickname is available</span>');
				}

			});	
		}
		else{
			$('#nickname-status').html('<span style="color:red">This nickname is too long</span>');
			$('#add-nickname-button').attr('disabled','disabled');
		}
		
	});
	$('#add-nickname-button').on('click',function(){
		var name = $('#add-nickname-input').val();
		getResults('/save-nick','json',{val: name}, function(res){
			if (res.val){
				$('#nickname').html(name);
				$('#nickname-status').hide();
			}
		});
	});
});