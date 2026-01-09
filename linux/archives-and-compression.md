# Linux Archives and Compression

Archiving and compression are commonly used for backups
and transferring multiple files.

## tar
The tar command is used to create and extract archives.

Examples:
tar -cvf archive.tar directory/
tar -xvf archive.tar

## gzip
gzip is used to compress files.

Examples:
gzip archive.tar
gunzip archive.tar.gz

## Combined usage
tar -czvf archive.tar.gz directory/
