# Peer Review Response

## Thông tin nhóm
- Thành viên 1: Ma Huy Vũ - 1871020669
- Thành viên 2: Phạm Huy Hoàng - 1871020251

## Thành viên 1 góp ý cho thành viên 2
Tài liệu và threat model được trình bày rõ ràng, tuy nhiên cần bổ sung thêm chi tiết về mitigation và residual risks. Ngoài ra cần kiểm tra lại format README để tránh còn TODO hoặc lỗi markdown.

## Thành viên 2 góp ý cho thành viên 1
Phần sender/receiver và DES-CBC hoạt động tốt, test đầy đủ và rõ ràng. Tuy nhiên cần cải thiện logging và thay đổi các dòng tiếng Việt trong console để tránh lỗi Unicode khi chạy test trên Windows.

## Nhóm đã sửa gì sau góp ý
Sau khi review chéo, nhóm đã bổ sung thêm negative test cho tamper ciphertext và wrong key. Nhóm cũng sửa lại logging, chuẩn hóa packet handling và thay đổi console output sang tiếng Anh để tránh lỗi encoding. Ngoài ra, README, threat model và report cũng được cập nhật đầy đủ thông tin nhóm và phân công công việc.