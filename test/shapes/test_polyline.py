from pathlib import Path

import fpdf
from fpdf.errors import FPDFException
from test.utilities import assert_pdf_equal

import pytest

HERE = Path(__file__).resolve().parent


def with_page_and_data(unit):
    pdf = fpdf.FPDF(unit=unit)
    pdf.add_page()
    data = []
    # pylint: disable=protected-access
    pdf._out = data.append
    return pdf, data


polyline_coordinates = [(10, 10), (40, 10), (10, 40)]
expected_pdf_str = "10.00 831.89 m40.00 831.89 l10.00 801.89 l S "
expected_pdf_str_fill = "10.00 831.89 m40.00 831.89 l10.00 801.89 l B "
expected_pdf_str_poly = "10.00 831.89 m40.00 831.89 l10.00 801.89 l h  S "
expected_pdf_str_polyfill = "10.00 831.89 m40.00 831.89 l10.00 801.89 l h  B "


def scale_points(raw_points, k_recip):
    return [(k_recip * coord[0], k_recip * coord[1]) for coord in raw_points]


scaling_factors_for_units = [
    ("pt", 1),
    ("mm", 1 / (72 / 25.4)),
    ("cm", 1 / (72 / 2.54)),
    ("in", 1 / 72),
]


@pytest.mark.parametrize("k,factor", scaling_factors_for_units)
def test_polyline_command_all_k(k, factor):
    pdf, data = with_page_and_data(k)
    pdf.polyline(scale_points(polyline_coordinates, factor))
    assert expected_pdf_str == "".join(data)

    data.clear()

    pdf.polyline(scale_points(polyline_coordinates, factor), fill=True)
    assert expected_pdf_str_fill == "".join(data)

    data.clear()

    pdf.polyline(scale_points(polyline_coordinates, factor), polygon=True)
    assert expected_pdf_str_poly == "".join(data)

    data.clear()
    pdf.polyline(scale_points(polyline_coordinates, factor), polygon=True, fill=True)
    assert expected_pdf_str_polyfill == "".join(data)


def test_check_page():
    pdf = fpdf.FPDF(unit="pt")
    with pytest.raises(FPDFException) as polyline_no_page:
        pdf.polyline(polyline_coordinates)

    msg = "No page open, you need to call add_page() first"
    assert msg == str(polyline_no_page.value)

    with pytest.raises(FPDFException) as polygon_no_page:
        pdf.polygon(polyline_coordinates)

    assert msg == str(polygon_no_page.value)


def test_polyline_fill_polygon(tmp_path):
    pdf = fpdf.FPDF(unit="cm")
    pdf.add_page()
    pdf.set_x(10)
    pdf.set_y(10)
    coords = scale_points(polyline_coordinates, scaling_factors_for_units[2][1])
    pdf.polyline(coords, fill=True, polygon=True)
    # pdf.output(HERE / "class_polyline.pdf")
    assert_pdf_equal(pdf, HERE / "class_polyline.pdf", tmp_path)
