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
        <h1 class="auth-title">Register</h1>
        <p class="auth-subtitle">Create your BuildSpace account.</p>

        <form @submit.prevent="submit">
          <div class="form-group">
            <label class="form-label">Full Name</label>
            <input v-model="name" class="form-input" type="text" required placeholder="Your name">
          </div>
          <div class="form-group">
            <label class="form-label">Email</label>
            <input v-model="email" class="form-input" type="email" required placeholder="you@example.com">
          </div>
          <div class="form-group">
            <label class="form-label">Password</label>
            <input v-model="password" class="form-input" type="password" required placeholder="Create a password">
          </div>
          <button class="btn btn-primary" style="width: 100%;" type="submit">Create Account</button>
        </form>

        <div class="auth-footer">
          Already have an account?
          <a @click="$router.push({ name: 'login' })">Login</a>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'RegisterPage',
  emits: ['register-success'],
  data() {
    return {
      name: '',
      email: '',
      password: '',
    };
  },
  methods: {
    submit() {
      this.$emit('register-success', { name: this.name, email: this.email });
    },
  },
};
</script>
