def analyze_tests(test_data: list) -> list:
    analyzed = []

    for test in test_data:
        status = "Normal"

        try:
            if "-" in test["normal_range"]:
                low, high = test["normal_range"].split("-")
                low = float(low)
                high = float(high)

                if test["value"] < low:
                    status = "Low"
                elif test["value"] > high:
                    status = "High"
        except:
            status = "Unknown"

        test["status"] = status
        analyzed.append(test)

    return analyzed