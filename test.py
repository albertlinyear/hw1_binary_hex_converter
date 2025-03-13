try:
    decimal_number = int(input("請輸入一個十進位數字 (0-255): "))

    if decimal_number < 0 or decimal_number > 255:
        print("請輸入範圍內的數字 (0-255)！")
    else:
        # 手動轉換為二進位
        binary_number = ""
        num = decimal_number
        if num == 0:
            binary_number = "0"
        while num > 0:
            binary_number = str(num % 2) + binary_number
            num //= 2

        # 手動轉換為16進位
        hex_digits = "0123456789ABCDEF"
        hex_number = ""
        num = decimal_number
        if num == 0:
            hex_number = "0"
        while num > 0:
            hex_number = hex_digits[num % 16] + hex_number
            num //= 16

        print(f"二進位表示: {binary_number}")
        print(f"16進位表示: {hex_number}")
except ValueError:
    print("請輸入有效的整數！")
