def generate_explanation(test_name, value, status):

    if status == "Unknown":
        return "Unable to interpret this test value."

    return f"""
The test '{test_name}' has a value of {value}, which is classified as {status}.
If abnormal, it may require medical attention or further diagnosis.
"""