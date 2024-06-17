#Nhập chuỗi muốn nhập
string = str(input("Enter:"))
#Hàm đếm
def count(chuoi):
    count_char = {char: chuoi.count(char) for char in chuoi}
    print(count_char)

count(string)