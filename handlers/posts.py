from flask import jsonify
from daos.posts import PostsDAO

posts_list = [{"post_id": 1, "user_id": "1", "imageURL": "www.test.com", "post_caption": "HI", "post_likes": "10",
               "post_dislikes": "1", "reply_id": "5", "post_Date": "2/15/2019", "topic_id": "9"}]
p_id = 2

class PostHandler:

    def build_post_dict(self, row):
        result = {}
        result['post_caption'] = row[0]
        result['hash_name'] = row[1]
        result['first_name'] = row[2]
        result['last_name'] = row[3]
        result['phone'] = row[4]
        result['u_email_address'] = row[5]
        result['post_date'] = row[6]

        return result

    def build_post_attributes(self, pid, uid, image, pcaption,plikes,
                              pdislikes, rid, pdate, tid):
        result = {}
        result['post_id'] = pid
        result['user_id'] = uid
        result['imageURL'] = image
        result['post_caption'] = pcaption
        result['post_likes'] = plikes
        result['post_dislikes'] = pdislikes
        result['reply_id'] = rid
        result['post_Date'] = pdate
        result['topic_id'] = tid
        return result

    def getAllPosts(self, chat_id):
      dao = PostsDAO()
      posts = dao.getAllPosts(chat_id)
      postsList = []
      for row in posts:
        postsList.append(self.build_post_dict(row))
      return jsonify(Posts=postsList)

    def getPostById(self, chat_id, post_id):
      dao = PostsDAO()
      row = dao.getPostById(chat_id, post_id)
      if not row:
        return jsonify(Error="Post Not Found"), 404
      else:
        post = self.build_post_dict(row)
        return jsonify(Post=post)

    def insertPostJson(self, json):
        global p_id
        user_id = json['user_id']
        imageURL = json['imageURL']
        post_caption = json['post_caption']
        post_likes = json['post_likes']
        post_dislikes = json['post_dislikes']
        reply_id = json['reply_id']
        post_Date = json['post_Date']
        topic_id = json['topic_id']
        if user_id and imageURL and post_caption and post_likes and post_dislikes and reply_id and post_Date and topic_id:
            result = self.build_post_attributes(p_id, user_id, imageURL, post_caption, post_likes, post_dislikes,
                                                reply_id, post_Date, topic_id)
            posts_list.append({"post_id": p_id, "user_id": user_id, "imageURL": imageURL, "post_caption": post_caption,
                               "post_likes": post_likes, "post_dislikes": post_dislikes, "reply_id": reply_id,
                               "post_Date": post_Date, "topic_id": topic_id})
            p_id = p_id + 1
            return jsonify(Post=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updatePost(self, post_id, json):
        if len(posts_list) < post_id or post_id < 1:
            return jsonify(Error = "Post not found."), 404
        else:
            if len(json) != 9:
                return jsonify(Error = "Update request incorrect."), 400
            else:
                user_id = json['user_id']
                imageURL = json['imageURL']
                post_caption = json['post_caption']
                post_likes = json['post_likes']
                post_dislikes = json['post_dislikes']
                reply_id = json['reply_id']
                post_Date = json['post_Date']
                topic_id = json['topic_id']
                if user_id and imageURL and post_caption and post_likes and post_dislikes and reply_id and post_Date and topic_id:
                    return jsonify(UpdateStatus = "AREA TO UPDATE POST BY ID"), 200

    def deletePost(self, post_id):
        global p_id
        if len(posts_list) < post_id or post_id < 1:
            return jsonify(Error = "Post not found."), 404
        else:
            return jsonify(DeleteStatus = "AREA TO DELETE POST BY ID"), 200
