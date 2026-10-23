# /****************/
# Mã sinh viên: 202419007
# Họ tên: Phạm Anh Tú
# /****************/

class TeachingDevice:
    """Lớp cha chung cho mọi loại thiết bị."""
    def __init__(self, device_id, name, storage_location):
        self.device_id = device_id
        self.name = name
        self.storage_location = storage_location
        self.status = "Available"  # Trạng thái mặc định: Available, Borrowed, UnderMaintenance
        self.borrower_id = None

    def is_ready_for_use(self):
        """Lớp con sẽ viết lại hàm này theo điều kiện riêng."""
        return self.status == "Available"

    def get_default_priority_score(self):
        """Tính điểm ưu tiên mặc định."""
        return 0.0

    def borrow(self, borrower_id=None):
        """Mượn thiết bị."""
        if not self.is_ready_for_use():
            raise DeviceNotReadyException(f"Thiết bị {self.device_id} chưa sẵn sàng để mượn!")
        self.status = "Borrowed"
        self.borrower_id = borrower_id

    def return_to_storage(self):
        """Trả thiết bị về kho."""
        if self.status != "Borrowed":
            raise InvalidDeviceStateException(f"Thiết bị {self.device_id} không ở trạng thái đang mượn.")
        self.status = "Available"
        self.borrower_id = None

    def mark_under_maintenance(self):
        """Đưa vào bảo trì."""
        if self.status != "Available":
            raise InvalidDeviceStateException("Chỉ thiết bị Available mới được mang đi bảo trì.")
        self.status = "UnderMaintenance"

    def finish_maintenance(self):
        """Hoàn thành bảo trì."""
        if self.status != "UnderMaintenance":
            raise InvalidDeviceStateException("Thiết bị này không trong trạng thái bảo trì.")
        self.status = "Available"


class ProjectorRemote(TeachingDevice):
    """Điều khiển máy chiếu: Cần pin >= 20%."""
    def __init__(self, device_id, name, storage_location, battery_level):
        super().__init__(device_id, name, storage_location)
        self.battery_level = battery_level

    def is_ready_for_use(self):
        return self.status == "Available" and self.battery_level >= 20

    def get_default_priority_score(self):
        return float(self.battery_level)


class AirConditionerRemote(TeachingDevice):
    """Điều khiển điều hòa: Có danh sách phòng tương thích."""
    def __init__(self, device_id, name, storage_location, compatible_rooms):
        super().__init__(device_id, name, storage_location)
        self.compatible_rooms = compatible_rooms  # Danh sách dạng list các mã phòng

    def is_ready_for_use(self):
        return self.status == "Available"

    def get_default_priority_score(self):
        return 100.0 if self.compatible_rooms else 0.0

    def is_compatible_with(self, room_id):
        return room_id in self.compatible_rooms


class WirelessMicrophone(TeachingDevice):
    """Micro không dây: Pin >= 30% và chất lượng tín hiệu >= 40%."""
    def __init__(self, device_id, name, storage_location, battery_level, signal_quality):
        super().__init__(device_id, name, storage_location)
        self.battery_level = battery_level
        self.signal_quality = signal_quality

    def is_ready_for_use(self):
        return (
            self.status == "Available" 
            and self.battery_level >= 30 
            and self.signal_quality >= 40
        )

    def get_default_priority_score(self):
        return (self.battery_level + self.signal_quality) / 2.0