#!/bin/sh
	
	mkdir -p ../installer
	cd install
	mkdir usr 
	cd usr
	mkdir bin share
	cd share
	mkdir applications gazorpazorp pixmaps
	cd ../..
	mv ./gapacalc.desktop ./usr/share/applications
	mv ./gapacalc.png ./usr/share/pixmaps
	cp ../gui.py ../LibMath.py ../LibProcExpr.py ../logo.png ./usr/share/gazorpazorp
	ln -sf /usr/share/gazorpazorp/gui.py ./usr/bin/gapacalc
	dpkg-deb --build ./ ../../installer/gapacalc_inst.deb
	mv  ./usr/share/applications/gapacalc.desktop ./usr/share/pixmaps/gapacalc.png ./
	rm -rf usr
