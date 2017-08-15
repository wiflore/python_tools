import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='database1_udemy' user='postgres' password='postgres123' "
                            "host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.5)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1_udemy' user='postgres' password='postgres123' "
                            "host='localhost' port='5432'")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()


#insert("Wine Glass",10,5)
#insert("Wine Glass2",23,2)


def view():
    conn = psycopg2.connect("dbname='database1_udemy' user='postgres' password='postgres123' "
                            "host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


#print(view())


def delete(item):
    conn = psycopg2.connect("dbname='database1_udemy' user='postgres' password='postgres123' "
                            "host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()


#delete("Wine Glass")
#print(view())


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database1_udemy' user='postgres' password='postgres123' "
                            "host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price,item))
    conn.commit()
    conn.close()


create_table()
insert("Orange", 9, 13)
print(view())
delete("Wine Glass")
print(view())
update(20, 38, 'Orange')
print(view())
#update(11, 6, "Wine Glass2")
#print(view())