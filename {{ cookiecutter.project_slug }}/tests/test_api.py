"""Tests API for solving problem {{ cookiecutter.problem_name }}"""

import pytest

from {{ cookiecutter.project_uslug }} import api


@pytest.mark.parametrize(
    ["result", ...],
    (
        [..., ...],
        [..., ...],
    )
)
def test_{{ cookiecutter.problem_api }}(result, ...) -> None:
    """Tests solution for problem {{ cookiecutter.problem_name }}"""

    assert api.{{ cookiecutter.problem_api }}(...) == result