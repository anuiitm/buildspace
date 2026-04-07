import { createRouter, createWebHistory } from 'vue-router';

import HomePage from './views/HomePage.vue';
import LoginPage from './views/LoginPage.vue';
import RegisterPage from './views/RegisterPage.vue';
import DashboardPage from './views/DashboardPage.vue';
import ProjectsPage from './views/ProjectsPage.vue';
import OpportunitiesPage from './views/OpportunitiesPage.vue';
import ProfilePage from './views/ProfilePage.vue';
import NotificationsPage from './views/NotificationsPage.vue';
import MessagesPage from './views/MessagesPage.vue';
import ActivityPage from './views/ActivityPage.vue';

const routes = [
  { path: '/', name: 'home', component: HomePage, meta: { guestOnly: true } },
  { path: '/login', name: 'login', component: LoginPage, meta: { guestOnly: true } },
  { path: '/register', name: 'register', component: RegisterPage, meta: { guestOnly: true } },
  { path: '/dashboard', name: 'dashboard', component: DashboardPage, meta: { requiresAuth: true } },
  { path: '/projects', name: 'projects', component: ProjectsPage, meta: { requiresAuth: true } },
  { path: '/opportunities', name: 'opportunities', component: OpportunitiesPage, meta: { requiresAuth: true } },
  { path: '/profile', name: 'profile', component: ProfilePage, meta: { requiresAuth: true } },
  { path: '/notifications', name: 'notifications', component: NotificationsPage, meta: { requiresAuth: true } },
  { path: '/messages', name: 'messages', component: MessagesPage, meta: { requiresAuth: true } },
  { path: '/activity', name: 'activity', component: ActivityPage, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 };
  },
});

router.beforeEach((to) => {
  const isAuthed = localStorage.getItem('bs-auth') === 'true';
  if (to.meta.requiresAuth && !isAuthed) {
    return { name: 'login' };
  }
  if (to.meta.guestOnly && isAuthed) {
    return { name: 'dashboard' };
  }
  return true;
});

export default router;
