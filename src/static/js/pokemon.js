function is_max_limits_ok(pokemon_list) {
    if (pokemon_list.length >= 6) return false;
    return true;
}

function is_min_limits_ok(pokemon_list) {
    if (pokemon_list.length < 1) return false;
    return true;
}

function add_pokemon(player_id, pokemon_id, pokemon_image, pokemon_list) {
    if (is_max_limits_ok(pokemon_list)) {
        pokemon_list.push(pokemon_id);
        var cur_pokemons_by_player = $("#player-".concat(player_id).concat("-detail"));
        var link_remove_pokemon = $.parseHTML("<a class=\"pokemon-remove\"></a>")[0];
        link_remove_pokemon.setAttribute('id', pokemon_id);
        link_remove_pokemon.prepend(pokemon_image);
        cur_pokemons_by_player.append(link_remove_pokemon);
    }
    else M.toast({html: 'You can\'t add more than 6 pokemons to player '.concat(player_id)})
}

$('.pokemon-add').on('click', function() {
    var id = this.attributes.id.value;
    var poke_image = $('#pokemon-image').clone(true)[0];

    var current_player_html = $('#player.active')[0].attributes.href.value;
    if (current_player_html == '#player-2') {
        add_pokemon('2', id, poke_image, player_2_pokemons);
    } else if (current_player_html == '#player-1') {
        add_pokemon('1', id, poke_image, player_1_pokemons)
    }
});

$('.remove-all').on('click', function() {
    var current_player_html = $('#player.active')[0].attributes.href.value;
    if (current_player_html == '#player-2') {
        $("#player-2-detail").empty();
        player_2_pokemons = [];
    } else if (current_player_html == '#player-1') {
        $("#player-1-detail").empty();
        player_1_pokemons = [];
    }
});

$('#trade-pokemon').off().on('click', function() {
    if (is_min_limits_ok(player_1_pokemons) && is_min_limits_ok(player_2_pokemons)) {
        $.ajax({
            type : 'POST',
            url : '/trade',
            contentType: 'application/json;charset=UTF-8',
            data : JSON.stringify({'data': [player_1_pokemons, player_2_pokemons]}),
            success: function (data) {
                $('.modal-content > p')[0].innerHTML= data['msg'];
                $('#modal1').modal();
                $('#modal1').modal('open');
            }
        });
    } else M.toast({html: 'Trade is not possible. Select at least one pokemon for each player.'})
    return false;
});
