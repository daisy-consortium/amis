rem the paths are relative to AmisGuiMFC2's folder

echo Copying Ambulant DLL
copy ..\..\..\..\..\ambulant\bin\win32\libambulant_shwin32_D.dll ..\..\bin\libambulant_shwin32_D.dll /y
copy ..\..\..\..\..\ambulant\bin\win32\libambulant_shwin32.dll ..\..\bin\libambulant_shwin32.dll /y

echo Creating resource.h.ini configuration file
c:\Perl\bin\perl ..\..\bin\resource.h.ini.pl resource.h ../../bin/settings/resource.h.ini