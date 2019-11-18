from lxml import html
import requests
import time
import re
from version_paths import version_paths
import os

base_url = "https://www.biblegateway.com"

# versions_path = "/versions"
book_part_ids = {"ot": 1, "nt": 2, "ap": 3}


def get_languages():
    page = requests.get("https://www.biblegateway.com/versions/")
    tree = html.fromstring(page.content)
    return tree.xpath('//span[@class="language-display"]/text()')


def start_scrapping(version_path, destination_base_path, is_skip_enable, starting_book):
    # books
    url = "{}{}".format(base_url, version_path)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    title = version_path.split("/")[2].replace("-Bible", "").split("-")
    version_title = " ".join(title[:-1])
    version_short = title[-1]

    version_folder = version_title + "_" + version_short
    # Adding bible version folder
    try:
        os.makedirs(destination_base_path + "\\" + version_folder)
        print("...{} directory created".format(version_folder))
    except Exception as e:
        print(e)
        print("Error in creation of version directory")
        if not str(e).find("file already exist"):
            return

    print("Scrapping bible version: ")
    print(version_title, "-", version_short)
    print("...")
    books = tree.xpath('//tr[contains(@class,"-list")]')
    is_starting_book_reached = False
    fetch_delay_reset_count = 1
    for book in books:
        b: str = book.get('class')
        book_part = b.split(" ")[-1][:2]
        book_name = tree.xpath("//tr[@class='{}']/td[@class='toggle-collapse2 book-name']/text()".format(b))[0]

        if is_skip_enable:
            if not is_starting_book_reached:
                if book_name == starting_book:
                    is_starting_book_reached = True
                else:
                    continue

        print(book_part)
        print("Book of {}...".format(book_name))

        num_of_chapters = tree.xpath("//tr[@class='{}']//span[@class='num-chapters collapse in']/text()".format(b))[0]
        print("Number of chapters: {}.".format(num_of_chapters))
        chapters = tree.xpath("//tr[@class='{}']/td[@class='chapters collapse']/a".format(b))
        current_chapter = 1

        # adding book folder
        book_folder = book_name
        book_full_path = destination_base_path + "\\" + version_folder + "\\" + book_folder
        try:
            os.makedirs(book_full_path)
            print("...{} directory created".format(book_folder))
        except Exception as e:
            print(e)
            print("Error in creation of book directory")
            if not str(e).find("file already exist"):
                return

        whole_book = ""
        for chapter in chapters:
            print("chapter {}...".format(current_chapter))
            chapter_path = chapter.get('href')
            try:
                whole_book = whole_book + scrape_verses(chapter_path, version_title, version_short, book_name,
                                                        book_part, current_chapter,
                                                        book_full_path)
            except UnicodeEncodeError as e:
                raise e

            if fetch_delay_reset_count < 6:
                time.sleep(1)
                fetch_delay_reset_count = fetch_delay_reset_count + 1
            else:
                fetch_delay_reset_count = 1
                time.sleep(10)

            current_chapter = current_chapter + 1

        whole_book_path = book_full_path + "\\" + book_name + "_whole_book"
        try:
            os.makedirs(whole_book_path)
            print("{} directory created".format(book_folder + "_whole_book"))
        except Exception as e:
            print(e)
            print("Error in creation of whole book directory")
            if not str(e).find("file already exist"):
                return

        try:
            with open(
                    whole_book_path + "\\" + version_short + "_whole_" + book_name + ".txt",
                    "w", encoding="utf-8") as f:
                f.write(whole_book)
                print("{} file created".format(version_short + "_whole_" + book_name + ".txt"))
        except UnicodeEncodeError as e:
            raise e


