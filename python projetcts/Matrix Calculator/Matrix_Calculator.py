def input_matrix(name="Matrix"):
    try:
        rows = int(input(f"Enter number of rows for {name}: "))
        cols = int(input(f"Enter number of columns for {name}: "))
        print(f"Enter elements row-wise for {name}:")
        matrix = []
        for i in range(rows):
            row = list(map(float, input(f"Row {i+1}: ").split()))
            if len(row) != cols:
                print("Invalid number of elements. Try again.")
                return input_matrix(name)
            matrix.append(row)
        return matrix
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return input_matrix(name)

def print_matrix(matrix, name="Result"):
    print(f"\n{name}:")
    for row in matrix:
        print(" ".join(f"{val:.2f}" for val in row))

def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Matrices must be of same dimensions for addition.")
        return None
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def subtract_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Matrices must be of same dimensions for subtraction.")
        return None
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        print("Number of columns of first matrix must equal rows of second.")
        return None
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def scalar_multiply(matrix, scalar):
    return [[scalar * val for val in row] for row in matrix]

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def main():
    while True:
        print("\nMatrix Calculator Menu:")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Scalar Multiplication")
        print("5. Transpose Matrix")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            a = input_matrix("Matrix A")
            b = input_matrix("Matrix B")
            result = add_matrices(a, b)
            if result: print_matrix(result)
        elif choice == '2':
            a = input_matrix("Matrix A")
            b = input_matrix("Matrix B")
            result = subtract_matrices(a, b)
            if result: print_matrix(result)
        elif choice == '3':
            a = input_matrix("Matrix A")
            b = input_matrix("Matrix B")
            result = multiply_matrices(a, b)
            if result: print_matrix(result)
        elif choice == '4':
            matrix = input_matrix()
            scalar = float(input("Enter scalar value: "))
            result = scalar_multiply(matrix, scalar)
            print_matrix(result)
        elif choice == '5':
            matrix = input_matrix()
            result = transpose_matrix(matrix)
            print_matrix(result)
        elif choice == '6':
            print("Exiting Matrix Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()