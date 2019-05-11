from flask import jsonify
from daos.image import ImagesDAO
import os
from os import path
import shutil

class ImagesHandler:

  def build_image_attributes(self, image_file, p_with_image):
    result = {}
    result['image_file'] = image_file
    result['p_with_image'] = p_with_image

    return result

  def insertImage(self, json):
    print(json)
    image_file = self.uploadImage(json['image_file'])
    p_with_image = json['p_with_image']


    if image_file and p_with_image:
      dao = ImagesDAO()
      image_id = dao.insertImage(image_file, p_with_image)
      result = self.build_image_attributes(image_file, p_with_image)
      return jsonify(Chat=result), 201
    else:
      return jsonify(Error="Unexpected attributes in post request"), 400


  def uploadImage(self, image_file):
    if path.exists(image_file):
      src = path.realpath(image_file)
      head,tail = path.split(src)
      dst = path.realpath("../DB_Project/src/assets/" + tail)
      shutil.copy(src, dst)
      return tail
