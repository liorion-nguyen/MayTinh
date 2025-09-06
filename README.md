# Connect project với repository
- B1: git init [Khởi tạo ra quản lý git cho folder]
- B2: git add [Khi đẩy code muốn đẩy file nào thì dùng git add(git add .-> tất cả file, tên từng file: git add index.py)]
- B3: git commit -m "message" [Nội dung mô tả tả commit mình có chức năng và làm được gì(ngắn gọn)]
    + feat: tạo tính năng mới [git commit -m "feat: abcxyz"]
    + fix: sửa hoặc cập nhật [git commit -m "fix: abcxyz"]
- B4: git branch -M main [Tạo nhánh main dùng nó làm nhánh chính]
- B5: git remote add origin ... [Liên kết quản lý git với repository(remote)]
- B6: git push -u origin main [Đẩy code lên nhánh main]

# Đẩy code lên github
- B1: git add .
- B2: git commit -m "message"
- B3: git push origin branchName

# Làm việc nhóm:
- Đặt tên nhánh:
    + main/master: Nhánh của product -> Ném vào nhánh này.
    + develop: Nhánh cho người lập trình viên kiểm thử -> Kiểm thử thành công 
    + tên từng lập trình viên(chungnq): Nhánh code của từng lập trình viên
- Làm việc với nhánh: 
    + git branch: Xem tất cả các nhánh và nhánh mình đang trỏ.
    + git checkout -b branchName: Tạo 1 nhánh mới
    + git checkout branchName: Chuyển sang nhánh khác....
- Cập nhật code mới nhất:
    + git pull origin main [cập nhật code mới nhất từ nhánh main về]
    + Thời điểm kéo code về: Khi chúng ta bắt đầu code, trước khi đẩy code lên.

# Thao tác khác với git:
- Lấy dự án từ github về:
    + git clone git@github.com:tDuowg/bookstore.git [Tạo ra dự án y hệt code trên github]
    + git log [Lấy ra lịch sử commit]
    + Chuyển về version cũ: git checkout (commit: b69bd88f4637cf0111008bf0bc03b3c799696009)