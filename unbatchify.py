{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function to unbatch a batched dataset\n",
    "def unbatchify(data):\n",
    "  \"\"\"\n",
    "  Takes a batched dataset of (image, label) Tensors and returns separate arrays\n",
    "  of images and labels.\n",
    "  \"\"\"\n",
    "  images = []\n",
    "  labels = []\n",
    "  # Loop through unbatched data\n",
    "  for image, label in data.unbatch().as_numpy_iterator():\n",
    "    images.append(image)\n",
    "    labels.append(unique_breeds[np.argmax(label)])\n",
    "  return images, labels"
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
