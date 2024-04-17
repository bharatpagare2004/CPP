#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include<iostream>
using namespace std;

// Function to accept data and write it to the file
void acceptData(const string& filename) {
    ofstream file(filename, std::ios::app);
    if (!file) {
        std::cerr << "Error opening file!" << std::endl;
        return;
    }

    string data;
    cout << "Enter data (type 'end' to stop):" << endl;
    while (true) {
        std::getline(std::cin, data);
        if (data == "end") break;
        file << data << std::endl;
    }
    file.close();
}

// Function to display the data from the file
void displayData(const std::string& filename) {
    std::ifstream file(filename);
    if (!file) {
        std::cerr << "Error opening file!" << std::endl;
        return;
    }

    std::string line;
    std::cout << "Data in the file:" << std::endl;
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }
    file.close();
}

// Function to delete data from the file
void deleteData(const std::string& filename) {
    std::ofstream file(filename, std::ofstream::out | std::ofstream::trunc);
    if (!file) {
        std::cerr << "Error opening file!" << std::endl;
        return;
    }
    file.close();
    std::cout << "Data deleted successfully from " << filename << std::endl;
}

int main() {
    std::string filename = "data.txt";

    // Accept data and write it to the file

    while(true)
    {
   int ch ;
    cout<<"enter the choice:";
    cin>>ch;



    switch(ch)
    {

    case 1 :acceptData(filename);
    break;

    // Display data from the file
    case 2:displayData(filename);
    break;


    // Delete data from the file
    case 3:deleteData(filename);
    break;

    }

    }
    return 0;
}
