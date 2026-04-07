<template>
  <aside class="dashboard-aside">
    <!-- Trending -->
    <div class="widget">
      <div class="widget-title">
        Trending Skills
        <span class="see-all">See all</span>
      </div>
      <div>
        <div class="trending-item" v-for="(skill, i) in trending" :key="skill.name">
          <span class="trending-rank">{{ i + 1 }}</span>
          <span class="trending-name">{{ skill.name }}</span>
          <span class="trending-count">{{ skill.count }} · {{ skill.trend }}</span>
        </div>
      </div>
    </div>

    <!-- Suggested Users -->
    <div class="widget">
      <div class="widget-title">
        People to Follow
        <span class="see-all">See all</span>
      </div>
      <div>
        <div class="user-suggestion" v-for="user in suggestedUsers" :key="user.id">
          <div class="avatar avatar-sm" :class="user.color">{{ user.avatar }}</div>
          <div class="user-suggestion-info">
            <div class="user-suggestion-name">{{ user.name }}</div>
            <div class="user-suggestion-role">{{ user.role }}</div>
          </div>
          <button class="btn btn-outline btn-sm">Follow</button>
        </div>
      </div>
    </div>

    <!-- Live Hackathons -->
    <div class="widget">
      <div class="widget-title">Live Hackathons</div>
      <div>
        <div class="hackathon-item" v-for="h in hackathons" :key="h.id">
          <div class="hackathon-name">{{ h.name }}</div>
          <div class="hackathon-meta">
            <span>{{ h.date }}</span>
            <span>{{ h.participants }} participants</span>
            <span v-if="h.live" class="hackathon-live">LIVE</span>
          </div>
        </div>
      </div>
    </div>
  </aside>
</template>

<script>
import api from '../api.js';

export default {
  name: 'WidgetPanel',
  data() {
    return {
      trending: [],
      suggestedUsers: [],
      hackathons: [],
    };
  },
  async mounted() {
    try {
      const [t, u, h] = await Promise.all([
        api.getTrending(),
        api.getSuggestedUsers(),
        api.getHackathons(),
      ]);
      this.trending = t.data;
      this.suggestedUsers = u.data;
      this.hackathons = h.data;
    } catch (err) {
      console.error('Failed to load widgets:', err);
    }
  },
};
</script>
