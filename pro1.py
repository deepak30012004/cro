class Process:
    def __init__(self, p_id, name, start_time, priority):
        self.p_id = p_id
        self.name = name
        self.start_time = start_time
        self.priority = priority
    
    def _str_(self):
        return f"{self.p_id} {self.name} {self.start_time} {self.priority}"

def sort_processes(processes, sort_key):
    if sort_key == 1:
        return sorted(processes, key=lambda p: p.p_id)
    elif sort_key == 2:
        return sorted(processes, key=lambda p: p.start_time)
    elif sort_key == 3:
        return sorted(processes, key=lambda p: (p.priority, p.start_time))

def main():
    processes = [
        Process("P1", "VSCode", 100, "MID"),
        Process("P23", "Eclipse", 234, "MID"),
        Process("P93", "Chrome", 189, "High"),
        Process("P42", "JDK", 9, "High"),
        Process("P9", "CMD", 7, "High"),
        Process("P87", "NotePad", 23, "Low")
    ]

    while True:
        print("Menu:")
        print("1. Sort by Process ID (P_ID)")
        print("2. Sort by Start Time (ms)")
        print("3. Sort by Priority")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 4:
            break

        if choice in [1, 2, 3]:
            sorted_processes = sort_processes(processes, choice)
            for process in sorted_processes:
                print(process)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "_main_":
    main()