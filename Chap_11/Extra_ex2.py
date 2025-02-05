def combine_in_dict(keys, values):
    return dict(zip(keys, values))

def Adding_to_dict(dict1, dict2):
    return {**dict1, **dict2}

def get_nested_value(d, key):
    if key in d:
        return d[key]
    for value in d.values():
        if isinstance(value, dict):
            result = get_nested_value(value, key)
            if result is not None:
                return result
    return None

def add_name_salary(employees, defaults):
    res = dict.fromkeys(employees, defaults)
    return res

def find_key(d, keys):
    return {k: d[k] for k in keys if k in d}

def remove_key(d, keys):
    return {k: d[k] for k in d.keys() - keys}

def find_value(value, sample):
    for key, val in sample.items():
        if val == value:
            return f"the {value} is in {key}"
    return f"there is {None} in the dictionary"

def change_value(sample, key, value):
    # Move the item from old 'value' key to the 'key'
    sample[value] = sample.pop(key)
    return sample

def find_min_value(sample):
    return min(sample.values())

def change_salary(sample, search_name, new_salary):
    """
    Update the salary for a specific employee in a dictionary of employees.

    Parameters
    ----------
    sample : dict
        A dictionary of employees, where keys are employee IDs (e.g., 'emp1', 'emp2')
        and values are dictionaries containing employee information, such as name and salary.
    search_name : str
        The name of the employee whose salary should be updated.
    new_salary : int or float
        The new salary to assign to the specified employee.

    Returns
    -------
    dict
        The updated dictionary of employees, with the salary changed for the matching employee.

    Examples
    --------
    # >>> employees = {
    # ...     'emp1': {'name': 'Jhon', 'salary': 7500},
    # ...     'emp2': {'name': 'Emma', 'salary': 8000},
    # ...     'emp3': {'name': 'Brad', 'salary': 500}
    # ... }
    # >>> updated = change_salary(employees, 'Brad', 8500)
    # >>> updated['emp3']['salary']
    8500
    """

    for emp_key, emp_data in sample.items():
        # Check if the 'name' in this employee matches search_name
        if emp_data.get('name') == search_name:
            emp_data['salary'] = new_salary
            break
    return sample



if __name__ == "__main__":
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    print(combine_in_dict(keys, values))
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    print(Adding_to_dict(dict1, dict2))
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    print(get_nested_value(sampleDict, "history"))
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}
    print(add_name_salary(employees, defaults))
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}
    keys = ["name", "salary"]
    print(find_key(sample_dict, keys))
    print(remove_key(sample_dict, keys))
    sample_dict1 = {'a': 100, 'b': 200, 'c': 300}
    value = 400
    print(find_value(value, sample_dict1))
    change = "location"
    print(change_value(sample_dict, 'city', change))
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }
    print(find_min_value(sample_dict))
    sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
    }
    print(change_salary(sample_dict, 'Brad', 8500))

