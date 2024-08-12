from app import app
import base64


@app.template_filter("to_base64")
def render_image(binary_date):
    base64_data = base64.b64encode(binary_date).decode("utf-8")
    return f"data:image/jpeg;base64,{base64_data}"
