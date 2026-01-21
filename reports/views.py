from django.shortcuts import render
from cvss import CVSS3
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

VULNERABILITY_EXAMPLES = {
    "Low": {
        "title": "Information Disclosure",
        "example": "Server version exposed in HTTP headers",
        "impact": "Helps attackers gather system information",
        "fix": "Hide server headers and debug information"
    },
    "Medium": {
        "title": "Cross-Site Scripting (XSS)",
        "example": "User input is reflected without sanitization",
        "impact": "Session hijacking or phishing attacks",
        "fix": "Validate and escape user input"
    },
    "High": {
        "title": "Authentication Bypass",
        "example": "Broken access control allows unauthorized login",
        "impact": "Account takeover and data exposure",
        "fix": "Enforce proper authentication and authorization checks"
    },
    "Critical": {
        "title": "SQL Injection / Remote Code Execution",
        "example": "Attacker executes database or system commands",
        "impact": "Full system compromise and data loss",
        "fix": "Use parameterized queries and input validation"
    }
}
OWASP_MAPPING = {
    "Low": {
        "id": "A06:2021",
        "name": "Vulnerable and Outdated Components",
        "description": "Using outdated libraries or components with known issues."
    },
    "Medium": {
        "id": "A03:2021",
        "name": "Injection",
        "description": "Untrusted data sent to interpreters such as SQL, OS, or LDAP."
    },
    "High": {
        "id": "A02:2021",
        "name": "Broken Authentication",
        "description": "Weak authentication mechanisms allowing account compromise."
    },
    "Critical": {
        "id": "A01:2021",
        "name": "Broken Access Control",
        "description": "Unauthorized access to data or functionality."
    }
}


from django.shortcuts import render
from cvss import CVSS3

def cvss_form(request):
    # Handle GET request (just show the form)
    if request.method == "GET":
        return render(request, 'reports/cvss_form.html')

    # Handle POST request (calculate CVSS)
    if request.method == "POST":
        av = request.POST.get('av')
        ac = request.POST.get('ac')
        pr = request.POST.get('pr')
        ui = request.POST.get('ui')
        s  = request.POST.get('s')
        c  = request.POST.get('c')
        i  = request.POST.get('i')
        a  = request.POST.get('a')

        vector = f"CVSS:3.1/AV:{av}/AC:{ac}/PR:{pr}/UI:{ui}/S:{s}/C:{c}/I:{i}/A:{a}"

        cvss = CVSS3(vector)
        score = cvss.scores()[0]
        severity = cvss.severities()[0]

        example = VULNERABILITY_EXAMPLES.get(severity, {})
        owasp = OWASP_MAPPING.get(severity, {})

        return render(request, 'reports/report.html', {
            'vector': vector,
            'score': score,
            'severity': severity,
            'example': example,
            'owasp': owasp,
        })


    return render(request, 'reports/cvss_form.html')

def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cvss_report.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    p.setFont("Helvetica", 14)
    p.drawString(50, height - 50, "CVSS Risk Severity Report")

    p.setFont("Helvetica", 11)
    p.drawString(50, height - 100, f"CVSS Vector: {request.GET.get('vector')}")
    p.drawString(50, height - 130, f"Score: {request.GET.get('score')}")
    p.drawString(50, height - 160, f"Severity: {request.GET.get('severity')}")

    p.drawString(50, height - 220, "Recommendation:")
    p.drawString(50, height - 250, "Apply security patches and validate inputs.")

    p.showPage()
    p.save()

    return response

