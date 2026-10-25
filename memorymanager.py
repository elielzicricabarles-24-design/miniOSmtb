# State variables
processes = {}
memory_blocks = {}
TOTAL_MEMORY = 1024
available_memory = TOTAL_MEMORY
next_pid = 1  # <-- Added to track auto-generated PIDs

class Process:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.state = "READY"

def list_processes():
    if not processes:
        return "No processes currently exist."
    result = "PID\tNAME\t\tSTATUS\n"
    for p in processes.values():
        result += f"{p.pid}\t{p.name}\t\t{p.state}\n"
    return result.strip()

def run_process(name):
    global next_pid
    pid = str(next_pid) # Convert to string to match existing logic
    next_pid += 1
    
    processes[pid] = Process(pid, name)
    processes[pid].state = "RUNNING"
    
    return f"Process started.\n\nPID: {pid}\nName: {name}\nStatus: RUNNING"

def kill_process(pid):
    global available_memory
    if pid not in processes:
        return f"Process {pid} not found."
    
    msg = ""
    if pid in memory_blocks:
        size = memory_blocks.pop(pid)
        available_memory += size
        msg += f"Freed {size}MB from Process [{pid}].\n"
        
    processes[pid].state = "TERMINATED"
    msg += f"Process {pid} terminated."
    return msg

# (Keep your existing show_memory, allocate_memory, and free_memory functions here)

def show_memory():
    status = "--- Memory Status ---\n"
    status += f"Total Memory: {TOTAL_MEMORY} MB\n"
    status += f"Available Memory: {available_memory} MB\n"
    status += f"Allocated Blocks: {memory_blocks}"
    return status

def allocate_memory(pid, size_str):
    global available_memory
    try:
        size = int(size_str)
    except ValueError:
        return "Size must be an integer."
        
    if pid not in processes:
        return f"Process {pid} must be created first."
    if size > available_memory:
        return f"Allocation failed: Not enough memory for Process [{pid}]."
        
    available_memory -= size
    memory_blocks[pid] = size
    return f"Allocated {size}MB to Process [{pid}]."

def free_memory(pid):
    global available_memory
    if pid not in memory_blocks:
        return f"No memory allocated for Process {pid}."
    
    size = memory_blocks.pop(pid)
    available_memory += size
    return f"Freed {size}MB from Process [{pid}]."