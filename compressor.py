import random

def generate_patterns(num_chains, chain_lengths, num_patterns):
    pattern_holder = []
    vals = []
    random.seed(7)
    for i in range(95):
        vals.append('X')
    for i in range(3):
        vals.append('0')
    for i in range(2):
        vals.append('1')
    random.shuffle(vals)
    for i in range(num_patterns):
        pattern_holder.append([])
        for j in range(num_chains):
            pattern_holder[i].append([])
            for k in range(chain_lengths):
                pattern_holder[i][j].append(vals[random.randint(0, 99)])
    return pattern_holder

def test_compare(test1, test2):
    if(len(test1) != len(test2)):
         return false
    for i in range(len(test1)):
        if((test1[i] != test2[i]) and (test1[i] != 'X') and (test2[i] != 'X')):
            return False
    return True

def inv_compare(test1, test2):
    if(len(test1) != len(test2)):
         return false
    for i in range(len(test1)):
        if((test1[i] == test2[i]) and not ((test1[i] == 'X') or (test2[i] == 'X'))):
            return False
    return True

def n_graph_coloring(color_num, graph):
    final_color_dict = {}
    for k in range(color_num):
        random_list = list(range(len(graph)))
        random.seed(k)
        random.shuffle(random_list)
        color_dict = {}
        for i in random_list:
            max_color = 0
            for j in range(len(graph[i])):
                if(str(graph[i][j]) in color_dict.keys()):
                    if(color_dict[str(graph[i][j])] > max_color):
                        max_color = color_dict[str(graph[i][j])]
            color_dict.update({str(i): max_color + 1})
        if(not bool(final_color_dict) or (max(color_dict.values()) < max(final_color_dict.values()))):
            final_color_dict = color_dict
    return final_color_dict

def fanout_decompressor(pattern_holder, num_chains):
    conflict_graph = []
    pattern_holder_length = len(pattern_holder)
    for i in range(num_chains):
        conflict_graph.append([])
        for j in range(num_chains):
            if(i != j):
                same = True
                inv = True
                for k in range(pattern_holder_length):
                    same = same and test_compare(pattern_holder[k][i], pattern_holder[k][j])
                    inv = inv and inv_compare(pattern_holder[k][i], pattern_holder[k][j])
                # if(same and not inv):
                #     print("Compatibility for chains {} and {}".format(i, j))
                # elif(inv and not same):
                #     print("Inverted compatibility for chains {} and {}".format(i, j))
                # elif(same and inv):
                #     print("Complete compatibility for chains {} and {}".format(i, j))
                # elif(not same and not inv):
                #     conflict_graph[i].append(j)
                if(not same and not inv):
                    conflict_graph[i].append(j)
    print("Conflict Graph:")
    print(*conflict_graph, sep="\n")
    return n_graph_coloring(16, conflict_graph)

pattern_holder = generate_patterns(16, 8, 100)
print("Heuristic choice for fanout coloring: " + str(fanout_decompressor(pattern_holder, 16)))
