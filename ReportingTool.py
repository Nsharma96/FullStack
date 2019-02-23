#!/usr/bin/env python2
import psycopg2
import pandas as pd
pd.set_option("display.colheader_justify","center")
dbname = "news"
def execute_q(q):
    db = psycopg2.connect(database=dbname)
    c=db.cursor()
    c.execute(q)
    return c.fetchall()
    db.close()

#The most popular three articles of all time.
result1 = execute_q("""select articles.title, artiView.num from articles , (select path , count(path) as num from log where status like '%200%' group by path order by num desc limit 4) as artiView  where '/article/' || articles.slug = artiView.path order by artiView.num desc;""")

#The most popular article authors of all time.
result2 =  execute_q("""select authors.name,authorViewSums.authorView from authors,authorViewSums where authors.id=authorViewSums.author""")

#Days on which more than 1% of requests lead to errors.
result3 =  execute_q("""select d as Day,m as Month,y as Year from error_Matrix where (err*1.0/total_Requests)*100>1;""")

def print_q(res):
    for row in res:
        for i in range(len(row)):
            print(row[i],)

print("\nThe most popular three articles of all time.\n")
res = pd.DataFrame(data=result1,columns=['Article', 'Views'])
print(res)
print("\n")
print("The most popular article authors of all time.\n")
res = pd.DataFrame(data=result2,columns=['Author', 'Views'])
print(res)
print("\n")
print("Days on which more than 1 percent of requests lead to errors.\n")
res = pd.DataFrame(data=result3,columns=['Day', 'Month', 'Year'])
res=res.astype(int)
print(res)
print("\n")


