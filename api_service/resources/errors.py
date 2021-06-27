class InternalServerError(Exception):
    pass


class InvalidParameterError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "InvalidParameterError": {
         "message": "Request is missing mandatory fields",
         "status": 400
     },
    "SchemaValidationError": {
         "message": "Mandatory fields cannot be empty & Filename should be unique",
         "status": 400
     }
}
