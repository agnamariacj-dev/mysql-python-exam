import mysql.connector
class library_management:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Agna",
                database="library_management"
            )
            print(self.con)
        except:
            print("Database connection failed")
    def create(self,title,author,category,total_copies,available_copies):
        try:
            cursor=self.con.cursor()
            query="insert into books(title,author,category,total_copies,available_copies) values(%s,%s,%s,%s,%s)"
            data=(title,author,category,total_copies,available_copies)
            cursor.execute(query,data)
            self.con.commit()
            print("Book added successfully")
        except:
            print("Failed to Add book")
    def read(self):
        try:
            cursor=self.con.cursor()
            query="select * from books"
            cursor.execute(query)
            records=cursor.fetchall()
            if records:
                for row in records:
                    print(row)
            else:
                print("No books available")
        except:
            print("Failed to read books")
    def retrieve(self,book_id):
        try:
            cursor=self.con.cursor()
            query="select * from books where book_id=%s"
            data=(book_id,)
            cursor.execute(query,data)
            records=cursor.fetchone()
            if records:
               print(records)
            else:
                print("No book found with ID",book_id)
        except:
            print("Failed to retrieve book")
    def update(self,book_id,available_copies):
        try:
            cursor=self.con.cursor()
            query="update books set available_copies=%s where book_id=%s"
            data=(available_copies,book_id)
            cursor.execute(query,data)
            self.con.commit()
            if cursor.rowcount>0:
                print("Book ID:",book_id,"updated successfully")
            else:
                print("No book found with id:",book_id,"to update")
        except:
            print("Failed to update")
    def delete(self,book_id):
        try:
            cursor=self.con.cursor()
            query="delete from books where book_id=%s"
            data=(book_id,)
            cursor.execute(query,data)
            self.con.commit()
            if cursor.rowcount>0:
                print("Book",book_id,"deleted successfully")
            else:
                print("No book found with id:",book_id,"to delete")
        except:
            print("Failed to delete")
    def summary(self):
        try:
            cursor=self.con.cursor()
            query="select count(*),sum(available_copies),Avg(total_copies) from books"
            cursor.execute(query)
            records=cursor.fetchone()
            if records:
                print("Total books:",records[0])
                print("available copies:",records[1])
                print("avg of total copies:", records[2])
            else:
                print("No records found")
        except:
            print("Summary Not available")
l=library_management()
while(True):
    print("LIBRARY MANAGEMENT")
    print("1.Add Book")
    print("2.View Available Books")
    print("3.Search Book")
    print("4.Update Available Copies")
    print("5.Delete Book")
    print("6.Libray Summary")
    print("7.Exit")
    ch=int(input("Enter your choice(1-7):"))
    if ch==1:
        t=input("Enter Title:")
        a=input("Enter author:")
        c=input("Enter category:")
        t_copies=int(input("Enter total copies:"))
        a_copies=int(input("Enter available copies:"))
        l.create(t,a,c,t_copies,a_copies)
    elif ch==2:
        l.read()
    elif ch==3:
        i=int(input("Enter id:"))
        l.retrieve(i)
    elif ch==4:
        i=input("Enter id:")
        a_copies=int(input("Enter available copies:"))
        l.update(i,a_copies)
    elif ch==5:
        i=int(input("Enter id:"))
        l.delete(i)
    elif ch==6:
        l.summary()
    elif ch==7:
        exit()
    else:
        print("Invalid Input")
