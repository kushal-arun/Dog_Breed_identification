{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function to turn data into batches\n",
    "def create_data_batches(X, y=None, batch_size=BATCH_SIZE, valid_data=False, test_data=False):\n",
    "  \"\"\"\n",
    "  Creates batches of data out of image (X) and label (y) pairs.\n",
    "  Shuffles the data if it's training data but doesn't shuffle if it's validation data.\n",
    "  Also accepts test data as input (no labels).\n",
    "  \"\"\"\n",
    "  # If the data is a test dataset, we probably don't have have labels\n",
    "  if test_data:\n",
    "    print(\"Creating test data batches...\")\n",
    "    data = tf.data.Dataset.from_tensor_slices((tf.constant(X))) # only filepaths (no labels)\n",
    "    data_batch = data.map(process_image).batch(BATCH_SIZE)\n",
    "    return data_batch\n",
    "  \n",
    "  # If the data is a valid dataset, we don't need to shuffle it\n",
    "  elif valid_data:\n",
    "    print(\"Creating validation data batches...\")\n",
    "    data = tf.data.Dataset.from_tensor_slices((tf.constant(X), # filepaths\n",
    "                                               tf.constant(y))) # labels\n",
    "    data_batch = data.map(get_image_label).batch(BATCH_SIZE)\n",
    "    return data_batch\n",
    "\n",
    "  else:\n",
    "    print(\"Creating training data batches...\")\n",
    "    # Turn filepaths and labels into Tensors\n",
    "    data = tf.data.Dataset.from_tensor_slices((tf.constant(X),\n",
    "                                               tf.constant(y)))\n",
    "    # Shuffling pathnames and labels before mapping image processor function is faster than shuffling images\n",
    "    data = data.shuffle(buffer_size=len(X))\n",
    "\n",
    "    # Create (image, label) tuples (this also turns the iamge path into a preprocessed image)\n",
    "    data = data.map(get_image_label)\n",
    "\n",
    "    # Turn the training data into batches\n",
    "    data_batch = data.batch(BATCH_SIZE)\n",
    "  return data_batch"
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
