# Basic Shell Scripts

## 1. Current Working Directory

Shows current working **[directory](0-current_working_directory)**

```
  pwd
```  

## 2. List It

**[Lists](1-listit)** files in  adirectory

```
  ls
``` 

## 3. Bring me Home

Changes directory to **[home](2-bring_me_home)**

```
  cd
  or
  cd ~
``` 

## 4. List Files

Lists **[files](3-listfiles)** in long-format.

```
  ls -l
``` 

## 5. List more Files

Lists all **[files](4-listmorefiles)** even *hidden* ones in log-format

```
  ls -al
``` 

## 6. List Files Digits Only

Lists  all directory contents using **[digit format](5-listfilesdigitonly)** even *hidden* ones in long-format

```
  ls -aln
``` 

## 7. Create Directory

Creates an empty **[directory](6-listmorefiles)**

```
  mkdir dir_name
```

## 8. Moving File

Moves **[files](7-movethatfile)**

```
  mv file_to_be_moved  destination
```

## 9. Delete File

Deletes selected **[file](8-firstdelete)**

```
  rm file_name
```

## 10. Delete directory

Deletes selected **[directory](9-firstdirdeletion)**
- *-r* recursive ~ deletes the contents of the directory recursively until it is empty

```
  rm -r directory_location
```

## 11. Back

Changes to the previous working **[directory](10-back)**

```
 cd -
```

## 12. File Type

Displays the **[type](12-file_type)** of file

```
  file file_location
```

## 13. Symbolic link

Creates a  symbolic **[link](listmorefiles)**

```
  ln - what_to_be_linked  name_of_symbolic_link
```

## 14. Remove files

Removes all **[emacs](listmorefiles)** files

- Those ending in **~**

```
  rm -r *~
```

## 15. Create Multiple Directories

Creates multiple [nested](102-tree) directories

```
    mkdir -p parent_dir/child_dir/child_dir
```    
