def total_salary(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        total = 0
        count = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue

            try:
                name, salary = line.split(",")
                total += float(salary)
                count += 1
            except ValueError:
                print(f"Skip wrong line: {line}")

        if count == 0:
            return 0, 0

        average = total / count

        return total, average

    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return 0, 0
    except Exception as e:
        print(f"Error: {e}")
        return 0, 0


path = "sample/salary.txt"

total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
