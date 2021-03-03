__Optimal Campusing__
-----
### **ALGORITHM**
##### 1. Take input of number_of_companies (m), number_of_students (n) and number_of_time_slots (t).
##### 2. Create the number of companies, students and slots as per requirement and keep them stored on separate lists or arrays. So the space complexity till now is *O(m+n+t)*.
##### 3. Initialize the mutual preferences of both the students and the companies with some randomization. Not considering time complexity of these steps as they are needed only to automate the testing. Create two dictionaries like slot-vs-student and slot-vs-company to mark the visited entries per slot.
##### 4. Next we take the combinations of both the preferences of compaies and students to calculate the priority. If a company c-1 prefers student s-1 and the student prefers the company in return, the priority will become 2, whereas one-sided priorities will be marked as 1. Not considering no priority as part of this solution though.
##### 5. Now we sort this combo-to-priority dictionary by values i.e. descending priorities. The assumption here is that priority-2 > priority-1 > priority-0.
##### 6. Now is the time to traverse the sorted combo-to-priority dictionary and check for some available slots.
##### 7. If the combo is not marked for the given company-slot (in slot-vs-company dictionary) or student-slot position (in slot-vs-student dictionary), then only we'll assign the student-company combination into the given slot, iterate over the other slots otherwise.
##### 8. As we are going by the priorities high to low, we value both the student and company preferences without bias.
&nbsp;
### **EXAMPLE OUTPUT**
##### Let's take a sample input of:
* **number_of_companies (m):** 5
* **number_of_students (n):** 10
* **number_of_time_slots (t):** 8

```javascript
{
    "1": {
        "C-3": "S-1, 2",
        "C-4": "S-3, 2",
        "C-2": "S-7, 1",
        "C-1": "S-4, 1",
        "C-5": "S-8, 1"
    },
    "2": {
        "C-4": "S-5, 2",
        "C-3": "S-2, 1",
        "C-1": "S-3, 1",
        "C-2": "S-9, 1",
        "C-5": "S-6, 1"
    },
    "3": {
        "C-4": "S-6, 2",
        "C-3": "S-4, 1",
        "C-1": "S-1, 1",
        "C-2": "S-2, 1",
        "C-5": "S-3, 1"
    },
    "4": {
        "C-4": "S-4, 1",
        "C-3": "S-7, 1",
        "C-2": "S-6, 1",
        "C-5": "S-2, 1"
    },
    "5": {
        "C-3": "S-8, 1",
        "C-4": "S-9, 1",
        "C-1": "S-7, 1"
    },
    "6": {
        "C-4": "S-10, 1",
        "C-3": "S-9, 1"
    },
    "7": {
        "C-3": "S-5, 1"
    },
    "8": {
        "C-3": "S-6, 1"
    }
}
```
##### This lists all the slots with the combination of company and student with their priority appended to the end.