import logging

logger = logging.getLogger(__name__)


def is_anagram(str1, str2):
    equal = sorted(str1.lower()) == sorted(str2.lower())
    logger.error(f"{str1} and {str2} are anagrams: {equal}")
    return equal


if __name__ == '__main__':
    print(is_anagram('yves', 'sevy'))
