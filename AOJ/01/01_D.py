S = int(input())
hour = S // 3600
minute = (S % 3600) // 60
second = (S % 3600) % 60
print(f"{hour}:{minute}:{second}")
