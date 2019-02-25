from flask import jsonify

posts_list = []
p_id = 0

class PostHandler:

    def build_post_dict(self, row):
        result = {}
        result['post_id'] = row[0]
        result['user_id'] = row[1]
        result['imageURL'] = row[2]
        result['post_caption'] = row[3]
        result['post_likes'] = row[4]
        result['post_dislikes'] = row[5]
        result['reply_id'] = row[6]
        result['post_Date'] = row[7]
        result['topic_id'] = row[8]

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

    def getAllPosts(self):
        return jsonify(Posts=posts_list)

    def getPostById(self, post_id):
        if len(posts_list) < post_id or post_id<1:
            return jsonify(Eror = "Post not found."), 404
        else:
            return jsonify(Post=posts_list[post_id-1])

    def insertPostJson(self, json):
        #post_id = json['post_id']
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
        if len(posts_list) <= post_id:
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
        if len(posts_list) <= post_id:
            return jsonify(Error = "Post not found."), 404
        else:
            #del posts_list[post_id]
            #p_id = p_id - 1
            return jsonify(DeleteStatus = "AREA TO DELETE POST BY ID"), 200
