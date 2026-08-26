import os

# Base directories
POLICIES_DIR = "data/policies"
RAW_DIR = "data/raw"

# Ensure directories exist
os.makedirs(POLICIES_DIR, exist_ok=True)
os.makedirs(RAW_DIR, exist_ok=True)

# Dictionary of new policies
policies = {
    "benefits_policy": {
        "txt": """# Benefits Policy

The company provides a comprehensive benefits package to support employee well‑being. 
Eligible employees receive health insurance, dental coverage, and vision plans beginning after 90 days of employment.

The company also offers a retirement savings plan with employer matching. 
Additional voluntary benefits include life insurance, disability coverage, and wellness programs.

Employees may review detailed benefit summaries through the HR portal.
""",
        "md": """# Benefits Policy

The company provides a comprehensive benefits package to support employee well‑being.

## Health & Wellness
Eligible employees receive:
- Health insurance  
- Dental coverage  
- Vision plans  
Starting after 90 days of employment.

## Retirement
The company offers a retirement savings plan with employer matching.

## Voluntary Benefits
Employees may enroll in:
- Life insurance  
- Disability coverage  
- Wellness programs  

More details are available in the HR portal.
"""
    },

    "attendance_policy": {
        "txt": """# Attendance Policy

Employees are expected to maintain regular and reliable attendance. 
Work schedules must be followed unless prior approval is obtained from a manager.

Absences should be reported at least one hour before the scheduled shift. 
Repeated unexcused absences may result in disciplinary action.

Employees arriving more than ten minutes late are considered tardy.
""",
        "md": """# Attendance Policy

## Expectations
Employees must maintain regular attendance and follow assigned work schedules.

## Absences
Absences must be reported at least one hour before the shift.  
Unexcused absences may lead to disciplinary action.

## Tardiness
Employees arriving more than ten minutes late are considered tardy.
"""
    },

    "travel_policy": {
        "txt": """# Travel Policy

Business travel must be approved by a manager before any reservations are made. 
Employees should use cost‑effective transportation and lodging options.

Receipts must be submitted within 14 days of completing travel. 
The company reimburses airfare, lodging, meals, and ground transportation when used for business purposes.

Personal travel expenses are not reimbursable.
""",
        "md": """# Travel Policy

## Approval
All business travel requires manager approval before booking.

## Reimbursable Items
The company reimburses:
- Airfare  
- Lodging  
- Meals  
- Ground transportation  

Receipts must be submitted within 14 days.

## Non‑Reimbursable
Personal travel costs are not reimbursed.
"""
    },

    "anti_harassment_policy": {
        "txt": """# Anti‑Harassment Policy

The company is committed to maintaining a workplace free from harassment. 
Harassment based on race, gender, religion, disability, or any protected characteristic is strictly prohibited.

Employees must report incidents immediately to HR or a manager. 
All reports will be investigated promptly and confidentially.

Retaliation against individuals who report harassment is prohibited.
""",
        "md": """# Anti‑Harassment Policy

## Zero Tolerance
Harassment of any kind is prohibited.

## Reporting
Employees must report incidents to HR or a manager.  
Reports are investigated promptly and confidentially.

## Retaliation
Retaliation against individuals who report harassment is not allowed.
"""
    },

    "data_protection_policy": {
        "txt": """# Data Protection Policy

Employees must protect company data from unauthorized access, disclosure, or loss. 
Confidential information must be stored only in approved systems.

Sensitive data should never be shared through personal email or unencrypted channels. 
Employees must follow all data retention and deletion guidelines.

Any suspected data breach must be reported immediately.
""",
        "md": """# Data Protection Policy

## Data Handling
Confidential data must be stored in approved systems only.

## Security Requirements
Employees must avoid:
- Personal email  
- Unencrypted channels  
- Unauthorized storage  

## Incident Reporting
Suspected data breaches must be reported immediately.
"""
    },

    "it_usage_policy": {
        "txt": """# IT Usage Policy

Company technology resources must be used responsibly and primarily for business purposes. 
Employees may not install unauthorized software on company devices.

Internet usage should align with professional standards. 
Accessing inappropriate or illegal content is prohibited.

Company devices must remain updated with approved security patches.
""",
        "md": """# IT Usage Policy

## Acceptable Use
Technology resources must be used for business purposes.

## Restrictions
Employees may not:
- Install unauthorized software  
- Access inappropriate content  

## Security
Devices must remain updated with approved patches.
"""
    },

    "reimbursement_policy": {
        "txt": """# Reimbursement Policy

Employees may request reimbursement for approved business expenses. 
All reimbursement claims must include itemized receipts.

Requests must be submitted within 14 days of the expense. 
Managers review all claims before payment is issued.

Luxury purchases or personal items are not reimbursable.
""",
        "md": """# Reimbursement Policy

## Requirements
Reimbursement requests must include itemized receipts.

## Submission Timeline
Requests must be submitted within 14 days.

## Restrictions
Personal items and luxury purchases are not reimbursed.
"""
    },

    "hr_general_policy": {
        "txt": """# HR General Policy

The HR department oversees employee relations, onboarding, performance reviews, and workplace compliance. 
Employees should contact HR for questions regarding policies, benefits, or workplace concerns.

HR maintains all personnel records and ensures compliance with labor regulations.
""",
        "md": """# HR General Policy

## Responsibilities
HR manages:
- Employee relations  
- Onboarding  
- Performance reviews  
- Compliance  

## Employee Support
Employees may contact HR for policy or benefits questions.

## Records
HR maintains personnel records and ensures regulatory compliance.
"""
    },

    "workplace_behavior_policy": {
        "txt": """# Workplace Behavior Policy

Employees are expected to behave professionally and respectfully at all times. 
Bullying, intimidation, or disruptive behavior is not tolerated.

Employees should resolve conflicts constructively and seek manager support when needed.
""",
        "md": """# Workplace Behavior Policy

## Expectations
Employees must behave professionally and respectfully.

## Prohibited Behavior
Bullying, intimidation, and disruptive conduct are not allowed.

## Conflict Resolution
Employees should resolve conflicts constructively and involve managers when necessary.
"""
    }
}

# Write files
for name, content in policies.items():
    txt_path = os.path.join(POLICIES_DIR, f"{name}.txt")
    md_path = os.path.join(RAW_DIR, f"{name}.md")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(content["txt"])

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content["md"])

print("All missing policy files created successfully!")
