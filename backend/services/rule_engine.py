def evaluate_status(test_name, value):

    try:
        if test_name == "Blood Pressure":
            sys, dia = map(int, str(value).split("/"))
            if sys > 130 or dia > 85:
                return "Abnormal"
            return "Normal"

        if test_name == "Pulse Rate":
            v = int(value)
            if v < 60 or v > 100:
                return "Abnormal"
            return "Normal"

    except:
        return "Unknown"

    return "Normal"