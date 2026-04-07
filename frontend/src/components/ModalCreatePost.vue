<template>
  <div class="modal-overlay" :class="{ active: visible }" @click.self="$emit('close')">
    <div class="modal">
      <div class="modal-header">
        <h3 class="modal-title">Create Post</h3>
        <button class="modal-close" @click="$emit('close')">✕</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label class="form-label">What's on your mind?</label>
          <textarea class="form-textarea" v-model="content" placeholder="Share an update, ask a question, or announce something..."></textarea>
        </div>
        <div class="form-group">
          <label class="form-label">Tags (comma-separated)</label>
          <input class="form-input" v-model="tags" placeholder="e.g., React, Firebase, OpenSource">
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-secondary" @click="$emit('close')">Cancel</button>
        <button class="btn btn-primary" @click="submit" :disabled="!content.trim()">Publish</button>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../api.js';

export default {
  name: 'ModalCreatePost',
  props: { visible: Boolean },
  emits: ['close', 'show-toast'],
  data() {
    return { content: '', tags: '' };
  },
  methods: {
    async submit() {
      try {
        await api.createPost({
          content: this.content,
          tags: this.tags,
          type: 'update',
          title: '',
        });
        this.$emit('show-toast', { message: 'Post published!', type: 'success' });
        this.$emit('close');
        this.content = '';
        this.tags = '';
      } catch (err) {
        this.$emit('show-toast', { message: 'Failed to publish post', type: 'error' });
      }
    },
  },
};
</script>
