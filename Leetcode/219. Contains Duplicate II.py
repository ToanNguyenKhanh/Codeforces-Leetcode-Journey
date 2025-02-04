def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    seen = set()
    left = 0  # Con trỏ trái

    for right in range(len(nums)):  # Con trỏ phải duyệt toàn bộ mảng
        if nums[right] in seen:  # Nếu phần tử đã xuất hiện trong cửa sổ, trả về True
            return True

        seen.add(nums[right])  # Thêm phần tử vào tập hợp

        # Nếu kích thước cửa sổ vượt quá k, loại bỏ phần tử cũ nhất (thu nhỏ cửa sổ)
        if right - left >= k:
            seen.remove(nums[left])
            left += 1  # Di chuyển con trỏ trái lên một bước

    return False  # Không tìm thấy cặp hợp lệ

if __name__ == '__main__':
    res = containsNearbyDuplicate([1,2,3,1,2,3], 2)
    print(res)
