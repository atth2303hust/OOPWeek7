# /****************/
# Mã sinh viên: 202419007
# Họ tên: Phạm Anh Tú
# /****************/

class AllocationService:
    """Dịch vụ xử lý nghiệp vụ mượn và trả thiết bị."""
    def __init__(self, repository, strategy):
        self.repository = repository
        self.strategy = strategy

    def change_strategy(self, new_strategy):
        """Đổi chiến lược lựa chọn thiết bị."""
        self.strategy = new_strategy

    def allocate(self, additional_condition=None, borrower_id=None):
        """Thực hiện tìm kiếm và cấp phát thiết bị cho người mượn."""
        # Bước 1: Lọc các thiết bị sẵn sàng sử dụng
        def check_condition(item):
            if not item.is_ready_for_use():
                return False
            if additional_condition is not None:
                return additional_condition(item)
            return True

        candidates = self.repository.find_all(check_condition)

        # Bước 2: Dùng chiến lược để chọn ra 1 thiết bị tối ưu nhất từ danh sách
        selected_device = self.strategy.select(candidates)

        # Bước 3: Đổi trạng thái thiết bị thành đang mượn
        selected_device.borrow(borrower_id)
        return selected_device

    def return_device(self, device_id):
        """Xử lý trả thiết bị về kho."""
        device = self.repository.find_by_id(device_id)
        if device is None:
            raise KeyError(f"Không tìm thấy thiết bị có mã '{device_id}'.")
        device.return_to_storage()
        return device