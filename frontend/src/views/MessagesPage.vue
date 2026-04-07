<template>
  <div class="page active">
    <div class="projects-page">
      <div class="section-header" style="text-align:left; margin-bottom: 24px;">
        <span class="section-label">Inbox</span>
        <h2 class="section-title">Messages</h2>
        <p class="section-subtitle" style="margin:0;">Conversations with collaborators.</p>
      </div>

      <div class="profile-section-card" style="max-width: 860px;">
        <div class="project-mini" v-for="thread in threads" :key="thread.id">
          <div class="project-mini-name">{{ thread.name }}</div>
          <div class="project-mini-desc">{{ thread.lastMessage }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MessagesPage',
  data() {
    return {
      threads: [
        { id: 1, name: 'DevSync Team', lastMessage: 'Can we review the API tasks today?' },
        { id: 2, name: 'Hackathon Group', lastMessage: 'Design review scheduled for tomorrow.' },
        { id: 3, name: 'Open Source Contributors', lastMessage: 'Issue triage is complete.' },
      ],
    };
  },
};
</script>
