def test_string_length(sample_string):
    assert len(sample_string) == 6

def test_string_upper(sample_string):
    assert sample_string.upper() == "PYTEST"