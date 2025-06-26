name = "    rebba sai sivesh  "
print(name.upper())
print(name.title())
print(name.strip())
print(name.replace("r", "v"))
print("siv" in name)
print("swift" not in name)


n = int(input("enter a number : "))

if n % 2 == 1:
    print("weird")
else n % 2 == 0 and 2 <= n <= 5:
    print("Not weird")
else n % 2 == 0 and 6 < = n <= 20:
    print("weird")
else n % 2 == 0 and n > 20:
    print("Not weird")
