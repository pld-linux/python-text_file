# $Revision: 1.3 $ $Date: 2004-05-29 05:54:27 $

%include	/usr/lib/rpm/macros.python
%define 	module	text_file

Summary:	Python module that simplifies text file processing
Summary(pl):	Modu³ Pythona upraszczaj±cy przetwarzanie plików tekstowych
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
test_file.py jest modu³em Pythona udostêpniaj±cym klasê TextFile,
której instancje s± obiektami podobnymi do pythonowych obiektów file.
Klasa TextFile w sposób przezroczysty odpowiada za przeprowadzanie
powszechnych i u¿ytecznych operacji podczas czytania plików
tekstowych znanych powszechnie w ¶rodowisku uniksowym: ³±czenie linii
fizycznych w logiczne, usuwanie pocz±tkowych i/lub koñcowych bia³ych
znaków oraz wewnêtrzne redukowanie bia³ych znaków. Wszystkie z tych
operacji s± opcjonalne i niezale¿nie konfigurowalne. Dokumentacja
modu³u umieszczona jest bezpo¶rednio w pliku text_file.py.

Nale¿y zauwa¿yæ, i¿ obiekty TextFile nie maj± semantyki zgodnej z
obiektami file Pythona, nie s± wiêc w stu procentach kompatybilne z
innymi modu³ami udostêpniaj±cymi podobn± funkcjonalno¶æ. Szczegó³y
opisane s± w dokumentacji klasy.

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
