# /****************/
# Mã sinh viên: 202419007
# Họ tên: Phạm Anh Tú
# /****************/

from .exceptions import NoSuitableItemException

class HighestPriorityStrategy:
    """Chiến lược chọn thiết bị có điểm ưu tiên cao nhất."""
    def __init__(self, score_selector):
        self.score_selector = score_selector  # Hàm tính điểm

    def select(self, candidates):
        if not candidates:
            raise NoSuitableItemException("Không có thiết bị nào phù hợp để chọn.")
        # Dùng hàm max của python dựa trên điểm số trả về từ score_selector
        return max(candidates, key=self.score_selector)


class FirstAvailableStrategy:
    """Chiến lược chọn thiết bị đầu tiên tìm thấy trong danh sách."""
    def select(self, candidates):
        if not candidates:
            raise NoSuitableItemException("Danh sách thiết bị trống.")
        return candidates[0]