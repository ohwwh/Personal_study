#include <iostream>

class Parent{
	public:
		Parent()
		{
			//Do();
		}
		virtual void what(){
			std::cout << "This is Parent" << std::endl;
		}
		~Parent(){
			//std::cout << "Parent deleted" << std::endl;
		}
		void Parent_only()
		{
			std::cout << "Parent only!!" << std::endl;
		}
		virtual void Do() { std::cout << "Parent Do" << std::endl; }
};

class Child : public Parent{
	public: 
		Child()
		{
			Do();
		}
		void what(){
			std::cout << "This is Child" << std::endl;
		}
		~Child(){
			//std::cout << "Child deleted" << std::endl;
		}
		void Child_only()
		{
			std::cout << "Child only!!" << std::endl;
		}
		virtual void Do() { std::cout << "Child Do" << std::endl; }
};

int main(void)
{
	Parent *p = new Child();
	//Parent parent = Child();
	//Child child = Child();
	//Parent& r = child;
	//p->what();
	//parent.what();
	//r.what();
	delete p;
}