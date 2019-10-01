
class ResponseHelper:

    @staticmethod
    def success_with_data(data):
        meta={
            "code" : 200,
            "message" : "Success",
            "error" : False
        }
        response = {
            "meta" : meta,
            "data" : data
        }
        return response

    @staticmethod
    def success_with_data_count(data,count):
        meta = {
            "code": 200,
            "message": "Success",
            "error": False
        }
        response = {
            "meta": meta,
            "total": count,
            "data": data
        }
        return response

    @staticmethod
    def success_without_data(msg):
        meta = {
            "code": 200,
            "message": msg,
            "error": False
        }
        response = {
            "meta": meta
        }
        return response

    @staticmethod
    def success_custom_with_data(msg, data):
        meta = {
            "code": 200,
            "message": msg,
            "error": False
        }
        response = {
            "meta": meta,
            "data": data
        }
        return response

    @staticmethod
    def error_something():
        meta = {
            "code": 400,
            "message": "Something Error",
            "error": True
        }
        response = {
            "meta": meta
        }
        return response

    @staticmethod
    def error_custom(code, msg):
        meta = {
            "code": code,
            "message": msg,
            "error": True
        }
        response = {
            "meta": meta
        }
        return response

    @staticmethod
    def data_not_found():
        meta = {
            "code": 204,
            "message": "Data Not Found",
            "error": True
        }
        response = {
            "meta": meta
        }
        return response

    @staticmethod
    def error_validation(msg):
        meta = {
            "code": 422,
            "message": msg,
            "error": True
        }
        response = {
            "meta": meta
        }
        return response