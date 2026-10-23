# /****************/
# Mã sinh viên: 202419007
# Họ tên: Phạm Anh Tú
# /****************/

from .exceptions import DuplicateIdException

class InMemoryRepository:
    """Kho lưu trữ dữ liệu trong bộ nhớ RAM sử dụng Dictionary."""
    def __init__(self):
        # Lưu dạng: {device_id: doi_tuong_thiet_bi}
        self._items = {}

    def add(self, item):
        """Thêm thiết bị vào kho."""
        if item.device_id in self._items:
            raise DuplicateIdException(f"Mã thiết bị '{item.device_id}' đã tồn tại trong kho.")
        self._items[item.device_id] = item

    def remove(self, item_id):
        """Xóa thiết bị khỏi kho theo mã."""
        if item_id in self._items:
            del self._items[item_id]
            return True
        return False

    def find_by_id(self, item_id):
        """Tìm thiết bị theo mã."""
        return self._items.get(item_id, None)

    def get_all(self):
        """Lấy danh sách tất cả thiết bị."""
        return list(self._items.values())

    def find_all(self, condition_func):
        """Lọc danh sách thiết bị dựa vào một hàm điều kiện."""
        result = []
        for item in self._items.values():
            if condition_func(item):
                result.append(item)
        return result