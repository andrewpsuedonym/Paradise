import pytest
import src.Grabber as Grabber
import src.util as util


# checks that no verse exceeds twitter's
# character limit
def test_verse_length_280():
    g = Grabber.Grabber()
    verse = ''
    for book_num in range(1,13):
        sec = 1
        verse, lineN = g.get_verse(book_num, sec)
        if verse.split('\n')[0].strip() == 'THE ARGUMENT':
            verse = 'BOOK ' + str(book_num) + '\n' + verse
            assert len(verse) < 281
        while verse != '' and not util.book_end(verse):
            sec += 1
            verse, lineN = g.get_verse(book_num, sec)
            if verse.split('\n')[0].strip() == 'THE END':
                break
            assert len(verse) < 281

