<template>
  <div class="page active" id="page-landing">
    <section class="hero">
      <div class="hero-bg">
        <div class="hero-grid"></div>
        <div class="hero-gradient-1"></div>
        <div class="hero-gradient-2"></div>
      </div>
      <div class="container hero-content">
        <div class="hero-badge">
          <span class="hero-badge-dot"></span>
          <span>Now in public beta — 2,400+ developers joined</span>
        </div>
        <h1 class="hero-title">
          Where devs<br>
          <span class="accent">collide</span> &amp; <span class="highlight">build</span>
        </h1>
        <p class="hero-subtitle">
          Stop juggling LinkedIn, GitHub, and Discord. BuildSpace unifies your developer identity,
          team formation, and opportunity discovery in one living platform.
        </p>
        <div class="hero-actions">
          <button class="btn btn-primary btn-lg" @click="$router.push({ name: 'dashboard' })">Enter BuildSpace →</button>
          <button class="btn btn-outline btn-lg" @click="$router.push({ name: 'projects' })">Browse Projects</button>
        </div>
        <div class="hero-stats">
          <div class="hero-stat" v-for="stat in stats" :key="stat.label">
            <div class="hero-stat-value">{{ stat.display }}</div>
            <div class="hero-stat-label">{{ stat.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Marquee -->
    <div class="marquee-container">
      <div class="marquee-track">
        <span class="marquee-item" v-for="(tech, i) in marqueeItems" :key="i">
          <span>●</span> {{ tech }}
        </span>
      </div>
    </div>

    <!-- Features -->
    <section class="features-section">
      <div class="container">
        <div class="section-header">
          <span class="section-label">Core Platform</span>
          <h2 class="section-title">Everything you need,<br>nothing you don't</h2>
          <p class="section-subtitle">Four pillars that replace the chaos of scattered tools with one focused experience.</p>
        </div>
        <div class="features-grid">
          <div class="feature-card animate-in" v-for="(f, i) in features" :key="f.title" :class="'animate-delay-' + i">
            <div class="feature-icon">{{ f.icon }}</div>
            <h3 class="feature-title">{{ f.title }}</h3>
            <p class="feature-desc">{{ f.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="cta-section">
      <div class="container">
        <div class="cta-box">
          <h2 class="cta-title">Ready to stop context-switching?</h2>
          <p class="cta-subtitle">Join thousands of student developers who build, collaborate, and discover — all in one place.</p>
          <button class="btn btn-primary btn-lg" @click="$router.push({ name: 'dashboard' })">Get Started Free →</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'LandingPage',
  data() {
    return {
      stats: [
        { target: 2847, display: 0, label: 'Developers' },
        { target: 438, display: 0, label: 'Projects' },
        { target: 156, display: 0, label: 'Teams Formed' },
        { target: 89, display: 0, label: 'Hackathons' },
      ],
      marqueeItems: [
        'React', 'Next.js', 'TypeScript', 'Python', 'Rust', 'Go',
        'Node.js', 'Firebase', 'PostgreSQL', 'Docker', 'Figma', 'TailwindCSS',
        'React', 'Next.js', 'TypeScript', 'Python', 'Rust', 'Go',
        'Node.js', 'Firebase', 'PostgreSQL', 'Docker', 'Figma', 'TailwindCSS',
      ],
      features: [
        { icon: '👤', title: 'Developer Profiles', desc: 'Unified identity with skills, projects, and interests. Your developer resume that actually stays updated.' },
        { icon: '🔨', title: 'Project Forge', desc: 'Create projects, define tech stacks, recruit collaborators. From idea to shipped product with the right team.' },
        { icon: '⚡', title: 'Opportunity Board', desc: 'Hackathon openings, project roles, freelance gigs. Discover what\'s happening and jump in.' },
        { icon: '📡', title: 'Live Feed', desc: 'Real-time community pulse. New projects, team updates, and opportunities streaming to your dashboard.' },
      ],
    };
  },
  mounted() {
    this.animateCounters();
  },
  methods: {
    animateCounters() {
      const duration = 2000;
      const steps = 60;
      const interval = duration / steps;

      this.stats.forEach((stat) => {
        let step = 0;
        const timer = setInterval(() => {
          step++;
          const progress = step / steps;
          const eased = 1 - Math.pow(1 - progress, 3);
          stat.display = Math.round(eased * stat.target);
          if (step >= steps) {
            stat.display = stat.target;
            clearInterval(timer);
          }
        }, interval);
      });
    },
  },
};
</script>
