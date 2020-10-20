{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create a function for viewing images in a data batches\n",
    "def show_25_images(images, labels):\n",
    "  \"\"\"\n",
    "  Display a plot of 25 images and their labels from a data batch.\n",
    "  \"\"\"\n",
    "  # Setup the figure\n",
    "  plt.figure(figsize=(10, 10))\n",
    "  # Loopthrougn 25 (for displaying 25 images)\n",
    "  for i in range(25):\n",
    "    # Create subplots (5 rows, 5 Columns)\n",
    "    ax = plt.subplot(5, 5, i+1)\n",
    "    # Display an image\n",
    "    plt.imshow(images[i])\n",
    "    # Add the image label as the title\n",
    "    plt.title(unique_breeds[labels[i].argmax()])\n",
    "    # Turn the grid lines off\n",
    "    plt.axis(\"off\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
