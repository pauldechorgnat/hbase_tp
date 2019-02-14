from happybase import Connection

if __name__ == '__main__':
    # creating a connection
    hbase_connection = Connection(host='localhost', port=9090)

    table_name = 't1'

    families_schema = {
        'cf1': dict(),
        'cf2': dict()
    }

    try :
        hbase_connection.create_table('test', families=families_schema)
    except :
        print('pas instantier la table')

    table = hbase_connection.table(table_name)

    data_to_put = {
        'cf1:c1': 'hello',
        'cf2:c1': 'world',
        'cf1:c2': '!'
    }

    table.put(row='r1', data=data_to_put)

    table.scan()

    hbase_connection.close()