<template>
  <div class="project-card" @click="$emit('select', project)">
    <div class="project-card-status" :class="'status-' + project.status">
      {{ project.status }}
    </div>
    <div class="project-card-icon">{{ projectInitial }}</div>
    <div class="project-card-title">{{ project.name }}</div>
    <div class="project-card-desc">{{ project.description }}</div>
    <div class="project-card-stack">
      <span class="tag" v-for="tech in project.stack" :key="tech">{{ tech }}</span>
    </div>
    <div class="project-card-footer">
      <div class="project-team">
        <div
          v-for="(member, i) in project.members"
          :key="i"
          class="avatar"
          :class="member.color"
        >{{ member.avatar }}</div>
        <span class="project-members-count">{{ project.memberCount }} members</span>
      </div>
      <span style="font-size: 12px; color: var(--text-tertiary)">by {{ project.owner }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectCard',
  props: {
    project: { type: Object, required: true },
  },
  emits: ['select'],
  computed: {
    projectInitial() {
      return (this.project.name || 'P').charAt(0).toUpperCase();
    },
  },
};
</script>
