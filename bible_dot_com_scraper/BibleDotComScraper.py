from selenium import webdriver
import os
import time
from bible_dot_com_versions import version_links, versions_map


def start_scrapping(version_link, destination_base_path, is_skip_enable, starting_book):
    # url = "https://www.bible.com/bible/1588/GEN.1.AMP"
    # url = version_link
    delimiter = "*"

    # NOTE: The path of the chrome driver installed
    chromedriver = "C:\\Users\\Evangelista\\PycharmProjects\\webScraper\\venv\\chromedriver-Windows"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    try:
        driver.get(version_link)
    except Exception as e:
        print("Invalid version link.")
        driver.close()
        return False

    # check the version
    try:
        version_dropdown = driver.find_element_by_xpath(
            "//div[@data-vars-event-category='Version Picker']//div[@class='tc pa2']")
        version_dropdown.click()
    except Exception as e:
        print("No connection or Invalid version link.")
        driver.close()
        return False

    time.sleep(3)
    version_elements = driver.find_elements_by_xpath("//ul[@class='list ma0 pa0']/descendant::*")

    version_title = ""
    version_short = ""

    for e in version_elements:
        if e.get_attribute('href') == version_link:
            link: str = e.get_attribute('href')
            version_title = '{}'.format(str(e.get_attribute("data-vars-event-label")).split(":")[-1])
            version_short = link.split(".")[-1]

    #         link: str = e.get_attribute('href')
    #         print("Version('{}',{},{}),".format(link,
    #                                             '"{}"'.format(
    #                                                 str(e.get_attribute("data-vars-event-label")).split(":")[-1]),
    #                                             '"{}"'.format(link.split(".")[-1])))
    #
    #         print("'{}': ({},{}),".format(link,
    #                                       '"{}"'.format(
    #                                           str(e.get_attribute("data-vars-event-label")).split(":")[-1]),
    #                                       '"{}"'.format(link.split(".")[-1])))

    title = version_title + " " + version_short

    version_folder = version_title + "_" + version_short

    cancel_button = driver.find_element_by_xpath("//button[@data-vars-event-action='Cancel']")
    cancel_button.click()

    # selecting of version
    book_drop_down = driver.find_element_by_xpath("//div[@class='tc pa2']")
    book_drop_down.click()

    time.sleep(3)
    book_elements = driver.find_elements_by_xpath("//ul[@class='list ma0 pa0 bg-white pb5 min-vh-100']/*")
    if len(book_elements) == 0:
        print("Network interrupted. please try again.")
        return False

    book_map = {}

    for e in book_elements:
        book_map[e.get_attribute('data-vars-event-label')] = e.text

    is_starting_book_reached = False
    fetch_delay_reset_count = 1
    book_sequence = []

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

    for k, v in book_map.items():
        time.sleep(3)
        book_select = driver.find_element_by_xpath("//li[@data-vars-event-label='{}']".format(k))
        book_part = ""  # no book part in bible.com
        book_part_id = ""  # no book part in bible.com
        book_name = v
        book_sequence.append(book_name)

        if is_skip_enable:
            if not is_starting_book_reached:
                if book_name.lower() == starting_book.lower():
                    is_starting_book_reached = True
                else:
                    print("skipping book of {}".format(book_name))
                    continue

        print("scrapping book of {}...".format(v))

        try:
            book_select.click()
        except Exception as e:
            try:
                driver.execute_script("arguments[0].scrollIntoView();", book_select)
            except Exception as ex:
                pass
            time.sleep(3)
            book_select.click()

        time.sleep(3)
        whole_book = ""
        chapters_elements = driver.find_elements_by_xpath("//div[@class='bg-white min-vh-100']/descendant::*")
        chapters_links = [e.get_attribute('href') for e in chapters_elements if e.get_attribute('href') is not None]
        num_of_chapters = len(chapters_links)
        if num_of_chapters == 0:
            print("Network interrupted. Please try again")
            return False

        current_chapter = 1

        book_short_name = str(chapters_links[0].split("/")[-1]).split(".")[0]
        if book_short_name[0] == "1" or book_short_name[0] == '2' or book_short_name[0] == '3':
            if book_name[0] != book_short_name[0]:
                book_name = book_short_name[0] + " " + book_name

        # adding book folder
        book_folder = book_name
        book_full_path = destination_base_path + "\\" + version_folder + "\\" + book_folder
        try:
            print("creating book of {} directory...".format(book_name))
            os.makedirs(book_full_path)
            print("...{} directory created".format(book_folder))
        except Exception as e:
            if not str(e).find("file already exist"):
                print(e)
                print("Error in creation of book directory")
                return
            else:
                offset_book_num = 1
                is_path_exist = True
                print("Appending prefix book number...")
                while is_path_exist:
                    offset_book_num = offset_book_num + 1
                    offset_book_name = "{} {}".format(offset_book_num, book_name)
                    offset_path = destination_base_path + "\\" + version_folder + "\\" + str(
                        offset_book_num) + "_" + book_folder
                    if not os.path.isdir(offset_path):
                        is_path_exist = False
                        book_name = offset_book_name
                        book_folder = book_name

                    book_full_path = destination_base_path + "\\" + version_folder + "\\" + book_folder
                    os.makedirs(book_full_path)
                    print("{} directory created".format(book_name))
        print("{} number of chapters...".format(num_of_chapters))
        for l in chapters_links:
            print("Chapter {}...".format(current_chapter))
            chapter_driver = webdriver.Chrome(chromedriver)
            chapter_driver.get(l)
            time.sleep(3)
            verses_elements = chapter_driver.find_elements_by_xpath("//span[contains(@class,'verse v')]")
            verses = []
            for verse in verses_elements:
                if verse.get_attribute('class') not in verses:
                    verses.append(verse.get_attribute('class'))

            if len(verses) == 0:
                retry_count = 0
                while len(verses) == 0:
                    time.sleep(1)
                    retry_count = retry_count + 1
                    print("retrying...")
                    print("{} retries...".format(retry_count))
                    verses_elements = chapter_driver.find_elements_by_xpath("//span[contains(@class,'verse v')]")

                    for verse in verses_elements:
                        if verse.get_attribute('class') not in verses:
                            verses.append(verse.get_attribute('class'))

                    if retry_count == 3:
                        print("Too many attempts. Please check your connection and try again.")
                        return False

            print(len(verses), "number of verses...")
            current_verse = 1
            footnotes = ""
            for s_verse in verses:
                verse_detail = ""
                verse = chapter_driver.find_elements_by_xpath("//span[@class='{}']/descendant::*".format(s_verse))

                verse_text = " ".join(
                    [v.text for v in verse if v.get_attribute('class') and v.get_attribute('class') == 'content'])

                verse_detail = version_title + delimiter + version_short + delimiter + book_name + delimiter + book_short_name + delimiter + book_part + delimiter + book_part_id + delimiter + str(
                    current_chapter) + delimiter + str(current_verse) + delimiter + verse_text + "\n"
                whole_book = whole_book + verse_detail
                current_verse = current_verse + 1

            chapter_driver.close()
            current_chapter = current_chapter + 1

        whole_book_path = book_full_path + "\\" + book_name + "_whole_book"
        try:
            print("creating whole book directory...")
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

        back_button = driver.find_element_by_xpath("//button[@data-vars-event-action='Back']")
        back_button.click()

    driver.close()
    return True


