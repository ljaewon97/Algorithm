def solution(stones, k):
    left = 0
    right = max(stones)
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for stone in stones:
            if stone <= mid:
                cnt += 1
            else:
                cnt = 0
            if cnt == k:
                break
        if cnt == k:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer