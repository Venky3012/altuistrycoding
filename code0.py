def occur(arr):
    count = {}
    2
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    result = []
    for num, freq in count.items():
        if freq == 1:
            result.append(num)
    
    return sorted(result)
N = int(input())  
arr = list(map(int, input().split()))  

print(occur(arr))
