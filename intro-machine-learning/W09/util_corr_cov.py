import matplotlib.pyplot as plt
import numpy as np

def plot_cov(df, cov_mat):

    # Plot Covariance Matrix with values
    plt.figure(figsize=(6, 5))
    plt.imshow(cov_mat, cmap='coolwarm', interpolation='none')
    plt.colorbar(label='Covariance')
    plt.title("Covariance Matrix")
    plt.xticks(range(len(df.columns)), df.columns, rotation=45)
    plt.yticks(range(len(df.columns)), df.columns)

    # Annotate each cell with its value
    for i in range(len(df.columns)):
        for j in range(len(df.columns)):
            plt.text(j, i, f"{cov_mat[i, j]:.2f}", ha='center', va='center', color='black')

    plt.tight_layout()
    plt.show()

def plot_corr(df, corr_mat):
    # Plot Correlation Matrix with values
    plt.figure(figsize=(6, 5))
    plt.imshow(corr_mat, cmap='coolwarm', vmin=-1, vmax=1, interpolation='none')
    plt.colorbar(label='Correlation')
    plt.title("Correlation Matrix")
    plt.xticks(range(len(df.columns)), df.columns, rotation=45)
    plt.yticks(range(len(df.columns)), df.columns)

    # Annotate each cell with its value
    for i in range(len(df.columns)):
        for j in range(len(df.columns)):
            plt.text(j, i, f"{corr_mat[i, j]:.2f}", ha='center', va='center', color='black')

    plt.tight_layout()
    plt.show()
