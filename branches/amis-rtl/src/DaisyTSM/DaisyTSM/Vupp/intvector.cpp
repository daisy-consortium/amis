#include "intvector.h"
#include <vector>

typedef std::vector<int> INTIS;

CIntVector::CIntVector(int vecValuei)
{
	INTIS rapper;

	vecValue = vecValuei;	
}
CIntVector::~CIntVector()
{
}

long CIntVector::size()
{
	int lala = 5;
	return vectorSize;
}

void CIntVector::push_back(int ival)
{
	// Skapa ett nytt objekt och l�gg dess v�rde d�ri.
//	newer = CIntVector(ival);	

}