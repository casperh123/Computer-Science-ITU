import numpy as np
import csv
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import torch
import matplotlib.pyplot as plt

def load_coordinates(file_name):
    result_coor = []
    result_target = []
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            frame_name = row[0]      
            x = float(row[1])
            y = float(row[2])

            result_coor.append([x, y])

            target_id = int(frame_name.split('_')[0])
            result_target.append(target_id)

    
    return np.asarray(result_coor), np.asarray(result_target)


def map_targets_to_values(target_list, csv_file):
    """
    Reads target values from CSV where each row corresponds to target index 0,1,2,...
    and returns a list of (sx, sy) for each target index in target_list.
    """

    # Load all sx, sy values in order
    target_values = []
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            sx = float(row[0])
            sy = float(row[1])
            target_values.append([sx, sy])

    # Map target_list indices to values
    result = [target_values[t] for t in target_list]

    return np.asarray(result)



def least_square(X_train, Y_train, X_test):
    X = []
    Y = []




    for i in range(X_train.shape[0]):
        X.append([X_train[i][0], X_train[i][1], 1, 0,0,0])
        X.append([0,0,0, X_train[i][0], X_train[i][1], 1])
        Y.append(Y_train[i][0])
        Y.append(Y_train[i][1])


    X = np.asarray(X)
    Y = np.asarray(Y)



    theta = np.linalg.lstsq(X, Y, rcond=None)[0] 

    A = np.asarray([[theta[0], theta[1]], [theta[3], theta[4]]])
    b = np.asarray([[theta[2]], [theta[5]]])

    pred_l = A @ X_test.T + b

    pred_l = pred_l.T

    return pred_l


def plot_least_square_results(pred, Y_test):
    """
    Visualizes the least square results with training data, predictions, true targets, and error bars.

    Args:
        X_train (torch.Tensor): Training input data (Nx2 Tensor).
        Y_train (torch.Tensor): Training target data (Nx2 Tensor).
        X_test (torch.Tensor): Test input data (Mx2 Tensor).
        Y_test (torch.Tensor): Test target data (Mx2 Tensor).
    """

    errors_ls = np.abs(Y_test - pred)

    mse = mean_squared_error(Y_test, pred)

    num_bins = 8

    plt.figure(figsize=(10, 6))
    plt.subplot(1,2,1)
    plt.scatter(Y_test[:, 0], Y_test[:, 1], label="True Targets", alpha=0.7, s=70)
    plt.scatter(pred[:, 0], pred[:, 1], label="Predictions", alpha=0.7, s=70)
    
    dx = Y_test[:, 0] - pred[:, 0]
    dy = Y_test[:, 1] - pred[:, 1]
    plt.quiver(pred[:, 0], pred[:, 1], dx, dy, angles='xy', scale_units='xy', scale=1, alpha=0.5, color='#2ca02c')

    # Add labels, legend, and grid
    plt.xlabel("px")
    plt.ylabel("py")
    plt.title(f"Least Squares Results (MSE: {mse:.4f})")
    plt.gca().invert_xaxis()  # Flip the x-axis
    plt.gca().invert_yaxis()
    plt.legend()
    plt.grid(linestyle='--', alpha=0.5)

    plt.subplot(1,2,2)
    plt.hist(errors_ls[:, 0], num_bins, edgecolor='white', label="x")
    plt.hist(errors_ls[:, 1], num_bins, edgecolor='white', alpha=0.7, label="y")
    plt.xlabel("Absolute error")
    plt.ylabel("Number estimates")
    plt.title(f'Error Histogram Linear Least Square', fontsize=14)
    plt.legend(loc='best')
    plt.margins(x=0.01, y=0.1)

    plt.tight_layout()
    plt.show()


def load_from_csv(filename):
    """
    Loads data from a CSV file with two columns into an Nx2 NumPy array.
    
    Parameters:
    - filename (str): The name of the input CSV file.
    
    Returns:
    - np.ndarray: An Nx2 NumPy array with the data.
    """
    data = np.loadtxt(filename, delimiter=",", skiprows=1) 
    return data


def plot_results(Y_test, Y_pred, errors_nn, losses, val_losses, model_name=None, training_time=None):
    """
    Visualizes results including predictions, least squares, errors, and loss curve.

    Args:
        X_train (Tensor): Training input data.
        Y_train (Tensor): Training target data.
        X_test (Tensor): Test input data.
        Y_test (Tensor): Test target data.
        Y_pred (np.ndarray): Model predictions.
        pred_l (np.ndarray): Least squares predictions.
        errors_nn (np.ndarray): Neural network prediction errors.
        errors_ls (np.ndarray): Least squares prediction errors.
        losses (list): Training loss values.
        model_name (str, optional): Name of the model for annotation in the plots.
        training_time (float, optional): Time taken to train the model.
    """
    plt.figure(figsize=(24, 6))
    plt.subplot(1, 3, 1)
    
    #plt.scatter(pred_l[:, 0], pred_l[:, 1], label='Linear Least Square Prediction', s=70, alpha=0.6)
    plt.scatter(Y_pred[:, 0], Y_pred[:, 1], label='NN test outputs', s=70, alpha=0.4, color='green')
    plt.scatter(Y_test[:, 0], Y_test[:, 1], label='Target', s=70)
    
    dx = Y_test[:, 0] - Y_pred[:, 0]
    dy = Y_test[:, 1] - Y_pred[:, 1]

    plt.quiver(Y_pred[:, 0], Y_pred[:, 1], dx, dy, angles='xy', scale_units='xy', scale=1, alpha=0.5, color='green')
    plt.title(f'True vs Predicted Outputs {model_name}', fontsize=14)
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plt.xlabel('Sx')
    plt.ylabel('Sy')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend()

    plt.subplot(1, 3, 2)
    epochs = range(len(losses))
    plt.plot(epochs, val_losses, label='Validation loss', linewidth=2)
    plt.fill_between(epochs, val_losses, alpha=0.3)
    plt.plot(epochs, losses, label='Training loss', linewidth=2)
    plt.fill_between(epochs, losses, alpha=0.3)
    training_time_str = f"Training Time: {training_time:.2f} sec" if training_time else ""
    plt.title(f'Training Loss Curve\n{training_time_str}' if model_name else 'Training Loss Curve', fontsize=14)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend()

    plt.subplot(1, 3, 3)
    num_bins = 8
    plt.hist(errors_nn[:, 0], num_bins, edgecolor='black', alpha=0.7, label="NN x")
    plt.hist(errors_nn[:, 1], num_bins, edgecolor='black', alpha=0.7, label="NN y")
    plt.xlabel("Absolute error")
    plt.ylabel("Number estimates")
    plt.title(f'Error Histogram' if model_name else 'Error Histogram', fontsize=14)
    plt.legend(loc='best')
    plt.margins(x=0.01, y=0.1)

    plt.tight_layout()
    plt.show()




