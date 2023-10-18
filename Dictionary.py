# Define functions for each data type
def list_functions(data):
     return {
        "Length": len(data),
        "First Element": data[0] if data else None,
        "Last Element": data[-1] if data else None,
    }

def dict_functions(data):
    return {
        "Keys": list(data.keys()),
        "Values": list(data.values()),
    }

def set_functions(data):
    return {
        "Number of Elements": len(data),
    }

def tuple_functions(data):
    return {
        "Length": len(data),
        "First Element": data[0] if data else None,
        "Last Element": data[-1] if data else None,
    }

# Create a dictionary containing lists of functions for different data types
data_operations = {
    "List": list_functions,
    "Dictionary": dict_functions,
    "Set": set_functions,
    "Tuple": tuple_functions,
}

# Sample data for each data type
sample_data = {
    "List": [1, 2, 3, 4, 5],
    "Dictionary": {"a": 1, "b": 2, "c": 3},
    "Set": {1, 2, 3, 4, 5},
    "Tuple": (1, 2, 3, 4, 5),
}

# Apply the functions to the sample data
for data_type, data in sample_data.items():
    operations = data_operations[data_type](data)
    print(f"{data_type} Data:")
    for operation, result in operations.items():
        print(f"{operation}: {result}")
    print()