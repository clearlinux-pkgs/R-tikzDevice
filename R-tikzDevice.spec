#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tikzDevice
Version  : 0.12.3.1
Release  : 34
URL      : https://cran.r-project.org/src/contrib/tikzDevice_0.12.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tikzDevice_0.12.3.1.tar.gz
Summary  : R Graphics Output in LaTeX Format
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-tikzDevice-lib = %{version}-%{release}
Requires: R-filehash
Requires: R-png
BuildRequires : R-filehash
BuildRequires : R-png
BuildRequires : buildreq-R

%description
in a LaTeX-friendly format. The device transforms plotting
        commands issued by R functions into LaTeX code blocks. When
        included in a LaTeX document, these blocks are interpreted with
        the help of 'TikZ'---a graphics package for TeX and friends
        written by Till Tantau. Using the 'tikzDevice', the text of R
        plots can contain LaTeX commands such as mathematical formula.
        The device also allows arbitrary LaTeX code to be inserted into
        the output stream.

%package lib
Summary: lib components for the R-tikzDevice package.
Group: Libraries

%description lib
lib components for the R-tikzDevice package.


%prep
%setup -q -c -n tikzDevice
cd %{_builddir}/tikzDevice

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641138913

%install
export SOURCE_DATE_EPOCH=1641138913
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tikzDevice
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tikzDevice
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tikzDevice
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tikzDevice || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tikzDevice/DESCRIPTION
/usr/lib64/R/library/tikzDevice/INDEX
/usr/lib64/R/library/tikzDevice/Meta/Rd.rds
/usr/lib64/R/library/tikzDevice/Meta/features.rds
/usr/lib64/R/library/tikzDevice/Meta/hsearch.rds
/usr/lib64/R/library/tikzDevice/Meta/links.rds
/usr/lib64/R/library/tikzDevice/Meta/nsInfo.rds
/usr/lib64/R/library/tikzDevice/Meta/package.rds
/usr/lib64/R/library/tikzDevice/Meta/vignette.rds
/usr/lib64/R/library/tikzDevice/NAMESPACE
/usr/lib64/R/library/tikzDevice/NEWS.md
/usr/lib64/R/library/tikzDevice/R/tikzDevice
/usr/lib64/R/library/tikzDevice/R/tikzDevice.rdb
/usr/lib64/R/library/tikzDevice/R/tikzDevice.rdx
/usr/lib64/R/library/tikzDevice/doc/index.html
/usr/lib64/R/library/tikzDevice/doc/tikzDevice.R
/usr/lib64/R/library/tikzDevice/doc/tikzDevice.Rnw
/usr/lib64/R/library/tikzDevice/doc/tikzDevice.pdf
/usr/lib64/R/library/tikzDevice/help/AnIndex
/usr/lib64/R/library/tikzDevice/help/aliases.rds
/usr/lib64/R/library/tikzDevice/help/paths.rds
/usr/lib64/R/library/tikzDevice/help/tikzDevice.rdb
/usr/lib64/R/library/tikzDevice/help/tikzDevice.rdx
/usr/lib64/R/library/tikzDevice/html/00Index.html
/usr/lib64/R/library/tikzDevice/html/R.css
/usr/lib64/R/library/tikzDevice/tests/testthat.R
/usr/lib64/R/library/tikzDevice/tests/testthat/Rplots.tex
/usr/lib64/R/library/tikzDevice/tests/testthat/Rplots_colors.tex
/usr/lib64/R/library/tikzDevice/tests/testthat/helper_bootstrap.R
/usr/lib64/R/library/tikzDevice/tests/testthat/helper_graphics.R
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/annotation_noflush.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/base_annotation.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/base_raster.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/base_raster_noresample.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/base_symbolic_simple.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/character_expansion.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/contour_lines.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/draw_circles.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/draw_filled_circles.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/filled_rectangle.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/ggplot2_superscripts.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/ggplot2_test.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/graph_box.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/grid_annotation.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/grid_raster.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/hello_TeX.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/line_color.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/line_color_width.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/line_types.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/line_weights.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/lots_of_elements.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/luatex_utf8_characters.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/pch_caracters.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/persp_3D.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/plot_legend.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/polypath.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/raster_reflection.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/string_placement.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/text_alignment.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/text_color.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/transparency.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/utf8_characters.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/standard_graphs/xetex_variants.pdf
/usr/lib64/R/library/tikzDevice/tests/testthat/test_error_handling.R
/usr/lib64/R/library/tikzDevice/tests/testthat/test_graphics.R
/usr/lib64/R/library/tikzDevice/tests/testthat/test_metrics_dict.R
/usr/lib64/R/library/tikzDevice/tests/testthat/test_misc.R
/usr/lib64/R/library/tikzDevice/tests/testthat/test_pointsize.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tikzDevice/libs/tikzDevice.so
/usr/lib64/R/library/tikzDevice/libs/tikzDevice.so.avx2
/usr/lib64/R/library/tikzDevice/libs/tikzDevice.so.avx512
