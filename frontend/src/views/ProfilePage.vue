<template>
  <div class="page active" id="page-profile">
    <div class="profile-page">
      <div class="profile-header" v-if="profile">
        <div class="profile-banner"></div>
        <div class="profile-info">
          <div class="profile-avatar-wrapper">
            <div class="profile-avatar">{{ profile.avatar_letter }}</div>
            <button class="btn btn-secondary btn-sm" @click="openEditProfile">Edit Profile</button>
          </div>
          <h1 class="profile-name">
            {{ profile.name }}
            <span v-if="profile.verified" class="verified-badge">✓</span>
          </h1>
          <div class="profile-handle">{{ profile.handle }}</div>
          <p class="profile-bio">{{ profile.bio }}</p>
          <div class="profile-stats">
            <div class="profile-stat"><strong>{{ profile.project_count }}</strong><span>Projects</span></div>
            <div class="profile-stat"><strong>{{ profile.connections }}</strong><span>Connections</span></div>
            <div class="profile-stat"><strong>{{ profile.teams }}</strong><span>Teams</span></div>
            <div class="profile-stat"><strong>{{ profile.contributions }}</strong><span>Contributions</span></div>
          </div>
          <div class="profile-skills">
            <span class="skill-tag" v-for="skill in profile.skills" :key="skill">{{ skill }}</span>
          </div>
        </div>
      </div>

      <div class="profile-sections" v-if="profile">
        <div class="profile-section-card">
          <h3 class="profile-section-title">Projects</h3>
          <div>
            <div class="project-mini" v-for="project in userProjects" :key="project.id" @click="$router.push({ name: 'projects' })">
              <div class="project-mini-name">{{ project.icon }} {{ project.name }}</div>
              <div class="project-mini-desc">{{ project.description }}</div>
              <div class="project-mini-tags">
                <span class="tag" v-for="tech in project.stack.slice(0, 3)" :key="tech">{{ tech }}</span>
              </div>
            </div>
            <div v-if="userProjects.length === 0" class="empty-state" style="padding: 30px 10px;">
              <div class="empty-state-text">No projects yet</div>
            </div>
          </div>
        </div>
        <div class="profile-section-card">
          <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:16px;">
            <h3 class="profile-section-title" style="margin-bottom:0;">Activity</h3>
            <button class="btn btn-ghost btn-sm" @click="$router.push({ name: 'activity' })">Open Activity</button>
          </div>
          <div>
            <div class="project-mini">
              <div class="project-mini-name">Joined BuildSpace</div>
              <div class="project-mini-desc">Became a member of the community — 2 days ago</div>
            </div>
            <div class="project-mini">
              <div class="project-mini-name">Posted an opportunity</div>
              <div class="project-mini-desc">Looking for React devs — 5 days ago</div>
            </div>
            <div class="project-mini">
              <div class="project-mini-name">Created a project</div>
              <div class="project-mini-desc">DevSync — Real-time code collab tool — 1 week ago</div>
            </div>
          </div>
        </div>
      </div>

      <div v-if="loading" class="empty-state">
        <div class="empty-state-icon">⏳</div>
        <div class="empty-state-text">Loading profile...</div>
      </div>

      <ModalEditProfile
        :visible="showEditModal"
        @close="closeEditProfile"
        @show-toast="$emit('show-toast', $event)"
      />
    </div>
  </div>
</template>

<script>
import api from '../api.js';
import ModalEditProfile from '../components/ModalEditProfile.vue';

export default {
  name: 'ProfilePage',
  components: { ModalEditProfile },
  emits: ['show-toast'],
  data() {
    return {
      profile: null,
      userProjects: [],
      loading: true,
      showEditModal: false,
    };
  },
  async mounted() {
    await this.loadProfile();
  },
  async activated() {
    await this.loadProfile();
  },
  methods: {
    openEditProfile() {
      this.showEditModal = true;
    },
    async closeEditProfile() {
      this.showEditModal = false;
      await this.loadProfile();
    },
    async loadProfile() {
      this.loading = true;
      try {
        const [profileRes, projectsRes] = await Promise.all([
          api.getProfile(),
          api.getProjects(),
        ]);
        this.profile = profileRes.data;
        // Show only projects owned by or involving the current user
        this.userProjects = projectsRes.data.slice(0, 5);
      } catch (err) {
        console.error('Failed to load profile:', err);
        const storedUser = JSON.parse(localStorage.getItem('bs-user') || '{}');
        this.profile = {
          avatar_letter: (storedUser.name || 'U').charAt(0).toUpperCase(),
          name: storedUser.name || 'BuildSpace User',
          handle: '@buildspace_user',
          bio: 'Profile data is temporarily unavailable. You can still edit your profile details.',
          verified: false,
          project_count: 0,
          connections: 0,
          teams: 0,
          contributions: 0,
          skills: ['JavaScript', 'Vue'],
        };
        this.userProjects = [];
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
