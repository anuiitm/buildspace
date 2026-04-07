<template>
  <div class="modal-overlay" :class="{ active: visible }" @click.self="$emit('close')">
    <div class="modal">
      <div class="modal-header">
        <h3 class="modal-title">Post Opportunity</h3>
        <button class="modal-close" @click="$emit('close')">✕</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">Title</label>
          <input class="form-input" v-model="title" placeholder="e.g., Looking for React Developer">
        </div>
        <div class="form-group">
          <label class="form-label">Description</label>
          <textarea class="form-textarea" v-model="description" placeholder="Describe the opportunity..."></textarea>
        </div>
        <div class="form-group">
          <label class="form-label">Type</label>
          <select class="form-select" v-model="oppType">
            <option value="teammates">Looking for Teammates</option>
            <option value="hiring">Hiring for Project Role</option>
            <option value="hackathon">Hackathon Team Opening</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">Skills Required (comma-separated)</label>
          <input class="form-input" v-model="skills" placeholder="e.g., React, Firebase, UI/UX">
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" @click="$emit('close')">Cancel</button>
        <button class="btn btn-primary" @click="submit" :disabled="!title.trim()">Post Opportunity</button>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../api.js';

export default {
  name: 'ModalCreateOpp',
  props: { visible: Boolean },
  emits: ['close', 'show-toast'],
  data() {
    return { title: '', description: '', oppType: 'teammates', skills: '' };
  },
  methods: {
    async submit() {
      try {
        await api.createOpportunity({
          title: this.title,
          description: this.description,
          type: this.oppType,
          skills: this.skills,
        });
        this.$emit('show-toast', { message: 'Opportunity posted!', type: 'success' });
        this.$emit('close');
        this.title = '';
        this.description = '';
        this.oppType = 'teammates';
        this.skills = '';
      } catch (err) {
        this.$emit('show-toast', { message: 'Failed to post opportunity', type: 'error' });
      }
    },
  },
};
</script>
