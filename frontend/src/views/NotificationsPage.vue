<template>
  <div class="page active">
    <div class="projects-page">
      <div class="section-header" style="text-align:left; margin-bottom: 24px;">
        <span class="section-label">Updates</span>
        <h2 class="section-title">Notifications</h2>
        <p class="section-subtitle" style="margin:0;">Recent activity for your account.</p>
      </div>

      <div class="profile-section-card" style="max-width: 860px;">
        <div class="project-mini" v-for="item in items" :key="item.id">
          <div class="project-mini-name">{{ item.title }}</div>
          <div class="project-mini-desc">{{ item.message }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotificationsPage',
  data() {
    return {
      items: [
        { id: 1, title: 'Project update', message: 'A new collaborator joined your project.' },
        { id: 2, title: 'Opportunity match', message: 'A new role matches your skills.' },
        { id: 3, title: 'Weekly summary', message: 'Your profile received 5 new views this week.' },
      ],
    };
  },
};
</script>
