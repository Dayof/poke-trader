
var player_1_pokemons, player_2_pokemons;
player_1_pokemons = [];
player_2_pokemons = [];

$('.tabs').tabs();
$('#modal1').modal();

$('a#pokemon').bind('click', function() {
  var url = this.attributes.href.value
  $.getJSON(url, function(data) {
      $("#pokemon-detail").html(data.results);
    });
  return false;
});
