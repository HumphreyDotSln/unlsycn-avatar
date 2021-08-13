import os
import base64
if os.path.exists("unlsycn.ttf"):
    with open("./unlsycn.ttf", "rb") as ttf_file:
        ttf_b64 = base64.b64encode(ttf_file.read())
    css_str = """@font-face {{
        font-family: "unlsycn";
        src: url(data:font/truetype;charset=utf-8;base64,{}) format("truetype");
        font-weight: normal;
        font-style: normal;
    }}"""
    css_str = css_str.format(str(ttf_b64)[2:-1])
    with open("./out/unlsycn.css", "w+") as css_file:
        css_file.write(css_str)
