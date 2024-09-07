import matplotlib.pyplot as plt
import time

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

            # Actualiza las barras graficas
            for k, bar in enumerate(bars):
                bar.set_height(arr[k])
                bar.set_color('red' if k == j + 1 else 'blue')
                
            plt.pause(0.2)  # Pausa de 0.2 segundos entre actualizaciones
        
        arr[j + 1] = key

        # Actualizacion final despues de insertar el cambio
        for k, bar in enumerate(bars):
            bar.set_height(arr[k])
            bar.set_color('blue')

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Actualizacion final para que muestre la matriz
    for bar in bars:
        bar.set_color('green')
    
    # Mostrar el número de iteraciones y el tiempo total
    ax.set_title(f'Insertion Sort Completed\nIterations: {iterations} | Time: {elapsed_time:.2f} seconds')

    plt.show()

# Lista definida
arr = [4, 3, 2, 10, 12, 1, 5]
insertion_sort_visualized(arr)
