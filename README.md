# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
<img width="936" height="750" alt="image" src="https://github.com/user-attachments/assets/b416f82a-e34b-4b31-bb73-9e735e3c4e44" />


### Flowchart of the main workflow

```mermaid
flowchart TD
    A[Start Application] --> B[Print Banner]
    B --> C[Initialize Data<br/>Load from files or seed defaults]
    C --> D[Display Login Menu]
    D --> E{User Choice}
    E -->|1. Login as Student| F[Student Login]
    E -->|2. Login as Admin| G[Admin Login]
    E -->|3. Exit| H[Save Data and Exit]
    
    F --> I{Valid Student ID?}
    I -->|Yes| J[Display Student Menu]
    I -->|No / New| K[Create New Student Profile]
    K --> L{Profile Created?}
    L -->|Yes| J
    L -->|No| D
    
    G --> M{Password Correct?}
    M -->|Yes| N[Display Admin Menu]
    M -->|No| D
    
    J --> O{Student Menu Choice}
    O -->|1. View Catalog| P[View Course Catalog]
    O -->|2. Register| Q[Register for Course]
    O -->|3. Drop| R[Drop Course]
    O -->|4. View Schedule| S[View My Schedule]
    O -->|5. Billing| T[Billing Summary]
    O -->|6. Edit Profile| U[Edit Profile]
    O -->|7. Logout| V[Save Data]
    V --> D
    
    N --> W{Admin Menu Choice}
    W -->|1. View Catalog| P
    W -->|2. View Roster| X[View Class Roster]
    W -->|3. View Students| Y[View All Students]
    W -->|4. Add Student| Z[Add New Student]
    W -->|5. Edit Student| AA[Edit Student Profile]
    W -->|6. Add Course| BB[Add New Course]
    W -->|7. Edit Course| CC[Edit Course]
    W -->|8. View Schedule| DD[View Student Schedule]
    W -->|9. Billing| EE[Billing Summary]
    W -->|10. Logout| V
    
    P --> J
    Q --> J
    R --> J
    S --> J
    T --> J
    U --> J
    X --> N
    Y --> N
    Z --> N
    AA --> N
    BB --> N
    CC --> N
    DD --> N
    EE --> N
```

### Prompts
create view function but in  python version
