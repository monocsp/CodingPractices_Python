receive_rope_count = int(input())
rope_list = []
max_weight = 0

for i in range(0, receive_rope_count):
    rope_list.append(int(input()))

rope_list.sort(reverse=True)

for index, limit_rope_weight in enumerate(rope_list):
    rope_count = index + 1
    current_limit_weight = rope_count * limit_rope_weight
    if current_limit_weight > max_weight:
        max_weight = current_limit_weight

print(max_weight)

