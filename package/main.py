from package import module1, module2, module3

# Menggunakan fungsi dari modul module1
name = "Alice"
greeting = module1.greet(name)
print(greeting)

# Menggunakan fungsi dari modul module2
print("Square of 5:", module2.calculate_square(5))

# Menggunakan fungsi dari modul module3
num = 17
print("Is 17 a prime number?", module3.is_prime(num))
