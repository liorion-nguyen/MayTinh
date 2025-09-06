def display_menu():
    """Hiển thị menu lựa chọn"""
    print("\n" + "="*30)
    print("    MÁY TÍNH CƠ BẢN")
    print("="*30)
    print("1. Phép cộng (+)")
    print("2. Phép trừ (-)")
    print("3. Phép nhân (×)")
    print("4. Phép chia (÷)")
    print("5. Lũy thừa (^)")
    print("0. Thoát")
    print("="*30)

def get_numbers():
    """Nhập hai số từ người dùng với xử lý lỗi"""
    while True:
        try:
            num1 = float(input("Nhập số thứ nhất: "))
            num2 = float(input("Nhập số thứ hai: "))
            return num1, num2
        except ValueError:
            print("❌ Lỗi: Vui lòng nhập số hợp lệ!")

def add(a, b):
    """Phép cộng"""
    return a + b

def subtract(a, b):
    """Phép trừ"""
    return a - b

def multiply(a, b):
    """Phép nhân"""
    return a * b

def divide(a, b):
    """Phép chia với xử lý chia cho 0"""
    if b == 0:
        return "❌ Lỗi: Không thể chia cho 0!"
    return a / b

def power(a, b):
    """Phép lũy thừa"""
    try:
        return a ** b
    except OverflowError:
        return "❌ Lỗi: Kết quả quá lớn!"

def calculator():
    """Hàm chính của máy tính"""
    print("🎯 Chào mừng bạn đến với Máy tính cơ bản!")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Chọn phép toán (0-5): "))
        except ValueError:
            print("❌ Vui lòng nhập số từ 0 đến 5!")
            continue
        
        if choice == 0:
            print("👋 Cảm ơn bạn đã sử dụng máy tính!")
            break
        elif choice in [1, 2, 3, 4, 5]:
            num1, num2 = get_numbers()
            
            if choice == 1:
                result = add(num1, num2)
                operation = "+"
            elif choice == 2:
                result = subtract(num1, num2)
                operation = "-"
            elif choice == 3:
                result = multiply(num1, num2)
                operation = "×"
            elif choice == 4:
                result = divide(num1, num2)
                operation = "÷"
            elif choice == 5:
                result = power(num1, num2)
                operation = "^"
            
            # Hiển thị kết quả
            if isinstance(result, str):  # Nếu là thông báo lỗi
                print(result)
            else:
                print(f"\n✅ Kết quả: {num1} {operation} {num2} = {result}")
                
            input("Nhấn Enter để tiếp tục...")
        else:
            print("❌ Lựa chọn không hợp lệ!")

# Chạy chương trình
if __name__ == "__main__":
    calculator()