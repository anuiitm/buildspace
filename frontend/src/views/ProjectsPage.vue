<template>
  <div class="page active" id="page-projects">
    <div class="projects-page">
      <div class="section-header" style="text-align:left; margin-bottom: 32px;">
        <span class="section-label">Project Forge</span>
        <h2 class="section-title">Explore Projects</h2>
        <p class="section-subtitle" style="margin:0;">Discover ongoing projects or start your own.</p>
      </div>
      <div class="projects-toolbar">
        <div class="search-bar">
          <input type="text" placeholder="Search projects by name, tech, or keyword..." v-model="search" @input="loadProjects">
        </div>
        <button class="btn btn-primary projects-add-btn" @click="$emit('open-modal', 'createProject')">Add Project</button>
        <div class="filter-chips">
          <button
            v-for="chip in chips"
            :key="chip"
            class="chip"
            :class="{ active: activeChip === chip }"
            @click="filterByStack(chip)"
          >{{ chip }}</button>
        </div>
      </div>
      <div class="projects-grid" id="projectsGrid">
        <ProjectCard
          v-for="project in projects"
          :key="project.id"
          :project="project"
        />
        <div v-if="loading" class="empty-state">
          <div class="empty-state-icon">⏳</div>
          <div class="empty-state-text">Loading projects...</div>
        </div>
        <div v-if="!loading && projects.length === 0" class="empty-state">
          <div class="empty-state-text">No projects found</div>
          <div class="empty-state-sub">Try a different search or filter.</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../api.js';
import ProjectCard from '../components/ProjectCard.vue';

export default {
  name: 'ProjectsPage',
  components: { ProjectCard },
  emits: ['open-modal'],
  data() {
    return {
      projects: [],
      loading: true,
      search: '',
      activeChip: 'All',
      chips: ['All', 'React', 'Python', 'Node.js', 'Firebase', 'AI/ML'],
    };
  },
  async mounted() {
    await this.loadProjects();
  },
  async activated() {
    await this.loadProjects();
  },
  methods: {
    async loadProjects() {
      this.loading = true;
      try {
        const params = {};
        if (this.activeChip !== 'All') params.stack = this.activeChip;
        if (this.search.trim()) params.search = this.search.trim();
        const res = await api.getProjects(params);
        this.projects = res.data;
      } catch (err) {
        console.error('Failed to load projects:', err);
      } finally {
        this.loading = false;
      }
    },
    filterByStack(chip) {
      this.activeChip = chip;
      this.loadProjects();
    },
  },
};
</script>