def run():
    destination = ""
    version_link = ""

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

    is_valid_version_link = False

    # while not is_valid_version_link:
    #     version_link = input("Input bible version link:\n")
    #     if version_link not in version_links:
    #         print("not a valid version_link")
    #     else:
    #         is_valid_version_link = True

    version_link = input("Input bible version link:\n")

    print("During scrapping, don't do anything from this computer.")
    print("The scrapping might be interrupted.")
    print("This process will take at least 3 hours.")
    confirmed = input("Do you want to continue?\n enter N or n if cancel.\n otherwise will continue.")
    if confirmed == "N" or confirmed == "n":
        return

    starting_book = input("If you wish to start to specific book, input starting book.\n Otherwise just press enter.\n"
                          "Starting book: ")

    if not starting_book == "":
        print("The scrapping will start from the book of {}.".format(starting_book))
        is_skip_enable = True
    else:
        print("The scrapping will start from the first book.")

    print("Scrapping started...")

    try:
        result = start_scrapping(version_link, destination, is_skip_enable, starting_book)
        if not result:
            print("... exit with error.")
            return
    except UnicodeEncodeError as e:
        print(e)
        print("Text format is not yet supported")
        print("Choose other versions")
        print("Process not completed")
        return

    print("Completed")


if __name__ == '__main__':
    run()
