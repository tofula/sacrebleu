import pytest

from sacrebleu.tokenizers.tokenizer_re import TokenizerRegexp

test_cases_with_tag = [
    ("My first<b>great</b> text.","My first <b> great </b> text ."),
    ("And nested <w><strong>content</strong></w> here.","And nested <w> <strong> content </strong> </w> here ."),
]

test_cases_with_tag_attrib_q = [
    ("My first<b id='10'>great</b> text.", "My first <b id='10'> great </b> text ."),
    ("And nested <w style='top'><strong>content</strong></w> here.", "And nested <w style='top'> <strong> content </strong> </w> here ."),
]

test_cases_with_tag_attrib_qq = [
    ('My first<b id="10">great</b> text.', 'My first <b id="10"> great </b> text .'),
    ('And nested <w style="top"><strong>content</strong></w> here.', 'And nested <w style="top"> <strong> content </strong> </w> here .'),
]

test_cases_email = [
    ("My first sweet@home.at e-mail.", "My first sweet@home.at e-mail ."),
    ("Please mail to john.Doe132@home_78.fr now!", "Please mail to john.Doe132@home_78.fr now !"),
]

@pytest.mark.parametrize("input, expected", test_cases_with_tag)
def test_regexp_tokenizer_default(input, expected):
    tokenizer = TokenizerRegexp()
    assert tokenizer(input) == expected

@pytest.mark.parametrize("input, expected", test_cases_with_tag_attrib_q)
def test_regexp_tokenizer_default(input, expected):
    tokenizer = TokenizerRegexp()
    assert tokenizer(input) == expected

@pytest.mark.parametrize("input, expected", test_cases_with_tag_attrib_qq)
def test_regexp_tokenizer_default(input, expected):
    tokenizer = TokenizerRegexp()
    assert tokenizer(input) == expected

@pytest.mark.parametrize("input, expected", test_cases_email)
def test_regexp_tokenizer_default(input, expected):
    tokenizer = TokenizerRegexp()
    assert tokenizer(input) == expected
