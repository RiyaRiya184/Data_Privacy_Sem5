# Practical 02 — Privacy Impact Assessment (PIA) of Ramanujan College ERP

**Subject:** Data Privacy
**Practical No.:** 02
**Practical Title:** Privacy Impact Assessment of a Student ERP System
**Organization:** Ramanujan College, University of Delhi
**System:** Ramanujan College Student ERP / Portal
**Assessment Type:** Privacy Impact Assessment (PIA)

---

## 1. Aim

To conduct a Privacy Impact Assessment (PIA) of the Ramanujan College Student ERP system in order to identify the types of personal data that may be processed, assess potential privacy risks, and suggest appropriate measures for protecting student privacy.

---

## 2. Objectives

The objectives of this practical are:

* To understand the purpose of a Privacy Impact Assessment.
* To identify personal and academic information handled by a student ERP system.
* To identify possible privacy risks associated with the collection, storage, and use of student data.
* To assess the possible impact of privacy risks on students.
* To recommend appropriate privacy safeguards and mitigation measures.
* To understand the importance of privacy-by-design in educational information systems.

---

## 3. Introduction

A Privacy Impact Assessment (PIA) is a structured process used to identify and evaluate privacy risks associated with a system, application, project, or technology.

Educational ERP systems can handle significant amounts of student information, including identity information, academic records, attendance, examination-related information, contact details, and other administrative information.

Ramanujan College, University of Delhi, uses digital systems and customized ERP solutions for student-related administrative processes. The college states that its customized ERP solution is used to manage student attendance and that digital portals are used for various student and examination-related processes.

Therefore, a privacy assessment is useful for identifying the types of information involved and considering appropriate safeguards.

---

## 4. System Under Assessment

**System:** Ramanujan College Student ERP / Student Portal

**Organization:** Ramanujan College, University of Delhi

**Website:** https://ramanujancollege.ac.in/

The college provides student-related online services through its website and associated portals. The college has also documented the use of a customized ERP solution for managing student attendance.

The publicly accessible Ramanujan College login page provides fields for a username/e-mail and password, along with a "Remember Me" option and a password recovery option.

---

## 5. Data Flow Considered in the Assessment

The simplified data flow for a student ERP system can be represented as:

```text
             STUDENT
                |
                v
        +----------------+
        |  Student ERP   |
        |    Portal      |
        +----------------+
                |
        +-------+-------+
        |       |       |
        v       v       v
    Student   Faculty  Administration
     Data      Data        Data
        |       |       |
        +-------+-------+
                |
                v
       Academic / Admin
          Processes
```

The exact internal architecture and data flows of the ERP were not publicly verified during this assessment.

---

## 6. Categories of Personal Data

The following categories may be relevant to a student ERP system. The exact fields should be verified from the authorized student interface.

| Data Category              | Examples                                           | Privacy Sensitivity |
| -------------------------- | -------------------------------------------------- | ------------------- |
| Identity Information       | Name, university/form number                       | Medium              |
| Contact Information        | Email, phone number, address                       | High                |
| Academic Information       | Course, semester, subjects, marks                  | High                |
| Attendance Information     | Attendance percentage, attendance records          | High                |
| Examination Information    | Examination forms, results, admit-card information | High                |
| Account Information        | Username, password-related information             | Very High           |
| Administrative Information | Fee or application-related records                 | High                |
| Supporting Documents       | Uploaded certificates or documents                 | High / Very High    |

**Note:** This table describes categories that may be processed by a student ERP. It does not claim that every listed field is currently collected by the publicly accessible portal.

---

## 7. Privacy Impact Assessment

### 7.1 Data Collection

A student ERP may require personal and academic information to provide student services.

### Potential Privacy Risk

If unnecessary information is collected, the amount of personal information exposed in the event of unauthorized access may increase.

### Recommended Mitigation

* Collect only information necessary for the particular service.
* Clearly communicate why each major category of information is required.
* Periodically review whether previously collected information is still necessary.

---

### 7.2 Data Storage

Student information may need to be stored so that authorized departments can provide academic and administrative services.

### Potential Privacy Risk

Unauthorized access to stored records could expose academic, contact, or identity information.

### Recommended Mitigation

* Use strong authentication mechanisms.
* Apply encryption to sensitive information where appropriate.
* Restrict database access to authorized personnel.
* Maintain appropriate access logs.

---

### 7.3 Authentication and Account Security

The publicly accessible Ramanujan College login page provides username/e-mail and password fields and includes a password-recovery option.

### Potential Privacy Risk

Compromised credentials could potentially allow unauthorized access to a student's account and information.

### Recommended Mitigation

* Encourage strong and unique passwords.
* Implement appropriate password policies.
* Use multi-factor authentication where feasible.
* Apply rate limiting and account protection mechanisms.
* Provide secure password-reset procedures.

---

### 7.4 Role-Based Access

Different users of an ERP system may have different responsibilities.

For example:

```text
Student
   |
   +--> Own academic information

Faculty
   |
   +--> Relevant teaching / attendance information

Administration
   |
   +--> Authorized administrative information

System Administrator
   |
   +--> Technical system management
```

### Potential Privacy Risk

If permissions are incorrectly configured, a user could potentially access information beyond what is required for their role.

