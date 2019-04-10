
def tam_designer(total_width, wrapper_widths, num_cores):
    wrapper_widths.sort(reverse = True)
    tam_routes = [0] * num_cores
    for i in range(len(wrapper_widths)):
        if((sum(tam_routes) == 0) or (sum(tam_routes) > total_width)):
            for j in range(num_cores):
                tam_routes[j] = wrapper_widths[i]
    while(sum(tam_routes) < total_width):
        min_index = tam_routes.index(min(tam_routes))
        tam_routes[min_index] += 1
    return tam_routes

print(tam_designer(36, [2, 3, 4, 5, 6], 8))
