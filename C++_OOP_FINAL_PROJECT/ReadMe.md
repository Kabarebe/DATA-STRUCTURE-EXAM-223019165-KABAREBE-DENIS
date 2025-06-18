Line 1, #include<iostream>: it help for allowing input and output libraries
Line 2, #include<iostream>: provide string function like strncpy
Line 3, Using namespace std: help for preventing duplication of std:: prefix 
Line 4, Struct contact: we create structure called contact for storing contact information
Line 5, Char name[30]: creating character  variable called name 
Line 6, Char phone[15]: creating character variable called phone 
Line 8, Class contactbase : creating base class called contactbase for all contacts
Line 10, Virtual void display()=0; all contacts must have display()
Line 11, Virtual 	~contactbase() : it is for cleanup when deleting
Line 12, Contact basicinfo: every contact has name/phone
Line 14, Class personalcontact: public contactbase : child class which inherits from class contactbase
Line 16, Char birthday[11]: variable called birthday 
Line 18, Personalcontact(const char*name,const char*phone,const char*bday): it help for creating constructor
Line 19, Strncpy(basicinfo.name,name,29): it copy name safely
Line 20, Basicinfo.name[29]=’\0’ :add end maker
Line 22, Strncpy(basicinfo.phone,phone,14): copy phone
Line 23, Strncpy(birthday,bday,10): copy birthday
Line 27, Void display() : function to display personal contacts
Line 28, Cout<<basicinfo.name: to display name
Line 29, Cout<<phone: to display phone
Line 30, Cout<<birthday: to display birthday
Line 33, Class professionalcontact: public contactbase : inheritance from contact base
Line 35,Char company[30] : variable called company
Line 37, Professionalcontact(const char*name,const char*phone,const char*comp): it help for creating constructor
Line 38, Strncpy(basicinfo.name,name,29): it copy name safely
Line 39, Basicinfo.name[29]=’\0’ :add end maker
Line 41, Strncpy(basicinfo.phone,phone,14): copy phone
Line 42, Strncpy(company,comp,29): copy company name
Line 43, Company[29]=’\0’ : add end maker
Line 46, Void display() : function to display personal contacts
Line 47, Cout<<basicinfo.name: to display name
Line 48, Cout<<phone: to display phone
Line 49, Cout<<birthday: to display birthday
Line 52, Struct group : structure called group
Line 53, Char name[20]: variable for group name
Line 54, Contactbase** : array to store group members
Line 55, Int membercount: integer variable for storing current members
Line 56, Int capacity: variable to store maximum capacity
Line 58, Group(const char* groupname) : creation of constructor
Line 61, Member=0 : we start with no members
Line 62, Membercount=0 : even count is zero
Line 63, Capacity=0: capacity equals zero
Line 66, ~group() : destructor
Line 67, Delete[]members: to free members array
Line 70, Void addmember(contactbase*contact) : function to add new contact
Line 71, If(!contact) return: is to ignore null contacts
Line 73, If(1membercount>=capacity) : need more space
Line 77, For(int i=0;i<=membercount;i++) : looping 
Line 78, Newmembers[i]=members[i] : copying old members
Line 81, Delete[]members : to remove old array
Line 82, Members=newmembers : use new bigger array
Line 86, Members[membercount++]=contact : add new member
Line 111, Class contactmanager : creation of class called contactmanager
Line 113, Contactbase**allcontacts : all contact list
Line 114, Int contactcount: for  current contacts
Line 115, Int contactcapacity: max contacts possible
Line 125, ~contactmanager() : destructor
Line 126, For(int i=0;i<contactcount;i++): looping
Line 129, Delete[]allcontacts : for deleting all contact
Line 131, For(int i=0;i<groupcount;i++): looping
Line 134, Delete[]groups : for deleting all contact
Line 221, Int main() : indicate program where it start to excute
Line 222, Contactmanager manager : creation of object.
Line 223, Adding contact1
Line 224, Adding contact2
Line 225, Adding contact 3
Line 226, Creation of group called family
Line 227, Creation of group called work
Line 230, Adding contact1 to family
Line 231, Adding contact2 to family
Line 236, Adding contact3 to work
Line 238, Manager.displayallcontacts(): displaying contact
Line 240, Manager.displayallgroups() : displaying groups
Line 242, Return 0 : end of our program


