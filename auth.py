{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "acb8f9c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dbc99edd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_credentials():\n",
    "\n",
    "    username = input('Enter your username: ')\n",
    "    password = input(f\"Enter your password: \")\n",
    "    \n",
    "    return username, password\n",
    "\n",
    "def read_passwdb(passwd):\n",
    "    with open('passwd.json', 'r') as pwdb_file:\n",
    "        jpwdb = json.load(pwdb_file)\n",
    "\n",
    "def write_passwdb(passwd):\n",
    "    with open('passwd.json', 'w') as pwdb_file:\n",
    "        json.dump(pwdb, pwdb_file)\n",
    "        \n",
    "def authenticate(username, password, pwdb):\n",
    "    if username in pwdb:\n",
    "        if password == pwdb[username]\n",
    "            return True\n",
    "        else:\n",
    "            return False\n",
    "    else:\n",
    "        return False\n",
    "\n",
    "        \n",
    "if __name__ == '__main__':\n",
    "    username, password = get_credentials()\n",
    "    pwdb = {username: password}\n",
    "    write_passwdb(pwdb)\n",
    "    \n"
   ]
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
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
