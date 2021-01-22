{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Copy of Copy of Untitled",
      "provenance": [],
      "authorship_tag": "ABX9TyNLtal/5Du1cQfWBtIDD5uJ",
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
        "<a href=\"https://colab.research.google.com/github/Janu-dot/Janani/blob/main/FACTORIAL.PY\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zzpJcSh87YWp",
        "outputId": "b37ca90a-2d91-4df5-c2a9-2ad190695b17"
      },
      "source": [
        "num=int(input(\"Enter a number:\"))\r\n",
        "fact=1\r\n",
        "for i in range (1,num+1):\r\n",
        "  fact=fact*i\r\n",
        "  print(\"The factorial of a number is :\",fact)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter a number:9\n",
            "The factorial of a number is : 1\n",
            "The factorial of a number is : 2\n",
            "The factorial of a number is : 6\n",
            "The factorial of a number is : 24\n",
            "The factorial of a number is : 120\n",
            "The factorial of a number is : 720\n",
            "The factorial of a number is : 5040\n",
            "The factorial of a number is : 40320\n",
            "The factorial of a number is : 362880\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}