# import random
# import pickle


def get_all_unicode():

    try:
        get_char = unichr
    except NameError:
        get_char = chr

    # Update this to include code point ranges to be sampled
    include_ranges = [
        (0x2200, 0x22FF), #Mathematical Operators
        (0x0400, 0x04FF), #Cyrillic
        (0x0250, 0x02AF), #IPA Extensions
        (0x30A0, 0x30FF), #Katakana
        (0x13A0, 0x13F4), #Cherokee
        (0x0600, 0x06FF), #Arabic
        (0x03A3, 0x03FF), #Greek
        (0x0500, 0x052F), #Cyrillic Supplementary
        (0x05D0, 0x05EA), #Hebrew
        (0x0904, 0x0939), #Devanagari
        (0x1510, 0x167D), #Unified Canadian Aboriginal Syllabivs
        (0xF900, 0xFA6D), #CJK compatibility ideographs
    ]

    alphabet = [
        get_char(code_point) for current_range in include_ranges
            for code_point in range(current_range[0], current_range[1] + 1)
    ]

    return alphabet

    # f = open('UnicodeChoices.pickle', 'wb')
    # pickle.dump(alphabet, f)
    # f.close
#     return random.choice(alphabet)
#
# if __name__ == '__main__':
#     x = (get_random_unicode())
#     print(x)
#
if __name__ == '__main__':
    x = (get_random_unicode(1))
    print(x)
