# Solving the 0/1 Knapsack Problem with Dynamic Programming using the Tabulation Method


class Knapsack:

    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def knapsack_solver(weights, values, capacity):
        # Create 2 dimensional grid/table to hold values
        table = [[0] * (capacity + 1) for _ in range(len(items) + 1)]

    def calculate_max_value(self):
        pass
