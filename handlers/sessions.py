from flask import jsonify

session_list = []
s_id = 0


class SessionHandler:

    def build_session_dict(self, row):
        result = {}
        result['session_id'] = row[0]
        result['session_date'] = row[1]
        result['post_count'] = row[2]
        result['likes_count'] = row[3]
        result['replies count'] = row[4]
        result['dislikes_count'] = row[5]

        return result

    def build_session_attributes(self, sid, sdate, spostc, slikesc, srepliesc,
                              sdislikesc):
        result = {}
        result['session_id'] = sid
        result['session_date'] = sdate
        result['post_count'] = spostc
        result['likes_count'] = slikesc
        result['replies_count'] = srepliesc
        result['dislikes_count'] = sdislikesc
        return result

    def getAllSessions(self):
        return jsonify(Sessions=session_list)

    def getSessionById(self, session_id):
        if len(session_list) < session_id or session_id<1:
            return jsonify(Eror = "Session not found."), 404
        else:
            return jsonify(Session=session_list[session_id])

    def insertSessionJson(self, json):
        # session_id = json['session_id']
        global s_id
        session_date = json['session_date']
        post_count = json['post_count']
        likes_count = json['likes_count']
        replies_count = json['replies_count']
        dislikes_count = json['dislikes_count']
        if session_date and post_count and likes_count and replies_count and dislikes_count:
            result = self.build_session_attributes(s_id, session_date, post_count, likes_count, replies_count, dislikes_count)
            session_list.append({"session_id": s_id, "session_date": session_date, "post_count": post_count,
                                 "likes_count": likes_count, "replies_count": replies_count, "dislikes_count": dislikes_count})
            s_id = s_id + 1
            return jsonify(Session=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateSession(self, session_id, json):
        if len(session_list) <= session_id:
            return jsonify(Error = "Session not found."), 404
        else:
            if len(json) != 6:
                return jsonify(Error = "Update request incorrect."), 400
            else:
                session_date = json['session_date']
                post_count = json['post_count']
                likes_count = json['likes_count']
                replies_count = json['replies count']
                dislikes_count = json['dislikes_count']
                if session_date and post_count and likes_count and replies_count and dislikes_count:
                    return jsonify(UpdateStatus = "AREA TO UPDATE SESSION BY ID"), 200

    def deleteSession(self, post_id):
        global p_id
        if len(session_list) <= post_id:
            return jsonify(Error = "Session not found."), 404
        else:
            #del sessions_list[post_id]
            #s_id = s_id - 1
            return jsonify(DeleteStatus = "AREA TO DELETE SESSION BY ID"), 200