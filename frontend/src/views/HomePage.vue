<template>
  <div class="page active">
    <section class="auth-page">
      <div class="auth-bg"></div>
      <div class="auth-grid"></div>
      <div class="home-landing-card">
        <div class="home-landing-main">
          <div class="auth-logo" style="justify-content: flex-start; margin-bottom: 20px;">
            <div class="auth-logo-icon">B</div>
            <div class="auth-logo-text">Build<span>Space</span></div>
          </div>
          <h1 class="home-landing-title">Build projects faster with the right developers.</h1>
          <p class="home-landing-subtitle">
            BuildSpace combines profile discovery, collaboration feed, opportunities, and team messaging
            in one place for student and indie developers.
          </p>
          <ul class="home-landing-points">
            <li>Share progress in a live developer feed.</li>
            <li>Discover projects and open roles by skill.</li>
            <li>Manage profile, notifications, and messages from one dashboard.</li>
          </ul>
          <div class="hero-actions" style="justify-content: flex-start; margin-bottom: 0;">
            <button class="btn btn-primary btn-lg" @click="$router.push({ name: 'login' })">Login</button>
            <button class="btn btn-outline btn-lg" @click="$router.push({ name: 'register' })">Register</button>
          </div>
        </div>

        <div class="home-landing-visual">
          <div class="home-visual-panel">
            <h3>Platform Overview</h3>
            <p>Everything important in one view.</p>
            <div class="home-visual-bars">
              <div class="home-visual-bar"><span>Projects</span><strong>438</strong></div>
              <div class="home-visual-bar"><span>Opportunities</span><strong>156</strong></div>
              <div class="home-visual-bar"><span>Active Teams</span><strong>89</strong></div>
            </div>
          </div>
          <div class="home-visual-grid">
            <div class="home-visual-card">Developer Profiles</div>
            <div class="home-visual-card">Project Workspace</div>
            <div class="home-visual-card">Opportunity Board</div>
            <div class="home-visual-card">Direct Messages</div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
};
</script>
