from flask import jsonify

posts_list = [{"post_id": 1, "user_id": "1", "imageURL": "www.test.com", "post_caption": "HI", "post_likes": "10",
               "post_dislikes": "1", "reply_id": "5", "post_Date": "2/15/2019", "topic_id": "9"}]
p_id = 1

class PostHandler:

    def build_post_dict(self, row):
        result = {'post_id': row[0], 'user_id': row[1], 'imageURL': row[2], 'post_caption': row[3],
                  'post_likes': row[4], 'post_dislikes': row[5], 'reply_id': row[6], 'post_Date': row[7],
                  'topic_id': row[8]}

        return result

    def build_post_attributes(self, pid, uid, image, pcaption,plikes,
                              pdislikes, rid, pdate, tid):
        result = {'post_id': pid, 'user_id': uid, 'imageURL': image, 'post_caption': pcaption, 'post_likes': plikes,
                  'post_dislikes': pdislikes, 'reply_id': rid, 'post_Date': pdate, 'topic_id': tid}
        return result

    def getAllPosts(self):
        return jsonify(Posts=posts_list)

    def getPostById(self, post_id):
        if len(posts_list) < post_id or post_id<1:
            return jsonify(Eror = "Post not found."), 404
        else:
            return jsonify(Post=posts_list[post_id-1])

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
            posts_list.append({"post_id": p_id, "user_id": user_id, "imageURL": imageURL, "post_caption": post_caption, "post_likes": post_likes, "post_dislikes": post_dislikes, "reply_id": reply_id, "post_Date": post_Date, "topic_id": topic_id})
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
