#code
#https://practice.geeksforgeeks.org/problems/next-permutation/0

T = int(input())
for i in range(T):
    N = int(input())
    nums = [int(x) for x in input().split(" ") if x is not '']
    
    found = False
    for j in range(len(nums)-1,-1,-1):
        if j!=len(nums)-1:
            if nums[j]<nums[j+1]:
                found = True
                
                just_greater_num = min(x for x in nums[j+1:] if x > nums[j])
                index = nums[j+1:].index(just_greater_num)
                
                temp = nums[j]
                nums[j] = just_greater_num
                nums[j+1+index] = temp
                
                tmpl = nums[j+1:]
                tmpl.sort()
                
                nums = nums[:j+1] + tmpl
                
                for j in nums:
                    print (j,end=" ")
                break
    
    if not found:
        nums.sort()
        for j in nums:
            print (j,end=" ")
    if i!=T-1:
        print ()
