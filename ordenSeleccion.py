import matplotlib.pyplot as plt
import time
import random

def selection_sort_visualized(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='blue')
    ax.set_title('Selection Sort Visualization')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    
    iterations = 0
    start_time = time.time()

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            iterations += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

            # Update the bars
            for k, bar in enumerate(bars):
                bar.set_height(arr[k])
                bar.set_color('red' if k == min_idx else 'blue')
                
            # Redraw the plot
            plt.pause(0.1)  # Pausa de 0.1 segundos entre actualizaciones

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # Final update after swapping
        for k, bar in enumerate(bars):
            bar.set_height(arr[k])
            bar.set_color('blue')

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Final actualizado de la lista de seleccion
    for bar in bars:
        bar.set_color('green')
    
    # Mostrar el número de iteraciones y el tiempo total
    ax.set_title(f'Selection Sort Completed\nIterations: {iterations} | Time: {elapsed_time:.2f} seconds')

    plt.show()
    return iterations, elapsed_time

# Comparar la lista definida con una lista aleatoria
fixed_list = [64, 25, 12, 22, 11]
random_list = random.sample(range(1, 70), len(fixed_list))

# Ordenar y visualizar la lista definida
print("Ordenando la lista definida:")
iterations_fixed, time_fixed = selection_sort_visualized(fixed_list)

# Ordenar y visualizar la lista aleatoria
print("Ordenando la lista aleatoria:")
iterations_random, time_random = selection_sort_visualized(random_list)

# Resultados
print(f"Lista definida: Iteraciones = {iterations_fixed}, Tiempo = {time_fixed:.2f} segundos")
print(f"Lista aleatoria: Iteraciones = {iterations_random}, Tiempo = {time_random:.2f} segundos")
