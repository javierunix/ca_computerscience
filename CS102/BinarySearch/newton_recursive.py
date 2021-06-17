def newton_recursive(target, allowed_error, upper_bound=None, lower_bound=0):

    if upper_bound is None:
        upper_bound = target

    middle_term = (upper_bound + lower_bound) / 2

    if abs(middle_term ** 2 - target) <= allowed_error:
        return middle_term

    elif  middle_term ** 2 > target:
        return newton_recursive(target, allowed_error, middle_term, lower_bound)
    else:
        return newton_recursive(target, allowed_error, upper_bound, middle_term)

print(newton_recursive(2021, 0.0001))