# memorymanager.py

class Process:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.state = "READY"

# State variables
processes = {}
memory_blocks = {}
TOTAL_MEMORY = 1024
available_memory = TOTAL_MEMORY

def list_processes():
    if not processes:
        return "No processes currently exist."
    result = "PID\tNAME\t\tSTATUS\n"
    for p in processes.values():
        result += f"{p.pid}\t{p.name}\t\t{p.state}\n"
    return result.strip()

def create_process(pid, name):
    if pid in processes:
        return f"Process {pid} already exists."
    processes[pid] = Process(pid, name)
    return f"Process [{pid}] '{name}' created."

def run_process(pid):
    if pid not in processes:
        return f"Process {pid} not found."
    processes[pid].state = "RUNNING"
    return f"Process [{pid}] ({processes[pid].name}) is now running."

def kill_process(pid):
    global available_memory
    if pid not in processes:
        return f"Process {pid} not found."
    
    msg = ""
    # Auto-free memory if the process had any allocated
    if pid in memory_blocks:
        size = memory_blocks.pop(pid)
        available_memory += size
        msg += f"Freed {size}MB from Process [{pid}].\n"
        
    processes[pid].state = "TERMINATED"
    msg += f"Process [{pid}] has been killed."
    return msg

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