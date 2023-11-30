// Test the assignment5.cc file

#include "assignment5.hpp"
#include <iostream>

// Namespaces
using namespace std;
using namespace rocksdb;

string load_test(DB* db, const string& id, const string& head) {
    // string key1 = id + head;
    // string value1;
    // Status s = db->Get(ReadOptions(), key1, &value1);
    
    // Options options;
    // options.create_if_missing = true;
    // options.IncreaseParallelism();
    // Status s = DB::Open(options, db_path, &db);
    // assert(s.ok());
    string key1 = id + "_" + head;
    // cout << key1 << endl;
    string value1;
    Status s = db->Get(ReadOptions(), key1, &value1);
    assert(s.ok());
    
    //string value2;
    //s = db->Get(ReadOptions(), "2qh1q", &value2);
    //assert(s.ok());
    //cout << "2qh1q :" << value2 << endl;
    return value1;
}

bool delete_test(DB* db, const string& key) {
    string value1;
    Status s = db->Get(ReadOptions(), key, &value1);
    if(!s.ok()) {
        return true;
    }
    return false;
}


int main() {

    // 0. set up the paths
    // Do not change these paths
    const std::string csv_file_path = "subreddits.csv";
    const std::string db_path = "./test/subreddits_rdb";

    // create the KVS
    rocksdb::DB* db = create_kvs(csv_file_path, db_path);
    if (db != nullptr) {
        cout << "RocksDB may be created successfully from CSV file." << std::endl;
    } else {
        cout << "Failed to create RocksDB from CSV file." << std::endl;
    }
    //my test for loading data
    cout << "---My test for loading start!---" << endl;
    string id = "2qim4";
    string header = "display_name";
    string res = load_test(db, id, header);
    string res2 = load_test(db, "2476", "banner_background_image");
    if(res == "blender" && res2 == "") {
        cout << "    load pass!!!" << endl;
    }else {
        cout << "    laod fail" << endl;
    }
 
    //cout << "****" << res2 << endl;



    // multi get
    vector<string> multi_get_keys = {"2qh1r_display_name", "2qh1k_display_name", "2qh1a_display_name", "2qh1b_display_name"};
    vector<string> multi_get_results = multi_get(db, multi_get_keys);
    
    // Convert the vector of keys to a vector of Slice objects
    for (auto result : multi_get_results) {
        // You should see the display_name of the subreddit
        // One display_name per line because of endl
        cout << result << endl;
    }
    //my test
    cout << "---My test for multi get start!---" << endl;
    vector<string> ans = {"auto", "productivity", "linux", "microsoft"};
    for(unsigned int i = 0; i < ans.size(); i++) {
        if(ans[i] != multi_get_results[i]) {
            cout << "      multi get fail" << endl;
            break;
        }
    }
    cout << "      multi get pass!!!" << endl;


    // iterate over range of keys
    // Only return the display_name of the subreddit
    vector<string> results = iterate_over_range(db, "2qh0x", "2qh1q");
    /*
u_Rachello10
u_BelatedBanoffee
u_Wistom444
u_Rabexio
u_NetflixOrigina1
BootyfulWomen
u_Glassmannc
    */
    //vector<string> results = iterate_over_range(db, "2cc2oz", "2cc4dl");
    for (auto result : results) {
        // You should see the display_name of the subreddit
        // One display_name per line because of endl
        cout << result << endl;
        
    }


    // delete a particular key
    Status s = delete_key(db, "2cneq_id");
    // You should see "Maybe successfully deleted key." if the key was deleted and your code is correct
    if (s.ok()) {
        cout << "Maybe successfully deleted key." << endl;
    } else {
        cout << "Failed to delete key." << endl;
    }

    // Implementing your own tests is highly recommended!!
    cout << "---My test for delete start!---" << endl;
    bool flag = delete_test(db, "2cneq_id");
    if(flag) {
        cout << "      delete pass!!!" << endl;
    }else {
         cout << "      delete fail" << endl;
    }
    delete db;

    return 0;
}

