function labels($this, label, e){


	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight');
			} else {
		    label.removeClass('highlight');
			}
    } else if (e.type === 'focus') {

      if( $this.val() === '' ) {
    		label.removeClass('highlight');
			}
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }
}

$('.form').find('input, textarea').on('keyup blur focus', function (e) {
    var $this = $(this),
    label = $this.prev('label');
    labels($this, label, e);
});

$('.modal-content').find('input, textarea, input[type="number"]').on('keyup blur focus', function (e) {
    var $this = $(this),
    label = $this.prev('label');
    labels($this, label, e);
});

$('.tab a').on('click', function (e) {

  e.preventDefault();

  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');

  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();
  $('h3').not(target).hide();

  $(target).fadeIn(600);

});

var modal = document.getElementById('id01');
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

