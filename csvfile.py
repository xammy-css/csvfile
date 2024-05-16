
with open("tarifas.csv", "r", encoding="ISO-8859-1") as file:
    data = file.readlines()
    data.pop(0)
    for item in data:
        row_data = item.split(";")
        if len(row_data) < 2:
            continue
        print(row_data[0], row_data[1], row_data[-1].strip())