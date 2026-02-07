from flask import Flask, render_template, request
import traceback

app = Flask(__name__)

def analyze_code(code):
    try:
        compile(code, "<input>", "exec")
        return {
            "status": "ok",
            "message": "✅ No syntax errors found"
        }
    except SyntaxError as e:
        line = e.lineno
        offset = e.offset or 0
        lines = code.splitlines()

        error_line = lines[line - 1] if line <= len(lines) else ""
        pointer = " " * (offset - 1) + "^"

        return {
            "status": "error",
            "message": e.msg,
            "line": line,
            "code": error_line,
            "pointer": pointer
        }

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    code = ""

    if request.method == "POST":
        code = request.form.get("code")
        result = analyze_code(code)

    return render_template("index.html", result=result, code=code)

if __name__ == "__main__":
    app.run(debug=True)
