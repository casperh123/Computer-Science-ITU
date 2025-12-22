import skimage
import matplotlib.pyplot as plt
import numpy as np

def visualize_points(points_source, points_destination):

    # Read and process ITU_image
    ITU_image = skimage.io.imread('data/image_ground.jpg')
    ITU_RGB = ITU_image[:, :, :3].copy()
    ITU_RGB[int(points_source[0, 1]) - 5:int(points_source[0, 1]) + 5,
            int(points_source[0, 0]) - 5:int(points_source[0, 0]) + 5] = [255, 0, 0]
    ITU_RGB[int(points_source[1, 1]) - 5:int(points_source[1, 1]) + 5,
            int(points_source[1, 0]) - 5:int(points_source[1, 0]) + 5] = [0, 255, 0]
    ITU_RGB[int(points_source[2, 1]) - 5:int(points_source[2, 1]) + 5,
            int(points_source[2, 0]) - 5:int(points_source[2, 0]) + 5] = [0, 0, 255]

    # Read and process ITU_Map
    ITU_Map = plt.imread('data/ITUMap.png')
    Map_RGB = ITU_Map[:, :, :3].copy()
    Map_RGB[int(points_destination[0, 1]) - 5:int(points_destination[0, 1]) + 5,
            int(points_destination[0, 0]) - 5:int(points_destination[0, 0]) + 5] = [1, 0, 0]
    Map_RGB[int(points_destination[1, 1]) - 5:int(points_destination[1, 1]) + 5,
            int(points_destination[1, 0]) - 5:int(points_destination[1, 0]) + 5] = [0, 1, 0]
    Map_RGB[int(points_destination[2, 1]) - 5:int(points_destination[2, 1]) + 5,
            int(points_destination[2, 0]) - 5:int(points_destination[2, 0]) + 5] = [0, 0, 1]

    # Plot side by side
    fig, ax = plt.subplots(1, 2, figsize=(16, 8))

    ax[0].imshow(ITU_RGB)
    ax[0].set_title("ITU Image")
    ax[0].axis('off')

    ax[1].imshow(Map_RGB)
    ax[1].set_title("ITU Map")
    ax[1].axis('off')

    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(14, 4))
    plt.subplot(1, 2, 1) 
    plt.plot(points_source[:, 0], points_source[:, 1], 'r*')
    plt.ylim(256, 0)
    plt.xlim(0, 320)
    plt.title('The 3 source points')

    plt.subplot(1, 2, 2)
    plt.plot(points_destination[:, 0], points_destination[:, 1], 'b*')
    plt.ylim(348, 0)
    plt.xlim(0, 800), 
    plt.title('The 3 destination points')

#### Visualize transformed points and original plane side by side
def visualize_transformed_points(points_source, points_destination, M_points, G_points):

    fig, ax = plt.subplots(1, 2, figsize=(30, 12))  # 1 row, 2 columns

    # ITU MAP plane
    ax[0].plot(points_destination[:, 0], points_destination[:, 1], 'b*', label="3 points for transformation estimation")
    ax[0].plot(M_points[:, 0], M_points[:, 1], 'g.', label="tracked person")
    ax[0].set_ylim(348, 0)
    ax[0].set_xlim(0, 800)
    ax[0].set_title('ITU MAP Plane')
    ax[0].legend()

    # Video plane
    ax[1].plot(points_source[:, 0], points_source[:, 1], 'b*', label="3 points for transformation estimation")
    ax[1].plot(G_points[:, 0], G_points[:, 1], 'g.', label="tracked person")
    ax[1].set_ylim(256, 0)
    ax[1].set_xlim(0, 320)
    ax[1].set_title('Video Plane')
    ax[1].legend()

    plt.tight_layout()
    plt.show()



