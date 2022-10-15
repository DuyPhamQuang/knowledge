# Các lệnh cơ bản trong helm
- helm repo
  - helm repo add [NAME] [URL] [flags]: Thêm chart repository
  - helm repo index [DIR] [flags] : tạo index file cho thư mục chứa các gói chart 
  - helm repo list: list các chart trong repo
  - helm repo remove [REPO1 [REPO2 ...]] [flags]: Xóa repo
  - helm repo update: Cập nhật thông tin của chart đã có trên local từ repo
- helm search 
  - helm search repo [keyword] [flags]: Tìm kiếm chart trong các repo theo từ khóa (helm search repo redis)
  - helm search hub [keyword] [flags] :search for charts in the Artifact Hub or your own hub instance
- helm uninstall
- helm list: liệt kê các charts đã cài
- hell rollback: rollback lại phiên bản trước
  - helm rollback <RELEASE> [REVISION] [flags]: 
  - helm history RELEASE
- helm upgrade [RELEASE] [CHART] [flags]
- helm pull:
  - helm pull [chart URL | repo/chartname] [...] [flags]: tải chart từ repository và giải nén vào thư mục
# Cấu trúc cơ bản trong helm
    /example-project
        /Chart.yaml # mô tả của chart
        /values.yaml # các giá trị mặc định, chúng ta có thể thay đổi trong khi cài đặt hay nâng cấp project của chúng ta
        /charts/ # subcharts
        /templates/ # template file
- helm create 
