class Employee:
    def __init__(self,emp_id,emp_ssn,emp_name,emp_role,emp_licence = "") -> None:
        self.emp_id = emp_id
        self.emp_ssn = emp_ssn
        self.emp_name = emp_name
        self.emp_role = emp_role
        self.emp_licence = emp_licence

    def __str__(self) -> str:
        if self.emp_licence == "":
            ret = f"--employee id : {self.emp_id}, employee ssn : {self.emp_ssn}, employee name : {self.emp_name}, role : {self.emp_role}"
        else:
            ret = f"--pilot id : {self.emp_id}, pilot ssn : {self.emp_ssn}, pilot name : {self.emp_name},  licence : {self.emp_licence} "
        return ret