{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled8.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyN2SbLEf90LbAXj+X2HjyVX",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Janu-dot/Janani/blob/main/dictionary.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "icog1EUSziGy",
        "outputId": "8605969f-45a2-49bb-a51a-e5c245e1847e"
      },
      "source": [
        " \n",
        "keys = ['a','b','c','d','e'] \n",
        "values = [1,2,3,4,5]   \n",
        "  \n",
        "# but this line shows dict comprehension here   \n",
        "myDict = { k:v for (k,v) in zip(keys, values)}   \n",
        "  \n",
        "# We can use below too \n",
        "# myDict = dict(zip(keys, values))   \n",
        "  \n",
        "print (myDict)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}