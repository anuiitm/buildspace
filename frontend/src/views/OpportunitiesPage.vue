<template>
  <div class="page active" id="page-opportunities">
    <div class="opportunities-page">
      <div class="section-header" style="text-align:left; margin-bottom: 32px;">
        <span class="section-label">Opportunity Board</span>
        <h2 class="section-title">Find Your Next Move</h2>
        <p class="section-subtitle" style="margin:0;">Teammates, roles, hackathons — all in one place.</p>
      </div>
      <div class="opps-toolbar">
        <div class="opps-tabs">
          <button
            v-for="tab in tabs"
            :key="tab.value"
            class="opps-tab"
            :class="{ active: activeTab === tab.value }"
            @click="filterOpps(tab.value)"
          >{{ tab.label }}</button>
        </div>
        <button class="btn btn-primary opportunities-add-btn" @click="$emit('open-modal', 'createOpportunity')">Add Opportunity</button>
      </div>
      <div id="oppsContainer">
        <OppCard v-for="opp in opportunities" :key="opp.id" :opp="opp" />
        <div v-if="loading" class="empty-state">
          <div class="empty-state-icon"></div>
          <div class="empty-state-text">Loading opportunities...</div>
        </div>
        <div v-if="!loading && opportunities.length === 0" class="empty-state">
          <div class="empty-state-text">No opportunities found</div>
          <div class="empty-state-sub">Check back later or post your own!</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../api.js';
import OppCard from '../components/OppCard.vue';

export default {
  name: 'OpportunitiesPage',
  components: { OppCard },
  emits: ['open-modal'],
  data() {
    return {
      opportunities: [],
      loading: true,
      activeTab: 'all',
      tabs: [
        { value: 'all', label: 'All' },
        { value: 'teammates', label: 'Teammates' },
        { value: 'hiring', label: 'Hiring' },
        { value: 'hackathon', label: 'Hackathons' },
      ],
    };
  },
  async mounted() {
    await this.loadOpportunities();
  },
  async activated() {
    await this.loadOpportunities();
  },
  methods: {
    async loadOpportunities() {
      this.loading = true;
      try {
        const params = {};
        if (this.activeTab !== 'all') params.type = this.activeTab;
        const res = await api.getOpportunities(params);
        this.opportunities = res.data;
      } catch (err) {
        console.error('Failed to load opportunities:', err);
      } finally {
        this.loading = false;
      }
    },
    filterOpps(tab) {
      this.activeTab = tab;
      this.loadOpportunities();
    },
  },
};
</script>
