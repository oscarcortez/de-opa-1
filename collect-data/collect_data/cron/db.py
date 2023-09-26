{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "import psycopg2\n",
    "import uuid\n",
    "\n",
    "host = localhost\n",
    "dbname = 'opa_binance'\n",
    "user = 'postgres'\n",
    "password = '123456'\n",
    "\n",
    "def save_data(data):\n",
    "    print(datetime.datetime.now())\n",
    "    print('Amount of currencies: ' + str(len(data)))\n",
    "\n",
    "    con = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port='5432')\n",
    "    con.autocommit = True\n",
    "    cur = con.cursor()\n",
    "\n",
    "    now = datetime.datetime.now()\n",
    "\n",
    "    for item in data:\n",
    "        cur.execute('''INSERT INTO \"Tickers\" (\"Id\", \"Symbol\", \"Price\", \"DateTime\") VALUES (%s, %s, %s, %s)''', (str(uuid.uuid4()), item[\"symbol\"], item[\"price\"], now))\n",
    "\n",
    "    con.commit()\n",
    "    con.close()"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
