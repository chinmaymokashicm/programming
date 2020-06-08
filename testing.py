import pprint
""" 
from nlp import NLP

nlp = NLP()

print(nlp.abbreviation('AbcDE','ADE'))
print(nlp.abbreviation(
    'hHhAhhcahhacaccacccahhchhcHcahaahhchhhchaachcaCchhchcaccccchhhcaahhhhcaacchccCaahhaahachhacaahhaachhhaaaCalhhchaccaAahHcchcazhachhhaaahaahhaacchAahccacahahhcHhccahaachAchahacaahcahacaahcahacaHhccccaahaahacaachcchhahhacchahhhaahcacacachhahchcaAhhcaahchHhhaacHcacahaccccaaahacCHhChchhhahhchcahaaCccccahhcaachhhacaaahcaaaccccaacaaHachaahcchaahhchhhcahahahhcaachhchacahhahahahAahaAcchahaahcaaaaahhChacahcacachacahcchHcaahchhcahaachnachhhhcachchahhhacHhCcaHhhhcaCccccaaahcahacahchahcaachcchaachahhhhhhhhcahhacacCcchahccaaaaaHhhccaAaaaCchahhccaahhacaccchhcahhcahaahhgacahcahhchcaaAccchahhhaahhccaaHcchaccacahHahChachhcaaacAhacacaacacchhchchacchchcacchachacaahachccchhhaccahcacchaccaahaaaccccccaaaaaaaHhcahcchmcHchcchaaahaccchaaachchHahcaccaaccahcacacahAhaacaacaccaccaaacahhhcacAhaCchcaacCcccachhchchcchhchahchchahchchhchcacaachahhccacachaAhaaachchhchchchhaachahaahahachhaaaccacahhcacchhhaaachaaacAahhcachchachhhcacchacaaChCahhhccahChaachhcahacchanaaacchhhccacacchcahccchAcahacaaachhacchachccaaHacaacAhahcCh', 
    'HAHHCHAACCCAHCHHAHHAHCACCHCCHHCAAHHCACCCAHHHACAAHHHHCHHCAHHAHHAAAHAACAAHAHHCAHAHACHACHCHACACHAAHHAAAHCAHHACACAACHHHCHAHCAHCHHHAHAHACCAAAHCHHCHHCCAACCCCAACHACAACAAHACHCHAHHACCHCAHHHAAACHACAACHCACACAHHCCHAHACCCACCAACHCHHHCCCCCHCCAHHCAAHHAHHHHHHHAACCCCAHCCAAAAAHHHAAAACCAHHCAHACACCHHCHAHAHHCHAACHHHHHCCHCCAHAHCHCAAACCACCCCHACCACHHACHHACACHACCAACCCCAAAAHHAHCHHHCCAHCCHACHHAHCCACACCHAHAAACACCCCAHCCAHACCCCCCHCCHHCHHHHCHCHCAHHHACHAHAACCCAAAACHAACAAAHHAAHAAAHACHHCACHCCHCHAACHACACHHCCCCCAHCACHAAAHCHCAHACAAC'
    ))



print(nlp.abbreviation('LDJAN','LJJM'))
print(nlp.abbreviation(
    'XbxxobxBobbbxooXobXxxBOXoOboxxbobXOoBbxbXooXBboxooOxxXbboxoOxlobbObbXoXXbbXobbbXoxbxXBxoobooxbxoxoxOxxOxbxbxXobbbbBbxoxoooxooobXxbooBbOXxXxbxqobbbboXxoXXbbbxObXXxobOXXOxoOoxoXOXBxOxBoxbobxoBxbobobXooOxxOBXbxxXbooxbxooOxoxoobxxBOxxbbbxBxzXxbBxOobBObooofbbBXXOxxoxxbXBbOboxxooBbxOoboXoooXBbBbooOoBbbObxobxbBBoOxoxobBoOXXobObxobxOObobbbxxoboxoXxbXoxxxxbbobbXoXooBXXxboxbobxxxXboxOoOoxBoboOXboBoobXobxXdxObbbBxbxBbOOXbxooXboxboonxxxXOBbbXXoobooxbbxboxoOxBBbxBOxoobXbbxxbXXObxBbxBXBxoxOxoBbxBobOXbboxooBxbooXbXbooBbbxXboxXbxXoxbboxOXOooXbobooXXoxobbxoOxOoBbxxoBboboxoOBBxoboBoOboxbbxxbbbObXbboXbObOjXOXBxbxXobbbboBxBoOooxbxxOooxxbxxobbobxbbXoOobbBXoObxobXxoobxBxBbxoobXxoxObboxobobooxOoooBBbbbxxXoxbXxoXooxOBxboobxooxXOxobXoXmObxxXObooXXXboOXxbXxObxxbbObObxbxxbxxBXxBxoxOooaxooxXBXoXOxoOXxbBoBXxXooboXboOooxoxOxXxbxoboOObbBoXxbboxxooBBbooxXBbBoxBOobbboobobooxoxOxoXOXXboxXOboBxoboOooxbxBxobooXOoxOOObbxbobxxoxbOBoBxboxoobbbxoooxBxoobBbobBbooOBbxoboooookxXoobbbbBbOoxOBOobXObXBxoXoboxobbXBXBBoxBxoxooOxobxo', 
    'XBOBBOBOXOXBOXOOBOXOXOBBXOXBXOXXBBOBXOXXXOBBXBOOOXXOXBBBXOXOOOXXOBBOXXOBBXXXOXXXOXXOOXOXBOBBBXBBXOOXOBXXOOOOBXBOXXBXBXXXBXOBBOBBXXOXXBOBBXOXXBBOOOBBBOXBBBOXXBXXOBOBXOOOXXXXXXOBXXBOXXOOOOBOOOXBBOOBXOXXOBBBBOOXXOOXXXOBBXXOXBBOXOXBBBOXOBXXXBXXOBBXBOOBBBOXBBBOXBXBOBBXXXOXBOOXOOXBOXXOOOOBBBBOOBBOBOOBOBXBBOXBOBOXOXBXOBBOBBOXBOOXXBBBBBXOBXOBXXXBBBXOOBOOOXOOBBBXXOXXOXOBOXOBXXOXOOXXXOXXOBOOXBBXBOXBXXOXOXBOBXXOOXOOOXXBOOBBXXXBBOXBBXBOBBOOBOOXOXXBXOBOOOXBOXOOXOOOBBOBBOOOBBBBBOOBOXBBBOBOBXOXBXOBXBXBXBBBXOOO'
    ))




# print(nlp.min_edit_distance('Execution', 'Swap', substitution_weight=1))
# print(nlp.min_edit_distance('Execution', 'Swap', substitution_weight=2))
print(nlp.min_edit_distance('ATGCGTGGCATGGCAGGCTAAATT', 'ATCCGCCCGTGGTACGGAGCTACCT', substitution_weight=2))

print(NLP().min_edit_distance('ATGCGTGGCATGGCAGGCTAAATT', 'ATCCGCCCGTGGTACGGAGCTACCT', substitution_weight=0))
 """
