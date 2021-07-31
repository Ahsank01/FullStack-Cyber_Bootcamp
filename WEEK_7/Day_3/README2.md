# Blue Team 08: Digital Forensics

## OUTLINE
1. What is a Filesystem?
2. Data Categories
3. Deletion

<br>

## WHAT IS A FILESYSTEM?
- Ways to store and organize information on a disk
- Has structure and a filing system

<br>

## DATA CATEGORIES
- File System
    - General file system information - a map
- Content
    - Actual data that is stored - data units
- Metadata
    - Data that describes data (location, size, timestamps, etc)
- File name
    - Human interface/names for files
- Application
    - Other, spcial features
- Content
    - This is the actual data/files
    - Deletiom will sometimes not actually delete the conttent, just the pointers / links to the content
- Metadata
    - Info like file creation/modification times
    - File size (maybe less than the 'data unit' size)
    - Slack space

<br>

## SUMMARY
1. Filesysttems store and orgaznize data
2. Five categories of data in file systems
3. Deletion doesn't really delete!