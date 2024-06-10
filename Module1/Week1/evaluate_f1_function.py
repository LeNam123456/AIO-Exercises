def check_var(tp, fp, fn):
    var = [tp, fp, fn]
#Kiểm tra xem giá trị nhận vào nếu lớn hơn hoặc 0 thì kiểm tra kiểu dữ liệu không thì ném ra lỗi
    for var_val in var:
        if var_val <= 0:
            raise ValueError(f'{var_val} must be greater than zero')
        elif not isinstance(var_val, int):
            raise TypeError(f'{var_val} must be int')   
    return var



# Kiểm tra với giá trị không hợp lệ
tp, fp, fn = 0, 10, 15
check_var(tp, fp, fn)
# Tính precision, recall, f1_score
precision = tp/tp+fp
recall = tp/tp+fn
f1_score = (2*(precision*recall))/ (precision+ recall)

print(f"Pre: {precision:.2f}")
print(f"recall: {recall:.2f}")
print(f"f1_score: {f1_score:.2f}")
