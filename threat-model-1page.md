# Threat Model - Lab 3

## Thông tin nhóm
- Thành viên 1: Ma Huy Vũ - 1871020669
- Thành viên 2: Phạm Huy Hoàng - 1871020251

## Assets
- Plaintext message được gửi giữa Sender và Receiver.
- DES key và IV sử dụng để mã hoá dữ liệu.
- Ciphertext được truyền qua TCP socket.
- Tính toàn vẹn và bảo mật của dữ liệu truyền qua mạng.

## Attacker model
Kẻ tấn công có khả năng nghe lén lưu lượng mạng TCP giữa Sender và Receiver. Attacker cũng có thể sửa đổi packet, thay đổi ciphertext hoặc gửi dữ liệu giả mạo đến Receiver. Ngoài ra, attacker có thể thử giải mã dữ liệu nếu lấy được key hoặc IV.

## Threats
1. DES key và IV được gửi plaintext trên cùng kết nối TCP nên attacker có thể đọc được và giải mã dữ liệu.
2. Ciphertext có thể bị chỉnh sửa trong quá trình truyền dẫn dẫn đến dữ liệu giải mã sai hoặc gây lỗi padding.
3. Hệ thống không có cơ chế xác thực nên attacker có thể giả mạo Sender và gửi packet độc hại đến Receiver.

## Mitigations
1. Sử dụng giao thức an toàn như TLS để mã hoá toàn bộ kết nối TCP thay vì gửi key plaintext.
2. Sử dụng thuật toán mạnh hơn như AES thay cho DES vì DES hiện không còn an toàn.
3. Bổ sung cơ chế xác thực và integrity check như HMAC để phát hiện packet bị sửa đổi.

## Residual risks
Dù đã có các biện pháp giảm thiểu, hệ thống vẫn có nguy cơ bị tấn công nếu endpoint bị compromise hoặc khóa mã hoá bị lộ. Ngoài ra, việc cấu hình sai hoặc sử dụng thư viện không an toàn cũng có thể tạo ra lỗ hổng bảo mật.