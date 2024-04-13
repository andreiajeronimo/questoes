def display_numbers(numbers):
    for i in range(len(numbers)):
        if i == len(numbers) - 1:  # Check if it's the last number
            print(numbers[i])  # Don't add space after the last number
        else:
            print(numbers[i], end=' ') 

   
lista = [1, 2, 3, 4]
display_numbers(lista) # 1 2 3 4