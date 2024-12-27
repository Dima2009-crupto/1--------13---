#students = {
    #"Петренко": 4,
    #"Сидоренко": 5,
    #"Коваленко": 2,
    #"Мельник": 4,
    #"Тарасенко": 5,
#}

#filtered_students = {surname: grade for surname, grade in students.items() if grade in [4, 5]}

#print(filtered_students)


temperatures = {
    "Київ": 10,
    "Львів": 8,
    "Одеса": 12,
    "Харків": 9,
    "Дніпро": 11,
}

average_temperature = sum(temperatures.values()) / len(temperatures)

print(f"Середня температура: {average_temperature:.2f}")
