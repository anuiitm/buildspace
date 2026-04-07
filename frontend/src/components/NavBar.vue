<template>
  <nav class="nav" :class="{ scrolled: isScrolled }" id="navbar">
    <div class="nav-inner">
      <div class="nav-logo" @click="$router.push(isAuthenticated ? '/dashboard' : '/')">
        <div class="nav-logo-icon">B</div>
        <div class="nav-logo-text">Build<span>Space</span></div>
      </div>

      <div v-if="isAuthenticated" class="nav-links" :class="{ 'mobile-open': mobileOpen }" id="navLinks">
        <button
          class="nav-link"
          :class="{ active: $route.name === 'dashboard' }"
          @click="navigate('dashboard')"
        >Feed</button>
        <button
          class="nav-link"
          :class="{ active: $route.name === 'projects' }"
          @click="navigate('projects')"
        >Projects</button>
        <button
          class="nav-link"
          :class="{ active: $route.name === 'opportunities' }"
          @click="navigate('opportunities')"
        >Opportunities</button>
        <button
          class="nav-link"
          :class="{ active: $route.name === 'profile' }"
          @click="navigate('profile')"
        >Profile</button>
        <button
          class="nav-link"
          :class="{ active: $route.name === 'notifications' }"
          @click="navigate('notifications')"
        >Notifications</button>
        <button
          class="nav-link"
          :class="{ active: $route.name === 'messages' }"
          @click="navigate('messages')"
        >Messages</button>
      </div>

      <div class="nav-actions">
        <template v-if="isAuthenticated">
          <button
            class="nav-icon-btn"
            :class="{ active: $route.name === 'notifications' }"
            @click="navigate('notifications')"
            title="Notifications"
          >
            N
            <span v-if="unreadNotifications > 0" class="notif-dot"></span>
          </button>
          <button
            class="nav-icon-btn"
            :class="{ active: $route.name === 'messages' }"
            @click="navigate('messages')"
            title="Messages"
          >
            M
            <span v-if="unreadMessages > 0" class="notif-dot"></span>
          </button>
        </template>
        <template v-if="isAuthenticated">
          <button class="btn btn-logout btn-sm" @click="$emit('logout')">Logout</button>
        </template>
        <template v-else>
          <button class="btn btn-secondary nav-auth-btn" @click="navigate('login')">Login</button>
          <button class="btn btn-primary nav-auth-btn" @click="navigate('register')">Register</button>
        </template>
        <button class="theme-switch" @click="$emit('toggle-theme')" title="Toggle theme">
          <span class="theme-switch-icon">Light</span>
          <span class="theme-switch-track" :class="{ active: theme === 'dark' }">
            <span class="theme-switch-thumb"></span>
          </span>
          <span class="theme-switch-icon">Dark</span>
        </button>
        <button class="hamburger" :class="{ open: mobileOpen }" @click="mobileOpen = !mobileOpen">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
  props: {
    theme: { type: String, default: 'dark' },
    isAuthenticated: { type: Boolean, default: false },
  },
  emits: ['toggle-theme', 'logout'],
  data() {
    return {
      isScrolled: false,
      mobileOpen: false,
      unreadNotifications: 3,
      unreadMessages: 2,
    };
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      this.isScrolled = window.scrollY > 20;
    },
    navigate(name) {
      this.mobileOpen = false;
      this.$router.push({ name });
    },
  },
};
</script>
