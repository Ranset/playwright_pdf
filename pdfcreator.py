from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright
import os

# 1. Prepare your dynamic data
data = {
    "title": "Monthly Report",
    "user": "Alex",
    "items": ["Automation", "Reporting", "Testing"]
}

# 2. Render HTML using Jinja2
ruta_template = os.path.join(os.path.dirname(__file__), 'Template1')
nombre_template = 'index.html'

env = Environment(loader=FileSystemLoader(ruta_template))
template = env.get_template(nombre_template)
html_content = template.render(data)

# 3. Write HTML to a temporary file in the template directory
temp_html_path = os.path.join(ruta_template, 'temp.html')
with open(temp_html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# 4. Use Playwright to generate the PDF
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Load the HTML file
    page.goto(f"file://{temp_html_path}")
    
    # Generate the PDF
    page.pdf(
        path="report.pdf",
        format="A4",
        print_background=True, # Importante para colores y fondos
        margin={"top": "1cm", "bottom": "1cm"}
        )
    browser.close()

# 5. Clean up the temporary file
os.remove(temp_html_path)
