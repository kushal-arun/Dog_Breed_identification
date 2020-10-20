{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Building a function to train and return a trained model\n",
    "def train_model():\n",
    "  \"\"\"\n",
    "  Trains a given model and returns the trained version.\n",
    "  \"\"\"\n",
    "  # Create a model\n",
    "  model = create_model()\n",
    "\n",
    "  # Create new TensorBoard session everytime we train a model\n",
    "  tensorboard = create_tensorboard_callback()\n",
    "\n",
    "  # Fit the model to the data passing it the callabcks we created\n",
    "  model.fit(x = train_data,\n",
    "           epochs = NUM_EPOCHS,\n",
    "           validation_data = val_data,\n",
    "           validation_freq = 1,\n",
    "           callbacks = [tensorboard, early_stopping])\n",
    "  # Return the fitted model\n",
    "  return model"
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
