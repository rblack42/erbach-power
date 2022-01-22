PROJECT	:= $(notdir $(PWD))
MK	:= mk

all:	test

include $(MK)/help.mk
include $(MK)/python.mk
include $(MK)/sphinx.mk
include $(MK)/version.mk
include $(MK)/jupyter.mk
