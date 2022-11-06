#include <iostream>

class date{
	int _year;
	int _month;
	int _day;

	public:
		//void SetDate(int year, int month, int date);
		void AddDay(int inc);
		void Addmonth(int inc);
		void AddYear(int inc);
		void ShowDate();

		date(int year, int month, int date)
		{
			_year = year;
			_month = month;
			_day = date;
		}

		void SetDate(int year, int month, int date)
		{
			_year = year;
			_month = month;
			_day = date;
		}
};

void date::ShowDate()
{
	std::cout << "오늘은" << _year << "년" << _month << "월" << _day << "일입니다" <<std::endl;
}

int main()
{
	date *ndate = new date(2022,6,16);
	date n1date = date(2022,6,16);
	date *mdate = (date *)malloc(sizeof(date));
	mdate->ShowDate();
}