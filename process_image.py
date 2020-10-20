{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function for preprocessing images\n",
    "def process_image(image_path, img_size= IMG_SIZE):\n",
    "  \"\"\"\n",
    "  Takes an iamge file and turn the image into a tensor.\n",
    "  \"\"\"\n",
    "  #Read an image file\n",
    "  image = tf. io.read_file(image_path)\n",
    "  #Turn th jpeg image into numerical Tensor with 3 colour RGB channel\n",
    "  image = tf.image.decode_jpeg(image, channels=3)\n",
    "  #Convert the colour channels from 0-255 to 0-1\n",
    "  image = tf.image.convert_image_dtype(image, tf.float32)\n",
    "  #Resize the image to our desired values(224, 224)\n",
    "  image = tf.image.resize(image, size=[IMG_SIZE, IMG_SIZE])\n",
    "\n",
    "  return image"
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
