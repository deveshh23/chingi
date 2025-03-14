from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Read the HTML file content
    with open('templates/birthday.html', 'r') as file:
        html_content = file.read()
    # Return the HTML content directly
    return html_content

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files (images, videos, etc.)"""
    return send_from_directory('static', filename)

if __name__ == '__main__':
    # Make sure the templates and static directories exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    # Create the birthday.html file in the templates directory if it doesn't exist
    if not os.path.exists('templates/birthday.html'):
        with open('templates/birthday.html', 'w') as file:
            # You'll need to paste your HTML content here
            file.write("""<!DOCTYPE html>
<!-- Your HTML content here -->
</html>""")
    
    # Run the Flask app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)