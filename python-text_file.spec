# $Revision: 1.3 $ $Date: 2004-05-29 05:54:27 $

%include	/usr/lib/rpm/macros.python
%define 	module	text_file

Summary:	Python module that simplifies text file processing
Summary(pl):	Modu� Pythona upraszczaj�cy przetwarzanie plik�w tekstowych
Name:		python-%{module}
Version:	1.0
Release:	1
License:	CNRI
Group:		Libraries/Python
Source0:	http://www.mems-exchange.org/software/files/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	de5e02741a0bf64635d0321eff635ee3
URL:		http://www.mems-exchange.org/software/text_file/
BuildRequires:	python-devel >= 2.3
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
text_file.py is a Python module that provides the class TextFile,
instances of which are file-like objects that take care of many common
tasks needed when reading text files in the traditional Unix way:
strip comments, skip blank lines, join physical lines into logical
lines, strip trailing and/or leading whitespace, and collapse internal
whitespace. All of these are optional and independently controllable.
See the documentation in text_file.py for full details.

Note that TextFile objects do not have precisely the same semantics as
Python file objects, so they are not 100% compatible with each other.
See the class documentation for details.

%description -l pl
test_file.py jest modu�em Pythona udost�pniaj�cym klas� TextFile,
kt�rej instancje s� obiektami podobnymi do pythonowych obiekt�w file.
Klasa TextFile w spos�b przezroczysty odpowiada za przeprowadzanie
powszechnych i u�ytecznych operacji podczas czytania plik�w
tekstowych znanych powszechnie w �rodowisku uniksowym: ��czenie linii
fizycznych w logiczne, usuwanie pocz�tkowych i/lub ko�cowych bia�ych
znak�w oraz wewn�trzne redukowanie bia�ych znak�w. Wszystkie z tych
operacji s� opcjonalne i niezale�nie konfigurowalne. Dokumentacja
modu�u umieszczona jest bezpo�rednio w pliku text_file.py.

Nale�y zauwa�y�, i� obiekty TextFile nie maj� semantyki zgodnej z
obiektami file Pythona, nie s� wi�c w stu procentach kompatybilne z
innymi modu�ami udost�pniaj�cymi podobn� funkcjonalno��. Szczeg�y
opisane s� w dokumentacji klasy.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/text_file.py[oc]
