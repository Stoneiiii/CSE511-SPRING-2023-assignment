// 4 major tasks using rocksdb
// 1. Read the file comments.csv and create a kvs using id+column name as key and value as the value of the column (Put)
// 2. Write a function that performs a range query on the kvs to get all the comments for a given post id (Get)
// 3. A function that explored the iterator in rocksdb to get all the comments for a given post id (Get)
// 4. A function that deletes a particular comment from the kvs (Delete)

// General Libraries
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "csv.hpp"

// RocksDB Libraries
#include <rocksdb/db.h>
#include <rocksdb/options.h>


// Namespaces
using namespace std;
using ROCKSDB_NAMESPACE::DB;
using ROCKSDB_NAMESPACE::DBOptions;
using ROCKSDB_NAMESPACE::Options;
using ROCKSDB_NAMESPACE::Status;
using ROCKSDB_NAMESPACE::WriteBatch;
using ROCKSDB_NAMESPACE::WriteOptions;
using ROCKSDB_NAMESPACE::ReadOptions;
using ROCKSDB_NAMESPACE::Slice;


// Function to create a kvs
DB* create_kvs(const string& csv_file_path, const string& db_path) {

    // Open the csv file
    csv::CSVReader reader(csv_file_path);
    csv::CSVRow row;

    // Get the headers
    vector<string> header = reader.get_col_names();

    #if 0
        /* Something that can help figure out some of the parsing through the data
        To print, you need to implement the main function and add a new rule to the Makefile
        However, just going over the general logic of this code block should be helpful 
        in addition to the documentation of csv.hpp */
        int col_no = 0;
        for (csv::CSVRow& row : reader) {
            col_no = 0;
            //cout << "ID: " << row["col_name"] << endl;
            for (csv::CSVField& field : row) {
                //cout << "!!!!!!" << typeid(row["id"]).name() << "\n+++++\n"<< typeid(header[col_no]).name() << endl;
                string key = row["id"].get<string>() + "_" + header[col_no];
                string value = row["id"].get<string>() + "_" + field.get<string>();
                cout << "!!!key: "<< key << endl;
                cout << "!!!value: "<< value << endl;
                //cout << header[col_no]  << ": " << field.get<string>() << endl;
                col_no++;
            }

            break;
            
            
        }
    #endif

    DB* db;
    // Options options;

    // Status s = DB::Open(options, db_path, &db);
    // {
    //     WriteBatch batch;
    //     batch.Put("key2", value);
    //     s = db->Write(WriteOptions(), &batch);
    // }
    // delete db;

    Options options;
    options.create_if_missing = true;
    options.IncreaseParallelism();
    Status s = DB::Open(options, db_path, &db);
    assert(s.ok());
   
    int col_no = 0;
    int n = 0;
    for (csv::CSVRow& row : reader) {
        col_no = 0;
        for (csv::CSVField& field : row) {
            string key = row["id"].get<string>() + "_" + header[col_no];
            string value = field.get<string>();
            // cout << "!!!key: "<< key << endl;
            // cout << "!!!value: "<< value << endl;
            s = db->Put(WriteOptions(), key, value);
            assert(s.ok());
            col_no++;
        }
        n++;
    }
    //cout << "!!!col_no: "<< col_no << endl;
    //cout << "!!!n: "<< n << endl;

    return db;
}


// Function to perform a MultiGet operation
vector<string> multi_get(DB* db, const vector<string>& keys) {
    vector<string> values;

    vector<Slice> newkeys;
    for(unsigned int i = 0; i < keys.size(); i++) {
        newkeys.push_back(keys[i]);
    }

    db->MultiGet(ReadOptions(), newkeys, &values);



    return values;
}

// Function to iterate over a range of keys and return the corresponding values
vector<string> iterate_over_range(DB* db, const string& start_key, const string& end_key) {
    vector<string> result;

    string key_s = start_key + "_display_name";
    //string key_s = start_key;
    string key_e = end_key + "_display_name";
    //string key_e = end_key;
    string::size_type idx;
    auto iterator = db->NewIterator(ReadOptions());
    

    for(iterator->Seek(key_s); iterator->Valid() && iterator->key().ToString() < key_e; iterator->Next()) {
        idx = iterator->key().ToString().find("_display_name");
        if(idx != string::npos) {
            result.push_back(iterator->value().ToString());
            //cout << "!!!result :" << iterator->value().ToString() << endl;
        }
    }




    assert(iterator->status().ok());
    delete iterator;
    return result;
}

// Function to delete a particular comment from the kvs
Status delete_key(DB* db, const string& key) {
    Status s;

    s = db->Delete(WriteOptions(), key);
    assert(s.ok());
    return s;
}



