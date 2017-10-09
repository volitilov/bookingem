var dropdown_controls = document.querySelectorAll('.dropdown-control');

dropdown_controls.forEach(function(element) {
  element.onclick = function() {
    var togl = this.nextElementSibling;
    var elem_clases = togl.classList;
    
    if (elem_clases.contains('active')) {
      elem_clases.remove('active');
    } else {
      elem_clases.toggle('active');
    }
  }
});