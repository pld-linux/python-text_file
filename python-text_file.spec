# $Revision: 1.8 $ $Date: 2007-02-13 08:06:43 $

%define 	module	text_file

Summary:	Python module that simplifies text file processing
Summary(pl.UTF-8):	Moduł Pythona upraszczający przetwarzanie plików tekstowych
Name:		python-%{module}
Version:	1.0
Release:	1
License:	CNRI
Group:		Libraries/Python
Source0:	http://www.mems-exchange.org/software/files/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	de5e02741a0bf64635d0321eff635ee3
URL:		http://www.mems-exchange.org/software/text_file/
BuildRequires:	python-devel >= 1:2.3
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

%description -l pl.UTF-8
test_file.py jest modułem Pythona udostępniającym klasę TextFile,
której instancje są obiektami podobnymi do pythonowych obiektów file.
Klasa TextFile w sposób przezroczysty odpowiada za przeprowadzanie
użytecznych i znanych w środowisku uniksowym operacji podczas czytania
plików tekstowych: łączenie linii fizycznych w logiczne, usuwanie
początkowych i/lub końcowych białych znaków oraz wewnętrzne
redukowanie białych znaków. Wszystkie z tych operacji są opcjonalne i
niezależnie konfigurowalne. Dokumentacja modułu umieszczona jest
bezpośrednio w pliku text_file.py.

Należy zauważyć, iż obiekty TextFile nie mają semantyki zgodnej z
obiektami file Pythona, nie są więc w stu procentach kompatybilne z
innymi modułami udostępniającymi podobną funkcjonalność. Szczegóły
opisane są w dokumentacji klasy.

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
