def read_requests(filepath):
    with open(filepath, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines() if line.strip().isdigit()]
    return requests

def calculate_head_movements_fcfs(requests, initial_position):
    movements = 0
    current_position = initial_position
    for request in requests:
        movements += abs(current_position - request)
        current_position = request
    return movements

def calculate_head_movements_sorted_fcfs(requests, initial_position):
    sorted_requests = sorted(requests)  
    return calculate_head_movements_fcfs(sorted_requests, initial_position)

initial_position = 1000  
filepath = 'C:\\Users\\Farrel\\Desktop\\OS-Forum-W9\\RNG.txt'  

requests = read_requests(filepath)
original_movements = calculate_head_movements_fcfs(requests, initial_position)
sorted_movements = calculate_head_movements_sorted_fcfs(requests, initial_position)

print(f'Total head movements for original FCFS: {original_movements}')
print(f'Total head movements for sorted FCFS: {sorted_movements}')
