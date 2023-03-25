# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
score_table = []
for i in range(m):
    subject_score = list(map(float, input().split()))
    subject_score = [float(i) for i in subject_score]
    score_table.append(subject_score)
    
# print(score_table)
students = zip(*score_table)

students_avg = [(sum(i) / len(i)) for i in students]

for i in students_avg:
    print(i)
    