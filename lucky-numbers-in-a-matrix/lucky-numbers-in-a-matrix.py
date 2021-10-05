class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        number=[]
        for i in range (len(matrix)):
            j= matrix[i].index(min(matrix[i]))

            for k in range (0,len(matrix)):

                if matrix[i][j]<matrix[k][j]:
                            break
                else:
                    if k==len(matrix)-1:
                        number.append(matrix[i][j])
                        return number