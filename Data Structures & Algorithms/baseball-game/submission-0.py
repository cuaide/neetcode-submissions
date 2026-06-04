class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for operation in operations:
            if operation == "+":
                record.append(record[-1]+record[-2])
            elif operation == "C":
                record.pop()
            elif operation == "D":
                record.append(record[-1]*2)
            else:
                record.append(int(operation))#str -> int

        return sum(record)                