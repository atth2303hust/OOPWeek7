# /****************/
# Mã sinh viên: 202419007
# Họ tên: Phạm Anh Tú
# /****************/

class DuplicateIdException(Exception):
    """Báo lỗi khi trùng mã thiết bị."""
    def __init__(self, message):
        super().__init__(message)


class NoSuitableItemException(Exception):
    """Báo lỗi khi không tìm thấy thiết bị phù hợp."""
    def __init__(self, message):
        super().__init__(message)


class DeviceNotReadyException(Exception):
    """Báo lỗi khi thiết bị chưa sẵn sàng để mượn (hết pin, hỏng,...)."""
    def __init__(self, message):
        super().__init__(message)


class InvalidDeviceStateException(Exception):
    """Báo lỗi khi thực hiện thao tác sai trạng thái (ví dụ: trả thiết bị chưa mượn)."""
    def __init__(self, message):
        super().__init__(message)