{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPPvVgcxWqsgdWGX7b21x12"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "data_type=[('name','S15'),('class',int),('height',float)]\n",
        "student_details=[('Nivaan',5,52.4),('Prithvi',6,37.9),('Rivaan',9,85.2),('Bhadra',6,67.8)]\n",
        "\n",
        "students=np.array(student_details, dtype=data_type)\n",
        "print(\"orignal array\",students)\n",
        "print(f\"sort by height: {np.sort(students,order='height')}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "02ytFSgI3zlM",
        "outputId": "f2ce2d77-5166-4864-db25-d29f5c4e6e17"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "orignal array [(b'Nivaan', 5, 52.4) (b'Prithvi', 6, 37.9) (b'Rivaan', 9, 85.2)\n",
            " (b'Bhadra', 6, 67.8)]\n",
            "sort by height: [(b'Prithvi', 6, 37.9) (b'Nivaan', 5, 52.4) (b'Bhadra', 6, 67.8)\n",
            " (b'Rivaan', 9, 85.2)]\n"
          ]
        }
      ]
    }
  ]
}