{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python: 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)]\n",
      "Pandas: 0.23.4\n",
      "Matplotlib: 3.0.0\n",
      "Seaborn: 0.9.0\n",
      "Scipy: 1.1.0\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "import numpy\n",
    "import pandas\n",
    "import matplotlib\n",
    "import seaborn\n",
    "import scipy\n",
    "print('Python: {}'.format(sys.version))\n",
    "print\n",
    "('Numpy: {}'.format(numpy.__version__))\n",
    "print('Pandas: {}'.format(pandas.__version__))\n",
    "print('Matplotlib: {}'.format(matplotlib.__version__))\n",
    "print('Seaborn: {}'.format(seaborn.__version__))\n",
    "print('Scipy: {}'.format(scipy.__version__))\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['id', 'type', 'name', 'yearpublished', 'minplayers', 'maxplayers',\n",
      "       'playingtime', 'minplaytime', 'maxplaytime', 'minage', 'users_rated',\n",
      "       'average_rating', 'bayes_average_rating', 'total_owners',\n",
      "       'total_traders', 'total_wanters', 'total_wishers', 'total_comments',\n",
      "       'total_weights', 'average_weight'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "data = pd.read_csv('board_games.csv')\n",
    "print(data.columns)\n"
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
