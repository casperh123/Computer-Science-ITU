import matplotlib.pyplot as plt

def limb_number_plot(s_pose_x,s_pose_y,n1,n2,c="red",label=None,axis = None):
  if label is not None:
    if (s_pose_x[n1]>-10.0) and (s_pose_x[n2]>-10.0) and (s_pose_y[n1]>-10.0) and (s_pose_y[n2]>-10.0): 
        axis.plot([s_pose_x[n1],s_pose_x[n2]], [s_pose_y[n1], s_pose_y[n2]],color = c, linestyle="-",label=label)
  else:
    if (s_pose_x[n1]>-10.0) and (s_pose_x[n2]>-10.0) and (s_pose_y[n1]>-10.0) and (s_pose_y[n2]>-10.0): 
        axis.plot([s_pose_x[n1],s_pose_x[n2]], [s_pose_y[n1], s_pose_y[n2]],color = c, linestyle="-")

def plot_single_pose(s_pose, a, c = "darkgreen", label=None, head = True):
    s_pose_x=s_pose[::2]
    s_pose_y=s_pose[1::2]
    limb_number_plot(s_pose_x,s_pose_y,2,5,c,axis=a)
    if label is not None:

        limb_number_plot(s_pose_x,s_pose_y,9,12,c,label,axis=a)
    else:
        limb_number_plot(s_pose_x,s_pose_y,9,12,c,axis=a)
    limb_number_plot(s_pose_x,s_pose_y,2,9,c,axis=a)
    limb_number_plot(s_pose_x,s_pose_y,5,12,c,axis=a)

    limb_number_plot(s_pose_x,s_pose_y,2,3,c,axis=a)
    limb_number_plot(s_pose_x,s_pose_y,3,4,c,axis=a)

    limb_number_plot(s_pose_x,s_pose_y,5,6,c,axis=a)
    limb_number_plot(s_pose_x,s_pose_y,6,7,c,axis=a)

    #left leg / foot
    limb_number_plot(s_pose_x,s_pose_y,9,10,c,axis=a)
    limb_number_plot(s_pose_x,s_pose_y,10,11,c,axis=a)
    limb_number_plot(s_pose_x,s_pose_y,11,22,c,axis=a)

    #right leg / foot
    limb_number_plot(s_pose_x,s_pose_y,12,13,c,axis=a)
    limb_number_plot(s_pose_x,s_pose_y,13,14,c,axis=a)
    limb_number_plot(s_pose_x,s_pose_y,14,19,c,axis=a)

    # head
    if head:
        limb_number_plot(s_pose_x,s_pose_y,0,15,c,axis=a)
        limb_number_plot(s_pose_x,s_pose_y,0,16,c,axis=a)

        limb_number_plot(s_pose_x,s_pose_y,15,17,c,axis=a)
        limb_number_plot(s_pose_x,s_pose_y,16,18,c,axis=a)
    return True 


def plot_single(ax, i, p):
    ax.scatter(p[:, 0], p[:, 1]) # Plot the pose coordinates

    ax.set_title(i)
    ax.set_xlim(-5, 5)
    ax.set_ylim(3,-3)



def plot_pair(a, b):
    """Plot two poses side by side. a and b are poses.
    """
    fig, ax = plt.subplots(1, 2)

    ap = a
    bp = b

    plot_single_pose(ap, ax[0])
    plot_single_pose(bp, ax[1])

    for axis in ax.flat:  # works if ax is a 2D array
        axis.set_xlim(-5, 5)
        axis.set_ylim(3, -3)
    #plot_single(ax[0], a, ap)
    #plot_single(ax[1], b, bp)
