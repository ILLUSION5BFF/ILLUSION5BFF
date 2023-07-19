{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPb+YRDWP/E3POmO1WZe9w7",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ILLUSION5BFF/ILLUSION5BFF/blob/main/python_adventure_game.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 32,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 131
        },
        "id": "IRnfTK-LxvaZ",
        "outputId": "337f8a80-05c1-4c56-8cf8-c1d03fdaf2b3"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-32-5980906e250e>\"\u001b[0;36m, line \u001b[0;32m16\u001b[0m\n\u001b[0;31m    elif ans1 in answer_no:\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ],
      "source": [
        "answer_yes =[\"Yes\",\"Y\",\"yes\",\"y\"]\n",
        "answer_no = [\"No\",\"N\",\"no\",\"n\"]\n",
        "\n",
        "print(\"\"\"\n",
        "WELCOME! LET'S START THE ADVENTURE\n",
        "\n",
        "      You are standing outside of your house and you see a man running towards you and asks for urgent shelter.\n",
        "Will you provide shelter to him(Yes/No)\"\"\")\n",
        "\n",
        "ans1 = input(\">>\")\n",
        "\n",
        "if ans1 in answer_yes:\n",
        "  print(\"\\nAfter 2 minutes,the Police came to your house, and ask you whether the thief is in your house or not. Will you say Yes/No\\n\")\n",
        "ans2 = input(\">>\")\n",
        "\n",
        "elif ans1 in answer_no:\n",
        "  print(\"\\nYou helped a theif.Now, go to Jail. GAME OVER\")\n",
        "\n",
        "else:\n",
        "  print(\"\\nYou typed the wrong input. GOODBYE!\")\n",
        "\n",
        "ans2 = input(\">>\")\n",
        "\n",
        "if ans2 in answer_yes:\n",
        "  print(\"\\nYou are an honest person. He was a thief & you won the Game!\")\n",
        "ans3 = input(\">>\")\n",
        "\n",
        "elif ans2 in answer_no:\n",
        "print(\"\\nYou helped a theif.Now, go to Jail. GAME OVER\")\n",
        "\n",
        "else:\n",
        "print(\"\\nYou typed the wrong input. GOODBYE!\")\n",
        "elif ans1 in answer_no(\\nNow, he is trying to kill you.Will, you knock him down(Yes/No\\]n))\n",
        "\n",
        "  ans3 = input(\">>\")\n",
        "\n",
        "   if ans3 in answer_yes:\n",
        "    print(\"\\nCongrats! He was a thief & You helped the police to catch him with your bravery. \")\n",
        "  elifans3 in answer_no:(\"\\nSorry! You are dead. He was a thief & He killed you. GAME OVER\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "answer_yes = [\"Yes\", \"Y\", \"yes\", \"y\"]\n",
        "answer_no = [\"No\", \"N\", \"no\", \"n\"]\n",
        "\n",
        "print(\"\"\"\n",
        "WELCOME! LET'S START THE ADVENTURE\n",
        "\n",
        "      You are standing outside of your house and you see a man running towards you and asks for urgent shelter.\n",
        "Will you provide shelter to him (Yes/No)\"\"\")\n",
        "ans1 = input(\">>\")\n",
        "\n",
        "if ans1 in answer_yes:\n",
        "    print(\"\\nAfter 2 minutes, the Police came to your house and asked you whether the thief is in your house or not. Will you say Yes/No\\n\")\n",
        "    ans2 = input(\">>\")\n",
        "\n",
        "    if ans2 in answer_yes:\n",
        "        print(\"\\nYou are an honest person. He was a thief, and you won the Game!\")\n",
        "    elif ans2 in answer_no:\n",
        "        print(\"\\nYou helped a thief. Now, go to Jail. GAME OVER\")\n",
        "    else:\n",
        "        print(\"\\nYou typed the wrong input. GOODBYE!\")\n",
        "\n",
        "elif ans1 in answer_no:\n",
        "    print(\"\\nYou helped a thief. Now, go to Jail. GAME OVER\")\n",
        "\n",
        "else:\n",
        "    print(\"\\nYou typed the wrong input. GOODBYE!\")\n",
        "\n",
        "    if ans3 in answer_yes:\n",
        "        print(\"\\nCongrats! He was a thief, and you helped the police catch him with your bravery.\")\n",
        "    elif ans3 in answer_no:\n",
        "        print(\"\\nSorry! You are dead. He was a thief, and he killed you. GAME OVER\")\n",
        "    else:\n",
        "        print(\"\\nYou typed the wrong input. GOODBYE!\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zrGob1zfd5DD",
        "outputId": "decbc215-ef6a-4729-ba9b-cecfc66b4af7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "WELCOME! LET'S START THE ADVENTURE\n",
            "\n",
            "      You are standing outside of your house and you see a man running towards you and asks for urgent shelter.\n",
            "Will you provide shelter to him (Yes/No)\n"
          ]
        }
      ]
    }
  ]
}