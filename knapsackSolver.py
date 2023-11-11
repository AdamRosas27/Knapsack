class Knapsack:

    def __init__(self, items, capacity):
        """Constructor method that initializes a knapsack with items/associated weights as well as the maximum capacity of the knapsack"""
        self.items = items
        self.capacity = capacity

    @staticmethod
    def knapsack_solver(items, capacity):
        """Knapsack solver method that utilizes a greedy tabulation method"""
        # Create 2 dimensional grid/table to hold values
        table = [[0] * (capacity + 1) for _ in range(len(items) + 1)]

        for row in range(1, len(items) + 1):
            item_weight, item_value = items[row - 1]
            for column in range(1, capacity + 1):
                if item_weight <= column:
                    table[row][column] = max(
                        table[row - 1][column], table[row - 1][column - item_weight] + item_value)
                else:
                    table[row][column] = table[row - 1][column]

        return table[len(items)][capacity]

    def calculate_max_value(self):
        """Returns the maximum achievable value within the knapsack's weight constraint"""
        max_value = self.knapsack_solver(self.items, self.capacity)
        return max_value
