def split_before_each_uppercases(formula):
    start = 0
    end = 0
    split_formula = []
    for char in formula:
      if (end != 0) and (char.isupper() == True):
        split_formula.append(formula[start:end])
        start = end
      end += 1
    if start != end:
      split_formula.append(formula[start:end])
    return split_formula


def split_at_first_digit(formula):
    digit_location = 0
    for char in formula:
        if char.isdigit() == True:
          return formula[:digit_location], int(formula[digit_location: ])
        digit_location += 1
    return formula, 1
