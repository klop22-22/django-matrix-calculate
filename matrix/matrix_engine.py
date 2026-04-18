class Matrix:
    def __init__(self, data):
        self.matrix = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
    

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры не совпадают")
        
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)


    def sub(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры не совпадают")

        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)


    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы не совпадает с количеством строк второй матрицы")

        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)


    def transpose(self):
        """Транспонирование матрицы (строки и столбцы меняются местами)"""
        result = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(result)


    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Определитель только для квадратных матриц")
        
        return self._det_recursive(self.matrix)
    

    def _det_recursive(self, matrix):
        n = len(matrix)
        
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for j in range(n):
            minor = [row[:j] + row[j+1:] for row in matrix[1:]]
            det += ((-1) ** j) * matrix[0][j] * self._det_recursive(minor)
        
        return det