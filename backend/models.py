"""
BuildSpace — SQLAlchemy Models
"""
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    handle = db.Column(db.String(50), unique=True, nullable=False)
    bio = db.Column(db.Text, default='')
    avatar_letter = db.Column(db.String(2), default='?')
    avatar_color = db.Column(db.String(20), default='avatar-lime')
    skills = db.Column(db.Text, default='[]')  # JSON array
    verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    posts = db.relationship('Post', backref='author', lazy=True)
    owned_projects = db.relationship('Project', backref='owner', lazy=True)
    opportunities = db.relationship('Opportunity', backref='poster', lazy=True)

    def get_skills(self):
        return json.loads(self.skills) if self.skills else []

    def set_skills(self, skill_list):
        self.skills = json.dumps(skill_list)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'handle': self.handle,
            'bio': self.bio,
            'avatar_letter': self.avatar_letter,
            'avatar_color': self.avatar_color,
            'skills': self.get_skills(),
            'verified': self.verified,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'project_count': len(self.owned_projects),
        }


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), default='')
    content = db.Column(db.Text, nullable=False)
    post_type = db.Column(db.String(20), default='update')  # project, opportunity, update, hackathon
    tags = db.Column(db.Text, default='[]')  # JSON array
    likes = db.Column(db.Integer, default=0)
    comments_count = db.Column(db.Integer, default=0)
    shares = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # Track which users have liked this post (simple JSON array of user IDs)
    liked_by = db.Column(db.Text, default='[]')

    def get_tags(self):
        return json.loads(self.tags) if self.tags else []

    def set_tags(self, tag_list):
        self.tags = json.dumps(tag_list)

    def get_liked_by(self):
        return json.loads(self.liked_by) if self.liked_by else []

    def to_dict(self, current_user_id=None):
        liked_by = self.get_liked_by()
        return {
            'id': self.id,
            'user': self.author.name,
            'handle': self.author.handle,
            'avatar': self.author.avatar_letter,
            'avatarColor': self.author.avatar_color,
            'verified': self.author.verified,
            'type': self.post_type,
            'time': self._time_ago(),
            'title': self.title,
            'content': self.content,
            'tags': self.get_tags(),
            'likes': self.likes,
            'comments': self.comments_count,
            'shares': self.shares,
            'liked': current_user_id in liked_by if current_user_id else False,
        }

    def _time_ago(self):
        if not self.created_at:
            return 'just now'
        now = datetime.now(timezone.utc)
        diff = now - self.created_at.replace(tzinfo=timezone.utc) if self.created_at.tzinfo is None else now - self.created_at
        seconds = int(diff.total_seconds())
        if seconds < 60:
            return 'just now'
        minutes = seconds // 60
        if minutes < 60:
            return f'{minutes}m ago'
        hours = minutes // 60
        if hours < 24:
            return f'{hours}h ago'
        days = hours // 24
        if days < 7:
            return f'{days}d ago'
        weeks = days // 7
        return f'{weeks}w ago'


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, default='')
    stack = db.Column(db.Text, default='[]')  # JSON array
    status = db.Column(db.String(20), default='active')  # active, recruiting, completed, upcoming
    icon = db.Column(db.String(10), default='📦')
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    members = db.relationship('ProjectMember', backref='project', lazy=True, cascade='all, delete-orphan')

    def get_stack(self):
        return json.loads(self.stack) if self.stack else []

    def set_stack(self, stack_list):
        self.stack = json.dumps(stack_list)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'stack': self.get_stack(),
            'status': self.status,
            'icon': self.icon,
            'owner': self.owner.name,
            'owner_id': self.owner_id,
            'members': [m.to_dict() for m in self.members],
            'memberCount': len(self.members),
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }


class ProjectMember(db.Model):
    __tablename__ = 'project_members'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', lazy=True)

    def to_dict(self):
        return {
            'avatar': self.user.avatar_letter,
            'color': self.user.avatar_color,
            'name': self.user.name,
        }


class Opportunity(db.Model):
    __tablename__ = 'opportunities'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    opp_type = db.Column(db.String(20), default='teammates')  # teammates, hiring, hackathon
    skills = db.Column(db.Text, default='[]')  # JSON array
    posted_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def get_skills(self):
        return json.loads(self.skills) if self.skills else []

    def set_skills(self, skill_list):
        self.skills = json.dumps(skill_list)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'type': self.opp_type,
            'skills': self.get_skills(),
            'postedBy': self.poster.name,
            'postedByHandle': self.poster.handle,
            'postedByAvatar': self.poster.avatar_letter,
            'postedByColor': self.poster.avatar_color,
            'time': self._time_ago(),
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

    def _time_ago(self):
        if not self.created_at:
            return 'just now'
        now = datetime.now(timezone.utc)
        diff = now - self.created_at.replace(tzinfo=timezone.utc) if self.created_at.tzinfo is None else now - self.created_at
        seconds = int(diff.total_seconds())
        if seconds < 60:
            return 'just now'
        minutes = seconds // 60
        if minutes < 60:
            return f'{minutes}m ago'
        hours = minutes // 60
        if hours < 24:
            return f'{hours}h ago'
        days = hours // 24
        if days < 7:
            return f'{days}d ago'
        weeks = days // 7
        return f'{weeks}w ago'
