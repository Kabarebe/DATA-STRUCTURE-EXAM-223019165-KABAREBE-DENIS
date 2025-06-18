#include <iostream>
#include <cstring>
using namespace std;
struct Contact {
    char name[30];
    char phone[15];
};
class ContactBase {
public:
    virtual void display() = 0;
    virtual ~ContactBase() {} 
    Contact basicInfo; 
};
class PersonalContact : public ContactBase {
public:
    char birthday[11];

    PersonalContact(const char* name, const char* phone, const char* bday) {
        strncpy(basicInfo.name, name, sizeof(basicInfo.name) - 1);
        basicInfo.name[sizeof(basicInfo.name) - 1] = '\0';
        strncpy(basicInfo.phone, phone, sizeof(basicInfo.phone) - 1);
        basicInfo.phone[sizeof(basicInfo.phone) - 1] = '\0';
        strncpy(birthday, bday, sizeof(birthday) - 1);
        birthday[sizeof(birthday) - 1] = '\0';
    }

    void display() {
        cout << "Personal Contact: " << basicInfo.name 
             << ", Phone: " << basicInfo.phone 
             << ", Birthday: " << birthday << endl;
    }
};
class ProfessionalContact : public ContactBase {
public:
    char company[40];

    ProfessionalContact(const char* name, const char* phone, const char* comp) {
        strncpy(basicInfo.name, name, sizeof(basicInfo.name) - 1);
        basicInfo.name[sizeof(basicInfo.name) - 1] = '\0';
        strncpy(basicInfo.phone, phone, sizeof(basicInfo.phone) - 1);
        basicInfo.phone[sizeof(basicInfo.phone) - 1] = '\0';
        strncpy(company, comp, sizeof(company) - 1);
        company[sizeof(company) - 1] = '\0';
    }

    void display() {
        cout << "Professional Contact: " << basicInfo.name 
             << ", Phone: " << basicInfo.phone 
             << ", Company: " << company << endl;
    }
};
struct Group {
    char name[30];
    ContactBase** members;
    int memberCount;
    int capacity;

    Group(const char* groupName) {
        strncpy(name, groupName, sizeof(name) - 1);
        name[sizeof(name) - 1] = '\0';
        members = 0;
        memberCount = 0;
        capacity = 0;
    }

    ~Group() {
        delete[] members;
    }

    void addMember(ContactBase* contact) {
        if (!contact) return;

        if (memberCount >= capacity) {
            int newCapacity = (capacity == 0) ? 2 : capacity * 2;
            ContactBase** newMembers = new ContactBase*[newCapacity];
            
            for (int i = 0; i < memberCount; i++) {
                newMembers[i] = members[i];
            }
            
            delete[] members;
            members = newMembers;
            capacity = newCapacity;
        }
        
        members[memberCount++] = contact;
    }

    void removeMember(const char* contactName) {
        if (!contactName) return;

        for (int i = 0; i < memberCount; i++) {
            if (strcmp(members[i]->basicInfo.name, contactName) == 0) {
                for (int j = i; j < memberCount - 1; j++) {
                    members[j] = members[j + 1];
                }
                memberCount--;
                return;
            }
        }
    }

    void displayMembers() {
        cout << "Group: " << name << " (" << memberCount << " members)" << endl;
        for (int i = 0; i < memberCount; i++) {
            cout << "  ";
            members[i]->display();
        }
    }
};
class ContactManager {
private:
    ContactBase** allContacts;
    int contactCount;
    int contactCapacity;
    
    Group** groups;
    int groupCount;
    int groupCapacity;

public:
    ContactManager() : allContacts(0), contactCount(0), contactCapacity(0),
                      groups(0), groupCount(0), groupCapacity(0) {}

    ~ContactManager() {
        for (int i = 0; i < contactCount; i++) {
            delete allContacts[i];
        }
        delete[] allContacts;
        
        for (int i = 0; i < groupCount; i++) {
            delete groups[i];
        }
        delete[] groups;
    }

    void addContact(ContactBase* contact) {
        if (!contact) return;

        if (contactCount >= contactCapacity) {
            int newCapacity = (contactCapacity == 0) ? 2 : contactCapacity * 2;
            ContactBase** newContacts = new ContactBase*[newCapacity];
            
            for (int i = 0; i < contactCount; i++) {
                newContacts[i] = allContacts[i];
            }
            
            delete[] allContacts;
            allContacts = newContacts;
            contactCapacity = newCapacity;
        }
        
        allContacts[contactCount++] = contact;
    }

    void addGroup(const char* groupName) {
        if (!groupName) return;

        if (groupCount >= groupCapacity) {
            int newCapacity = (groupCapacity == 0) ? 2 : groupCapacity * 2;
            Group** newGroups = new Group*[newCapacity];
            
            for (int i = 0; i < groupCount; i++) {
                newGroups[i] = groups[i];
            }
            
            delete[] groups;
            groups = newGroups;
            groupCapacity = newCapacity;
        }
        
        groups[groupCount++] = new Group(groupName);
    }

    void removeGroup(const char* groupName) {
        if (!groupName) return;

        for (int i = 0; i < groupCount; i++) {
            if (strcmp(groups[i]->name, groupName) == 0) {
                delete groups[i];
                for (int j = i; j < groupCount - 1; j++) {
                    groups[j] = groups[j + 1];
                }
                groupCount--;
                return;
            }
        }
    }

    Group* findGroup(const char* groupName) {
        if (!groupName) return 0;

        for (int i = 0; i < groupCount; i++) {
            if (strcmp(groups[i]->name, groupName) == 0) {
                return groups[i];
            }
        }
        return 0;
    }

    void displayAllContacts() {
        cout << "All Contacts (" << contactCount << "):" << endl;
        for (int i = 0; i < contactCount; i++) {
            allContacts[i]->display();
        }
    }

    void displayAllGroups() {
        cout << "All Groups (" << groupCount << "):" << endl;
        for (int i = 0; i < groupCount; i++) {
            groups[i]->displayMembers();
        }
    }
    ContactBase* getContact(int index) {
        if (index >= 0 && index < contactCount) {
            return allContacts[index];
        }
        return 0;
    }
};
int main() {
    ContactManager manager;
    manager.addContact(new PersonalContact("kabarebe denis", "079-189-3416", "2003-12-19"));
    manager.addContact(new ProfessionalContact("ihirwe daric", "073-104-0833", "comp arch"));
    manager.addContact(new PersonalContact("mukamunana alice", "078-026-2428", "1982-11-1"));
    manager.addGroup("Family");
    manager.addGroup("Work");
    Group* family = manager.findGroup("Family");
    if (family) {
        family->addMember(manager.getContact(0)); 
        family->addMember(manager.getContact(2));
    }
    
    Group* work = manager.findGroup("Work");
    if (work) {
        work->addMember(manager.getContact(1));
    }
    manager.displayAllContacts();
    cout << endl;
    manager.displayAllGroups();
    
    return 0;
}
