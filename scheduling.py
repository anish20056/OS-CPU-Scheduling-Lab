class Process:
	"""Class to represent a process"""
	def __init__(self, pid, at, bt):
		self.pid = pid
		self.at = at
		self.bt = bt

def main():
	print("\n" + "="*50)
	print("TASK 1: PROCESS CREATION & INPUT HANDLING")
	print("="*50)

	processes = []

	n = int(input("\nEnter number of processes: "))

	if n < 4:
		print(" Minimum 4 processes required. Setting to 4.")
		n = 4
	
	print("\n--- Enter Process Details ---")

	for i in range(n):
		print(f"\nProcess {i+1}:")

		pid = int(input(" Enter Process ID: "))

		at = int(input(" Enter Arrival Time: "))

		bt = int(input(" Enter Burst TIme: "))

		p = Process(pid, at, bt)
		processes.append(p)

	print("\n" + "="*50)
	print("PROCESS TABLE")
	print("="*50)
	print("PID\tArrival Time\tBurst Time")
	print("-" * 40)

	for p in processes:
		print(f"{p.pid}\t\t{p.at}\t\t{p.bt}")

	print("\n" + "="*50)
	print("TASK 1 COMPLETED")
	print("="*50)

if __name__ == "__main__":
	main()
