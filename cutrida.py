a = input("masukan bilangan1: ")
b = input("masukan bilangan2: ")
c = input("masukan bilangan3: ")

if a > b and a > c:
  print(a,"adalah bilangan yang terbesar")
elif b > a and b > c:
  print(b,"adalah bilangan yang terbesar")
elif c > a and c > b:
  print(c,"adalah bilangan yang terbesar")
else: 
  print("silakan masukan pilihan")