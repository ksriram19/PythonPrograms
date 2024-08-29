def countPerfectSums(arr, n, target_sum):
    # Create a 2D dp array with all values initialized to 0
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(n + 1)]

    # There is one way to achieve a sum of 0: by selecting no elements
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill dp array
    for i in range(1, n + 1):
        for j in range(target_sum + 1):
            if arr[i-1] <= j:  # If the current element can be included
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][target_sum]

# Example usage:
arr = [1, 2, 3, 4, 5]
target_sum = 5
n = len(arr)
print(f"Number of perfect sums: {countPerfectSums(arr, n, target_sum)}")