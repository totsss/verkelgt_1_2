class destination:
    def __init__(self,des_id,des_name,des_time,emergency_name,emergency_phone) -> None:
        self.des_id = des_id
        self.des_name = des_name
        self.des_time = des_time
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone

    def __str__(self) -> str:
        ret = f"--destination id : {self.des_id}, destination name : {self.des_name}, time to destination is : {self.des_time}, emergency name and phone is {self.emergency_name}:{self.emergency_phone}"
        return ret
            
    