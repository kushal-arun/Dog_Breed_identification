{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function which builds a Keras model\n",
    "def create_model(input_shaape = INPUT_SHAPE, output_shape = OUTPUT_SHAPE, model_url = MODEL_URL):\n",
    "  print(\"Building with:\", MODEL_URL)\n",
    "\n",
    "  #Setup the model layers\n",
    "  model = tf.keras.Sequential([\n",
    "    hub.KerasLayer(MODEL_URL), #Layer 1 (i/p layer)\n",
    "    tf.keras.layers.Dense(units = OUTPUT_SHAPE,\n",
    "                         activation = \"softmax\") #LAyer 2 (o/p layer)\n",
    "  ])\n",
    "\n",
    "  # Compile the model\n",
    "  model.compile(\n",
    "      loss = tf.keras.losses.CategoricalCrossentropy(),\n",
    "      optimizer = tf.keras.optimizers.Adam(),\n",
    "      metrics = [\"accuracy\"]\n",
    "  )\n",
    "\n",
    "  #Build the model\n",
    "  model.build(INPUT_SHAPE)\n",
    "\n",
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
