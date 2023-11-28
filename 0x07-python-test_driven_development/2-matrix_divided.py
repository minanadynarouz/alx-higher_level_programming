def matrix_divided(matrix, div):
  result_matrix = []
  for row in matrix:
    if not isinstance(row, list):
      raise TypeError(
          "matrix must be a matrix (list of lists) of integers/floats")

  row_size = len(matrix[0])
  for row in matrix:
    if len(row) != row_size:
      raise TypeError("Each row of the matrix must have the same size")
    else:
      for item in row:
        if not isinstance(item, (int, float)):
          raise TypeError(
              "matrix must be a matrix (list of lists) of integers/floats")

  if not isinstance(div, (int, float)):
    raise TypeError("div must be a number")
  elif div == 0:
    raise ZeroDivisionError("division by zero")

  for row in matrix:
      result_matrix.append([float("{:.2f}".format(item / div)) for item in row])

  print(result_matrix)
