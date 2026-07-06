
# RAID Log – Healthcare Appointment System

## Purpose

The RAID Log is used to identify, track, and monitor **Risks, Assumptions, Issues, and Dependencies** throughout the project lifecycle. It is reviewed during Sprint Planning, Sprint Review, and regular project governance meetings to ensure proactive risk management.

---

# Risks

| ID   | Risk                                                  | Probability | Impact | Mitigation                                                 | Owner            | Status    |
| ---- | ----------------------------------------------------- | ----------- | ------ | ---------------------------------------------------------- | ---------------- | --------- |
| R-01 | Delay in third-party notification service integration | Medium      | High   | Engage vendor early and validate APIs during Sprint 1      | Technical Lead   | Open      |
| R-02 | Changing business requirements                        | High        | Medium | Conduct regular backlog refinement and stakeholder reviews | Product Owner    | Open      |
| R-03 | Key team member unavailable                           | Medium      | High   | Cross-train team members and maintain documentation        | Scrum Master     | Mitigated |
| R-04 | Performance issues during peak booking hours          | Low         | High   | Perform load testing before production release             | Development Team | Open      |

---

# Assumptions

| ID   | Assumption                                                          | Owner            | Status |
| ---- | ------------------------------------------------------------------- | ---------------- | ------ |
| A-01 | Doctors will maintain accurate availability schedules               | Product Owner    | Valid  |
| A-02 | Patients have internet access and valid contact information         | Business Sponsor | Valid  |
| A-03 | Required APIs from external providers will be available on schedule | Technical Lead   | Valid  |
| A-04 | All stakeholders will participate in Sprint Reviews                 | Scrum Master     | Valid  |

---

# Issues

| ID   | Issue                                                                     | Priority | Action                               | Owner            | Status      |
| ---- | ------------------------------------------------------------------------- | -------- | ------------------------------------ | ---------------- | ----------- |
| I-01 | Appointment reminder service intermittently fails in the test environment | High     | Investigate logs and retry mechanism | Development Team | In Progress |
| I-02 | UI alignment issues on mobile devices                                     | Medium   | Update responsive layouts            | UI Developer     | Open        |
| I-03 | Test environment unavailable during regression testing                    | High     | Coordinate with infrastructure team  | DevOps Engineer  | Resolved    |

---

# Dependencies

| ID   | Dependency                 | Owner               | Status    |
| ---- | -------------------------- | ------------------- | --------- |
| D-01 | Authentication service     | Technical Lead      | On Track  |
| D-02 | Email notification service | Development Team    | On Track  |
| D-03 | SMS gateway integration    | External Vendor     | Pending   |
| D-04 | Database provisioning      | Infrastructure Team | Completed |

---

# RAID Review Process

The RAID Log is reviewed:

* During Sprint Planning
* During Backlog Refinement
* In Weekly Project Status Meetings
* During Sprint Reviews (for major risks)
* During Release Planning

Any new Risks, Assumptions, Issues, or Dependencies identified by the Scrum Team or stakeholders are added, assessed, assigned an owner, and tracked until closure.

---

# Escalation Criteria

Items should be escalated when they:

* Impact Sprint Goal achievement.
* Affect the planned release timeline.
* Introduce significant business or technical risk.
* Require external stakeholder decisions.
* Cannot be resolved by the Scrum Team within the sprint.

---

# Version History

| Version | Date      | Description                                                         |
| ------- | --------- | ------------------------------------------------------------------- |
| 1.0     | July 2026 | Initial RAID Log created for Healthcare Appointment System project. |
