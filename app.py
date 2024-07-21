def calculate_area(length, width):
    return length * width

if __name__ == "__main__":
    length = float(input("Digite o comprimento: "))
    width = float(input("Digite a largura: "))
    area = calculate_area(length, width)
    print(f"A área do retângulo é: {area}")
