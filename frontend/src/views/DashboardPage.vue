<template>
  <div class="page active" id="page-dashboard">
    <div class="dashboard-layout">
      <!-- Main Feed -->
      <main class="dashboard-main" id="feedContainer">
        <div class="dashboard-top-actions">
          <button class="btn btn-primary" @click="$emit('open-modal', 'createPost')">Create Post</button>
          <button class="btn btn-secondary" @click="$emit('open-modal', 'createProject')">Add Project</button>
          <button class="btn btn-secondary" @click="$emit('open-modal', 'createOpportunity')">Add Opportunity</button>
        </div>

        <!-- Create Post -->
        <div class="create-post">
          <div class="create-post-top">
            <div class="avatar avatar-lime">A</div>
            <div class="create-post-input" @click="$emit('open-modal', 'createPost')">What are you building today?</div>
          </div>
          <div class="create-post-actions">
            <button class="post-action-btn" @click="$emit('open-modal', 'createProject')">Project</button>
            <button class="post-action-btn" @click="$emit('open-modal', 'createOpportunity')">Opportunity</button>
            <button class="post-action-btn">Link</button>
            <button class="post-action-btn">Tag Skills</button>
          </div>
        </div>

        <!-- Feed Cards -->
        <div id="feedCards">
          <FeedCard
            v-for="(post, i) in posts"
            :key="post.id"
            :post="post"
            :index="i"
            @like="handleLike"
          />
          <div v-if="loading" class="empty-state">
            <div class="empty-state-icon">⏳</div>
            <div class="empty-state-text">Loading feed...</div>
          </div>
          <div v-if="!loading && posts.length === 0" class="empty-state">
            <div class="empty-state-icon">📡</div>
            <div class="empty-state-text">No posts yet</div>
            <div class="empty-state-sub">Be the first to share something!</div>
          </div>
        </div>
      </main>

      <WidgetPanel />
    </div>
  </div>
</template>

<script>
import api from '../api.js';
import FeedCard from '../components/FeedCard.vue';
import WidgetPanel from '../components/WidgetPanel.vue';

export default {
  name: 'DashboardPage',
  components: { FeedCard, WidgetPanel },
  emits: ['open-modal', 'show-toast'],
  data() {
    return {
      posts: [],
      loading: true,
    };
  },
  async mounted() {
    await this.loadFeed();
  },
  async activated() {
    await this.loadFeed();
  },
  methods: {
    async loadFeed() {
      this.loading = true;
      try {
        const res = await api.getFeed();
        this.posts = res.data;
      } catch (err) {
        console.error('Failed to load feed:', err);
      } finally {
        this.loading = false;
      }
    },
    async handleLike(postId) {
      try {
        const res = await api.toggleLike(postId);
        const updated = res.data;
        const idx = this.posts.findIndex(p => p.id === postId);
        if (idx !== -1) {
          this.posts[idx] = updated;
        }
      } catch (err) {
        console.error('Failed to like post:', err);
      }
    },
  },
};
</script>
