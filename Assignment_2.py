#Covid riski var mi yok mu bakar
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Assignment - 2 (Covid-19)\n",
    "Are you a cigarette addict older than 75 years old? Variable → age\n",
    "\n",
    "Do you have a severe chronic disease? Variable → chronic\n",
    "\n",
    "Is your immune system too weak? Variable → immune\n",
    "\n",
    "Set a logical algorithm using boolean logic operators (and/or) and use if-statements with the given variables in order to print out us a message : \"You are in risky group\"(if True ) or \"You are not in risky group\" (if False)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "cigarette = input(\"Are you a cigarette addict older than 75 years old? (Yes/No)\").title().strip()\n",
    "chronic = input(\"Do you have a severe chronic disease? (Yes/No)\").title().strip()\n",
    "immune = input(\"Is your immune system too weak? (Yes/No)\").title().strip()\n",
    "risk = bool(cigarette == \"Yes\" or chronic == \"Yes\" or immune == \"Yes\")\n",
    "if risk:\n",
    "    print(\"You are in risky group\")\n",
    "else:\n",
    "    print(\"You are not in risky group\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
