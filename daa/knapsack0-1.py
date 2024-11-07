def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    
    if wt[n-1] > W:
        return knapSack(W, wt, val, n-1)

    else:
        return max(
            val[n-1] + knapSack(W - wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1)
        )
    
if __name__ == '__main__':

    n = int(input("Enter the number of items: "))

    profit = []
    print("Enter the profit values:")
    for i in range(n):
        p = int(input(f"Profit for item {i+1}: "))
        profit.append(p)

    weight = []
    print("Enter the weight values:")
    for i in range(n):
        w = int(input(f"Weight for item {i+1}: "))
        weight.append(w)

    W = int(input("Enter the maximum weight capacity of the knapsack: "))

    print("Maximum profit:", knapSack(W, weight, profit, n))

    # N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}