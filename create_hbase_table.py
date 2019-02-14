from happybase import Connection
import pprint

if __name__ == '__main__':

    # creating a connection with HBase
    hbase_connection = Connection(host='localhost', port=9090, autoconnect=True)

    # name of the table to create
    table_name = 'animals'

    # printing out the tables in HBase
    tables = hbase_connection.tables()
    print('Current tables :')
    print(tables)

    # column families to create
    families_schema = {
        'id': dict(),  # keeping default parameters
        'features': dict()  # keeping default parameters
    }
    # Creating a table
    hbase_connection.create_table(table_name, families=families_schema)

    # printing out the tables in HBase
    tables = hbase_connection.tables()
    print('Current tables :')
    print(tables)

    # getting access to the table
    table = hbase_connection.table(table_name)

    # flipper
    data_for_flipper = {
        'id:name': 'flipper',
        'features:race': 'dolphin',
        'features:gender': 'male',
        'features:apnea': 10
    }

    # lassie
    data_for_lassie = {
        'id:chip_number': 314,
        'id:name': 'lassie',
        'features:race': 'colley',
        'features:gender': 'female'
    }

    # gary
    data_for_gary = {
        'id:name': 'gary',
        'features:race': 'snail'
    }

    # putting data into the table
    table.put(row='1', data=data_for_lassie)
    table.put(row='2', data=data_for_flipper)
    table.put(row='3', data=data_for_gary)

    # printing out the content of the table
    for data in table.scan():
        pprint.pprint(data)

    # closing hbase connection
    hbase_connection.close()
