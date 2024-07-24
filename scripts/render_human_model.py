import bpy
import os

def render_model():
    blend_file_path = os.path.join(os.path.dirname(__file__), '../models/human_model.blend')
    output_dir = os.path.join(os.path.dirname(__file__), '../output')
    output_file_path = os.path.join(output_dir, 'rendered_model.png')
    
    # output 디렉토리 생성
    os.makedirs(output_dir, exist_ok=True)
    
    bpy.ops.wm.open_mainfile(filepath=blend_file_path)
    # 렌더링 설정 (필요에 따라 수정)
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath = output_file_path
    bpy.ops.render.render(write_still=True)

if __name__ == "__main__":
    render_model()