def plot_results_collected(Y_test, Y_pred, errors_nn, models, losses_dict, val_losses_dict, training_time):
    """
    Visualizes results for multiple models.

    Args:
        X_train (Tensor): Training input data.
        Y_train (Tensor): Training target data.
        X_test (Tensor): Test input data.
        Y_test (Tensor): Test target data.
        models (dict): Dictionary of models with names as keys.
        losses_dict (dict): Dictionary of loss values for each model.
        training_time (dict): Dictionary of training times for each model.
    """
    for model_name, model in models.items():
        
        plot_results(
            Y_test,
            Y_pred[model_name],
            errors_nn[model_name],
            losses_dict[model_name],
            val_losses_dict[model_name],
            model_name=model_name,
            training_time=training_time[model_name] if training_time else None
        )



def plot_mse_bar(mse_dict):
    """
    Plots a bar plot of MSE values for different models, highlighting the top three best-performing models.

    Args:
        mse_dict (dict): Dictionary with model names as keys and MSE values as values.
    
    Returns:
        None
    """
    # Sort models by MSE in ascending order
    sorted_mse = sorted(mse_dict.items(), key=lambda item: item[1])
    model_names, mse_values = zip(*sorted_mse)
    
    # Define colors for the bars
    bar_colors = ['#1f77b4'] * len(mse_values)
    if len(mse_values) >= 3:
        bar_colors[mse_values.index(sorted_mse[0][1])] = '#ff7f0e'   # Best model
        bar_colors[mse_values.index(sorted_mse[1][1])] = '#2ca02c'  # Second best model
        bar_colors[mse_values.index(sorted_mse[2][1])] = '#d62728'     # Third best model
    
    # Create the bar plot
    plt.figure(figsize=(8, 5))
    bars = plt.bar(model_names, mse_values, color=bar_colors, alpha=0.85, edgecolor=bar_colors, linewidth=1.5)
    
    # Add labels and title
    plt.xlabel("Model", fontsize=12, color='gray')
    plt.ylabel("Mean Squared Error (MSE)", fontsize=12, color='gray')
    if 'Synthetic' in model_names[0]:
        plt.title("Synthetic MSE", fontsize=10, color='black')
    else:
        plt.title("MSE", fontsize=10, color='black')
    
    # Annotate bars with MSE values
    for bar, mse in zip(bars, mse_values):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 0.02, f"{mse:.4f}", 
                 ha='center', va='bottom', fontsize=6, color='black', alpha=0.8)
    
    # Customize ticks and grid
    plt.xticks(rotation=45, ha='right', fontsize=10, color='gray')
    plt.yticks(fontsize=10, color='gray')
    plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
    
    # Adjust layout and display the plot
    plt.tight_layout(pad=1.2)
    plt.show()


def plot_data_splits(train_data, test_data, val_data):
    """
    Creates a scatterplot for training, testing, and validation data.

    Args:
        train_data (np.ndarray): Training data, shape (N, 2).
        test_data (np.ndarray): Testing data, shape (N, 2).
        val_data (np.ndarray): Validation data, shape (N, 2).

    Returns:
        None: Displays the scatterplot.
    """
    plt.figure(figsize=(24, 6))

    plt.subplot(1, 3, 1)
    
    # Scatter plot for each dataset
    plt.scatter(train_data[:, 0], train_data[:, 1], label='Training', s=50)
    plt.title("Training data", fontsize=14)
    plt.xlabel("px", fontsize=12)
    plt.ylabel("py", fontsize=12)
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plt.legend(fontsize=10, loc='best')
    plt.grid(linestyle='--', alpha=0.5)

    plt.subplot(1, 3, 2)
    plt.scatter(test_data[:, 0], test_data[:, 1], label='Validation', alpha=0.7, s=50)
    plt.title("Testing data", fontsize=14)
    plt.xlabel("px", fontsize=12)
    plt.ylabel("py", fontsize=12)
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plt.legend(fontsize=10, loc='best')
    plt.grid(linestyle='--', alpha=0.5)

    plt.subplot(1, 3, 3)
    plt.scatter(val_data[:, 0], val_data[:, 1], label='Test', alpha=0.4, s=50)
    plt.title("Validation data", fontsize=14)
    plt.xlabel("px", fontsize=12)
    plt.ylabel("py", fontsize=12)
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plt.legend(fontsize=10, loc='best')
    plt.grid(linestyle='--', alpha=0.5)
    
    # Display the plot
    plt.tight_layout()
    plt.show()


