import matplotlib.pyplot as plt
import numpy as np
import time

def bubble_sort_visualized(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='blue')
    ax.set_title('Ordenamiento de Burbuja')
    ax.set_xlabel('Base')
    ax.set_ylabel('Barras de valores')
    
    iterations = 0
    start_time = time.time()

    for i in range(n):
        for j in range(0, n-i-1):
            iterations += 1
            if arr[j] > arr[j+1]:
                # Hace intercambio
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # Actualiza las barras
                for k, bar in enumerate(bars):
                    bar.set_height(arr[k])
                    bar.set_color('red' if k == j or k == j+1 else 'blue')

                # Aumento o Reduccion del tiempo del ordenamiento
                plt.pause(0.1)
    
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Final update to show the sorted array
    for bar in bars:
        bar.set_color('green')
    
    # Mostrar el número de iteraciones y el tiempo total
    ax.set_title(f'Bubble Sort Completed\nIterations: {iterations} | Time: {elapsed_time:.2f} seconds')

    plt.show()

# Lista a ordenar o variar
arr = np.random.randint(1, 100, 20)
#arr = [5, 2, 9, 1, 5, 6]
bubble_sort_visualized(arr)
