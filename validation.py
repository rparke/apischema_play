

from dataclasses import dataclass

from pytest import raises

from apischema import ValidationError, deserialize, serialize, validator


@dataclass
class PasswordForm:
    password: str
    confirmation: str

    @validator
    def password_match(self):
        # DO NOT use assert
        if self.password != self.confirmation:
            raise ValueError("password doesn't match its confirmation")


with raises(ValidationError) as err:
    deserialize(PasswordForm, {"password": "p455w0rd", "confirmation": "..."})
assert serialize(err.value) == [
    {"loc": [], "err": ["password doesn't match its confirmation"]}
]