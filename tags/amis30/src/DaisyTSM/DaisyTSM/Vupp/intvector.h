

class CIntVector  
{


public:
	// Functions
	CIntVector(int vecValuei);
	virtual ~CIntVector();
	long size();
	void push_back(int vali); // L�gg p� ett v�rde l�ngst bak i listan
	void eraseAll(); // Ta bort hela listan
	int getValue(int index); // Spottar ut v�rdet p� den platsen i listan
	

private:
	long vectorSize;
	int vecValue;
//	CIntVector newer;
//	CIntVector older;

};
