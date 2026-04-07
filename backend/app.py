"""
BuildSpace — Flask API Backend
"""
import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User, Post, Project, ProjectMember, Opportunity

# ── App Config ──
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'buildspace.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'buildspace-dev-key'

CORS(app, resources={r"/api/*": {"origins": "*"}})
db.init_app(app)

# The "current user" is always Alex Chen (user id=1) for mock auth
CURRENT_USER_ID = 1


# ═══════════════════════════════════════════
#  FEED ENDPOINTS
# ═══════════════════════════════════════════

@app.route('/api/feed', methods=['GET'])
def get_feed():
    """Get all feed posts, newest first."""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return jsonify([p.to_dict(current_user_id=CURRENT_USER_ID) for p in posts])


@app.route('/api/feed', methods=['POST'])
def create_post():
    """Create a new feed post."""
    data = request.get_json()
    if not data or not data.get('content'):
        return jsonify({'error': 'Content is required'}), 400

    tags = data.get('tags', [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(',') if t.strip()]

    post = Post(
        user_id=CURRENT_USER_ID,
        title=data.get('title', ''),
        content=data['content'],
        post_type=data.get('type', 'update'),
        tags=json.dumps(tags),
    )
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict(current_user_id=CURRENT_USER_ID)), 201


@app.route('/api/feed/<int:post_id>/like', methods=['POST'])
def toggle_like(post_id):
    """Toggle like on a post."""
    post = Post.query.get_or_404(post_id)
    liked_by = post.get_liked_by()

    if CURRENT_USER_ID in liked_by:
        liked_by.remove(CURRENT_USER_ID)
        post.likes = max(0, post.likes - 1)
    else:
        liked_by.append(CURRENT_USER_ID)
        post.likes += 1

    post.liked_by = json.dumps(liked_by)
    db.session.commit()
    return jsonify(post.to_dict(current_user_id=CURRENT_USER_ID))


# ═══════════════════════════════════════════
#  PROJECTS ENDPOINTS
# ═══════════════════════════════════════════

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """Get projects with optional status and stack filters."""
    status = request.args.get('status')
    stack = request.args.get('stack')
    search = request.args.get('search', '').lower()

    query = Project.query

    if status and status != 'all':
        query = query.filter(Project.status == status)

    projects = query.order_by(Project.created_at.desc()).all()

    results = []
    for p in projects:
        proj_dict = p.to_dict()
        # Stack filter
        if stack and stack != 'all':
            if stack not in proj_dict['stack']:
                continue
        # Search filter
        if search:
            searchable = f"{proj_dict['name']} {proj_dict['description']} {' '.join(proj_dict['stack'])}".lower()
            if search not in searchable:
                continue
        results.append(proj_dict)

    return jsonify(results)


@app.route('/api/projects', methods=['POST'])
def create_project():
    """Create a new project."""
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({'error': 'Project name is required'}), 400

    stack = data.get('stack', [])
    if isinstance(stack, str):
        stack = [s.strip() for s in stack.split(',') if s.strip()]

    icons = ['🔨', '🚀', '💡', '⚙️', '🎯', '🔥', '📦', '🛠️', '✨', '🌟']
    import random

    project = Project(
        name=data['name'],
        description=data.get('description', ''),
        stack=json.dumps(stack),
        status=data.get('status', 'active'),
        icon=random.choice(icons),
        owner_id=CURRENT_USER_ID,
    )
    db.session.add(project)
    db.session.flush()

    # Add current user as a member
    member = ProjectMember(project_id=project.id, user_id=CURRENT_USER_ID)
    db.session.add(member)
    db.session.commit()

    return jsonify(project.to_dict()), 201


# ═══════════════════════════════════════════
#  OPPORTUNITIES ENDPOINTS
# ═══════════════════════════════════════════

