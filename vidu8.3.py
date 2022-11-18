# chương trình phân loại sinh viên dựa xét kết quả học tập theo điểm trung bình
diem_TB =eval(input(" Nhập điểm trung bình :"))
if diem_TB >= 0 and diem_TB<=10:
    if diem_TB<5:
        print(" Xếp loại Yếu/Kém!!! ")
    elif diem_TB<6:
        print(" Xếp loại Trung Bình ")
    elif diem_TB<7:
        print(" Xếp loại Trung Bình/Khá")
    elif diem_TB<8:
        print(" Xếp loại Khá")
    elif diem_TB<9:
        print(" Xếp loại Khá/Giỏi")
    elif diem_TB<=10:
        print(" Xếp loại giỏi")
else:
    print(" SOS ")