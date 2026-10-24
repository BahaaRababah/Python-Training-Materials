def get_salary(employee_dict, emp_id):
    employee = employee_dict.get(emp_id)
    if employee is None:
        return "Not Found"
    else:
       return employee.get("salary")
   


def update_salary(employee_dict, emp_id, new_salary):
   employee_dict[emp_id]["salary"] = new_salary