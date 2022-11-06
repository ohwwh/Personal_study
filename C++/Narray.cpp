#include <iostream>

class Int;
class NthArray;

class NthArray
{
	int		n;
	int 	*size;
	void	*ret;

	class Int
	{
		void	*data;
		int		level;
		int		depth;
		
		public:
			Int(int lv, int depth){data = 0; level = lv; this->depth = depth;};
			operator int() {return (*static_cast<int *>(data));};
			void	set_data(void * address){data = address;};
			Int operator[](const int index)
			{
				/*if (level > depth)
				{
					std::cout << "error!" << std::endl;
					return (0);
				}*/
				Int ret(level + 1, depth);
				if (level == depth - 1)
					ret.set_data(static_cast<void *>(static_cast<int *>(data) + index));
				else
					ret.set_data(static_cast<void **>(data)[index]);
				return (ret);
			}
			Int& operator=(int a){*static_cast<int *>(data) = a; return (*this);}
	};
	public:
		NthArray(int n, int *size);
		void *init_addr(int n);
		void	delete_addr(int n, void **addr);
		void	print_2_array(void);
		Int operator[](const int index);
		~NthArray();
};

NthArray::Int NthArray::operator[](const int index)
{
	Int ret(1, n);
	ret.set_data(static_cast<void **>(this->ret)[index]);
	return (ret);
}

void *NthArray::init_addr(int n)
{
		void	**ret;
		int		*final_ret;

		if (n == this->n - 1)
		{
			final_ret = new int[size[n]];
			for (int i = 0; i < size[n]; i++)
				final_ret[i] =  0;
			return (static_cast<void *>(final_ret));
		}
		ret = new void*[size[n]];
		for (int i = 0; i < size[n]; i++)
			ret[i] =  init_addr(n + 1);
		return (static_cast<void *>(ret));
}

void NthArray::delete_addr(int n, void **addr)
{
	if (n == this->n - 2)
	{
		for (int i = 0; i < size[n]; i++)
			delete[] static_cast<int *>(addr[i]);
		return ;
	}
	for (int i=0; i < size[n]; i++)
	{
		delete_addr(n + 1, static_cast<void **>(addr[i]));
		delete[] static_cast<void **>(addr[i]);
	}
}

NthArray::NthArray(int n, int *size)
{
	this->n = n;
	this->size = new int[n];
	for (int i = 0; i < n; i ++)
		this->size[i] = size[i];
	ret = init_addr(0);
}

NthArray::~NthArray()
{
	delete_addr(0, static_cast<void **>(ret));
	delete[] size;
}

void NthArray::print_2_array(void)
{
	void	**temp;

	for (int i=0; i < size[0]; i ++)
	{
		temp = static_cast<void **>(ret);
		for (int j=0; j < size[1]; j ++)
		{
			std::cout << static_cast<int *>(temp[i])[j] << " ";
		}
		std::cout << std::endl;
	}
}

int main(void)
{
	int size[2] = {5, 5};
	NthArray array = NthArray(2, size);
	array[2][4] = 5;
	array.print_2_array();
	std::cout << array[2][4] << std::endl;
}