{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def save_model(model, suffix=None):\n",
    "  \"\"\"\n",
    "  Saves a given model in a models directory and appends a suffix (str)\n",
    "  for clarity and reuse.\n",
    "  \"\"\"\n",
    "  # Create model directory with current time\n",
    "  modeldir = os.path.join(\"drive/My Drive/Data/models\",\n",
    "                          datetime.datetime.now().strftime(\"%Y%m%d-%H%M%s\"))\n",
    "  model_path = modeldir + \"-\" + suffix + \".h5\" # save format of model\n",
    "  print(f\"Saving model to: {model_path}...\")\n",
    "  model.save(model_path)\n",
    "  return model_path"
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
