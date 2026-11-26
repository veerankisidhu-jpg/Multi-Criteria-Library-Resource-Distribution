
# Multi-Criteria Library Resource Distribution
# Python Case Study

# Library branches and book requirements
branches = ["Central Library", "North Branch", "South Branch"]

books = {
    "Python Programming": {
        "available": 20,
        "priority": 1,
        "demand": [12, 10, 8]
    },
    "Data Structures": {
        "available": 15,
        "priority": 2,
        "demand": [8, 12, 10]
    },
    "Operating Systems": {
        "available": 10,
        "priority": 3,
        "demand": [6, 7, 5]
    }
}

# Store allocation results
allocation_results = {}

print("=" * 60)
print("MULTI-CRITERIA LIBRARY RESOURCE DISTRIBUTION")
print("=" * 60)

# Process each book
for book_name, details in books.items():

    available = details["available"]
    priority = details["priority"]
    demand = details["demand"]

    total_demand = sum(demand)

    # Create branch allocation list
    allocation = [0] * len(branches)

    # Calculate allocation based on priority
    remaining_copies = available

    # Priority 1: Higher-priority books are processed first.
    # Within each book, branches receive copies in order
    # of their demand, highest demand first.

    branch_order = list(range(len(branches)))

    branch_order.sort(
        key=lambda i: demand[i],
        reverse=True
    )

    for i in branch_order:
        if remaining_copies > 0:
            copies_to_allocate = min(
                demand[i],
                remaining_copies
            )

            allocation[i] = copies_to_allocate
            remaining_copies -= copies_to_allocate

    # Calculate unmet demand
    unmet = []

    for i in range(len(branches)):
        unmet_demand = demand[i] - allocation[i]
        unmet.append(unmet_demand)

    total_allocated = sum(allocation)
    total_unmet = sum(unmet)

    allocation_results[book_name] = {
        "available": available,
        "total_demand": total_demand,
        "allocation": allocation,
        "unmet": unmet,
        "allocated": total_allocated,
        "total_unmet": total_unmet,
        "priority": priority
    }

# Display results
for book_name, result in allocation_results.items():

    print("\nBook:", book_name)
    print("Priority:", result["priority"])
    print("Available Copies:", result["available"])
    print("Total Demand:", result["total_demand"])

    print("\nBranch-wise Allocation:")

    for i in range(len(branches)):
        print(
            branches[i],
            "- Demand:",
            books[book_name]["demand"][i],
            "| Allocated:",
            result["allocation"][i],
            "| Unmet:",
            result["unmet"][i]
        )

    print("Total Allocated:", result["allocated"])
    print("Total Unmet Demand:", result["total_unmet"])

    if result["total_unmet"] == 0:
        print("Status: Demand Fully Satisfied")
    else:
        print("Status: Demand Not Fully Satisfied")

# Overall summary
total_available = 0
total_allocated = 0
total_unmet = 0

for result in allocation_results.values():
    total_available += result["available"]
    total_allocated += result["allocated"]
    total_unmet += result["total_unmet"]

print("\n" + "=" * 60)
print("OVERALL LIBRARY RESOURCE SUMMARY")
print("=" * 60)

print("Total Available Copies:", total_available)
print("Total Allocated Copies:", total_allocated)
print("Total Unmet Demand:", total_unmet)

print("\nBranch-wise Total Allocation:")

for i in range(len(branches)):
    branch_total = 0

    for result in allocation_results.values():
        branch_total += result["allocation"][i]

    print(branches[i], ":", branch_total, "copies")

print("\nProgram completed successfully.")
