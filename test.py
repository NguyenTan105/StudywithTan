def frange(start, final, interval):
    result = []
    while start < final:
        result.append(start)
        start += interval
    return result
x = frange(0,2,0.2)
from matplotlib import pyplot 
import math
def draw_graph(x,y):
    pyplot.plot(x,y)
    pyplot.xlabel("Truc X")
    pyplot.ylabel("TRuc Y")
    pyplot.title("Đồ thị bài toán ném bóng")
def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start += interval
    return numbers
def draw_trajectory(u,theta):
    # Gia tốc
    g = 9.8
    # Gốc bay
    theta = math.radians(theta)
    # Thời gian bay:
    t_flight = 2*u*math.sin(theta)/g
    # Tính khoảng cách thời gian
    intervals = frange(0, t_flight, 0.001)
    # Danh sách tọa độ x và y
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t-0.5*g*t**2)
    draw_graph(x,y)
if __name__ == "__main__":
    try:
        u = float(input("Nhập vận tốc ban đầu (m/s): "))
        theta = float(input("Nhập góc bay (degrees): "))
    except ValueError:
        print("Nhập các gia trị sai!")
    else:
        draw_trajectory(u,theta)
        pyplot.show()
    finally:
        print("Hoàn thành chương trình")