#include <iostream>
#include <string.h>

class MyString {
	char	*content;
	int		string_length;
	int		mem;

	public:

	MyString(char c);
	MyString(const char* str);
	MyString(const MyString& str);
	~MyString();
	int length() const;
	void print() const;
	MyString& assign(const MyString& string);
	MyString& assign(const char *string);
	int	capacity() const;
	void reserve(int size);
	char at(int i) const;
	int compare(MyString& str);
	bool operator==(MyString& str);
};

MyString::MyString(char c){
	content = new char[1];
	content[0] = c;
	string_length = 1;
	mem = 1;
}

MyString::MyString(const char *str){
	string_length = strlen(str);
	mem = string_length;
	content = new char[string_length];
	for (int i = 0; i < string_length; i ++)
		content[i] = str[i];
}

MyString::MyString(const MyString& str){
	string_length = str.string_length;
	mem = string_length;
	content = new char[string_length];
	for (int i = 0; i < string_length; i ++)
		content[i] = str.content[i];
}

MyString::~MyString(){
	delete [] content;
}

int MyString::length() const{
	return (string_length);
}

void MyString:: print() const{
	std::cout << content << std::endl;
}

MyString& MyString::assign(const MyString& string){
	if (string_length < string.mem){
		delete [] content;
		content = new char[string.string_length];
		mem = string.mem;
	}
	for (int i = 0; i < string.string_length; i ++)
		content[i] = string.content[i];
	string_length = string.string_length;
	return *this;
}

MyString& MyString::assign(const char *string){
	int	new_len = strlen(string);

	if (string_length < new_len){
		delete [] content;
		content = new char[new_len];
		mem = new_len;
	}
	for (int i = 0; i < new_len; i ++)
		content[i] = string[i];
	string_length = new_len;
	return *this;
}

int	MyString::capacity() const{
	return (mem);
}

void MyString::reserve(int size){
	char	*del;

	if (string_length < size){
		del = content;
		content = new char[size];
		mem = size;
		for (int i = 0; i < string_length; i ++)
			content[i] = del[i];
		delete [] del;
	}
}

char MyString::at(int i) const{
	if (i >= string_length || i < 0)
		return ('\0');
	return (content[i]);
}

int MyString::compare(MyString& str) {
	for (int i = 0; i < std::min(string_length, str.string_length); i++) {
		if (content[i] > str.content[i])
			return 1;
		else if (content[i] < str.content[i])
			return -1;
	}
	if (string_length == str.string_length)
		return 0;
	else if (string_length > str.string_length)
		return 1;
	return -1;
}

bool MyString::operator==(MyString& str){
	return (!compare(str));
}

int main(void)
{
	MyString str1("Hello World!");
	str1.print();
	std::cout << str1.length() << std::endl;
	str1.assign("World Hello!");
	str1.print();
	std::cout << str1.capacity() << std::endl;
	str1.reserve(25);
	std::cout << str1.capacity() << std::endl;;
	std::cout << str1.at(0);
}