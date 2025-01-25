class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        # Tính các hàng tiếp theo đến khi đạt rowIndex
        for i in range(1, rowIndex + 1):
            # Xây dựng hàng mới dựa trên hàng trước đó
            new_row = [1]  # Phần tử đầu luôn là 1
            for j in range(1, len(row)):
                new_row.append(row[j-1] + row[j])
            new_row.append(1)  # Phần tử cuối luôn là 1
            row = new_row  # Cập nhật hàng hiện tại
        return row