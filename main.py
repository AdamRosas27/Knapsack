from knapsackSolver import Knapsack

"""Driver code that calls the Knapsack solver class with item and capacity arguments"""


def main():
    items = [(2, 6), (2, 10), (3, 12)]
    capacity = 5

    k = Knapsack(items, capacity)

    max_value = k.calculate_max_value()
    print(f"Max Value: {max_value}")


if __name__ == "__main__":
    main()


"""
TESTING CASES:

Items: [(2, 6), (2, 10), (3, 12)]
Capacity: 5
Maximum Value: 22

Items: [(1, 1), (2, 4), (3, 4), (4, 5)]
Capacity: 7
Maximum Value: 10

Items: [(10, 60), (20, 100), (30, 120)]
Capacity: 50
Maximum Value: 220

Items: [(5, 10), (4, 40), (6, 30), (3, 50)]
Capacity: 10
Maximum Value: 90
"""
