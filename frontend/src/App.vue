<template>
  <div :data-theme="theme">
    <NavBar
      :theme="theme"
      :is-authenticated="isAuthenticated"
      @toggle-theme="toggleTheme"
      @logout="logout"
    />
    <router-view
      @open-modal="openModal"
      @show-toast="showToast"
      @login-success="handleLoginSuccess"
      @register-success="handleRegisterSuccess"
    />

    <!-- Modals -->
    <ModalCreatePost
      :visible="activeModal === 'createPost'"
      @close="closeModal"
      @show-toast="showToast"
    />
    <ModalCreateProject
      :visible="activeModal === 'createProject'"
      @close="closeModal"
      @show-toast="showToast"
    />
    <ModalCreateOpp
      :visible="activeModal === 'createOpportunity'"
      @close="closeModal"
      @show-toast="showToast"
    />
    <ModalEditProfile
      :visible="activeModal === 'editProfile'"
      @close="closeModal"
      @show-toast="showToast"
    />

    <!-- Toast Container -->
    <ToastNotification ref="toastRef" />
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue';
import ModalCreatePost from './components/ModalCreatePost.vue';
import ModalCreateProject from './components/ModalCreateProject.vue';
import ModalCreateOpp from './components/ModalCreateOpp.vue';
import ModalEditProfile from './components/ModalEditProfile.vue';
import ToastNotification from './components/ToastNotification.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    ModalCreatePost,
    ModalCreateProject,
    ModalCreateOpp,
    ModalEditProfile,
    ToastNotification,
  },
  data() {
    return {
      theme: localStorage.getItem('bs-theme') || 'dark',
      isAuthenticated: localStorage.getItem('bs-auth') === 'true',
      activeModal: null,
    };
  },
  mounted() {
    document.documentElement.setAttribute('data-theme', this.theme);
  },
  methods: {
    toggleTheme() {
      this.theme = this.theme === 'dark' ? 'light' : 'dark';
      localStorage.setItem('bs-theme', this.theme);
      document.documentElement.setAttribute('data-theme', this.theme);
    },
    openModal(name) {
      this.activeModal = name;
    },
    closeModal() {
      this.activeModal = null;
    },
    showToast(toast) {
      this.$refs.toastRef.addToast(toast);
    },
    handleLoginSuccess(user) {
      localStorage.setItem('bs-auth', 'true');
      localStorage.setItem('bs-user', JSON.stringify(user || {}));
      this.isAuthenticated = true;
      this.$router.push({ name: 'dashboard' });
      this.showToast({ message: 'Logged in successfully', type: 'success' });
    },
    handleRegisterSuccess(user) {
      localStorage.setItem('bs-auth', 'true');
      localStorage.setItem('bs-user', JSON.stringify(user || {}));
      this.isAuthenticated = true;
      this.$router.push({ name: 'dashboard' });
      this.showToast({ message: 'Account created successfully', type: 'success' });
    },
    logout() {
      localStorage.removeItem('bs-auth');
      this.isAuthenticated = false;
      this.activeModal = null;
      this.$router.push({ name: 'home' });
      this.showToast({ message: 'Logged out', type: 'info' });
    },
  },
};
</script>
