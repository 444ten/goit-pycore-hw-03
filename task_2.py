
def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        res = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            try:
                iden, name, age = line.split(',')
                res.append({"id": iden, "name": name, "age": age})
            except ValueError:
                print(f"Skip wrong line: {line}")

        return res
    
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


path = "sample/cats.txt"

cats_info = get_cats_info(path)
print(cats_info)
