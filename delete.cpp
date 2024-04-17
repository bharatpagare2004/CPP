#include <iostream>
#include <fstream>

void deleteFileContent(const std::string& bharat1) {
    // Open the file in write mode with truncation flag
    std::ofstream file("bharat.txt", std::ios::trunc);

    if (!file) {
        std::cerr << "Error opening file!" << std::endl;
        return;
    }

    // Close the file
    file.close();

    std::cout << "Content deleted successfully from " << bharat1 << std::endl;
}

int main() {

    
    std::string bharat1 = "delete1.txt";

    // Call the function to delete content from the file
    deleteFileContent(bharat1);

    return 0;
}
