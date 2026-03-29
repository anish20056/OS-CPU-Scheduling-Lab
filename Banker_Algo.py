# =========================================================
# FOS LAB ASSIGNMENT 2
# Implementation of Banker's Algorithm for Deadlock Avoidance
# =========================================================

# -----------------------------
# TASK 1: System Input and Data Representation
# -----------------------------

print("\n=========== TASK 1: SYSTEM INPUT AND DATA REPRESENTATION ===========")

# Number of processes and resources
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))

# Allocation Matrix
print("\nEnter Allocation Matrix:")
allocation = []
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    allocation.append(row)

# Maximum Matrix
print("\nEnter Maximum Matrix:")
maximum = []
for i in range(n):
    row = list(map(int, input(f"P{i}: ").split()))
    maximum.append(row)

# Available Resources
print("\nEnter Available Resources:")
available = list(map(int, input().split()))

# Display System State
print("\nAllocation Matrix:")
for i in range(n):
    print(f"P{i}: {allocation[i]}")

print("\nMaximum Matrix:")
for i in range(n):
    print(f"P{i}: {maximum[i]}")

print("\nAvailable Resources:", available)


# -----------------------------
# TASK 2: Need Matrix Calculation
# -----------------------------

print("\n=========== TASK 2: NEED MATRIX CALCULATION ===========")

need = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(maximum[i][j] - allocation[i][j])
    need.append(row)

print("\nNeed Matrix (Need = Maximum - Allocation):")
for i in range(n):
    print(f"P{i}: {need[i]}")


# -----------------------------
# TASK 3: Banker's Safety Algorithm
# -----------------------------

print("\n=========== TASK 3: BANKER'S SAFETY ALGORITHM ===========")

finish = [False] * n
safe_sequence = []
work = available.copy()

print("Initial Work (Available Resources):", work)

while len(safe_sequence) < n:
    found = False

    for i in range(n):
        if not finish[i]:
            if all(need[i][j] <= work[j] for j in range(m)):

                print(f"\nProcess P{i} can execute since Need <= Work")

                # Update work
                for j in range(m):
                    work[j] += allocation[i][j]

                print("Updated Work:", work)

                safe_sequence.append(i)
                finish[i] = True
                found = True

    if not found:
        break


# -----------------------------
# TASK 4: Safe Sequence Determination
# -----------------------------

print("\n=========== TASK 4: SAFE SEQUENCE DETERMINATION ===========")

if len(safe_sequence) == n:
    print("System is in SAFE state.")
    print("Safe Sequence:", end=" ")

    for i in range(len(safe_sequence)):
        print(f"P{safe_sequence[i]}", end=" ")

    print()

else:
    print("System is NOT in safe state.")


# -----------------------------
# TASK 5: Result Analysis
# -----------------------------

print("\n=========== TASK 5: RESULT ANALYSIS ===========")

if len(safe_sequence) == n:
    print("The system is safe because all processes can complete execution.")
    print("There exists a safe sequence for process execution.")
    print("Therefore, deadlock will NOT occur.")
else:
    print("The system is unsafe because no safe sequence exists.")
    print("Deadlock may occur in this state.")
