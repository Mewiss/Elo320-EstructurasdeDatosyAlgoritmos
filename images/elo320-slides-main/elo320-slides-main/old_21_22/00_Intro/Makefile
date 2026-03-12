SHELL=/bin/bash
PAPER=00_Intro

all: paper clean

paper: 
	@echo "Generando presentación por primera vez..."
	@pdflatex $(PAPER).tex
#	@echo "Bibliografía por primera vez.."
#	@bibtex $(PAPER)
#	@echo "y por segunda vez..."
#	@pdflatex $(PAPER).tex
#	@echo "y por tercera vez..."
#	@pdflatex $(PAPER).tex

clean:
	@echo "Limpiando..."
	@rm -f $(PAPER).{aux,toc,log,tmp,dvi,idx,ilg,ind,bbl,blg,out,nav,snm,nlo,thm}

distclean:
	@echo "Limpiando todo!..."
	@rm -f $(PAPER).{pdf,aux,toc,log,tmp,dvi,idx,ilg,ind,bbl,blg,out,nav,snm}

