from python_enum_strong_scoped import *

#
# Color1:
# 
if type(RED) != Color1:
    print "type(RED) == %r" % type(RED)
    raise RuntimeError("failed")
if intval(RED) != 0:
    print "intval(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")
if intval_r(RED) != 0:
    print "intval_r(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")
if intval_p(RED) != 0:
    print "intval_p(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")
if intval_cr(RED) != 0:
    print "intval_cr(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")
if intval_cp(RED) != 0:
    print "intval_cp(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")

if type(GREEN) != Color1:
    print "type(RED) == %r" % type(RED)
    raise RuntimeError("failed")
if intval(GREEN) != 1:
    print "intval(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")
if intval_r(GREEN) != 1:
    print "intval_r(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")
if intval_p(GREEN) != 1:
    print "intval_p(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")
if intval_cr(GREEN) != 1:
    print "intval_cr(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")
if intval_cp(GREEN) != 1:
    print "intval_cp(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")

if type(BLUE) != Color1:
    print "type(RED) == %r" % type(RED)
    raise RuntimeError("failed")
if intval(BLUE) != 2:
    print "intval(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")
if intval_r(BLUE) != 2:
    print "intval_r(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")
if intval_p(BLUE) != 2:
    print "intval_p(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")
if intval_cr(BLUE) != 2:
    print "intval_cr(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")
if intval_cp(BLUE) != 2:
    print "intval_cp(RED) ==  %r" % intval(RED)
    raise RuntimeError("failed")

if type(Color2.CYAN) != int:
    print "type(Color2.CYAN) == %r" % type(Color2.CYAN)
    raise RuntimeError("failed");
if Color2.CYAN != 20:
    print "Color2.CYAN == %r" % Color2.CYAN
    raise RuntimeError("failed");
if Color2.MAGENTA != 21:
    print "Color2.MAGENTA == %r" % Color2.MAGENTA
    raise RuntimeError("failed");
if Color2.YELLOW != 22:
    print "Color2.YELLOW == %r" % Color2.YELLOW
    raise RuntimeError("failed");
if Color2.BLACK != 23:
    print "Color2.BLACK == %r" % Color2.BLACK
    raise RuntimeError("failed");

if type(Color3.BROWN) != Color3:
    print "type(Color3.BROWN) == %r" % type(Color3.BROWN)
    raise RuntimeError("failed")
if intval(Color3.BROWN) != 31:
    print "Color3.BROWN == %r" % Color3.BROWN

if type(Color4.C4_BROWN) != int:
    print "type(Color4.C4_BROWN) == %r" % type(Color4.C4_BROWN)
    raise RuntimeError("failed")
if Color4.C4_BROWN != intval(Color3.BROWN):
    print "Color4.C4_BROWN == %r" % Color4.C4_BROWN
