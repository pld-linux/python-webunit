
%include	/usr/lib/rpm/macros.python
%define 	module	webunit

Summary:	Website unit/regression testing tool
Summary(pl):	Narzêdzie do testowania modu³ów sieci Web
Name:		python-%{module}
Version:	1.3.8
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	http://www.mechanicalcat.net/tech/webunit/%{module}-%{version}.tar.gz
# Source0-md5:	97b9e6b5149dadce48b86adbf2db3b0a
URL:		http://www.mechanicalcat.net/tech/webunit/
BuildRequires:	python-devel >= 2.3
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
webunit test your websites with code that acts like a web browser.

Features in a nutshell:

1. Browser-like page fetching including fetching the images and
   stylesheets needed for a page and following redirects
2. Cookies stored and trackable (all automatically handled)
3. HTTP, HTTPS, GET, POST, basic auth all handled, control over
   expected status codes, ...
4. DOM parsing of pages to retrieve and analyse structure, including
   simple form re-posting
5. Two-line page-fetch followed by form-submit possible, with error
   checking
6. Ability to register error page content across multiple tests
7. Uses python's standard unittest module as the underlying framework

%description -l pl
webunit u¿ywany jest do testowania stron WWW przy pomocy kodu
symuluj±cego dzia³anie przegl±darki internetowej.

Cechy webunit:

1. Pobieranie stron WWW symuluj±ce dzia³anie przegl±darki
   internetowej, pobieranie obrazków i styli, pod±¿anie za
   przekierowaniami.
2. Automatyczna obs³uga ciasteczek (cookies).
3. Obs³uga protoko³ów HTTP, HTTPS, metod GET, POST, uwierzytelniania,
   kontrola oczekiwanych kodów statusu.
4. Parsowanie struktury DOM stron w celu pobrania i analizy strony,
   tak¿e w celu ³atwego odsy³ania formularzy.
5. Dwutorowe pobieranie strony koñczone wysy³k± formularza wraz ze
   sprawdzaniem b³êdów.
6. Mo¿liwo¶æ okre¶lenia zawarto¶ci strony z b³êdem przy przechodzeniu
   przez kolejne testy.
7. U¿ycie standardowego modu³u pythona unittest jako zasadniczego
   szkieletu testu.

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
%doc CHANGES.txt demo README.txt run_tests
%{py_sitescriptdir}/webunit
