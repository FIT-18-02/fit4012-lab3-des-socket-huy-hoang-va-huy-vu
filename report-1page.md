# Report 1 page - Lab 3

## Thông tin nhóm
- Thành viên 1: Ma Huy Vũ - 1871020669
- Thành viên 2: Phạm Huy Hoàng - 1871020251

## Mục tiêu
Mục tiêu của bài lab là xây dựng hệ thống gửi và nhận dữ liệu mã hoá DES qua TCP socket bằng Python. Nhóm cần hiểu cách hoạt động của DES-CBC, IV, padding PKCS#7 và quy trình gửi packet qua socket. Ngoài ra, bài lab còn giúp nhóm luyện kỹ năng xử lý packet, kiểm thử hệ thống và nhận biết các rủi ro bảo mật khi truyền dữ liệu mã hoá không an toàn.

## Phân công thực hiện
Ma Huy Vũ phụ trách chính phần sender.py, receiver.py, DES encryption/decryption, xử lý socket, packet handling, debugging và pytest testing. Phạm Huy Hoàng phụ trách README, report, threat model, peer review response và hỗ trợ testing. Cả hai cùng thực hiện integration testing, chuẩn bị demo và nộp GitHub.

## Cách làm
Nhóm triển khai Sender và Receiver bằng Python TCP socket. Sender nhận plaintext, tạo DES key và IV 8 byte, mã hoá dữ liệu bằng DES-CBC với PKCS#7 padding, sau đó gửi packet gồm key, IV, length header và ciphertext. Receiver nhận packet, parse header, nhận ciphertext và giải mã để lấy plaintext. Nhóm sử dụng pytest để kiểm thử padding, encrypt/decrypt, protocol contract, tamper test và wrong key test.

## Kết quả
Hệ thống sender/receiver hoạt động thành công trên local machine. Dữ liệu được mã hoá và giải mã đúng qua TCP socket. Toàn bộ 7 test đều PASS, bao gồm cả negative test cho tamper ciphertext và wrong key. Nhóm cũng lưu log minh chứng trong thư mục logs/ để phục vụ kiểm tra và demo.

## Kết luận
Qua bài lab, nhóm em  hiểu rõ hơn về TCP socket, block cipher và DES-CBC encryption. Nhóm em cũng nhận ra rằng việc gửi key và IV dưới dạng plaintext là không an toàn trong thực tế. Bài lab giúp nâng cao kỹ năng lập trình mạng, kiểm thử phần mềm và nhận thức về các vấn đề bảo mật trong quá trình truyền dữ liệu.