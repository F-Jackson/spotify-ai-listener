class SerializerValidator:
    @classmethod
    def validate(cls, validators):
        errors = []
        for is_valid, error in validators:
            if not is_valid:
                errors.append(error)

        return errors
