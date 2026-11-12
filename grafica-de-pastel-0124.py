import matplotlib.pyplot as plt
# Alan Romero NC 0124
print("Alan Romero NC 0124")
categories =["ML","Lenguaje N","VA","Matematicas","Lengua"]
sales= [10,8,10,7,8]

plt.pie(sales, labels=categories, autopct = '%1.1f%%')
plt.title("Grafica circular ejemplo,0124")
plt.xlabel("Nivel X")
plt.ylabel("Nivel Y")
plt.show()

print("Alan Romero NC 0124")