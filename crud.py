from datetime import datetime
from database import projects_col, posts_col

class CRUD:
    @staticmethod
    def create_project(project_data):
        project_data['created_at'] = datetime.now()
        return projects_col.insert_one(project_data)

    @staticmethod
    def update_project(project_id, update_data):
        return projects_col.update_one(
            {'_id': project_id},
            {'$set': update_data}
        )

    @staticmethod
    def delete_project(project_id):
        return projects_col.delete_one({'_id': project_id})

    @staticmethod
    def create_post(post_data):
        post_data['created_at'] = datetime.now()
        return posts_col.insert_one(post_data)

    @staticmethod
    def update_post(post_id, update_data):
        return posts_col.update_one(
            {'_id': post_id},
            {'$set': update_data}
        )
    
    @staticmethod
    def delete_post(post_id):
        return posts_col.delete_one({'_id': post_id})
    