def two_sum(srt_lst, target):
    left = 0
    right = len(srt_lst) - 1
    while left < right:
        if srt_lst[left] + srt_lst[right] < target:
            left += 1
        elif srt_lst[left] + srt_lst[right] > target:
            right -= 1
        elif srt_lst[left] + srt_lst[right] == target:
            return (left, right)
    return None


def main():
    srt_lst1 = [-2, 7, 11, 15, 20, 21]
    target1 = 18


