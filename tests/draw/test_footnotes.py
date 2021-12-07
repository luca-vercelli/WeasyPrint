"""
    weasyprint.tests.test_draw.test_footnotes
    -----------------------------------------

    Test how footnotes are drawn.

"""

from ..testing_utils import assert_no_logs
from . import assert_pixels


@assert_no_logs
def test_inline_footnote():
    assert_pixels('span_footnote', 9, 7, '''
        RRRRRRRR_
        RRRRRRRR_
        _________
        _________
        _________
        RRRRRRRR_
        RRRRRRRR_
    ''', '''
    <style>
        @font-face {src: url(weasyprint.otf); font-family: weasyprint}
        @page {
            size: 9px 7px;
            background: white;
        }
        div {
            color: red;
            font-family: weasyprint;
            font-size: 2px;
            line-height: 1;
        }
        span {
            float: footnote;
        }
    </style>
    <div>abc<span>de</span></div>''')


@assert_no_logs
def test_block_footnote():
    assert_pixels('div_footnote', 9, 7, '''
        RRRRRRRR_
        RRRRRRRR_
        _________
        _________
        _________
        RRRRRRRR_
        RRRRRRRR_
    ''', '''
    <style>
        @font-face {src: url(weasyprint.otf); font-family: weasyprint}
        @page {
            size: 9px 7px;
            background: white;
        }
        div {
            color: red;
            font-family: weasyprint;
            font-size: 2px;
            line-height: 1;
        }
        div.footnote {
            float: footnote;
        }
    </style>
    <div>abc<div class="footnote">de</div></div>''')


@assert_no_logs
def test_long_footnote():
    assert_pixels('long_footnote', 9, 7, '''
        RRRRRRRR_
        RRRRRRRR_
        _________
        RRRRRRRR_
        RRRRRRRR_
        RR_______
        RR_______
    ''', '''
    <style>
        @font-face {src: url(weasyprint.otf); font-family: weasyprint}
        @page {
            size: 9px 7px;
            background: white;
        }
        div {
            color: red;
            font-family: weasyprint;
            font-size: 2px;
            line-height: 1;
        }
        span {
            float: footnote;
        }
    </style>
    <div>abc<span>de f</span></div>''')
