{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Copy of Untitled4.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPWVD3dhYvPgKa+giZQAFh+",
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
        "<a href=\"https://colab.research.google.com/github/Janu-dot/Janani/blob/main/Remove%20Empty%20list.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KnmYj41oXwmj",
        "outputId": "c3860f71-723d-4d6e-faa3-3fdcd01432c2"
      },
      "source": [
        " \n",
        "test_list = [3, 6, [], 9, [], [], 12] \n",
        "  \n",
        "  \n",
        "print(\"The original list is : \" + str(test_list)) \n",
        "  \n",
        "res = [ele for ele in test_list if ele != []] \n",
        "  \n",
        " \n",
        "print (\"List after empty list removal : \" + str(res))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "The original list is : [3, 6, [], 9, [], [], 12]\n",
            "List after empty list removal : [3, 6, 9, 12]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "L6osCPCQYLoi"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vdzdsNbpYSPW"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}