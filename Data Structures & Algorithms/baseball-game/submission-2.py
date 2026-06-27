class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        sum = 0

        for i in range(len(operations)):
            n = len(record)
            
                
            if operations[i] == '+':
                record.append(record[n-1] + record[n - 2])
                sum += (record[n-1] + record[n - 2])
            elif operations[i] == 'D':
                record.append(2 * record[n-1])
                sum += (2 * record[n-1])
            elif operations[i] == 'C':
                item = record.pop()
                sum = sum - item
            else:
                record.append(int(operations[i]))
                sum += int(operations[i])

        return sum



    