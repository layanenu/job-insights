from src.pre_built.counter import count_ocurrences


def test_counter():
    counter_python_high_case = count_ocurrences('data/jobs.csv', 'Python')
    assert counter_python_high_case == 1639
    counter_python_low_case = count_ocurrences('data/jobs.csv', 'Python')
    assert counter_python_low_case == 1639
    counter_js_high_case = count_ocurrences('data/jobs.csv', 'Javascript')
    assert counter_js_high_case == 122
    counter_js_low_case = count_ocurrences('data/jobs.csv', 'javascript')
    assert counter_js_low_case == 122
