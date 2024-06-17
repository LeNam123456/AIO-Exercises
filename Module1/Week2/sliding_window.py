k = int(input('Enter K:'))
num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]

new_list = []

def sliding_window_max(k):
    # Lặp qua từng vị trí trong danh sách, từ 0 đến độ dài danh sách trừ k
    for i in range(len(num_list) - k + 1):
        # Cửa sổ hiện tại từ vị trí i đến i+k
        current_window = num_list[i:i+k]
        # Tìm giá trị lớn nhất trong cửa sổ hiện tại
        max_value = max(current_window)
        # Thêm giá trị lớn nhất vào new_list
        new_list.append(max_value)

sliding_window_max(k)
print(new_list)