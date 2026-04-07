<template>
  <div class="modal-overlay" :class="{ active: visible }" @click.self="$emit('close')">
    <div class="modal">
      <div class="modal-header">
        <h3 class="modal-title">Edit Profile</h3>
        <button class="modal-close" @click="$emit('close')">✕</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">Display Name</label>
          <input class="form-input" v-model="name">
        </div>
        <div class="form-group">
          <label class="form-label">Handle</label>
          <input class="form-input" v-model="handle">
        </div>
        <div class="form-group">
          <label class="form-label">Bio</label>
          <textarea class="form-textarea" v-model="bio"></textarea>
        </div>
        <div class="form-group">
          <label class="form-label">Skills (comma-separated)</label>
          <input class="form-input" v-model="skills">
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" @click="$emit('close')">Cancel</button>
        <button class="btn btn-primary" @click="submit">Save Changes</button>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../api.js';

export default {
  name: 'ModalEditProfile',
  props: { visible: Boolean },
  emits: ['close', 'show-toast'],
  data() {
    return { name: '', handle: '', bio: '', skills: '' };
  },
  watch: {
    visible(val) {
      if (val) this.loadProfile();
    },
  },
  methods: {
    async loadProfile() {
      try {
        const res = await api.getProfile();
        const p = res.data;
        this.name = p.name;
        this.handle = p.handle;
        this.bio = p.bio;
        this.skills = p.skills.join(', ');
      } catch (err) {
        console.error('Failed to load profile:', err);
      }
    },
    async submit() {
      try {
        await api.updateProfile({
          name: this.name,
          handle: this.handle,
          bio: this.bio,
          skills: this.skills,
        });
        this.$emit('show-toast', { message: 'Profile updated!', type: 'success' });
        this.$emit('close');
      } catch (err) {
        this.$emit('show-toast', { message: 'Failed to update profile', type: 'error' });
      }
    },
  },
};
</script>
