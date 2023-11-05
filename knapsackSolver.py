# Solving the 0/1 Knapsack Problem with Dynamic Programming using the Tabulation Method


class Knapsack:

    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def knapsack_solver(items, capacity):
        # Create 2 dimensional grid/table to hold values
        table = [[0] * (capacity + 1) for _ in range(len(items) + 1)]

        for row in range(1, len(items) + 1):
            for column in range(1, capacity + 1):
                item_weight, item_value = items[i - 1]

    def calculate_max_value(self):
        pass
