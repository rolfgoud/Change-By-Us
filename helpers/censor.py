"""
    :copyright: (c) 2011 Local Projects, all rights reserved
    :license: Affero GNU GPL v3, see LICENSE for more details.
"""

import os
import framework.util as util
from framework.log import log


def has_words(text, words_list):
    """
    Returns True if the given text contains and words in the given word list,
    otherwise returns False.
    """
    words = util.depunctuate(text, replacement=" ").split()
    words_list = [] if words_list is None else words_list
    num_found = [word for word in words if word.lower() in words_list]
    return len(num_found) != 0

def badwords(db, text):
    """
    Checks if the given text contains any "kill" or "warning" words. Returns
    2 on kill words, 1 on warning words, otherwise 0.
    """
    try:
        badwords = db.query("SELECT * FROM badwords LIMIT 1")[0]
        kill_words = badwords['kill_words'] or ""
        warn_words = badwords['warn_words'] or ""
    except Exception, e:
        log.error(e)
        return False

    if has_words(text, kill_words.split()):
        return 2

    if has_words(text, warn_words.split()):
        return 1

    return 0
