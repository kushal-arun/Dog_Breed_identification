{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function to build a TensorBoard callback\n",
    "def create_tensorboard_callback():\n",
    "  # Create a log directory for storing TensorBoard logs\n",
    "  logdir = os.path.join(\"/content/drive/My Drive/Dog-vision/logs\",\n",
    "                        #Make it so the logs gets tracked whenever we run an experiment\n",
    "                        datetime.datetime.now().strftime(\"%Y%m%d-%H%M%S\"))\n",
    "  return tf.keras.callbacks.TensorBoard(logdir)"
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
