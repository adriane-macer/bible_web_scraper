from lxml import html
import requests
import time
import re

base_url = "https://www.biblegateway.com"

# versions_path = "/versions"
book_part_ids = {"ot": 1, "nt": 2, "ap": 3}


def get_languages():
    page = requests.get("https://www.biblegateway.com/versions/")
    tree = html.fromstring(page.content)
    return tree.xpath('//span[@class="language-display"]/text()')


def start_scrapping(version_path):
    # books
    url = "{}{}".format(base_url, version_path)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    title = version_path.split("/")[2].replace("-Bible", "").split("-")
    version_title = " ".join(title[:-1])
    version_short = title[-1]
    print("Scrapping bible version: ")
    print(title)
    print("...")
    books = tree.xpath('//tr[contains(@class,"-list")]')
    for book in books:
        b: str = book.get('class')
        book_part = b.split(" ")[-1][:2]
        print(book_part)
        book_name = tree.xpath("//tr[@class='{}']/td[@class='toggle-collapse2 book-name']/text()".format(b))[0]
        print("Book of {}...".format(book_name))
        num_of_chapters = tree.xpath("//tr[@class='{}']//span[@class='num-chapters collapse in']/text()".format(b))[0]
        print("Number of chapters: {}.".format(num_of_chapters))
        chapters = tree.xpath("//tr[@class='{}']/td[@class='chapters collapse']/a".format(b))
        current_chapter = 1

        for chapter in chapters:
            print("chapter {}...".format(current_chapter))
            chapter_path = chapter.get('href')
            scrape_verses(chapter_path, version_title, version_short, book_name, book_part, current_chapter)
            time.sleep(10)
            current_chapter = current_chapter + 1
            # TODO cut to 2 chapters for testing only
            if current_chapter == 3:
                break
        # TODO Cut to book of joshua. testing only
        if book_name == "Joshua" or book_name == "Proverbs":
            break


def scrape_verses(path, version_title, version_short, book, book_part, chapter):
    url = "{}{}".format(base_url, path)
    page = requests.get(url)
    tree = html.fromstring(page.content)

    passage_box = tree.xpath("//div[contains(@class,'passage-box')]")
    data_osis = passage_box[0].get("data-osis")
    book_short = data_osis.split(".")[0]
    total_verses = data_osis.split(".")[-1]
    print(data_osis)
    print(book_short)
    print(total_verses)
    footnotes_root = tree.xpath("//ol/li[@*]")
    footnotes = []
    for fNote in footnotes_root:
        footnotes.append(fNote.get("id"))

    footnotes_texts = []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(footnotes)):
        f_texts = tree.xpath("//li[@id='{}']/span[@class='footnote-text']/descendant-or-self::node()/text()"
                             .format(footnotes[i]))
        footnotes_texts.append("[{}] {}".format(alpha[i], " ".join(f_texts)))

    delimiter = "*"
    for n in range(int(total_verses)):
        verse = tree \
            .xpath('//p[*]/span[@class="text {book_short}-{chapter}-{verse}"]/descendant-or-self::node()/text()'
                   .format(book_short=book_short, chapter=chapter, verse=n + 1))
        verse_text = "".join(verse[1:])

        # add other details
        verse_text = "{title}{delimiter}{short}{delimiter}{book}{delimiter}{part}{delimiter}{part_id}{delimiter}{chapter}{delimiter}{verse_num}{delimiter}{verse}" \
            .format(title=version_title, short=version_short, book=book, part=book_part,
                    part_id=book_part_ids[book_part], chapter=chapter, verse_num=n + 1,
                    verse=verse_text, delimiter=delimiter)
        # check if there is/ are footnotes
        footnote_pattern = r'\[[a-z]\]'
        verse_footnotes = re.findall(footnote_pattern, verse_text)

        if len(verse_footnotes) > 0:
            verse_text = verse_text + delimiter
            for verse_footnote in verse_footnotes:
                matched_footnote = ""
                for fn in footnotes_texts:
                    if fn.startswith(verse_footnote[0:3]):
                        if fn.endswith("\n"):
                            fn = fn[:-2]

                        matched_footnote = fn
                        break

                if matched_footnote == "":
                    print("Verse {}. No footnote matched for {}".format(n + 1, verse_footnotes))
                else:
                    verse_text = verse_text + matched_footnote + ";"

        print(verse_text)


def get_all_version_links():
    page = requests.get("https://www.biblegateway.com/versions/")
    tree = html.fromstring(page.content)
    return tree.xpath('//td[@*]/span/a[@*]')


def run():
    # destination = input("Enter destination folder:\n")
    #
    # version_path = input("Input bible version path:\n")

    version_path = "/versions/New-Revised-Standard-Version-NRSV-Bible/#booklist"
    start_scrapping(version_path, )


if __name__ == '__main__':
    run()
