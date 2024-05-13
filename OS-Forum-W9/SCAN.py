def read_requests(filepath):
    with open(filepath, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines() if line.strip().isdigit()]
    return requests

def scan_algorithm(requests, initial_position, total_cylinders=4999):
    requests.append(initial_position)  
    requests.sort()
    
    start_index = requests.index(initial_position)
    
    if initial_position - min(requests) < total_cylinders - initial_position:
        to_start_movements = sum(requests[i] - requests[i - 1] for i in range(start_index, 0, -1))
        to_end_movements = requests[start_index] - requests[0] + (requests[-1] - requests[0])
    else:
        to_end_movements = sum(requests[i + 1] - requests[i] for i in range(start_index, len(requests) - 1))
        to_start_movements = requests[-1] - requests[start_index] + (requests[-1] - requests[0])
    
    total_movements = to_start_movements + to_end_movements
    return total_movements

filepath = 'C:\\Users\\Farrel\\Desktop\\OS-Forum-W9\\RNG.txt'  
initial_position = 1000 

requests = read_requests(filepath)
total_movements = scan_algorithm(requests, initial_position)
print(f'Total head movements for SCAN: {total_movements}')
