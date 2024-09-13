
student_grades = {
    'Alice': [85, 90, 88, 82],
    'Bob': [75, 80, 78, 72],
    'Charlie': [90, 85, 88, 92],
    'David': [80, 75, 82, 78]
}

def get_student_average(arr):
    return sum(arr) / len(arr)

def get_student_median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        return arr[n // 2]
    
def get_student_standard_deviation(arr):
    mean = get_student_average(arr)
    return (sum([(x - mean) ** 2 for x in arr]) / len(arr)) ** 0.5

def get_student_stats(student_grades):
    stats = {}
    for student, grades in student_grades.items():
        stats[student] = {
            'average': get_student_average(grades),
            'median': get_student_median(grades),
            'standard_deviation': get_student_standard_deviation(grades)
        }
    return stats

def print_student_stats(stats):
    for student, data in stats.items():
        print(f'{student}:')
        print(f'  Average: {data["average"]:.2f}')
        print(f'  Median: {data["median"]:.2f}')
        print(f'  Standard Deviation: {data["standard_deviation"]:.2f}')

print_student_stats(get_student_stats(student_grades))