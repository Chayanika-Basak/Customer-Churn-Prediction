from pandas import *
import sqlalchemy as sqa

database_connection=sqa.create_engine('sqlite:///students.db')
df=read_sql_query('select * from student;', database_connection)
df.head()