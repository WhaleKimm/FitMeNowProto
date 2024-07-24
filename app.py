from flask import Flask, render_template, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/render')
def render_model():
    # Blender 스크립트 실행
    script_path = os.path.join(os.path.dirname(__file__), 'scripts/render_human_model.py')
    blender_path = r'C:/Program Files/Blender Foundation/Blender 4.2/4.2/python/bin/python.exe'
    
    # Blender 스크립트 실행
    result = subprocess.run([blender_path, script_path], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

    # 렌더링된 이미지 반환
    output_file_path = os.path.join(os.path.dirname(__file__), 'output/rendered_model.png')
    if os.path.exists(output_file_path):
        return send_file(output_file_path, mimetype='image/png')
    else:
        return "Render failed or file not found!", 500

if __name__ == '__main__':
    app.run(debug=True)