"""
Utility functions for manipulation with Python dictionaries.
"""


def group_keys_by_values(d):
    """
    Take a dict (A -> B( and return another one (B -> [A]). It groups keys
    from the original dict by their values.

    .. testsetup::

        from proso.dict import group_keys_by_values

    .. doctest::

        >>> group_keys_by_values({1: True, 2: False, 3: True, 4: True})
        {False: [2], True: [1, 3, 4]}

    Args:
        d (dict): original dictionary which will be transformed.
    Returns:
        dict: new keys are taken from original values, each new key points to a
            list where all values are original keys pointing to the same value
    """
    result = {}
    for k, v in d.items():
        saved = result.get(v, [])
        saved.append(k)
        result[v] = saved
    return result
