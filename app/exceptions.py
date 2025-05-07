from fastapi import HTTPException


class PermissionDeniedException(HTTPException):
    status_code = 403
    detail = "Permission denied"


class WorkInProgressException(HTTPException):
    status_code = 501
    detail = "Work in progress"
