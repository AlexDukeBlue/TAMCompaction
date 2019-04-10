from compressor import generate_patterns, fanout_decompressor

def reconfigurable_compressor(pattern_holder1, pattern_holder2, num_chains):
    print("Configuration 1 coloring: " + str(fanout_decompressor(pattern_holder1, num_chains)))
    print("Configuration 2 coloring: " + str(fanout_decompressor(pattern_holder2, num_chains)))

def split_pattern_holder(pattern_holder):
    half_holders = [[], []]
    for i in range(len(pattern_holder)):
        if(i <= len(pattern_holder)/2):
            half_holders[0].append(pattern_holder[i])
        else:
            half_holders[1].append(pattern_holder[i])
    return half_holders

pattern_holder = generate_patterns(16, 8, 100)
half_holders = split_pattern_holder(pattern_holder)
pattern_holder1 = half_holders[0]
pattern_holder2 = half_holders[1]

reconfigurable_compressor(pattern_holder1, pattern_holder2, 16)
