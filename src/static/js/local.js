$( document ).ready(function(){
  $('.tabs').tabs();
  
  $('a#pokemon').bind('click', function(self) {
    var url = self.currentTarget.attributes.href.value
    $.getJSON(url, function(data) {
        $("#pokemon-detail").html(data.results);
      });
    return false;
  });
});
