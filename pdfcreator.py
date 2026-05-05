from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright

# 1. Prepare your dynamic data
data = {
    "title": "Monthly Report",
    "user": "Alex",
    "items": ["Automation", "Reporting", "Testing"]
}

# 2. Render HTML using Jinja2
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')
html_content = template.render(data)

# 3. Use Playwright to generate the PDF
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Set the content directly from the Jinja2 output
    page.set_content(html_content)
    
    # Generate the PDF
    page.pdf(path="report.pdf", format="A4")
    browser.close()
