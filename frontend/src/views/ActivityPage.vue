<template>
  <div class="page active">
    <div class="projects-page">
      <div class="section-header" style="text-align:left; margin-bottom: 24px;">
        <span class="section-label">Timeline</span>
        <h2 class="section-title">Activity</h2>
        <p class="section-subtitle" style="margin:0;">Recent actions across your account.</p>
      </div>

      <div class="profile-section-card" style="max-width: 900px;">
        <div class="project-mini" v-for="item in activities" :key="item.id">
          <div class="project-mini-name">{{ item.title }}</div>
          <div class="project-mini-desc">{{ item.text }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ActivityPage',
  data() {
    return {
      activities: [
        { id: 1, title: 'Joined BuildSpace', text: 'You created your account and set up your profile.' },
        { id: 2, title: 'Shared an update', text: 'You posted a progress update on your feed.' },
        { id: 3, title: 'Started a project', text: 'You created a new project and invited collaborators.' },
      ],
    };
  },
};
</script>
