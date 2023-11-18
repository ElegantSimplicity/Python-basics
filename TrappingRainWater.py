""" Trapping Rain Water: still error so far!
https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map
where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section)
is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""
def trapped_positions(arr):
    S=0
    for level in range(max(arr)-1):
        print('LEVEL ',level)
        a = []
        for i in range(len(arr)):
            if arr[i]==0: a.append(0)
            else: a.append(arr[i]-level)

        start = 0
        stop = len(a)-1
        while a[start] == 0: start += 1      
        while a[start] > 0: start += 1       
        while a[stop] == 0: stop -= 1       
        while a[stop] > 0: stop -= 1       
        print('  ',a[start-1:stop+2])
        for i in range(start-1,stop+2):
            if a[i]==0:
                print('   Chỉ số hứng nước ',i) 
                S +=1
    return S       
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
#height = [4,2,0,3,2,5]
print('Số nước hứng được', trapped_positions(height))

