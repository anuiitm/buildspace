<template>
  <div class="page active">
    <section class="auth-page">
      <div class="auth-bg"></div>
      <div class="auth-grid"></div>
      <div class="auth-bg-orb auth-bg-orb-1"></div>
      <div class="auth-bg-orb auth-bg-orb-2"></div>

      <div class="auth-card">
        <div class="auth-logo">
          <div class="auth-logo-icon">B</div>
          <div class="auth-logo-text">Build<span>Space</span></div>
        </div>
        <h1 class="auth-title">Login</h1>
        <p class="auth-subtitle">Access your projects, feed, and opportunities.</p>

        <form @submit.prevent="submit">
          <div class="form-group">
            <label class="form-label">Email</label>
            <input v-model="email" class="form-input" type="email" required placeholder="you@example.com">
          </div>
          <div class="form-group">
            <label class="form-label">Password</label>
            <input v-model="password" class="form-input" type="password" required placeholder="Enter your password">
          </div>
          <button class="btn btn-primary" style="width: 100%;" type="submit">Login</button>
        </form>

        <div class="auth-footer">
          Don’t have an account?
          <a @click="$router.push({ name: 'register' })">Register</a>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  emits: ['login-success'],
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    submit() {
      this.$emit('login-success', { email: this.email });
    },
  },
};
</script>
