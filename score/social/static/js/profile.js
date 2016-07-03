$(document).ready(function(){


	$('#nickname__save-button').removeAttr('disabled');


	$('#nickname__edit-input').on('keyup', function(){
		if ($(this).val().length<30) {
			getResults('/check-nick','json',{val: $(this).val()}, function(res){
				if (res.val == 1){
					$('#nickname__group').removeClass('has-success');
					$('#nickname__group').addClass('has-error');
					$('#nickname__save-button').attr('disabled','disabled');
					$('#nickname__status').html('<span style="color:red">This nickname has already taken</span>');
				} else if (res.val==0){
					$('#nickname__group').removeClass('has-error');
					$('#nickname__group').addClass('has-success');
					$('#nickname__save-button').removeAttr('disabled');
					$('#nickname__status').html('<span style="color:green">This nickname is available</span>');
				}
				$('#nickname__status').show();

			});	
		}
		else{
			$('#nickname__status').html('<span style="color:red">This nickname is too long</span>');
			$('#nickname__save-button').attr('disabled','disabled');
		}
		
	});


	$('#nickname__save-button').on('click',function(){
		var name = $('#nickname__edit-input').val();
		getResults('/save-nick','json',{val: name}, function(res){
			if (res.val){
				$('#nickname__title').html(name);
				$('#user__nickname-link').html(name);
				$('#nickname__status').hide();
			}
		});
	});

	$('.dropzone').dmUploader({
		url:'/avatar-upload',
		method:'POST',
		dataType:'json',
		onInit: function(){
		  console.log('Plugin successfully initialized');
		},
		onUploadSuccess: function(id, data){
			console.log(data.url);
			$('#avatar__image').hide(300);
			setTimeout(function(){
				$('#avatar__image').attr('src', data.url);
				$('#user__avatar').attr('src', data.url);
				$('#avatar__image').show(300);
			},350);
			
		}
	});




});