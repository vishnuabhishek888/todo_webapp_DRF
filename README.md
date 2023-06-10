# todo_webapp_DRF
todo webapp using Django Rest framework.
To use this code you need to install some 
To create Virtual Enviornment --

1). python -m venv <path/to/venv>
2). Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
3). .\myenv\Scripts\Activate.ps1

- To install Django --
   pip install django
- To intall Djnago Rest Framework
   pip install djangorestframework
  
 migrations command -
    python manage.py makemigrations
    
migrate command- 
    python manage.py migrate
    
create superuser-
    python manage.py createsuperuser 
    
to runserver -
    python manage.py runserver
    
    
Description:  You  need  to  design  backend  for  a  web-based  To-do  List  application,  as  per  the given  requirements:
1.      Create  a  Django  app  with  appropriate  models  to  store  information  for  the  To-do  List app.  The  app  should  be  able  to  store  the  following  information:
a.      Timestamp:  Timestamp  at  which  a  task  was  created.
Should  be  auto-set  when  creating  a  new  entry.  A  user  should  not  be  able  to edit  this.
b.      Title:  Title  of  the  task  to  be  done.
i.             A  user  can  set  this  while  creating  a  new  entry.  A  user  can  also  change this  while  updating  an  existing  entry.
ii.             Max  length:  100  characters.
iii.             Mandatory  field
c.      Description:  Description  of  the  task  to  be  done.
i.             A  user  can  add  details  about  this  task.
ii.             Max  length:  1000  characters
iii.             Mandatory  field
d.      Due  Date:  Expected  due  date  to  finish  the  task
i.             A  user  can  set  this  while  creating  a  new  entry.  A  user  can  also  change this  while  updating  an  existing  entry.
ii.             Optional  field
e.      Tag:  One  or  more  tags  that  the  user  can  add  to  the  entry
i. A user can set this while creating a new entry. A user can also change this while updating an existing entry. Multiple tags can be added to the same entry
ii.             Optional  field
iii.             Multiple  tags  with  the  same  value  should  be  saved  only  once.
f.        Status:  Shows  status  of  a  task
i.             Should  be  one  of  these  values.
1.      OPEN  (Default  value)
2.      WORKING
3.      DONE
4.      OVERDUE
ii.             Mandatory  field
  
  
   
