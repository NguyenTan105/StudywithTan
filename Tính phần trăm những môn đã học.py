phut = 60
tuhoccode = 4*phut
hocenggt = 15
cacmonkhac = 2*phut
callcn = 3*phut
callbt = 2*phut
hocengcn = 2*phut-30
hocengtr = 1*phut+15
school = 5*phut-10
book = phut
typing = phut
list2 = {
    1 : "Tự học code(4h)",
    2 : "Học English giao tiếp(15p)",
    3 : "Các Môn khác (3-4-6)(2h)",
    4 : "Call (chủ nhật)(3h)",
    5 : "Call (các ngày bth)(2h)",
    6 : "Học English chuyên ngành(1h30)",
    7 : "Học English ở trường(1h15)",
    8 : "Các tiết học trên trường(4h50)",
    9 : "Reading books(1h)",
    10: "Typing training(15p)"
    }
for keys, values in list2.items():
    print(keys, ":",values)
mon2 = list2.keys()
try:
    z = int(input("Hãy nhập môn học bạn muốn theo số: "))
    if z in list2:
        print(f"Môn học bạn chọn là {list2[z]}")
        if z == 1:
            x = int(input("Môn bạn học bn giờ: "))
            y = int(input("Môn bạn học bn phút: ")) 
            a = (x*60+y)*100/tuhoccode
            if x >= 0 and y > 60:
                print("Nhập sai số phút vui lòng nhập lại")
            elif 0 <= x:
                print(f"Bạn đã hoàn thành {int(a)}% của bài học")

        elif z == 2:
            x = int(input("Môn bạn học bn giờ: "))
            y = int(input("Môn bạn học bn phút: "))
            b = (x*60+y)*100/hocenggt
            if y > 60 and x >= 0:
                print("Nhập sai số phút vui lòng nhập lại")
            elif 0 <= x:
                print(f"Bạn đã hoàn thành {int(b)}% của bài học")

        elif z == 3:
            x = int(input("Môn bạn học bn giờ: "))
            y = int(input("Môn bạn học bn phút: "))
            c = (x*60+y)*100/cacmonkhac
            if y > 60 and x >= 0:
                print("Nhập sai số phút vui lòng nhập lại")
            elif 0 <= x:
                print(f"Bạn đã hoàn thành {int(c)}% của bài học")

        elif z == 4:
            x = int(input("Môn bạn học bn giờ: "))
            y = int(input("Môn bạn học bn phút: "))
            d = (x*60+y)*100/callcn
            if y > 60 and x >= 0:
                print("Nhập sai số phút vui lòng nhập lại")
            elif 0 <= x:
                print(f"Bạn đã hoàn thành {int(d)}% của bài học")

        elif z == 5:
            x = int(input("Môn bạn học bn giờ: "))
            y = int(input("Môn bạn học bn phút: "))
            e = (x*60+y)*100/callbt
            if y > 60 and x >= 0:
                print("Nhập sai số phút vui lòng nhập lại")         
            elif 0 <= x:
                print(f"Bạn đã hoàn thành {int(e)}% của bài học")
        
        elif z == 6:
            x = int(input("Môn bạn học bn giờ: "))
            y = int(input("Môn bạn học bn phút: "))
            f = (x*60+y)*100/hocengcn
            if y > 60 and x >= 0:
                print("Nhập sai số phút vui lòng nhập lại")         
            elif 0 <= x:
                print(f"Bạn đã hoàn thành {int(f)}% của bài học")
        
        elif z == 7:
            x = int(input("Môn bạn học bn giờ: "))
            y = int(input("Môn bạn học bn phút: "))
            g = (x*60+y)*100/hocengtr
            if y > 60 and x >= 0:
                print("Nhập sai số phút vui lòng nhập lại")         
            elif 0 <= x:
                print(f"Bạn đã hoàn thành {int(g)}% của bài học")

        elif z == 8:
            x = int(input("Môn bạn học bn giờ: "))
            y = int(input("Môn bạn học bn phút: "))
            h = (x*60+y)*100/school
            if y > 60 and x >= 0:
                print("Nhập sai số phút vui lòng nhập lại")         
            elif 0 <= x:
                print(f"Bạn đã hoàn thành {int(h)}% của bài học")
     
        
        elif z == 9:
            x = int(input("Môn bạn học bn giờ: "))
            y = int(input("Môn bạn học bn phút: "))
            i = (x*60+y)*100/book
            if y > 60 and x >= 0:
                print("Nhập sai số phút vui lòng nhập lại")         
            elif 0 <= x:
                print(f"Bạn đã hoàn thành {int(i)}% của bài học")

        elif z == 10:
            x = int(input("Môn bạn học bn giờ: "))
            y = int(input("Môn bạn học bn phút: "))
            j = (x*60+y)*100/typing
            if y > 60 and x >= 0:
                print("Nhập sai số phút vui lòng nhập lại")         
            elif 0 <= x:
                print(f"Bạn đã hoàn thành {int(j)}% của bài học")


        
        if x < 0 or y < 0:
            print("Bạn không được nhập số âm")
    else:
        print("Số bạn nhập không hợp lệ")

except:
    print("Xin hãy nhập đúng gói")
