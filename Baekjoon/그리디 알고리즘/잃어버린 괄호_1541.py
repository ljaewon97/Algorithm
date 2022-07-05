s = input().split('-')
nums = []
for i in s:
    i = map(int, i.split('+'))
    nums.append(sum(i))

answer = nums[0]
for i in range(1, len(nums)):
    answer -= nums[i]
print(answer)