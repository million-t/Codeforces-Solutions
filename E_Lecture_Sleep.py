n, k = list(map(int, input().split(' ')))

all_theorems = list(map(int, input().split(' ')))
awake_at = list(map(int, input().split(' ')))

sum_before_technique = 0
for indx, theorems_at_a_time in enumerate(all_theorems):
    if awake_at[indx]:
        sum_before_technique += theorems_at_a_time

left = 0
max_num_theorems = sum_before_technique

for right in range(n):
    if not awake_at[right]:
        sum_before_technique += all_theorems[right]

    max_num_theorems = max(max_num_theorems, sum_before_technique)
    
    if right - left + 1 == k:
        if not awake_at[left]:
            sum_before_technique -= all_theorems[left]
        left += 1 

    
print(max_num_theorems)

         



    

