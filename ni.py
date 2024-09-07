import matplotlib.pyplot as plt
import time
import random

def insertion_sort_visualized(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='blue')
    ax.set_title('Insertion Sort Visualization')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    iterations = 0
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            iterations += 1
            arr[j + 1] = arr[j]
            j -= 1

            # Update the bars
            for k, bar in enumerate(bars):
                bar.set_height(arr[k])
                bar.set_color('red' if k == j + 1 else 'blue')
                
            # Redraw the plot
            plt.pause(0.1)  # Pausa de 0.1 segundos entre actualizaciones
        
        arr[j + 1] = key

        # Final update after inserting the key
        for k, bar in enumerate(bars):
            bar.set_height(arr[k])
            bar.set_color('blue')

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Final update to show the sorted array
    for bar in bars:
        bar.set_color('green')
    
    # Mostrar el número de iteraciones y el tiempo total
    ax.set_title(f'Insertion Sort Completed\nIterations: {iterations} | Time: {elapsed_time:.2f} seconds')

    plt.show()
    return iterations, elapsed_time

# Comparar la lista definida con una lista aleatoria
fixed_list = [4, 3, 2, 10, 12, 1, 5]
random_list = random.sample(range(1, 20), len(fixed_list))

# Ordenar y visualizar la lista definida
print("Ordenando la lista definida:")
iterations_fixed, time_fixed = insertion_sort_visualized(fixed_list)

# Ordenar y visualizar la lista aleatoria
print("Ordenando la lista aleatoria:")
iterations_random, time_random = insertion_sort_visualized(random_list)

# Resultados
print(f"Lista definida: Iteraciones = {iterations_fixed}, Tiempo = {time_fixed:.2f} segundos")
print(f"Lista aleatoria: Iteraciones = {iterations_random}, Tiempo = {time_random:.2f} segundos")
