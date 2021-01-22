{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Copy of Untitled3.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPHBK1FkaN3HL9yuP2oIR0s",
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
        "<a href=\"https://colab.research.google.com/github/Janu-dot/Janani/blob/main/N%20numbers%20in%20while%20loop.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r3rWpDtL9EaY",
        "outputId": "2eef37fe-aa7b-4a60-9cc7-bb08cce9acb2"
      },
      "source": [
        "n=int(input(\"enter a number:\"))\r\n",
        "fact = 1\r\n",
        "while(n>=2):\r\n",
        "  fact = fact*n\r\n",
        "  n-=1\r\n",
        "  print(\"Factorial:\",fact)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "enter a number:9\n",
            "Factorial: 9\n",
            "Factorial: 72\n",
            "Factorial: 504\n",
            "Factorial: 3024\n",
            "Factorial: 15120\n",
            "Factorial: 60480\n",
            "Factorial: 181440\n",
            "Factorial: 362880\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}