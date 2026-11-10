{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c3d02896-11e9-4287-81c9-4ebca17c12e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model Accuracy: 98.33 %\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAGbCAYAAAAr/4yjAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjksIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvJkbTWQAAAAlwSFlzAAAPYQAAD2EBqD+naQAAFrZJREFUeJzt3HuQlXX9wPHP4gJyCwEB74Aoat4yFc0b4AUN0YAQb5lYE4yjmJmXdCaFfs2QCgI6xqQ5bsqijTCgJZaaUmKF5GUmTRMITBMVExAvgMj39wezn1x3F9YVXbPXa+b8wTnPec7nnH32vM/znGepKKWUAICIaNHcAwDw2SEKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKnyM9e/aMkSNH5r/nzp0bFRUVMXfu3Gab6cM+PCOfPR9nu1m6dGlUVFREVVXVFp+LT4cobCFVVVVRUVGRl6233jr69OkT559/frz66qvNPd5HMmfOnBg7dmxzjxFr1qyJSZMmxSGHHBIdO3as9Zo+//zz9d7n0ksvjYqKijj11FPrvb3mTavmstVWW8Uuu+wSQ4cOjaeeeioiIkaOHFlrmYYuH4zbrFmz4qtf/Wpsu+220apVq9hhhx1ixIgR8dBDD+UyNW+2M2bMqHe2kSNHRvv27Rt8Pfr27RsVFRUxderUzbxyDT/fli1bxrbbbhuHHXZYXHHFFfHPf/6z0etqqi25Pa1evTouvfTS6NWrV7Ru3Tp23HHHGD58eLzzzjtbZP1EVDb3AJ83P/rRj6JXr16xZs2amDdvXkydOjXmzJkTTz/9dLRt2/ZTneWoo46Kd999N1q1avWR7jdnzpy48cYbmzUMr7/+epxwwgnx+OOPx+DBg+OMM86I9u3bx9///ve4884746abbop169bVuk8pJe64447o2bNn/OpXv4rVq1dHhw4d6l3/6aefHoMGDYr3338/nn322Zg6dWrcd9998ec//zlGjx4dxx57bC67ZMmSuPLKK2PUqFFx5JFH5vW9e/eOUkp861vfiqqqqjjggAPioosuiu222y6WLVsWs2bNimOOOSYeffTROOywwz7W67Fw4cJYsGBB9OzZM6qrq+Pcc8/9SPeveb4bNmyIFStWxIIFC2Ly5MkxZcqUuOWWW+K0007LZZu63URE9OjRI959991o2bJlXreltqdVq1ZFv3794qWXXopRo0bFbrvtFsuXL49HHnkk1q5d+6n/fn1uFbaIW2+9tUREWbBgQa3rL7roohIRZfr06Q3e96233toiM/To0aOcffbZH3s95513XvmkNo3GznjiiSeWFi1alBkzZtS5bc2aNeX73/9+nesfeuihEhHloYceKi1btixVVVV1llmyZEmJiHLttdfWuv6ee+4pEVFGjRpV5z4LFiwoEVFuvfXWOrdde+21JSLKhRdeWDZs2FDn9ttuu63Mnz+/lFLKww8/XCKi3HXXXfU+57PPPru0a9eu3tuuvPLK0q1btzJz5sxSUVFRlixZUu9yH9bQ8y2llKVLl5Y+ffqUVq1alaeeeqpR62uKLbU9nXvuuWWbbbYp//jHP7bAVDTE4aNP2NFHHx0RGz9tRvznEMHixYtj0KBB0aFDhzjzzDMjImLDhg0xefLk2HvvvWPrrbeO7t27x+jRo2PFihW11llKiR//+Mex0047Rdu2bWPAgAHxzDPP1Hnsho4Nz58/PwYNGhSdOnWKdu3axX777RdTpkzJ+W688caIiFqHHWps6RnrM3/+/Lj33nvj29/+dnz961+vc3vr1q1jwoQJda6vrq6OL37xizFgwIA49thjo7q6ulGPF1H359QY7777bowfPz723HPPmDBhQq3XqcZZZ50Vffv2bfQ6GzJ9+vQYPnx4DB48ODp27BjTp0//2Ovs0aNHVFVVxbp16+Kaa67J6xvabm688cbYddddo02bNtG3b9945JFHon///tG/f/9c5sPfKWxue1q2bFk899xz8d57721y1pUrV8att94ao0aNil69esW6deti7dq1H+8FoF6i8AlbvHhxRER06dIlr1u/fn0cf/zx0a1bt5gwYUK+8Y0ePTouueSSOPzww2PKlClxzjnnRHV1dRx//PG1fmmuvPLK+OEPfxj7779/XHvttbHrrrvGwIED4+23397sPA888EAcddRR8be//S2++93vxsSJE2PAgAHx61//Omc47rjjIiLi9ttvz0uNT2PGe+65JyI2vqE21tq1a2PmzJlx+umnR8TGwyUPPfRQvPLKK426f30/p82ZN29evPHGG3HGGWfEVltt1ej7rV69Ol5//fU6l4be5ObPnx+LFi2K008/PVq1ahXDhg37SMHblK985SvRu3fveOCBBza53NSpU+P888+PnXbaKa655po48sgjY8iQIfHSSy9t8n6b254uv/zy2GuvveJf//rXJtczb968WLNmTey2224xfPjwaNu2bbRp0yYOP/zw/C6ILaS5d1U+L2oOHz344INl+fLl5cUXXyx33nln6dKlS2nTpk156aWXSikbDxFERPnBD35Q6/6PPPJIiYhSXV1d6/rf/OY3ta5/7bXXSqtWrcqJJ55Y63DFFVdcUSKi1qGZmsMVDz/8cCmllPXr15devXqVHj16lBUrVtR6nA+uq6Hd/U9ixvoMHTq0RESdGTdlxowZJSLKwoULSymlvPnmm2XrrbcukyZNqrVczeGUcePGleXLl5dXXnmlzJ07txxwwAElIsrMmTPrrLuhw0dTpkwpEVFmzZrVqBlrfh6butR3+Oj8888vO++8c76W999/f4mI8uSTT272MTd1+KjG1772tRIRZdWqVbXmrNlu1q5dW7p06VIOPvjg8t577+X9qqqqSkSUfv361Xm8D75Wmzp8VPP7sLnDYdddd12JiNKlS5fSt2/fUl1dXX7605+W7t27l06dOpWXX3550y8EjWZPYQs79thjo2vXrrHzzjvHaaedFu3bt49Zs2bFjjvuWGu5D39ReNddd0XHjh3juOOOq/Xp8cADD4z27dvHww8/HBERDz74YKxbty7GjBlTazf8wgsv3OxsTz75ZCxZsiQuvPDC2GabbWrdVt+hjw/7NGaMiHjzzTcjIhr8krg+1dXVcdBBB8Vuu+2W9z3xxBMb/ER91VVXRdeuXWO77baL/v37x+LFi+Pqq6+OYcOGNfoxmzJnxMa9qAceeKDOZeDAgXWWXb9+ffzyl7+MU089NV/Lo48+Orp167bF9hZqznhavXp1vbf/5S9/iX//+9/xne98Jyor/3NuyplnnhmdOnX6WI9dVVUVpZTo2bPnJpd76623ImLjdvq73/0uzjjjjDj33HNj9uzZsWLFijxExcfn7KMt7MYbb4w+ffpEZWVldO/ePfbYY49o0aJ2eysrK2OnnXaqdd3ChQtj1apV0a1bt3rX+9prr0VExAsvvBAREbvvvnut27t27brZX9CaQyT77LNP45/QpzxjRMQXvvCFiNj4JvXheNVn5cqVMWfOnDj//PNj0aJFef3hhx8eM2fOjOeffz769OlT6z6jRo2KU045JVq0aBHbbLNN7L333tG6devNPlZDc34U++67b62zm2pMmzatznX3339/LF++PPr27VvruQ0YMCDuuOOOuPrqq+tsXx9VzRtuQ3Gr+XnWBLdGZWXlZt/Mt5Q2bdpERMRJJ51U67TdQw89NHr16hV//OMfP5U5/heIwhbWt2/fOOiggza5TOvWrev8Im/YsGGTn/66du26xWZsqk9rxj333DMiIv7617/WOgW0IXfddVesXbs2Jk6cGBMnTqxze3V1dYwbN67Wdbvvvnu9b8xNnXPIkCEfa10NqXmtR4wYUe/tv//972PAgAEf6zGefvrp6NatW0bus2iHHXaIiIju3bvXua1bt251TnSg6UThM6J3797x4IMPxuGHH56fiurTo0ePiNj4qX3XXXfN65cvX77ZX4zevXtHxMY3gU29ITZ0KOnTmDFi46fB8ePHx7Rp0xoVherq6thnn33iqquuqnPbz372s5g+fXqdKGwJRxxxRHTq1CnuuOOOuOKKKz7Sl82N8fbbb8fdd98dp556agwfPrzO7RdccEFUV1d/rCj86U9/isWLF8c3vvGNBpep+XkuWrSo1mOtX78+li5dGvvtt98mH6MxhyY358ADD4yIqPcL6ZdffjkDzcfnO4XPiBEjRsT7778f//d//1fntvXr18fKlSsjYuN3Fi1btowbbrghSim5zOTJkzf7GF/+8pejV69eMXny5FxfjQ+uq127dhERdZb5NGaM2HhGzAknnBA///nPY/bs2XVuX7duXVx88cUREfHiiy/GH/7whxgxYkQMHz68zuWcc86JRYsWxfz58xv12B9F27Zt47LLLotnn302LrvsslrPtca0adPisccea9L6Z82aFW+//Xacd9559T63wYMHx8yZM5t8auYLL7wQI0eOjFatWsUll1zS4HIHHXRQdOnSJW6++eZYv359Xl9dXd2oyDe0PUU0/pTUPfbYI/bff/+4++674/XXX8/r77///njxxRfzDCc+PnsKnxH9+vWL0aNHx/jx4+Opp56KgQMHRsuWLWPhwoVx1113xZQpU2L48OHRtWvXuPjii2P8+PExePDgGDRoUDz55JNx3333xbbbbrvJx2jRokVMnTo1TjrppPjSl74U55xzTmy//fbx3HPPxTPPPBO//e1vI+I/n8ouuOCCOP7442OrrbaK00477VOZscZtt90WAwcOjGHDhsVJJ50UxxxzTLRr1y4WLlwYd955ZyxbtiwmTJgQ06dPj1JKnHzyyfWuZ9CgQVFZWRnV1dVxyCGHfISfSONccskl8cwzz8TEiRPj4YcfjuHDh8d2220Xr7zySsyePTsee+yxJh/vrq6uji5dujT419Ann3xy3HzzzXHvvfdu9gvyJ554IqZNmxYbNmyIlStXxoIFC2LmzJlRUVERt99++yY/7bdq1SrGjh0bY8aMiaOPPjpGjBgRS5cujaqqqujdu/dm9wQa2p4iNp6S+otf/CKWLFmy2e8nJk2aFMcdd1wcccQRMXr06Fi1alVcd9110adPn4/8F95sQnOe+vR50tBfNH/Ypv5qtZRSbrrppnLggQeWNm3alA4dOpR99923XHrppbVOuXv//ffLuHHjyvbbb1/atGlT+vfvX55++uk6fy384VMLa8ybN68cd9xxpUOHDqVdu3Zlv/32KzfccEPevn79+jJmzJjStWvXUlFRUed0wi0546a88847ZcKECeXggw8u7du3L61atSq77757GTNmTFm0aFEppZR999237LLLLptcT//+/Uu3bt3Ke++916hTND9sU3/RXGPGjBll4MCBpXPnzqWysrJsv/325dRTTy1z587NZT7KXzS/+uqrpbKyspx11lkNPuY777xT2rZtW4YOHdrgMjXPt+ZSWVlZOnfuXA455JBy+eWXlxdeeKHOfRrabq6//vrSo0eP0rp169K3b9/y6KOPlgMPPLCccMIJdR7vg6/Vpranxp6SWuOBBx4ohx56aNl6661L586dy1lnnVWWLVvWqPvSOBWl1LPPC7AZGzZsiK5du8awYcPi5ptvbu5x2EJ8pwBs1po1a+p8Z3LbbbfFG2+8Ueu/ueC/nz0FYLPmzp0b3/ve9+KUU06JLl26xBNPPBG33HJL7LXXXvH444836X9U5bPJF83AZvXs2TN23nnnuP766+ONN96Izp07xze/+c34yU9+IgifM/YUAEi+UwAgiQIAqdHfKWyJP1Xnf0Nj/zfUz5pP6v8v+qQ5+4fGasy3BfYUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAVNncA1C//v37N/cITTZp0qTmHqFJxo0b19wjQLOzpwBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKACRRACCJAgBJFABIogBAEgUAkigAkEQBgCQKAKSKUkpp1IIVFZ/0LHzA3Llzm3uEJlu5cmVzj9AkQ4YMae4R4BPVmLd7ewoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQBSRSmlNGrBiopPehY+YOXKlc09QpPNnj27uUdokqVLlzb3CE3y3zr3f+t2EvHf+/vZmLd7ewoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAECqKKWURi1YUfFJz8IHrFy5srlHaLKOHTs29whNMm7cuOYeoUl69uzZ3CM0ydKlS5t7hCYbO3Zsc4/QJI15u7enAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoApMrmHoD6rVy5srlHaLKxY8c29whNMnny5OYe4X/K3Llzm3sE6mFPAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASJXNPQD1q6qqau4Rmqx///7NPUKTTJ48ublHaJIhQ4Y09whN0q9fv+Yeocl69uzZ3CN8YuwpAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASKIAQBIFAJIoAJBEAYAkCgAkUQAgiQIASRQASJXNPQD1Gzt2bHOP0GSTJ09u7hGaZOnSpc09wv+UoUOHNvcITfZ53lbsKQCQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQRAGAJAoAJFEAIIkCAKmilFKaewgAPhvsKQCQRAGAJAoAJFEAIIkCAEkUAEiiAEASBQCSKACQ/h9ytCdR89G1HQAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Predicted CAPTCHA Digit: 6\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.datasets import load_digits\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "# Load sample handwritten digit images\n",
    "digits = load_digits()\n",
    "X = digits.data\n",
    "y = digits.target\n",
    "\n",
    "# Split data into training and testing sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(\n",
    "    X, y, test_size=0.2, random_state=42\n",
    ")\n",
    "\n",
    "# Train the machine learning model\n",
    "model = KNeighborsClassifier(n_neighbors=3)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Test the model\n",
    "y_pred = model.predict(X_test)\n",
    "print(\"Model Accuracy:\", round(accuracy_score(y_test, y_pred) * 100, 2), \"%\")\n",
    "\n",
    "# Display one test image and predict its digit\n",
    "image = X_test[index].reshape(8, 8)\n",
    "prediction = model.predict([X_test[index]])[0]\n",
    "\n",
    "plt.imshow(image, cmap=\"gray\")\n",
    "plt.title(\"Predicted CAPTCHA Digit: \" + str(prediction))\n",
    "plt.axis(\"off\")\n",
    "plt.show()\n",
    "\n",
    "print(\"Predicted CAPTCHA Digit:\", prediction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31bb9e41-1998-4f61-a952-3fa02eb218e1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
