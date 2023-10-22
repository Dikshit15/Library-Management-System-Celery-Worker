from pydantic import BaseModel

# Message class defined in Pydantic
class User(BaseModel):
    firstName: str
    lastName: str
    email: str
    phone: str

    def get_full_name(self):
        return self.firstName + ' ' + self.lastName

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone