def read_requests(filepath):
    with open(filepath, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines() if line.strip().isdigit()]
    return requests

def c_scan_algorithm(requests, initial_position, total_cylinders=4999):
    requests.append(initial_position)  
    requests.sort()
    
    
    start_index = requests.index(initial_position)
    
    to_end_movements = sum(requests[i + 1] - requests[i] for i in range(start_index, len(requests) - 1))
    
    if requests[-1] != total_cylinders:
        to_end_movements += total_cylinders - requests[-1]
    
    wrap_around_movements = total_cylinders + requests[0]
    
    if start_index != 0:
        wrap_around_movements += sum(requests[i + 1] - requests[i] for i in range(0, start_index - 1))
    
    total_movements = to_end_movements + wrap_around_movements
    
    return total_movements


initial_position = 1000  
filepath = 'C:\\Users\\Farrel\\Desktop\\OS-Forum-W9\\RNG.txt'

requests = read_requests(filepath)
total_movements = c_scan_algorithm(requests, initial_position)
print(f'Total head movements for C-SCAN: {total_movements}')
