#include <iostream>

int main(int argc, char** argv)
{
    std::cout << "Hello GitHub Actions" << std::endl;
    std::cout << "Passed Arguments Are: " << std::endl;
    for(int i = 0; i < argc; i++)
    {
        std::cout << "Arg[" << i << "]: " << argv[i] << std::endl;  
    }
    return 0;
}