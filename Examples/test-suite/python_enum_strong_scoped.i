%module "python_enum_strong_scoped"
%include <enums.swg>


%feature("python:enum",strong=1) Color1;
%feature("python:enum",scoped=1) Color2;
%feature("python:enum",scoped=1, strong=1) Color3;
%feature("python:enum",scoped=1) Color4;

enum Color1 { RED, GREEN, BLUE };
enum Color2 { CYAN, MAGENTA, YELLOW, BLACK };
enum Color3 { BROWN };
enum Color4 { C4_BROWN };

int intval(Color1 x);

int intval_r(Color1& x);
int intval_p(Color1* x);

int intval_cr(Color1 const& x);
int intval_cp(Color1 const* x);

int intval(Color3 x);


%{
enum Color1 { RED, GREEN, BLUE };
enum Color2 { CYAN = 20, MAGENTA = 21, YELLOW = 22, BLACK = 23 };
enum Color3 { BROWN = 31 };
enum Color4 { C4_BROWN = BROWN };

int intval(Color1 x) { return static_cast<int>(x); }

int intval_r(Color1& x) { return static_cast<int>(x); }
int intval_p(Color1* x) { return static_cast<int>(*x); }

int intval_cr(Color1 const& x) { return static_cast<int>(x); }
int intval_cp(Color1 const* x) { return static_cast<int>(*x); }

int intval(Color3 x) { return static_cast<int>(x); }
%}