@app.route('/api/opportunities', methods=['GET'])
def get_opportunities():
    """Get opportunities with optional type filter."""
    opp_type = request.args.get('type')

    query = Opportunity.query

    if opp_type and opp_type != 'all':
        query = query.filter(Opportunity.opp_type == opp_type)

    opps = query.order_by(Opportunity.created_at.desc()).all()
    return jsonify([o.to_dict() for o in opps])


@app.route('/api/opportunities', methods=['POST'])
def create_opportunity():
    """Create a new opportunity."""
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400

    skills = data.get('skills', [])
    if isinstance(skills, str):
        skills = [s.strip() for s in skills.split(',') if s.strip()]

    opp = Opportunity(
        title=data['title'],
        description=data.get('description', ''),
        opp_type=data.get('type', 'teammates'),
        skills=json.dumps(skills),
        posted_by=CURRENT_USER_ID,
    )
    db.session.add(opp)
    db.session.commit()

    return jsonify(opp.to_dict()), 201


# ═══════════════════════════════════════════
#  PROFILE ENDPOINTS
# ═══════════════════════════════════════════

@app.route('/api/profile', methods=['GET'])
def get_profile():
    """Get current user profile."""
    user = User.query.get_or_404(CURRENT_USER_ID)
    data = user.to_dict()
    # Add extra profile stats
    data['connections'] = 128
    data['teams'] = 3
    data['contributions'] = 12
    return jsonify(data)


@app.route('/api/profile', methods=['PUT'])
def update_profile():
    """Update current user profile."""
    user = User.query.get_or_404(CURRENT_USER_ID)
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    if 'name' in data:
        user.name = data['name']
    if 'handle' in data:
        user.handle = data['handle']
    if 'bio' in data:
        user.bio = data['bio']
    if 'skills' in data:
        skills = data['skills']
        if isinstance(skills, str):
            skills = [s.strip() for s in skills.split(',') if s.strip()]
        user.set_skills(skills)

    db.session.commit()
    return jsonify(user.to_dict())


# ═══════════════════════════════════════════
#  SIDEBAR/WIDGET ENDPOINTS
# ═══════════════════════════════════════════

@app.route('/api/trending', methods=['GET'])
def get_trending_skills():
    """Get trending skills (aggregated from all posts/projects)."""
    trending = [
        {'name': 'React', 'count': 847, 'trend': '+12%'},
        {'name': 'AI/ML', 'count': 634, 'trend': '+28%'},
        {'name': 'TypeScript', 'count': 521, 'trend': '+8%'},
        {'name': 'Rust', 'count': 412, 'trend': '+45%'},
        {'name': 'Next.js', 'count': 389, 'trend': '+15%'},
    ]
    return jsonify(trending)


@app.route('/api/users/suggested', methods=['GET'])
def get_suggested_users():
    """Get suggested users to follow."""
    users = User.query.filter(User.id != CURRENT_USER_ID).limit(4).all()
    results = []
    roles = ['Full-Stack Dev', 'Backend Engineer', 'Open Source Contributor', 'ML Engineer', 'Frontend Dev']
    for i, u in enumerate(users):
        results.append({
            'id': u.id,
            'name': u.name,
            'avatar': u.avatar_letter,
            'color': u.avatar_color,
            'role': roles[i % len(roles)],
        })
    return jsonify(results)


@app.route('/api/hackathons', methods=['GET'])
def get_hackathons():
    """Get live/upcoming hackathons."""
    hackathons = [
        {
            'id': 1,
            'name': 'MLH Global Hack Week',
            'date': 'Apr 14-20',
            'participants': 2400,
            'live': True,
        },
        {
            'id': 2,
            'name': 'HackGreen 2025',
            'date': 'May 1-3',
            'participants': 850,
            'live': False,
        },
        {
            'id': 3,
            'name': 'AI Builder Sprint',
            'date': 'May 15-17',
            'participants': 1200,
            'live': False,
        },
    ]
    return jsonify(hackathons)


# ═══════════════════════════════════════════
#  INIT
# ═══════════════════════════════════════════

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
