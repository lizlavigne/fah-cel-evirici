def fahrenheitancelsius(f):
    return (f - 32) * 5 / 9

def celsiustanfahrenheit(c):
    return (c * 9 / 5) + 32

print("Fahrenheit - Celsius Çevirici")
seçim = input("Dönüşüm türünü seçin (1: Fahrenheit -> Celsius, 2: Celsius -> Fahrenheit): ")

if seçim == "1":
    f = float(input("Fahrenheit değerini girin: "))
    print(f"{f}°F = {fahrenheitancelsius(f):.2f}°C")
elif seçim == "2":
    c = float(input("Celsius değerini girin: "))
    print(f"{c}°C = {celsiustanfahrenheit(c):.2f}°F")
else:
    print("Geçersiz seçim lütfen 1 veya 2 girin.")