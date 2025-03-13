import os, requests as req
import vision
import bucket
import time
import base64

USAGE = "Please upload a picture and I will tell you what I see"
FORM = [
  {
    "label": "any pics?",
    "name": "pic",
    "required": "true",
    "type": "file"
  },
]

def form(args):
  res = {}
  out = USAGE
  inp = args.get("input", "")

  if type(inp) is dict and "form" in inp:
    img = inp.get("form", {}).get("pic", "")
    decoded_img = base64.b64decode(img)
    buc = bucket.Bucket(args)
    filename = f"image_s.jpg"
    result = buc.write(filename, decoded_img)
    if result == "OK":
      presigned_url = buc.exturl(filename, 60*60)  # 1 hour expiration
      vis = vision.Vision(args)
      out = vis.decode(img)
      res['html'] = f'<img src="{presigned_url}">'
    else:
      print(f"Failed to save image: {result}")
      out = "Failed to save image"
  res['form'] = FORM
  res['output'] = out
  return res
