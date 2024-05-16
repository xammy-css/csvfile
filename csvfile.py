
with open("tarifas.csv", "r", encoding="ISO-8859-1") as file:
    data = file.readlines()
    data.pop(0)
    lowprice = data[0].split(";")
    for item in data:
        row_data = item.split(";")
        if (row_data[-1].strip()) == "Precio pvd globomatik":
            continue
        if len(row_data) < 2:
            continue
        try:
            if float(row_data[-1].strip().replace("," , ".")) > float(lowprice[-1].strip().replace("," , ".")):
                lowprice = row_data
        except ValueError:
            pass
    print(lowprice[0], lowprice[1], lowprice[-1].strip())