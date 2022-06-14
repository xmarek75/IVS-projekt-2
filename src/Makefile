#!/bin/sh

###################################################################
# Project name: Gazorpazorp calculator
# File: Makefile
# Authors: Pavel Marek
# Description: Makefile for GazorPazorp Calculator project
# Date: 30. 3. 2021
# Last Edit: 28. 04. 2021
###################################################################

NAME=xbilek25_xmarek75_xgottw07


#all (nainstaluje potrebne programy ke spusteni programu)
all:
	sudo apt-get install python3
	sudo apt-get install python3-tk
	sudo apt-get install python3-pil python3-pil.imagetk
#pack (zabalí projekt tak, aby mohl být odevzdán)
pack: doc installer folder clean zip

#vytvori slozky install,repo, doc
folder:
	mkdir -p ../../$(NAME)/repo
	mkdir ../../$(NAME)/install
	mkdir ../../$(NAME)/doc
	cp -a ../../ivs-2/. ../../$(NAME)/repo/
	cp -a ../documentation/html ../../$(NAME)/doc/
	cp -a ../installer/. ../../$(NAME)/install/
	
#clean (smaže všechny soubory, co nemají být odevzdány)
clean:
	cd ../../$(NAME)/repo && rm -rf installer
	cd ../../$(NAME)/repo && rm -rf documentation
	cd ../../$(NAME)/repo/src && rm -rf __pycache__
zip:
	cd ../.. && zip -r $(NAME).zip $(NAME)
	cd ../.. && rm -rf $(NAME)	

#run (spustí program - lze předpokládat, že jej před tím někdo manuálně zkompiluje ve VS)
run:
	python3 gui.py
#profile (spustí program pro výpočet směrodatné odchylky s ukázkovým testovacím vstupem)
profile:
	echo "10 20 30 40 50" | python3 profiling.py 
#help (vypíše nápovědu s popisem, co je potřeba udělat před spuštěním programu)
help:
	$(info 	Programme can be installed only on Linux Ubuntu distribution.)
	$(info 	Before first run of the program run command "make all" in folder src)
#test spusti testy matematicke knihovny
test: LibMath_Tests.py
	python3 $<
#aktualizuje installer 	
installer:
	./cr_inst.sh
#vygeneruje doxygen dokumentaci
doc: Doxyfile
	doxygen $<
	
