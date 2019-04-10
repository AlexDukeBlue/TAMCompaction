
#compact(flops, is_tapped, input_polynomial) simulates an LFSR given input params.
#flops- gives the instantiation value of the flip-flopsself.
#is_tapped- is asserted if the flop input should be tapped (Type-2 LFSR) goes from high-order to low-order.
#input_polynomial- the input bits that are xor'ed into the x^{n-1} flop in order.
def compact(flops, is_tapped, input_polynomial):
    into_one = False
    #Iterating through the input_polynomial bits.
    for i in range(len(input_polynomial)):
        #Setting temporary flops so that we can update sequentially.
        temp_flops = flops.copy()
        #Update each flop depending on tap value and value of previous flop.
        for j in range(len(flops)):
            if(is_tapped[j] == 1 and j != 0):
                temp_flops[j] = flops[len(flops) - 1] ^ flops[j - 1]
            else:
                if(j != 0):
                    temp_flops[j] = flops[j - 1]
        temp_flops[0] = input_polynomial[i] ^ flops[len(flops) - 1]
        #Set current values to updated values.
        flops = temp_flops
        #Printing result.
        print("Timestep Result " + str(i + 1) + ": " + str(flops))
    #Printing final flop values.
    for i in range(len(flops)):
        print("x^{}".format(i) + ": " + str(flops[i]))

#Calling the function with the values for the homework.
compact([0, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1])