### Recommended Mitigation

* Implement role-based access control.
* Follow the principle of least privilege.
* Regularly review user permissions.
* Remove access when a person's role changes.
* Maintain audit logs for sensitive operations.

---

### 7.5 Data Sharing

Student information may need to move between authorized institutional systems for academic and administrative purposes.

### Potential Privacy Risk

Students may not always understand which organizations, departments, or service providers can access their information.

### Recommended Mitigation

* Clearly disclose relevant categories of data sharing.
* Use contractual and technical safeguards for third-party processors.
* Share only the minimum information necessary.
* Maintain records of authorized data flows.

---

### 7.6 Data Retention

Student records may need to be retained for academic, legal, administrative, or archival purposes.

### Potential Privacy Risk

Retaining personal information longer than necessary increases the period during which the information could be exposed.

### Recommended Mitigation

* Define retention periods for different categories of information.
* Review stored information periodically.
* Securely delete or anonymize information when retention is no longer required.

---

### 7.7 Student Rights and Transparency

Students should be able to understand how their personal information is processed and whom they can contact regarding privacy concerns.

### Potential Privacy Risk

If privacy information is difficult to locate or understand, students may not have sufficient awareness of how their data is handled.

### Recommended Mitigation

Provide an accessible privacy notice explaining:

* What information is collected.
* Why it is collected.
* How it is used.
* Who may receive it.
* How long it is retained.
* How students can raise privacy-related concerns.

---

## 8. Risk Assessment

| Risk                                    | Likelihood | Potential Impact | Risk Level      |
| --------------------------------------- | ---------- | ---------------- | --------------- |
| Compromised student credentials         | Medium     | High             | High            |
| Unauthorized access to academic records | Medium     | High             | High            |
| Excessive data collection               | Unknown    | Medium           | Review Required |
| Incorrect user permissions              | Unknown    | High             | Review Required |
| Excessive data retention                | Unknown    | Medium           | Review Required |
| Lack of privacy awareness               | Medium     | Medium           | Medium          |
| Exposure through screenshots/exports    | Medium     | Medium           | Medium          |

**Note:** These are qualitative assessment values for an academic PIA. They are not measurements of confirmed vulnerabilities in the Ramanujan College ERP.

---

## 9. Privacy-by-Design Recommendations

The following measures can help reduce privacy risks:

1. **Data Minimization**
   Collect only the information required for a specific purpose.

2. **Purpose Limitation**
   Use information for clearly defined and legitimate purposes.

3. **Access Control**
   Ensure users can access only information required for their role.

4. **Strong Authentication**
   Use strong passwords and consider multi-factor authentication.

5. **Encryption**
   Protect sensitive information during transmission and storage where appropriate.

6. **Audit Logging**
   Maintain logs of important access and administrative actions.

7. **Retention Management**
   Establish and review data retention periods.

8. **Transparency**
   Provide students with understandable privacy information.

9. **Secure Data Disposal**
   Securely delete or anonymize information that is no longer required.

10. **Regular Privacy Reviews**
    Conduct periodic privacy and security assessments.

---

## 10. Overall PIA Summary

The Ramanujan College ERP supports digital student-related processes and therefore may involve the processing of important personal and academic information.

The major privacy considerations identified in this assessment are:

* Protection of student credentials.
* Protection of academic and attendance records.
* Appropriate role-based access.
* Data minimization.
* Secure storage and transmission.
* Appropriate retention periods.
* Transparency regarding data processing.
* Secure handling of exported or shared student information.

A complete internal assessment would require access to system documentation, data-flow diagrams, retention schedules, privacy notices, security configurations, and authorized administrative information. These were outside the scope of this student-side assessment.

---

## 11. Conclusion

The Privacy Impact Assessment demonstrates that student ERP systems require strong privacy controls because they can process multiple categories of personal and academic information.

The assessment highlights the importance of data minimization, access control, authentication, secure storage, transparency, retention management, and regular privacy reviews.

Privacy should be considered throughout the lifecycle of an ERP system rather than only after a privacy incident occurs.

---

## 12. Evidence / Screenshots

The following screenshots can be included as evidence:

| Screenshot                   | Description                                        |
| ---------------------------- | -------------------------------------------------- |
| `01-ramanujan-homepage.png`  | Ramanujan College official homepage                |
| `02-erp-login.png`           | ERP / student login page                           |
| `03-student-services.png`    | Relevant student-services page                     |
| `04-privacy-information.png` | Privacy-related information, if publicly available |

**Important:** Personal information, usernames, student IDs, passwords, phone numbers, email addresses, and other sensitive information must be hidden before uploading screenshots.

---

## 13. References

1. Ramanujan College, University of Delhi — Official Website
   https://ramanujancollege.ac.in/

2. Ramanujan College — Student Section
   https://ramanujancollege.ac.in/students/

3. Ramanujan College — e-Governance Information
   https://ramanujancollege.ac.in/6-2-3/6.2.3-E-Governance.pdf/

4. Ramanujan College — Student/ERP Login
   https://ramanujancollege.ac.in/accounts/login/

---

**Practical Status:** Completed as a non-invasive, student-side Privacy Impact Assessment.
