{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "cae8fedc-9d21-4f9e-9749-53ef9396a7eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PROJECT_ROOT: C:\\Users\\Kartavya\\bootcamp_Kartavya_Joshi\\homework\\homework\\homework2\\src\n",
      "DATA_DIR: C:\\Users\\Kartavya\\bootcamp_Kartavya_Joshi\\homework\\homework\\homework2\\src\\data\n"
     ]
    }
   ],
   "source": [
    "import os,pathlib\n",
    "from typing import Optional\n",
    "from pathlib import Path\n",
    "\n",
    "def get_key(name: str, default: Optional[str] = None) -> Optional[str]:\n",
    "    return os.getenv(name, default)\n",
    "\n",
    "# PROJECT_ROOT = Path.cwd()\n",
    "# DATA_DIR = PROJECT_ROOT / \"data\"\n",
    "# print(\"PROJECT_ROOT:\", PROJECT_ROOT)\n",
    "# print(\"DATA_DIR:\", DATA_DIR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f937d17-52fe-4de0-a65e-7f92549697b5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python(Fe-course_env)",
   "language": "python",
   "name": "fe-course"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
