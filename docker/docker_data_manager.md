# Quản lý dữ liệu trong docker
## 1. Docker system

- docker system df: 
  - --format: Pretty-print images using a Go template
  - --v: Show detailed information on space usage
    - SHARED SIZE is the amount of space that an image shares with another one (i.e. their common data)
    - UNIQUE SIZE is the amount of space that is only used by a given image
    - SIZE is the virtual size of the image, it is the sum of SHARED SIZE and UNIQUE SIZE
- docker system events: lấy thông tin sự kiện theo thời gian thực từ máy chủ
- docker system info: Hiển thị thông tin rộng của hệ thống
- docker system prune: 
  - --all , -a		Loại bỏ tất cả các image không sử dụng
  - --filter		Provide filter values (e.g. 'label=<key>=<value>')
  - --force , -f		Không cần lời nhắc xác nhận
  - --volumes		loại bỏ volumes
  