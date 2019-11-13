# bible_web_scraper

This python script used  to get the bible of a particular version of the bible from website.

# Features
  Web scrapping
  
# Sample inputs
  Folder location: C:\Users\UserName\Documents\
  Version path: /versions/King-James-Version-KJV-Bible/#booklist
  
# Output
   Format: txt file <br>
   Structure: [Version name]/[Book name]/[Chapter] <br>
   File content: chapter of the bible with delimiter of "*" <br>
   Column order: <br>
    - Bible version<br>
    - Bible version abbreviation<br>
    - Book name<br>
    - Book part name (e.g. ot for Old Testament)<br>
    - Book part id (e.g. 1 for ot)<br>
    - Book chapter<br>
    - Verse number<br>
    - Verse content<br>
    - Footnotes<br>

[] Websites to be scraped
  - biblegateway.com

[]  Todos
  - add other website
  - make executable file
  - make ui
