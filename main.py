from flask import Flask, render_template_string

# Create Flask app
app = Flask(__name__)

# HTML template as a string
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>My Python Web Page</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; text-align: center; }
        h1 { color: #333; }
        p { font-size: 18px; }
    </style>
</head>
<body>
    <h1>Welcome to My Python Web Page!</h1>
    <p>This page is served using Flask in Python.</p>
</body>
</html>
"""

# Route for home page
@app.route("/")
def home():
    return render_template_string(html_template)

# Run the app
if __name__ == "__main__":
    try:
        app.run(debug=True)  # debug=True for auto-reload during development
    except Exception as e:
        print(f"Error starting server: {e}")
