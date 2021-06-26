Changelog
---------

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/),
and [PEP 440](https://www.python.org/dev/peps/pep-0440/).

## [2.4.2] - not released yet
### Added
- disable font caching when `fpdf.FPDF` constructor invoked with `font_cache_dir=None`
- `FPDF.circle`: new method added.
- [`FPDF.will_page_break`](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.will_page_break)
utility method to let users know in advance when adding an elemnt will trigger a page break.
This can be useful to repeat table headers on each page for exemple,
_cf._ [documentation on Tables](https://pyfpdf.github.io/fpdf2/Tables.html#repeat-table-header-on-each-page).
- `FPDF.set_link` now support a new optional `x` parameter to set the horizontal position after following the link

## [2.4.1] - 2021-06-12
### Fixed
- erroneous page breaks occured for full-width / full-height images
- rendering issue of non-ASCII characaters with unicode fonts

## [2.4.0] - 2021-06-11
### Changed
- now `fpdf2` uses the newly supported `DCTDecode` image filter for JPEG images,
  instead of `FlateDecode` before, in order to improve the compression ratio without any image quality loss.
  On test images, this reduced the size of embeded JPEG images by 90%.
- `FPDF.cell`: the `w` (width) parameter becomes optional, with a default value of `None`, meaning to generate a cell with the size of the text content provided
- the `h` (height) parameter of the `cell`, `multi_cell` & `write` methods gets a default value change, `None`, meaning to use the current font size
- removed the useless `w` & `h` parameters of the `FPDF.text_annotation()` method
### Added
- Support setting HTML font colors by name and short hex codes
- new `FPDF.add_action()` method, documented in the [Annotations section](https://pyfpdf.github.io/fpdf2/Annotations.html)
- `FPDF.cell`: new optional `markdown=True` parameter that enables basic Markdown-like styling: `**bold**, __italics__, --underlined--`
- `FPDF.cell`: new optional boolean `center` parameter that positions the cell horizontally
- `FPDF.set_link`: new optional `zoom` parameter that sets the zoom level after following the link.
  Currently ignored by Sumatra PDF Reader, but observed by Adobe Acrobat reader.
- `HTMLMixin` / `HTML2FPDF`: now support `align="justify"`
- new method `FPDF.image_filter` to control the image filters used for images
- `FPDF.add_page`: new optional `duration` & `transition` parameters
  used for [presentations (documentation page)](https://pyfpdf.github.io/fpdf2/Presentations.html)
- extra documentation on [how to configure different page formats for specific pages](https://pyfpdf.github.io/fpdf2/PageFormatAndOrientation.html)
- support for Code 39 barcodes in `fpdf.template`, using `type="C39"`
### Fixed
- avoid an `Undefined font` error when using `write_html` with unicode bold or italics fonts
### Deprecated
- the `FPDF.set_doc_option()` method is deprecated in favour of just setting the `core_fonts_encoding` property
  on an instance of `FPDF`
- the `fpdf.SYSTEM_TTFONTS` configurable module constant is now ignored

## [2.3.5] - 2021-05-12
### Fixed
- a bug in the `deprecation` module that prevented to configure `fpdf2` constants at the module level

## [2.3.4] - 2021-04-30
### Fixed
- a "fake duplicates" bug when a `Pillow.Image.Image` was passed to `FPDF.image`

## [2.3.3] - 2021-04-21
### Added
- new features: **document outline & table of contents**! Check out the new dedicated [documentation page](https://pyfpdf.github.io/fpdf2/DocumentOutlineAndTableOfContents.html) for more information
- new method `FPDF.text_annotation` to insert... Text Annotations
- `FPDF.image` now also accepts an `io.BytesIO` as input
### Fixed
- `HTMLMixin` / `HTML2FPDF`: properly handling `<img>` inside `<td>` & allowing to center them horizontally

## [2.3.2] - 2021-03-27
### Added
- `FPDF.set_xmp_metadata`
- made `<li>` bullets & indentation configurable through class attributes, instance attributes or optional method arguments, _cf._ [`test_customize_ul`](https://github.com/PyFPDF/fpdf2/blob/2.3.2/test/html/test_html.py#L242)
### Fixed
- `FPDF.multi_cell`: line wrapping with justified content and unicode fonts, _cf._ [#118](https://github.com/PyFPDF/fpdf2/issues/118)
- `FPDF.multi_cell`: when `ln=3`, automatic page breaks now behave correctly at the bottom of pages

## [2.3.1] - 2021-02-28
### Added
- `FPDF.polyline` & `FPDF.polygon` : new methods added by @uovodikiwi - thanks!
- `FPDF.set_margin` : new method to set the document right, left, top & bottom margins to the same value at once
- `FPDF.image` now accepts new optional `title` & `alt_text` parameters defining the image title
  and alternative text describing it, for accessibility purposes
- `FPDF.link` now honor its `alt_text` optional parameter and this alternative text describing links
  is now properly included in the resulting PDF document
- the document language can be set using `FPDF.set_lang`
### Fixed
- `FPDF.unbreakable` so that no extra page jump is performed when `FPDF.multi_cell` is called inside this context
### Deprecated
- `fpdf.FPDF_CACHE_MODE` & `fpdf.FPDF_CACHE_DIR` in favor of a configurable new `font_cache_dir` optional argument of the `fpdf.FPDF` constructor

## [2.3.0] - 2021-01-29
Many thanks to [@eumiro](https://github.com/PyFPDF/fpdf2/pulls?q=is%3Apr+author%3Aeumiro) & [@fbernhart](https://github.com/PyFPDF/fpdf2/pulls?q=is%3Apr+author%3Aeumiro) for their contributions to make `fpdf2` code cleaner!
### Added
- `FPDF.unbreakable` : a new method providing a context-manager in which automatic page breaks are disabled.
  _cf._ https://pyfpdf.github.io/fpdf2/PageBreaks.html
- `FPDF.epw` & `FPDF.eph` : new `@property` methods to retrieve the **effective page width / height**, that is the page width / height minus its horizontal / vertical margins.
- `FPDF.image` now accepts also a `Pillow.Image.Image` as input
- `FPDF.multi_cell` parameters evolve in order to generate tables with multiline text in cells:
  * its `ln` parameter now accepts a value of `3` that sets the new position to the right without altering vertical offset
  * a new optional `max_line_height` parameter sets a maximum height of each sub-cell generated
- new documentation pages : how to add content to existing PDFs, HTML, links, tables, text styling & page breaks
- all PDF samples are now validated using 3 different PDF checkers
### Fixed
- `FPDF.alias_nb_pages`: fixed this feature that was broken since v2.0.6
- `FPDF.set_font`: fixed a bug where calling it several times, with & without the same parameters,
prevented strings passed first to the text-rendering methods to be displayed.
### Deprecated
- the `dest` parameter of `FPDF.output` method

## [2.2.0] - 2021-01-11
### Added
- new unit tests, a code formatter (`black`) and a linter (`pylint`) to improve code quality
- new boolean parameter `table_line_separators` for `HTMLMixin.write_html` & underlying `HTML2FPDF` constructor
### Changed
- the documentation URL is now simply https://pyfpdf.github.io/fpdf2/
### Removed
- dropped support for external font definitions in `.font` Python files, that relied on a call to `exec`
### Deprecated
- the `type` parameter of `FPDF.image` method
- the `infile` parameter of `Template` constructor
- the `dest` parameter of `Template.render` method

## [2.1.0] - 2020-12-07
### Added
* [Introducing a rect_clip() function](https://github.com/reingart/pyfpdf/pull/158)
* [Adding support for Contents alt text on Links](https://github.com/reingart/pyfpdf/pull/163)
### Modified
* [Making FPDF.output() x100 time faster by using a bytearray buffer](https://github.com/reingart/pyfpdf/pull/164)
* Fix user's font path ([issue](https://github.com/reingart/pyfpdf/issues/166) [PR](https://github.com/PyFPDF/fpdf2/pull/14))
### Deprecated
* [Deprecating .rotate() and introducing .rotation() context manager](https://github.com/reingart/pyfpdf/pull/161)
### Fixed
* [Fixing #159 issue with set_link + adding GitHub Actions pipeline & badges](https://github.com/reingart/pyfpdf/pull/160)
* `User defined path to font is ignored`
### Removed
* non-necessary dependency on `numpy`
* support for Python 2
 
## [2.0.6] - 2020-10-26
### Added
* Python 3.9 is now supported

## [2.0.5] - 2020-04-01
### Added
* new specific exceptions: `FPDFException` & `FPDFPageFormatException`
* tests to increase line coverage in `image_parsing` module
* a test which uses most of the HTML features
### Fixed
* handling of fonts by the HTML mixin (weight and style) - thanks `cgfrost`!

## [2.0.4] - 2020-03-26
### Fixed
* images centering - thanks `cgfrost`!
* added missing import statment for `urlopen` in `image_parsing` module
* changed urlopen import from `six` library to maintain python2 compatibility

## [2.0.3] - 2020-01-03
### Added
* Ability to use a `BytesIO` buffer directly. This can simplify loading `matplotlib` plots into the PDF.
### Modified
* `load_resource` now return argument if type is `BytesIO`, else load.

## [2.0.1] - 2018-11-15
### Modified
* introduced a dependency to `numpy` to improve performances by replacing pixel regexes in image parsing (s/o @pennersr)

## [2.0.0] - 2017-05-04
### Added
* support for more recent Python versions
* more documentation
### Fixed
* PDF syntax error when version is > 1.3 due to an invalid `/Transparency` dict
### Modified
* turned `accept_page_break` into a property
* unit tests now use the standard `unittest` lib
* massive code cleanup using `flake8`
