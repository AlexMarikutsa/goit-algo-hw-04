def get_cats_info(path: str) -> list:
    cats = []

    with open(path, "r") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 3:
                continue
        
            try:
                cat = dict(id=parts[0], name=parts[1], age=int(parts[2]))
                cats.append(cat)
            except ValueError as e:
                print(f"Cannot read cat info: {e}")
                continue

    return cats

def print_cats_info():
    path="/Users/triare/PythonProjects/goit-algo-hw-04/cats_file.txt"
    try:
        cats_info = get_cats_info(path)
        print(cats_info)
    except FileNotFoundError:
        print(f"No such file or directory: '{path}'")

if __name__ == '__main__':
    print_cats_info()