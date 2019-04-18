import math

def minimize_function(wrapper_chains, objects_to_add, activity_monitor, name):
    for i in range(len(objects_to_add)):
        min_chain = wrapper_chains.index(min(wrapper_chains))
        max_chain = wrapper_chains.index(max(wrapper_chains))
        minimum_chain_val = math.inf
        minimum_chain_num = -1
        for j in range(len(wrapper_chains)):
            value_to_minimize = wrapper_chains[max_chain] - (objects_to_add[i] + wrapper_chains[j])
            if((value_to_minimize >= 0) and (value_to_minimize < minimum_chain_val)):
                minimum_chain_val = value_to_minimize
                minimum_chain_num = j
        if(minimum_chain_num == -1):
            wrapper_chains[min_chain] += objects_to_add[i]
            activity_monitor[min_chain].append("{}: {}".format(name, objects_to_add[i]))
        else:
            wrapper_chains[minimum_chain_num] += objects_to_add[i]
            activity_monitor[minimum_chain_num].append("{}: {}".format(name, objects_to_add[i]))

def design_wrapper(tam_width, primary_input_num, primary_output_num, internal_scan):
    wrapper_chains = []
    activity_monitor = []
    for i in range(tam_width):
        wrapper_chains.append(0)
        activity_monitor.append(["Wrapper-Chain {}".format(i + 1)])
    #Step 1
    internal_scan.sort(reverse = True)
    minimize_function(wrapper_chains, internal_scan, activity_monitor, "sc")
    #Step 2
    primary_inputs = [1] * primary_input_num
    wrapper_chains_copy1 = wrapper_chains.copy()
    minimize_function(wrapper_chains_copy1, primary_inputs, activity_monitor, "pi")
    #Step 3
    primary_outputs = [1] * primary_output_num
    wrapper_chains_copy2 = wrapper_chains.copy()
    minimize_function(wrapper_chains_copy2, primary_outputs, activity_monitor, "po")
    print(*activity_monitor, sep = "\n")
    return wrapper_chains

# design_wrapper(4, 8, 11, [12, 12, 8, 8, 8, 6, 6, 6, 6])
# design_wrapper(2, 16, 8, [12, 12, 8, 8])
# design_wrapper(3, 16, 8, [12, 12, 8, 8])
# design_wrapper(4, 16, 8, [12, 12, 8, 8])
# design_wrapper(5, 16, 8, [12, 12, 8, 8])
design_wrapper(6, 16, 8, [12, 12, 8, 8])
