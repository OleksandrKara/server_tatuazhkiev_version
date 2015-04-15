//// ---> Function for user_phone id
(function( $ ){
	
	//// ---> Проверка на существование элемента на странице
	jQuery.fn.exists = function() {
	   return jQuery(this).length;
	}
	
	//	Phone Mask
	$(function() {
		
    if(!is_mobile()){
    
      if($('#user_phone').exists()){
        
        $('#user_phone').each(function(){
          $(this).mask("(999) 999-99-99");
        });
        $('#user_phone')
          .addClass('rfield')
          .removeAttr('required')
          .removeAttr('pattern')
          .removeAttr('title')
          .attr({'placeholder':'(___) ___ __ __'});
      }
      
      if($('.phone_form').exists()){
        
        var form = $('.phone_form'),
          btn = form.find('.btn_submit');
        
        form.find('.rfield').addClass('empty_field');
      
        setInterval(function(){
        
          if($('#user_phone').exists()){
            var pmc = $('#user_phone');
            if ( (pmc.val().indexOf("_") != -1) || pmc.val() == '' ) {
              pmc.addClass('empty_field');
            } else {
                pmc.removeClass('empty_field');
            }
          }
          
          var sizeEmpty = form.find('.empty_field').size();
          
          if(sizeEmpty > 0){
            if(btn.hasClass('disabled')){
              return false
            } else {
              btn.addClass('disabled')
            }
          } else {
            btn.removeClass('disabled')
          }
          
        },200);

        btn.click(function(){
          if($(this).hasClass('disabled')){
            return false
          } else {
            form.submit();
          }
        });
        
      }
    }

	});

})( jQuery );



//// ---> Function for user_phone1 id
(function( $ ){
	
	//// ---> Проверка на существование элемента на странице
	jQuery.fn.exists = function() {
	   return jQuery(this).length;
	}
	
	//	Phone Mask
	$(function() {
		
    if(!is_mobile()){
    
      if($('#user_phone1').exists()){
        
        $('#user_phone1').each(function(){
          $(this).mask("(999) 999-99-99");
        });
        $('#user_phone1')
          .addClass('rfield')
          .removeAttr('required')
          .removeAttr('pattern')
          .removeAttr('title')
          .attr({'placeholder':'(___) ___ __ __'});
      }
      
      if($('.phone_form').exists()){
        
        var form = $('.phone_form'),
          btn = form.find('.btn_submit');
        
        form.find('.rfield').addClass('empty_field');
      
        setInterval(function(){
        
          if($('#user_phone1').exists()){
            var pmc = $('#user_phone1');
            if ( (pmc.val().indexOf("_") != -1) || pmc.val() == '' ) {
              pmc.addClass('empty_field');
            } else {
                pmc.removeClass('empty_field');
            }
          }
          
          var sizeEmpty = form.find('.empty_field').size();
          
          if(sizeEmpty > 0){
            if(btn.hasClass('disabled')){
              return false
            } else {
              btn.addClass('disabled')
            }
          } else {
            btn.removeClass('disabled')
          }
          
        },200);

        btn.click(function(){
          if($(this).hasClass('disabled')){
            return false
          } else {
            form.submit();
          }
        });
        
      }
    }

	});

})( jQuery );