<template>
  <div class="modal-overlay" :class="{ active: visible }" @click.self="$emit('close')">
    <div class="modal">
      <div class="modal-header">
        <h3 class="modal-title">Create Project</h3>
        <button class="modal-close" @click="$emit('close')">✕</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">Project Name</label>
          <input class="form-input" v-model="name" placeholder="e.g., DevSync">
        </div>
        <div class="form-group">
          <label class="form-label">Description</label>
          <textarea class="form-textarea" v-model="description" placeholder="What does this project do?"></textarea>
        </div>
        <div class="form-group">
          <label class="form-label">Tech Stack (comma-separated)</label>
          <input class="form-input" v-model="stack" placeholder="e.g., React, Node.js, MongoDB">
        </div>
        <div class="form-group">
          <label class="form-label">Status</label>
          <select class="form-select" v-model="status">
            <option value="active">Active</option>
            <option value="recruiting">Recruiting</option>
            <option value="completed">Completed</option>
          </select>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" @click="$emit('close')">Cancel</button>
        <button class="btn btn-primary" @click="submit" :disabled="!name.trim()">Create Project</button>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../api.js';

export default {
  name: 'ModalCreateProject',
  props: { visible: Boolean },
  emits: ['close', 'show-toast'],
  data() {
    return { name: '', description: '', stack: '', status: 'active' };
  },
  methods: {
    async submit() {
      try {
        await api.createProject({
          name: this.name,
          description: this.description,
          stack: this.stack,
          status: this.status,
        });
        this.$emit('show-toast', { message: `Project "${this.name}" created!`, type: 'success' });
        this.$emit('close');
        this.name = '';
        this.description = '';
        this.stack = '';
        this.status = 'active';
      } catch (err) {
        this.$emit('show-toast', { message: 'Failed to create project', type: 'error' });
      }
    },
  },
};
</script>
