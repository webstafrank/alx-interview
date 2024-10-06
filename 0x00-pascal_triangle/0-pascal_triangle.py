def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        # Start the row with a 1
        row = [1]
        # Compute the values for the middle of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End the row with a 1
        row.append(1)
        triangle.append(row)

    return triangle

