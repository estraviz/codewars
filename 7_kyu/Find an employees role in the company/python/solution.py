"""Find an employees role in the company"""

employees = [
    {'first_name': 'Ollie', 'last_name': 'Hepburn', 'role': 'Boss'},
    {'first_name': 'Morty', 'last_name': 'Smith', 'role': 'Truck Driver'},
    {'first_name': 'Peter', 'last_name': 'Ross', 'role': 'Warehouse Manager'},
    {'first_name': 'Cal', 'last_name': 'Neil', 'role': 'Sales Assistant'},
    {'first_name': 'Jesse', 'last_name': 'Saunders', 'role': 'Admin'},
    {'first_name': 'Anna', 'last_name': 'Jones', 'role': 'Sales Assistant'},
    {'first_name': 'Carmel', 'last_name': 'Hamm', 'role': 'Admin'},
    {'first_name': 'Tori', 'last_name': 'Sparks', 'role': 'Sales Manager'},
    {'first_name': 'Peter', 'last_name': 'Jones', 'role': 'Warehouse Picker'},
    {'first_name': 'Mort', 'last_name': 'Smith', 'role': 'Warehouse Picker'},
    {'first_name': 'Anna', 'last_name': 'Bell', 'role': 'Admin'},
    {'first_name': 'Jewel', 'last_name': 'Bell', 'role': 'Receptionist'},
    {'first_name': 'Colin', 'last_name': 'Brown', 'role': 'Trainee'}
]


def find_employees_role(name):
    for employee in employees:
        first_name, last_name, role = None, None, None
        for key, value in employee.items():
            if key == 'first_name':
                first_name = employee[key]
            elif key == 'last_name':
                last_name = employee[key]
            elif key == 'role':
                role = employee[key]
        if name == " ".join([first_name, last_name]):
            return role
    return "Does not work here!"
