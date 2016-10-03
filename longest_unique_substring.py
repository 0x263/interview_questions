"""
Given a string 'abcdabcdf', you're code should return the maximum substring which
has zero repetition in the substring. So in this example it would be 'abcdf'. If
there are 2 substrings with same length return the first one.
"""


def max_substring(text):
    beg = -1
    end = -1
    pre = 0
    post = 0
    max_len = 0
    tset = set()

    while post < len(text) and pre < len(text):
        if not text[post] in tset:
            tset.add(text[post])
            post += 1
        else:
            while text[post] in tset:
                if text[pre] in tset:
                    tset.remove(text[pre])
                pre += 1
            if pre > post:
                post = pre
            tset.add(text[post])
            post += 1

        size = post - pre

        if size > max_len:
            max_len = size
            beg = pre
            end = post

    return text[beg:end]


if __name__ == "__main__":
    sample = 'abcdabcdf'
    sample2 = 'bbbbbbbbc'
    print(max_substring(sample2))
