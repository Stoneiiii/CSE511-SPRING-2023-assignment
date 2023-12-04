# Import required libraries
# Do not install/import any additional libraries
import psycopg2
import psycopg2.extras
import json
import csv
import math 


# Lets define some of the essentials
# We'll define these as global variables to keep it simple
username = "postgres"
password = "postgres"
dbname = "assignment3"
host = "127.0.0.1"


def get_open_connection():
    """
    Connect to the database and return connection object
    
    Returns:
        connection: The database connection object.
    """

    return psycopg2.connect(f"dbname='{dbname}' user='{username}' host='{host}' password='{password}'")



def load_data(table_name, csv_path, connection, header_file):
    """
    Create a table with the given name and load data from the CSV file located at the given path.

    Args:
        table_name (str): The name of the table where data is to be loaded.
        csv_path (str): The path to the CSV file containing the data to be loaded.
        connection: The database connection object.
        header_file (str): The path to where the header file is located
    """

    cursor = connection.cursor()

    # Creating the table
    with open(header_file) as json_data:
        header_dict = json.load(json_data)

    table_rows_formatted = (", ".join(f"{header} {header_type}" for header, header_type in header_dict.items()))
    create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            {table_rows_formatted}
            )'''

    cursor.execute(create_table_query)
    connection.commit()


    # # TODO: Implement code to insert data here

    # with open(csv_path,'r') as f:
    #     data = csv.DictReader(f)

    #     for row in data:
    #         row_data=[]
    #         for key in row:
    #             if(row[key] == ''):
    #                 row_data.append(None)
    #             else:
    #                 row_data.append(row[key])

    #         psycopg2.extras.execute_values(cursor, f"INSERT INTO {table_name} VALUES %s", row_data, page_size=100000)

    with open(csv_path) as f:
        insert_sql = f"""COPY {table_name} FROM STDIN WITH (FORMAT CSV,HEADER true, NULL '', DELIMITER ',')""" 
        cursor.copy_expert(insert_sql, f)


    connection.commit()
    cursor.close()
    # raise Exception("Function yet to be implemented!")




def range_partition(data_table_name, partition_table_name, num_partitions, header_file, column_to_partition, connection):
    """
    Use this function to partition the data in the given table using a range partitioning approach.

    Args:
        data_table_name (str): The name of the table that contains the data loaded during load_data phase.
        partition_table_name (str): The name of the table to be created for partitioning.
        num_partitions (int): The number of partitions to create.
        header_file (str): path to the header file that contains column headers and their data types
        column_to_partition (str): The column based on which we are creating the partition.
        connection: The database connection object.
    """

    # TODO: Implement code to perform range_partition here
    
    # create partition table
    cursor = connection.cursor()

    with open(header_file) as json_data:
        header_dict = json.load(json_data)

    table_rows_formatted = (", ".join(f"{header} {header_type}" for header, header_type in header_dict.items()))
    create_partition_table_query = f'''
        CREATE TABLE IF NOT EXISTS {partition_table_name} (
            {table_rows_formatted}) 
            partition by range ({column_to_partition})'''

    cursor.execute(create_partition_table_query)
    connection.commit()

    # calculation min and max of created_utc
    cursor.execute(f"SELECT MIN({column_to_partition}) FROM {data_table_name}")
    min_val = cursor.fetchone()[0]
    cursor.execute(f"SELECT MAX({column_to_partition}) FROM {data_table_name}")
    max_val = cursor.fetchone()[0]
    
    # add partitions to partitioned table
    interval = math.ceil((max_val - min_val + 1)/num_partitions)
    lower_bound = min_val
    for i in range(num_partitions):
        cursor.execute(f'''create table {partition_table_name}{i}
                        partition of {partition_table_name}
                        for values from ({lower_bound}) to ({lower_bound + interval})''')
        connection.commit()
        lower_bound += interval

    # insert data
    cursor.execute(f"insert into {partition_table_name} select * from {data_table_name}")
    connection.commit()

    cursor.close()
    # raise Exception("Function yet to be implemented!")



def round_robin_partition(data_table_name, partition_table_name, num_partitions, header_file, connection):
    """
    Use this function to partition the data in the given table using a round-robin approach.

    Args:
        data_table_name (str): The name of the table that contains the data loaded during load_data phase.
        partition_table_name (str): The name of the table to be created for partitioning.
        num_partitions (int): The number of partitions to create.
        header_file (str): path to the header file that contains column headers and their data types
        connection: The database connection object.
    """

    # TODO: Implement code to perform round_robin_partition here

    #creat main partition table
    cursor = connection.cursor()

    with open(header_file) as json_data:
        header_dict = json.load(json_data)

    table_rows_formatted = (", ".join(f"{header} {header_type}" for header, header_type in header_dict.items()))
    table_rows_header = (", ".join(f"{header}" for header, header_type in header_dict.items()))
    
    create_main_partition_table_query = f'''
            CREATE TABLE IF NOT EXISTS {partition_table_name} (
                {table_rows_formatted}) 
             '''
    cursor.execute(create_main_partition_table_query)
    connection.commit()

    # creat partition table
    for i in range(num_partitions):
        create_partition_table_query = f'''
            CREATE TABLE {partition_table_name}{i} () INHERITS ({partition_table_name})
                '''
        cursor.execute(create_partition_table_query)
        connection.commit()

    # insert data
    cursor.execute(f"SELECT * FROM {data_table_name}")
    rows = cursor.fetchall()

    

    cur_partition_id = 0
    for row in rows:
        cur_table_name = partition_table_name + str(cur_partition_id)
        cursor.execute(f"INSERT INTO {cur_table_name}({table_rows_header}) VALUES %s", (row,))
        # psycopg2.extras.execute_values(cursor, f"INSERT INTO {cur_table_name} VALUES %s", row, page_size=100000)
        cur_partition_id = (cur_partition_id+1) % num_partitions
    
    connection.commit()


    # trigger

    #     计算每个partition的列数
    # cursor.execute(f"CREATE TABLE IF NOT EXISTS counts (name TEXT, count INTEGER)")
    # counts = []
    # for i in range(num_partitions):
    #     cursor.execute(f"SELECT count(*) FROM {partition_table_name}{i}")
    #     count = cursor.fetchone()[0]
    #     cursor.execute(f"INSERT INTO counts(name, count) VALUES ('{partition_table_name}{i}', {count})")
    #     # print(str(count)+ '----')
    # connection.commit()

    relocate_trigger_query = f'''CREATE OR REPLACE FUNCTION insert_trigger()
                                RETURNS TRIGGER AS $$
                                DECLARE 
                                    num integer;
						            table_name TEXT;
                                BEGIN
                                    select count(*) from {partition_table_name} into num;
                                    num := num%{num_partitions};
                                    table_name := '{partition_table_name}' || num;
                                    execute 'INSERT INTO ' || table_name || '({table_rows_header}) VALUES ($1.*)' USING NEW;
                                    RETURN NULL;
                                END;
                                $$
                                LANGUAGE plpgsql;
                                '''

    set_trigger_query = f'''
                        CREATE TRIGGER partition_insert_trigger
                        BEFORE INSERT ON {partition_table_name}
                        FOR EACH ROW EXECUTE FUNCTION insert_trigger();
                        '''
    
    cursor.execute(relocate_trigger_query)
    cursor.execute(set_trigger_query)
    connection.commit()
    cursor.close()
                            
    





    # raise Exception("Function yet to be implemented!")




def delete_partitions(table_name, num_partitions, connection):
    """
    This function in NOT graded and for your own testing convinience.
    Use this function to delete all the partitions that are created by you.

    Args:
        table_name (str): The name of the table containing the partitions to be deleted.
        num_partitions (int): The number of partitions to be deleted.
        connection: The database connection object.
    """

    # TODO: UNGRADED: Implement code to delete partitions here
    
    raise Exception("Function yet to be implemented!")

