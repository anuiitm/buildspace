<template>
  <div class="opp-card">
    <div class="opp-icon" :class="iconClass">{{ iconText }}</div>
    <div class="opp-content">
      <div class="opp-title">{{ opp.title }}</div>
      <div class="opp-desc">{{ opp.description }}</div>
      <div class="opp-meta">
        <span class="opp-meta-item">By {{ opp.postedBy }}</span>
        <span class="opp-meta-item">{{ opp.time }}</span>
        <span class="opp-meta-item" v-if="opp.skills && opp.skills.length">
          Skills: {{ opp.skills.join(', ') }}
        </span>
      </div>
    </div>
    <div class="opp-actions">
      <button class="btn btn-primary btn-sm">Apply</button>
      <button class="btn btn-ghost btn-sm">Save</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OppCard',
  props: {
    opp: { type: Object, required: true },
  },
  computed: {
    iconClass() {
      const map = { teammates: 'team', hiring: 'hire', hackathon: 'hack' };
      return map[this.opp.type] || 'team';
    },
    iconText() {
      const map = { teammates: 'TM', hiring: 'HR', hackathon: 'HK' };
      return map[this.opp.type] || 'OP';
    },
  },
};
</script>
