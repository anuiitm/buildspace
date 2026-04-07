"""
BuildSpace — Database Seeder
Seeds mock data into the SQLite database.
"""
from datetime import datetime, timezone, timedelta
from models import db, User, Post, Project, ProjectMember, Opportunity
import json


def seed_database():
    """Drop all tables, recreate, and seed with mock data."""
    db.drop_all()
    db.create_all()

    now = datetime.now(timezone.utc)

    # ── Users ──
    users = [
        User(
            name='Alex Chen', handle='@alexchen',
            bio='Full-stack developer obsessed with clean architecture and developer tooling. Building things that make other builders faster. CS Junior @ Stanford.',
            avatar_letter='A', avatar_color='avatar-lime',
            skills=json.dumps(['React', 'Node.js', 'TypeScript', 'Python', 'Firebase', 'Docker', 'Figma']),
            verified=True, created_at=now - timedelta(days=30)
        ),
        User(
            name='Priya Sharma', handle='@priyabuilds',
            bio='Backend-focused dev building real-time collaboration tools. Open source contributor.',
            avatar_letter='P', avatar_color='avatar-pink',
            skills=json.dumps(['React', 'Node.js', 'WebSocket', 'Redis', 'PostgreSQL']),
            verified=True, created_at=now - timedelta(days=45)
        ),
        User(
            name='Marcus Johnson', handle='@marcusj',
            bio='Climate-tech enthusiast & data visualization nerd. Building dashboards for a greener future.',
            avatar_letter='M', avatar_color='avatar-cyan',
            skills=json.dumps(['Vue.js', 'D3.js', 'Node.js', 'MongoDB', 'UI/UX']),
            verified=False, created_at=now - timedelta(days=20)
        ),
        User(
            name='Sarah Kim', handle='@sarahcodes',
            bio='Open source champion. 50+ PRs merged this year. Passionate about making tech accessible.',
            avatar_letter='S', avatar_color='avatar-purple',
            skills=json.dumps(['React', 'Firebase', 'WebRTC', 'TailwindCSS', 'GitHub']),
            verified=True, created_at=now - timedelta(days=60)
        ),
        User(
            name='Raj Patel', handle='@rajdev',
            bio='Hackathon organizer and full-stack developer. Always building something new.',
            avatar_letter='R', avatar_color='avatar-orange',
            skills=json.dumps(['Python', 'React', 'MLH', 'Event Planning']),
            verified=False, created_at=now - timedelta(days=15)
        ),
        User(
            name='Emily Torres', handle='@emilyt',
            bio='AI/ML engineer building tools for developers. PeerReview founder. Stanford AI Lab.',
            avatar_letter='E', avatar_color='avatar-lime',
            skills=json.dumps(['Python', 'AI/ML', 'FastAPI', 'React', 'PostgreSQL', 'GPT-4']),
            verified=True, created_at=now - timedelta(days=90)
        ),
    ]
    db.session.add_all(users)
    db.session.flush()

    # ── Feed Posts ──
    posts = [
        Post(
            user_id=users[1].id,
            title='Just shipped DevSync v2.0 🚀',
            content='Real-time collaborative code editor with WebSocket support, syntax highlighting for 30+ languages, and live cursor tracking. Built with React, Node.js, and Redis.',
            post_type='project',
            tags=json.dumps(['React', 'Node.js', 'WebSocket', 'Redis']),
            likes=47, comments_count=12, shares=8,
            created_at=now - timedelta(hours=2)
        ),
        Post(
            user_id=users[2].id,
            title='Looking for a UI/UX designer for hackathon team',
            content="We're building a climate-tech dashboard for HackGreen 2025. Need someone who can design beautiful data visualizations and has experience with D3.js or Chart.js.",
            post_type='opportunity',
            tags=json.dumps(['UI/UX', 'D3.js', 'Hackathon', 'Climate-Tech']),
            likes=23, comments_count=18, shares=5,
            created_at=now - timedelta(hours=4)
        ),
        Post(
            user_id=users[3].id,
            title='Open source contribution milestone 🎉',
            content="Just had my 50th PR merged into major open source projects this year! If you're new to open source, I wrote a guide on finding beginner-friendly issues. Link in my profile.",
            post_type='update',
            tags=json.dumps(['OpenSource', 'GitHub', 'Contribution']),
            likes=156, comments_count=34, shares=45,
            created_at=now - timedelta(hours=6)
        ),
        Post(
            user_id=users[4].id,
            title='MLH Global Hack Week — Team forming!',
            content="Registrations open for MLH Global Hack Week starting next Monday. We have 2 backend devs and need a frontend developer and a designer. Who's in?",
            post_type='hackathon',
            tags=json.dumps(['MLH', 'Hackathon', 'Frontend', 'Design']),
            likes=89, comments_count=42, shares=31,
            created_at=now - timedelta(hours=8)
        ),
        Post(
            user_id=users[5].id,
            title='Introducing PeerReview — AI-powered code review',
            content='After 3 months of building, PeerReview is live! It uses GPT-4 to provide intelligent code reviews, suggest optimizations, and catch potential bugs before they ship.',
            post_type='project',
            tags=json.dumps(['AI/ML', 'Python', 'GPT-4', 'DevTools']),
            likes=234, comments_count=67, shares=89,
            created_at=now - timedelta(hours=12)
        ),
    ]
    db.session.add_all(posts)
    db.session.flush()

    # ── Projects ──
    projects_data = [
        {
            'name': 'DevSync', 'description': 'Real-time collaborative code editor with WebSocket support, syntax highlighting, live cursors, and built-in video chat for pair programming sessions.',
            'stack': ['React', 'Node.js', 'WebSocket', 'Redis', 'Monaco Editor'],
            'status': 'active', 'icon': '🔄', 'owner_id': users[1].id,
            'members': [users[1], users[0], users[2]]
        },
        {
            'name': 'PeerReview', 'description': 'AI-powered code review tool using GPT-4. Automatically analyzes pull requests, suggests improvements, catches bugs, and enforces coding standards.',
            'stack': ['Python', 'AI/ML', 'FastAPI', 'React', 'PostgreSQL'],
            'status': 'recruiting', 'icon': '🤖', 'owner_id': users[5].id,
            'members': [users[5], users[3]]
        },
        {
            'name': 'GreenDash', 'description': 'Climate data visualization dashboard that tracks carbon emissions, renewable energy usage, and environmental impact metrics for organizations.',
            'stack': ['Vue.js', 'D3.js', 'Node.js', 'MongoDB'],
            'status': 'recruiting', 'icon': '🌍', 'owner_id': users[2].id,
            'members': [users[2], users[4]]
        },
        {
            'name': 'StudyPal', 'description': 'Collaborative study platform with shared notes, flashcards, Pomodoro timers, and video study rooms. Built for students, by students.',
            'stack': ['React', 'Firebase', 'WebRTC', 'TailwindCSS'],
            'status': 'active', 'icon': '📚', 'owner_id': users[3].id,
            'members': [users[3], users[0], users[4]]
        },
        {
            'name': 'HackGreen', 'description': 'Annual climate-tech hackathon bringing together developers, designers, and activists to build solutions for a sustainable future.',
            'stack': ['Event', 'Hackathon', 'Climate-Tech'],
            'status': 'upcoming', 'icon': '🌱', 'owner_id': users[4].id,
            'members': [users[4], users[2], users[1]]
        },
    ]

    for pdata in projects_data:
        project = Project(
            name=pdata['name'], description=pdata['description'],
            stack=json.dumps(pdata['stack']), status=pdata['status'],
            icon=pdata['icon'], owner_id=pdata['owner_id'],
            created_at=now - timedelta(days=10)
        )
        db.session.add(project)
        db.session.flush()

        for member_user in pdata['members']:
            pm = ProjectMember(project_id=project.id, user_id=member_user.id)
            db.session.add(pm)

    # ── Opportunities ──
    opportunities = [
        Opportunity(
            title='Frontend Developer for DevSync',
            description='Looking for a React developer to help build the next version of DevSync. Experience with WebSocket and real-time systems preferred.',
            opp_type='teammates',
            skills=json.dumps(['React', 'WebSocket', 'TypeScript']),
            posted_by=users[1].id,
            created_at=now - timedelta(hours=3)
        ),
        Opportunity(
            title='ML Engineer — PeerReview',
            description='Join PeerReview to build AI-powered code analysis features. Must have experience with LLMs and Python.',
            opp_type='hiring',
            skills=json.dumps(['Python', 'AI/ML', 'LLMs', 'FastAPI']),
            posted_by=users[5].id,
            created_at=now - timedelta(hours=6)
        ),
        Opportunity(
            title='HackGreen 2025 — Designer Needed',
            description='Our climate-tech hackathon team needs a UI/UX designer who can create beautiful data visualizations for environmental data.',
            opp_type='hackathon',
            skills=json.dumps(['UI/UX', 'D3.js', 'Figma', 'Data Viz']),
            posted_by=users[2].id,
            created_at=now - timedelta(hours=10)
        ),
        Opportunity(
            title='Backend Developer for StudyPal',
            description='StudyPal is growing! We need a backend developer with Firebase experience to help scale our collaborative study platform.',
            opp_type='teammates',
            skills=json.dumps(['Firebase', 'Node.js', 'WebRTC']),
            posted_by=users[3].id,
            created_at=now - timedelta(hours=16)
        ),
        Opportunity(
            title='DevOps Engineer — Open Source Project',
            description='Help us set up CI/CD pipelines, Docker containers, and monitoring for our growing open source project.',
            opp_type='hiring',
            skills=json.dumps(['Docker', 'CI/CD', 'AWS', 'Kubernetes']),
            posted_by=users[0].id,
            created_at=now - timedelta(days=1)
        ),
    ]
    db.session.add_all(opportunities)

    db.session.commit()
    print('✅ Database seeded successfully!')
    print(f'   → {len(users)} users')
    print(f'   → {len(posts)} posts')
    print(f'   → {len(projects_data)} projects')
    print(f'   → {len(opportunities)} opportunities')


if __name__ == '__main__':
    from app import app
    with app.app_context():
        seed_database()
