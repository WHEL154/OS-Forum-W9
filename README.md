# Disk Scheduling Algorithms: FCFS, SCAN, and C-SCAN

This repository contains Python implementations of three common disk scheduling algorithms:
1. First-Come, First-Served (FCFS)
2. SCAN (also known as the Elevator Algorithm)
3. Circular SCAN (C-SCAN)

These algorithms are used to determine the order in which disk I/O requests should be serviced, optimizing the movement of the disk's arm and thus improving performance.

## Algorithms Overview

### FCFS (First-Come, First-Served)
- **Description**: Services requests in the order they were made, without reordering.
- **Characteristics**: Simple and fair, but can lead to high seek times.

### SCAN (Elevator Algorithm)
- **Description**: Moves the disk arm across the entire disk, servicing requests as it goes from one end to the other, then reverses direction at each end of the disk.
- **Characteristics**: Provides more uniform wait times and can be more efficient than FCFS.

### C-SCAN (Circular SCAN)
- **Description**: Similar to SCAN, but the disk arm only moves in one direction. When it reaches the end, it jumps back to the beginning and continues in the same direction.
- **Characteristics**: Provides more predictable wait times than SCAN by treating the cylinders as a circular list that wraps around.

## Implementation

The Python scripts for these algorithms take a list of disk requests from a text file and the initial position of the disk's head. They then calculate and print the total head movements required for each algorithm.

### Code Structure

1. `read_requests(filepath)`
   - Reads disk request numbers from a file.
   - Returns a list of integers representing cylinder requests.

2. `calculate_head_movements_fcfs(requests, initial_position)`
   - Calculates the total head movements for FCFS.
   - Takes a list of requests and an initial head position as arguments.

3. `scan_algorithm(requests, initial_position, total_cylinders)`
   - Implements the SCAN algorithm.
   - Takes a list of requests, an initial head position, and the total number of cylinders.

4. `c_scan_algorithm(requests, initial_position, total_cylinders, sort_requests)`
   - Implements the C-SCAN algorithm.
   - `sort_requests`: A flag to choose between handling requests as they appear or sorting them.

### How to Run the Code

1. Make sure Python is installed on your system.
2. Place the disk request file in the same directory as the script or provide the path to the file.
3. Run the script from a terminal or command line:
   ```bash
   python disk_scheduling.py