distance_1 = [
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 900], [0, 0, 0, 0, 0]]
]

distance_2 = [
    [0, 0, 0, 1, 1, 0],
    [9, 2, 3, 1, 1, 1]]


def recurse(result, array, list_current_dimensions):
    if(len(list_current_dimensions) == 0):
        return(array)
    else:
        current_dimension = list_current_dimensions[0]
        list_next_dimensions = list_current_dimensions[1:]
        # list_past_dimensions.append(current_dimension)
        result = dict(
            [
                (current_dimension - 1, None),
                (current_dimension, None),
                (current_dimension + 1, None),
            ]
        )
        for i in [-1, 0, 1]:
            try:
                new_array = array[current_dimension + i]
                result[current_dimension + i] = recurse(
                    result[current_dimension + i],
                    new_array,
                    list_next_dimensions)
            except IndexError:
                # Remove the keys with None values
                result.pop(current_dimension + i)
                pass

        return(result)


# values_1 = recurse({}, distance_1, [2, 1, 4])
# values_2 = recurse({}, distance_2, [2,1])
# pprint.pprint(values_1)
# pprint.pprint(values_2)


result = {
  1: {
    1: {
      3: 1,
      4: 0
    },
    2: {
      3: 15,
      4: 10
    }
  },
  2: {
    1: {
      3: 11,
      4: 0
    },
    2: {
      3: 90,
      4: 0
    }
  }
}


def clean_adj_cells_dict(input_dict, output_dict):
    """ 
    Start with
    output_dict = {key: {} for key,value in result.items()}
    """
    for key,value in input_dict.items():
        if(not isinstance(value, dict)):
            if(value != 0):
                output_dict[key] = value
        else:
            output_dict[key] = clean_adj_cells_dict(
                input_dict[key],
                {key: {} for key,value in result.items()}[key]
            )
    return(output_dict)




# output_dict = {key: {} for key,value in result.items()}

# print(clean_adj_cells_dict(result, output_dict))


def recurse(list_prev_coord, weight, dictionary):
    result = []
    for key, value in dictionary.items():
        if(not isinstance(dictionary[key], dict)):
            list_prev_coord.append(key)
            weight = value
            result.append([list_prev_coord, weight])
        else:
            print('Here')
            list_prev_coord.append(key)
            result.append(recurse(
                list_prev_coord, 
                None, 
                dictionary[key]
                ))
    return(result)

graph_1 = {-1: {-1: {2: 3}, 0: {1: 3, 2: 2, 3: 1}, 1: {2: 1, 3: 1}},
 0: {-1: {3: 2}, 0: {1: 2, 2: 1}, 1: {}},
 1: {-1: {1: 1, 2: 1}, 0: {2: 1}, 1: {1: 1}}}
graph_2 = {1: {2: 1}, 2: {1: 3, 2: 2, 3: 1}}

print(recurse([], None, graph_2))