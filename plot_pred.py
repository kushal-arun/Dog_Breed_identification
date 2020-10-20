{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_pred(prediction_probabilities, labels, images, n=1):\n",
    "  \"\"\"\n",
    "  View the prediction, ground truth label and image for sample n.\n",
    "  \"\"\"\n",
    "  pred_prob, true_label, image = prediction_probabilities[n], labels[n], images[n]\n",
    "  \n",
    "  # Get the pred label\n",
    "  pred_label = get_pred_label(pred_prob)\n",
    "  \n",
    "  # Plot image & remove ticks\n",
    "  plt.imshow(image)\n",
    "  plt.xticks([])\n",
    "  plt.yticks([])\n",
    "\n",
    "  # Change the color of the title depending on if the prediction is right or wrong\n",
    "  if pred_label == true_label:\n",
    "    color = \"green\"\n",
    "  else:\n",
    "    color = \"red\"\n",
    "\n",
    "  plt.title(\"{} {:2.0f}% ({})\".format(pred_label,\n",
    "                                      np.max(pred_prob)*100,\n",
    "                                      true_label),\n",
    "                                      color=color)"
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
