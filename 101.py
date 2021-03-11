A = eval(input())
B = eval(input())
C = eval(input())
D = eval(input())
print('|%5d %5d|' % (A , B))
print('|%-5d %-5d|' % (A, B))
print('|%5.2f %5.2f|' % (A, B))

# circle算法 Example Input :10
import math 

Radius = eval(input())
Perimeter = 2*Radius*math.pi
Area = Radius**2*math.pi
print('Radius = %.2f' % Radius)
print('Perimeter = %.2f' % Perimeter)
print('Area = %.2f' % Area)


# 長寬高 Example Input:34.7,12
Height = eval(input())
Width = eval(input()) 
# H, W = (eval(input()), eval(input()))
Perimeter = (Height + Width)*2
Area = Height*Width
print('Height = %.2f' % Height)
print('Width = %.2f' % Width)
print('Perimeter = %.2f' % Perimeter)
print('Area = %.2f' % Area)


# 公里英哩換算 Example Input:分9,秒46,公里3
x, y, z = (eval(input()), eval(input()), eval(input())/1.6)
print('speed = %.1f' % (z/((x*60+y)/3600)))


# 數值計算
A = eval(input())
B = eval(input())
C = eval(input())
D = eval(input())
E = eval(input())
print(A, B, C, D, E)
print('Sum = %.1f' % (A+B+C+D+E))
print('Average = %.1f' % ((A+B+C+D+E)/5))


# 座標距離計算
x1, y1 = (eval(input()), eval(input()))
x2, y2 = (eval(input()), eval(input()))
print('(%s %s)' % (x1, y1))
print('(%s %s)' % (x2, y2))
print('Distance = %.4f' % ((((x1-x2)**2+(y1-y2)**2)**0.5)))

# 正n邊形面積計算
import math
n = eval(input())
s = eval(input())
Area = (n*(s**2))/(4*math.tan(math.pi/n))
print('正n邊形面積 = %.4f' %(Area))