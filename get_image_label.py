{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a dimple function to return a tuple (image, label)\n",
    "def get_image_label(image_path, label):\n",
    "  \"\"\"\n",
    "  Takes an image file path name and assosciated label, processes the image and return a tuple \n",
    "  \"\"\"\n",
    "  image = process_image(image_path)\n",
    "  return image, label"
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
