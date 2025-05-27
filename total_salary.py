def total_salary(path: str) -> tuple[int, int]:
    total = 0
    salary_count = 0

    with open(path, "r") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 2:
                continue
        
            total += int(parts[1])
            salary_count += 1

    average = int(total / salary_count) if (total > 0 and salary_count > 0) else 0

    return total, average

def print_total_salary():
    path="/Users/triare/PythonProjects/goit-algo-hw-04/salary_file.txt"
    try:
        total, average = total_salary(path)
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except FileNotFoundError:
        print(f"No such file or directory: '{path}'")


if __name__ == '__main__':
    print_total_salary()