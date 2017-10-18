fronts = []
back = [1, 2, 3, 4]
operator = ["*", "+", "-", "/"]
loop_count = 0
hop_count = 0
limit_sum = 0
total_sum = 0

for i in range(1000):
    fronts.append(i+1)

for front in fronts:

    if operator[loop_count] == "*":
        limit_sum = front * back[loop_count]
    if operator[loop_count] == "+":
        limit_sum = front + back[loop_count]
    if operator[loop_count] == "-":
        limit_sum = front - back[loop_count]
    if operator[loop_count] == "/":
        limit_sum = front / back[loop_count]

    print (limit_sum)
    total_sum += limit_sum

    if total_sum > 100:
        hop_count += 1
        #print("hop_count:", hop_count, "total_sum", total_sum)
        total_sum = 0

    if loop_count == 3:
        loop_count = 0
    else:
        loop_count += 1

print("count:", hop_count)