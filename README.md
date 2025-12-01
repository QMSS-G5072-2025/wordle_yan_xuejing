# wordle_xy2723

A Python package implementing core logic for the Wordle game. This project focuses on designing clean functions for evaluating Wordle guesses and developing a complete, well structured pytest test suite using fixtures, parametrization, and edge-case testing.

## Installation

```bash
$ pip install wordle_xy2723
```

## Project Overview
This package implements key Wordle operations:
- Validating user guesses
- Checking guesses against a secret word
- Handling duplicate-letter matching rules
- Calculating scores
- Filtering word lists
- Analyzing guess patterns
Alongside the package, I wrote a comprehensive pytest test suite testing:
- Basic functional behavior
- Edge cases and invalid input handling
- Duplicate-letter logic
- Parametrized test scenarios
- Fixture-based reusable test data


## Usage
```bash
from wordle_xy2723.wordle import check_guess, validate_guess

validate_guess("crane")        # True
check_guess("apple", "paper")  # Returns green/yellow/gray pattern
```

## Contributing

Pull requests are welcome!
This project includes:
CONTRIBUTING.md
CONDUCT.md

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`wordle_xy2723` was created by Xuejing Yan. It is licensed under the terms of the MIT license.

## Credits
`wordle_xy2723` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
