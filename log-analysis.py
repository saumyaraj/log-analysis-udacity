import psycopg2

# What are the three most popular articles of all time?
popular_articles = """select a.title,count(*) as views from articles a left
             join log l on l.path = '/article/' || a.slug group by a.title
             order by views desc limit 3;"""

# Who are the most popular article authors of all time?
popular_authors = """select u.name,count(*) as views
             from articles a, log l,authors
             u where l.path = '/article/' || a.slug and
             u.id = a.author group by
             u.name order by views desc;"""

# On which day did more than 1% of requests lead to errors?
error_days = """select d.day, ROUND((r*100)/cast((r+e)as decimal), 2)
             as per from (select Date(time) as day,status,count(*) as e from
             log group by DATE(time),status) as d, (select Date(time) as
              day,status,count(*) as r from
              log group by DATE(time),status) as f
              where d.day = f.day and d.status < f.status
              group by d.day,f.r,d.e
              having ((r::float*100/(r+e)::float)) > 1;"""


# Query data from the database, open and close the connection
def fetchData(query):
    connection = psycopg2.connect(database="news")
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results


# Print the top three articles of all time
def get_popular_articles():
    results = fetchData(popular_articles)
    print_output("The three most popular articles of all time are:")
    for article, views in results:
        print(" \"{}\" -- {} views".format(article, views))


# Print the top authors of all time
def get_popular_authors():
    results = fetchData(popular_authors)
    print_output("The most popular article authors of all time are:")
    for author, views in results:
        print(" {} -- {} views".format(author, views))


# Print the days in which there were more than 1% bad requests
def get_error_days():
    results = fetchData(error_days)
    print_output("Days on which more than 1% of requests lead to errors are:")
    for day, percentage_errors in results:
        print("{0:%B %d, %Y} -- {1:.2f} % errors"
              .format(day, percentage_errors))


# Writing each output on new line
def print_output(output):
    print("\n" + output)


if __name__ == '__main__':
    get_popular_articles()
    get_popular_authors()
    get_error_days()