def scrape_verses(path, version_title, version_short, book, book_part, chapter, book_full_path):
    url = "{}{}".format(base_url, path)
    page = requests.get(url)
    tree = html.fromstring(page.content)

    passage_box = tree.xpath("//div[contains(@class,'passage-box')]")
    data_osis = passage_box[0].get("data-osis")
    book_short = data_osis.split(".")[0]
    total_verses = data_osis.split(".")[-1]
    print(data_osis)
    # print(book_short)
    # print(total_verses)
    footnotes_root = tree.xpath("//ol/li[@*]")
    footnotes = []
    for fNote in footnotes_root:
        footnotes.append(fNote.get("id"))

    footnotes_texts = []
    alpha = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z",
        "aa", "ab", "ac", "ad", "ae", "af", "ag", "ah", "ai", "aj", "ak", "al", "am", "an", "ao", "ap", "aq", "ar",
        "as", "at", "au", "av", "aw", "ax", "ay", "az", "ba", "bb", "bc", "bd", "be", "bf", "bg", "bh", "bi", "bj",
        "bk", "bl", "bm",
        "bn", "bo", "bp", "bq", "br", "bs", "bt", "bu", "bv",
        "bw", "bx", "by", "bz", "ca", "cb", "cc", "cd", "ce", "cf", "cg", "ch", "ci", "cj", "ck", "cl", "cm", "cn",
        "co", "cp", "cq", "cr", "cs", "ct", "cu", "cv",
        "cw", "cx", "cy", "cz",
        "da", "db", "dc", "dd", "de", "df", "dg", "dh", "di", "dj", "dk", "dl", "dm", "dn", "do", "dp", "dq", "dr",
        "ds", "dt", "du", "dv",
        "dw", "dx", "dy", "dz",
        "ea", "eb", "ec", "ed", "ee", "ef", "eg", "eh", "ei", "ej", "ek", "el", "em", "en", "eo", "ep", "eq", "er", "es", "et", "eu", "ev",
        "ew", "ex", "ey", "ez",
    ]
    for i in range(len(footnotes)):
        f_texts = tree.xpath("//li[@id='{}']/span[@class='footnote-text']/descendant-or-self::node()/text()"
                             .format(footnotes[i]))
        footnotes_texts.append("[{}] {}".format(alpha[i], " ".join(f_texts)))

    delimiter = "*"
    # string for all verses of the chapter
    chapter_text = ""
    for n in range(int(total_verses)):
        verse = tree \
            .xpath('//p[*]/span[@class="text {book_short}-{chapter}-{verse}"]/descendant-or-self::node()/text()'
                   .format(book_short=book_short, chapter=chapter, verse=n + 1))
        verse_text = "".join(verse[1:])
        verse_text_indents = tree \
            .xpath('//span[@class="indent-1"]//span[@class="text {book_short}-{chapter}-{verse}"]/text()'
                   .format(book_short=book_short, chapter=chapter, verse=n + 1))
        verse_text = verse_text + " ".join(verse_text_indents)

        # add other details
        verse_complete = "{title}{delimiter}{short}{delimiter}{book}{delimiter}{part}{delimiter}{part_id}{delimiter}{chapter}{delimiter}{verse_num}{delimiter}{verse}" \
            .format(title=version_title, short=version_short, book=book, part=book_part,
                    part_id=book_part_ids[book_part], chapter=chapter, verse_num=n + 1,
                    verse=verse_text, delimiter=delimiter)

        # check if there is/ are footnotes
        footnote_pattern = r'\[[a-z]+\]'
        verse_footnotes = re.findall(footnote_pattern, verse_text)

        if len(verse_footnotes) > 0:
            verse_complete = verse_complete + delimiter
            for verse_footnote in verse_footnotes:
                matched_footnote = ""
                for fn in footnotes_texts:
                    if fn.startswith(verse_footnote[0:3]):
                        if fn.endswith("\n"):
                            fn = fn[:-2]

                        matched_footnote = fn
                        break

                if matched_footnote == "":
                    print("Verse {}. No footnote matched for {}".format(n + 1, verse_footnote))
                else:
                    verse_complete = verse_complete + matched_footnote + ";"

        verse_complete = verse_complete + "\n"

        chapter_text = chapter_text + verse_complete

        try:
            with open(
                    book_full_path + "\\" + version_short + "_" + book + "_" + "chapter" + str(chapter) + ".txt",
                    "w", encoding="utf-8") as f:
                f.write(chapter_text)
        except UnicodeEncodeError as e:
            raise e

    return chapter_text


def get_all_version_links():
    page = requests.get("https://www.biblegateway.com/versions/")
    tree = html.fromstring(page.content)
    return tree.xpath('//td[@*]/span/a[@*]')


def run():
    destination = ""
    version_path = ""

    is_valid_destination = False

    starting_book = "Genesis"
    is_skip_enable = False

    while not is_valid_destination:
        destination = input("Enter destination folder:\n")
        if not os.path.exists(destination):
            print("Directory you have entered is not valid.")
        else:
            if len(os.listdir(destination)) > 0:
                print("The folder you have entered is not empty.")
                print("Please choose empty location.")
            else:
                is_valid_destination = True

    is_valid_version_path = False

    while not is_valid_version_path:
        version_path = input("Input bible version path:\n")
        if version_path not in version_paths:
            print("not a valid version_path")
        else:
            is_valid_version_path = True

    print("This process will take at least 3 hours.")
    confirmed = input("Do you want to continue?\n enter N or n if cancel.\n otherwise will continue.")
    if confirmed == "N" or confirmed == "n":
        return

    starting_book = input("If you wish to start to specific book, input starting book.\n Otherwise just press enter.\n"
                          "Starting book: ")

    if not starting_book == "":
        is_skip_enable = True

    try:
        start_scrapping(version_path, destination, is_skip_enable, starting_book)
    except UnicodeEncodeError as e:
        print(e)
        print("Text format is not yet supported")
        print("Choose other versions")
        print("Process not completed")
        return

    print("Completed")


if __name__ == '__main__':
    run()
