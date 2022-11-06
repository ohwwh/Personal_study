class Complex{
	double	real, img;

	public:
	Complex(double real, double img): real(real), img(img){}
	Complex operator+(const Complex& c) const;
	Complex operator-(const Complex& c) const;
	Complex operator*(const Complex& c) const;
	Complex operator/(const Complex& c) const;
	Complex& operator=(const Complex& c);
};

Complex Complex::operator+(const Complex& c) const{
	Complex temp(real + c.real, img + c.img);
	return (temp);
}

Complex Complex::operator-(const Complex& c) const{
	Complex temp(real - c.real, img - c.img);
	return (temp);
}

Complex Complex::operator*(const Complex& c) const{
	Complex temp(real * c.real - img * c.img, real * c.img + img * c.real);
	return (temp);
}

Complex Complex::operator*(const Complex& c) const{
	Complex temp(
		(real * c.real + img * c.img) / (c.real * c.real + c.img * c.img),
    	(img * c.real - real * c.img) / (c.real * c.real + c.img * c.img)
	);
	return (temp);
}

Complex& Complex::operator=(const Complex& c)
{
	real = c.real;
	img = c.img;
	return *this;
}