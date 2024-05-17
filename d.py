def funct(Filename):
    with open(Filename, "r", encoding="ISO-8859-1") as file:
        # data = file.readlines()
        # data.pop(0)
        # lowprice = data[0].split(";")
        for item in file:
            row_data = item.split(";")
            if (row_data[-1].strip()) == "Precio pvd globomatik":
                continue
            if len(row_data) < 2:
                continue
            try:
                row_data[-1] = float(row_data[-1].strip().replace("," , "."))
                yield row_data
            except ValueError:
                pass