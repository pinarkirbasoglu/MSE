import numpy as np
def mse(original, noisy, step=1):
    """
    Calculate the Mean Squared Error (MSE) between two lists.

    Parameters:
    - original (list): The original data.
    - noisy (list): The noisy or predicted data.
    - step (int, optional): The step size to iterate through the lists. Default is 1.

    Returns:
    - float: The mean squared error between the two lists.
    """
    if len(original) != len(noisy):
        raise ValueError("Both lists must have the same length.")

    sum_squared_error = 0
    for i in range(0, len(original), step):
        error = original[i] - noisy[i]
        sum_squared_error += error ** 2

    return sum_squared_error / len(original)

# Örnek kullanım
dosya_yolu_orgin_1 = "original_matrix_1.npy" 
dosya_yolu_genereted_1="generated_matrix_1.npy"

dosya_yolu_orgin_2 = "original_matrix_2.npy"
dosya_yolu_genereted_2="generated_matrix_2.npy"

original_1 = np.load(dosya_yolu_orgin_1)
noisy_1 = np.load(dosya_yolu_genereted_1)

original_2 = np.load(dosya_yolu_orgin_2)
noisy_2 = np.load(dosya_yolu_genereted_2)

result_1 = mse(original_1, noisy_1)
print("Mean Squared Error ilk resim :", result_1)

result_2 = mse(original_2, noisy_2)
print("Mean Squared Error ilk resim :", result_2)




