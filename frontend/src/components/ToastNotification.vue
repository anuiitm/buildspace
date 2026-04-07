<template>
  <div class="toast-container" id="toastContainer">
    <div
      v-for="toast in toasts"
      :key="toast.id"
      class="toast"
      :class="['toast-' + toast.type, { removing: toast.removing }]"
    >
      <span class="toast-icon">{{ iconFor(toast.type) }}</span>
      <span class="toast-message">{{ toast.message }}</span>
      <span class="toast-close" @click="removeToast(toast.id)">✕</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ToastNotification',
  data() {
    return {
      toasts: [],
      nextId: 0,
    };
  },
  methods: {
    addToast({ message, type = 'success' }) {
      const id = this.nextId++;
      this.toasts.push({ id, message, type, removing: false });
      setTimeout(() => this.removeToast(id), 4000);
    },
    removeToast(id) {
      const toast = this.toasts.find(t => t.id === id);
      if (toast) {
        toast.removing = true;
        setTimeout(() => {
          this.toasts = this.toasts.filter(t => t.id !== id);
        }, 300);
      }
    },
    iconFor(type) {
      const map = { success: '✓', error: '✕', info: 'ℹ', warning: '⚠' };
      return map[type] || '✓';
    },
  },
};
</script>
