from happybase import Connection
import json
import re

if __name__ == '__main__':
    # connection to thrift server
    connection = Connection(host='localhost', port=9090, autoconnect=True)

    # creating a table called tweets
    table_name = 'tweets'
    families_schema = {
        'metadata': dict(),
        'textdata': dict()
    }
    connection.create_table(name=table_name, families=families_schema)

    # connecting to the table
    table = connection.table(name=table_name)

    # opening the file containing tweets
    path = './tweets.json'
    with open(path, 'r') as tweet_file:
        data = json.load(tweet_file)

    # defining regular expressions
    pseudo_re = re.compile('\\@[a-zA-Z0-9_]*')
    hashtag_re = re.compile('\\#[a-zA-Z0-9_]*')

    # parsing data and putting it in hbase
    for index, tweet_data in enumerate(data):
        data_to_put = {
            'metadata:date': tweet_data['created_at'],
            'metadata:id': str(tweet_data['id']),
            'metadata:auhtor': tweet_data['user']['screen_name'],
            'textdata:text': tweet_data['text']
        }

        # dealing with hashtags
        for j, hashtag in enumerate(hashtag_re.findall(tweet_data['text'])):
            data_to_put['textdata:hashtag'+str(j)] = hashtag

        # dealing with pseudos
        for j, pseudo in enumerate(pseudo_re.findall(tweet_data['text'])):
            data_to_put['textdata:pseudo' + str(j)] = pseudo

        # putting data into the table
        table.put(row='row_id_' + str(index), data=data_to_put)

    connection.close()
