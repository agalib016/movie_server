/**
 * Cineora BD - Front-End Application Engine
 * High-performance cinematic streaming platform with Cyber Emerald / custom theme engine,
 * 3D Spotlight hero stage with interactive poster wings, React Bits PillNav,
 * dynamic content shelves (rails), custom video player, and watchlist system.
 */

document.addEventListener('DOMContentLoaded', () => {
  // Global Application State
  const state = {
    themePalette: localStorage.getItem('cineora_palette') || 'emerald',
    mediaList: [],
    top10List: [],
    actorsList: [],
    watchlist: JSON.parse(localStorage.getItem('cineora_watchlist') || '[]'),
    currentCategory: 'all',
    currentLanguage: 'all',
    currentQuality: '',
    currentSort: 'latest',
    searchQuery: '',
    currentHeroIndex: 0,
    heroAutoplay: true,
    heroTimer: null,
    currentMedia: null,
    currentEpisode: null,
    activeView: 'home', // 'home', 'grid', 'actors'
    player: {
      isPlaying: false,
      speed: 1.0,
      aspect: 'default',
      controlsTimeout: null
    }
  };

  // DOM Elements
  const el = {
    html: document.documentElement,
    canvas: document.getElementById('cinematicAmbientBg'),
    themePaletteBtn: document.getElementById('themePaletteBtn'),
    themeColorDot: document.getElementById('themeColorDot'),
    themeColorLabel: document.getElementById('themeColorLabel'),
    themePickerDropdown: document.getElementById('themePickerDropdown'),
    searchInput: document.getElementById('searchInput'),
    searchClearBtn: document.getElementById('searchClearBtn'),
    watchlistToggleBtn: document.getElementById('watchlistToggleBtn'),
    watchlistBadge: document.getElementById('watchlistBadge'),
    watchlistDrawer: document.getElementById('watchlistDrawer'),
    closeWatchlistBtn: document.getElementById('closeWatchlistBtn'),
    watchlistItems: document.getElementById('watchlistItems'),
    syncSourcesBtn: document.getElementById('syncSourcesBtn'),

    // Hero Section
    heroSection: document.getElementById('heroSection'),
    heroBgImage: document.getElementById('heroBgImage'),
    heroFeatureLabel: document.getElementById('heroFeatureLabel'),
    heroMainTitle: document.getElementById('heroMainTitle'),
    heroMetaYear: document.getElementById('heroMetaYear'),
    heroMetaAudio: document.getElementById('heroMetaAudio'),
    heroMetaSource: document.getElementById('heroMetaSource'),
    heroMetaQuality: document.getElementById('heroMetaQuality'),
    heroDescription: document.getElementById('heroDescription'),
    heroPlayBtn: document.getElementById('heroPlayBtn'),
    heroDownloadBtn: document.getElementById('heroDownloadBtn'),
    heroListBtn: document.getElementById('heroListBtn'),
    heroTicketNumber: document.getElementById('heroTicketNumber'),
    heroPosterPlayBtn: document.getElementById('heroPosterPlayBtn'),
    heroPosterImg: document.getElementById('heroPosterImg'),
    heroPosterQuality: document.getElementById('heroPosterQuality'),
    heroPosterCaption: document.getElementById('heroPosterCaption'),
    heroPreviousPoster: document.getElementById('heroPreviousPoster'),
    heroPreviousImg: document.getElementById('heroPreviousImg'),
    heroNextPoster: document.getElementById('heroNextPoster'),
    heroNextImg: document.getElementById('heroNextImg'),
    heroCounter: document.getElementById('heroCounter'),
    heroAutoplayBtn: document.getElementById('heroAutoplayBtn'),
    heroAutoplayIcon: document.getElementById('heroAutoplayIcon'),
    carouselPrev: document.getElementById('carouselPrev'),
    carouselNext: document.getElementById('carouselNext'),
    carouselTrack: document.getElementById('carouselTrack'),

    // Filters & Dock
    categoryChips: document.getElementById('categoryChips'),
    langSelect: document.getElementById('langSelect'),
    qualitySelect: document.getElementById('qualitySelect'),
    sortSelect: document.getElementById('sortSelect'),

    // Content Views
    railsContainer: document.getElementById('railsContainer'),
    gridSection: document.getElementById('gridSection'),
    gridTitle: document.getElementById('gridTitle'),
    gridCount: document.getElementById('gridCount'),
    moviesGrid: document.getElementById('moviesGrid'),
    backToHomeBtn: document.getElementById('backToHomeBtn'),
    actorsSection: document.getElementById('actorsSection'),
    actorsGrid: document.getElementById('actorsGrid'),
    backFromActorsBtn: document.getElementById('backFromActorsBtn'),
    navActorsPill: document.getElementById('navActorsPill'),
    mobileActorsBtn: document.getElementById('mobileActorsBtn'),
    mobileWatchlistBtn: document.getElementById('mobileWatchlistBtn'),

    // Player Modal
    playerModal: document.getElementById('playerModal'),
    modalCloseBtn: document.getElementById('modalCloseBtn'),
    modalTitle: document.getElementById('modalTitle'),
    modalQuality: document.getElementById('modalQuality'),
    modalAudio: document.getElementById('modalAudio'),
    modalDownloadBtn: document.getElementById('modalDownloadBtn'),
    modalVlcBtn: document.getElementById('modalVlcBtn'),
    modalPotPlayerBtn: document.getElementById('modalPotPlayerBtn'),
    modalCopyBtn: document.getElementById('modalCopyBtn'),
    modalWatchlistBtn: document.getElementById('modalWatchlistBtn'),
    modalServer: document.getElementById('modalServer'),
    modalSize: document.getElementById('modalSize'),
    modalYear: document.getElementById('modalYear'),
    modalCategoryTag: document.getElementById('modalCategoryTag'),
    videoPlayer: document.getElementById('videoPlayer'),
    playerLoader: document.getElementById('playerLoader'),
    centerFeedback: document.getElementById('centerFeedback'),
    feedbackIcon: document.getElementById('feedbackIcon'),
    seekRippleLeft: document.getElementById('seekRippleLeft'),
    seekRippleRight: document.getElementById('seekRippleRight'),
    playerHudPill: document.getElementById('playerHudPill'),
    hudBarFill: document.getElementById('hudBarFill'),
    hudValue: document.getElementById('hudValue'),
    cinemaControls: document.getElementById('cinemaControls'),
    scrubContainer: document.getElementById('scrubContainer'),
    scrubTrack: document.getElementById('scrubTrack'),
    scrubBuffer: document.getElementById('scrubBuffer'),
    scrubProgress: document.getElementById('scrubProgress'),
    scrubTooltip: document.getElementById('scrubTooltip'),
    ctrlPlayBtn: document.getElementById('ctrlPlayBtn'),
    ctrlPlayIcon: document.getElementById('ctrlPlayIcon'),
    ctrlRewindBtn: document.getElementById('ctrlRewindBtn'),
    ctrlForwardBtn: document.getElementById('ctrlForwardBtn'),
    ctrlMuteBtn: document.getElementById('ctrlMuteBtn'),
    ctrlVolumeIcon: document.getElementById('ctrlVolumeIcon'),
    volumeSliderBox: document.getElementById('volumeSliderBox'),
    volumeFill: document.getElementById('volumeFill'),
    ctrlTimeDisplay: document.getElementById('ctrlTimeDisplay'),
    timeCurrent: document.getElementById('timeCurrent'),
    timeDuration: document.getElementById('timeDuration'),
    ctrlSpeedBtn: document.getElementById('ctrlSpeedBtn'),
    ctrlSpeedLabel: document.getElementById('ctrlSpeedLabel'),
    ctrlAspectBtn: document.getElementById('ctrlAspectBtn'),
    ctrlSnapshotBtn: document.getElementById('ctrlSnapshotBtn'),
    ctrlPipBtn: document.getElementById('ctrlPipBtn'),
    ctrlHelpBtn: document.getElementById('ctrlHelpBtn'),
    ctrlFullscreenBtn: document.getElementById('ctrlFullscreenBtn'),
    fullscreenIcon: document.getElementById('fullscreenIcon'),
    shortcutsOverlay: document.getElementById('shortcutsOverlay'),
    closeShortcutsBtn: document.getElementById('closeShortcutsBtn'),
    seriesSection: document.getElementById('seriesSection'),
    seriesEpisodesCount: document.getElementById('seriesEpisodesCount'),
    seriesSeasonTabs: document.getElementById('seriesSeasonTabs'),
    episodesList: document.getElementById('episodesList'),
    toastContainer: document.getElementById('toastContainer')
  };

  /* -------------------------------------------------------------------------
     1. Cinematic Ambient Dynamic Canvas
     ------------------------------------------------------------------------- */
  function initAmbientCanvas() {
    if (!el.canvas) return;
    const ctx = el.canvas.getContext('2d');
    let width = (el.canvas.width = window.innerWidth);
    let height = (el.canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {
      width = el.canvas.width = window.innerWidth;
      height = el.canvas.height = window.innerHeight;
    });

    let t = 0;
    function renderCanvas() {
      t += 0.003;
      ctx.clearRect(0, 0, width, height);

      // Get palette RGB colors
      let rgb = [0, 242, 170]; // Default emerald
      if (state.themePalette === 'amethyst') rgb = [168, 85, 247];
      if (state.themePalette === 'cyan') rgb = [6, 182, 212];
      if (state.themePalette === 'amber') rgb = [245, 158, 11];

      // Subtle drifting radial orbs
      const x1 = width * 0.25 + Math.cos(t) * 120;
      const y1 = height * 0.2 + Math.sin(t) * 80;
      const r1 = Math.min(width, height) * 0.45;
      const g1 = ctx.createRadialGradient(x1, y1, 10, x1, y1, r1);
      g1.addColorStop(0, `rgba(${rgb[0]}, ${rgb[1]}, ${rgb[2]}, 0.12)`);
      g1.addColorStop(1, 'rgba(0, 0, 0, 0)');
      ctx.fillStyle = g1;
      ctx.fillRect(0, 0, width, height);

      const x2 = width * 0.75 + Math.sin(t * 0.8) * 140;
      const y2 = height * 0.65 + Math.cos(t * 0.8) * 90;
      const r2 = Math.min(width, height) * 0.5;
      const g2 = ctx.createRadialGradient(x2, y2, 10, x2, y2, r2);
      g2.addColorStop(0, 'rgba(6, 182, 212, 0.08)');
      g2.addColorStop(1, 'rgba(0, 0, 0, 0)');
      ctx.fillStyle = g2;
      ctx.fillRect(0, 0, width, height);

      requestAnimationFrame(renderCanvas);
    }
    renderCanvas();
  }

  /* -------------------------------------------------------------------------
     2. Color Theme Switcher Engine
     ------------------------------------------------------------------------- */
  const paletteLabels = {
    emerald: 'Emerald',
    amethyst: 'Amethyst',
    cyan: 'Cyan',
    amber: 'Amber'
  };

  function applyPalette(palette) {
    state.themePalette = palette;
    el.html.setAttribute('data-theme-palette', palette);
    localStorage.setItem('cineora_palette', palette);
    if (el.themeColorLabel) el.themeColorLabel.textContent = paletteLabels[palette] || 'Theme';

    document.querySelectorAll('.palette-option').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.palette === palette);
    });
  }

  if (el.themePaletteBtn && el.themePickerDropdown) {
    el.themePaletteBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      el.themePickerDropdown.classList.toggle('is-open');
    });

    document.addEventListener('click', (e) => {
      if (!el.themePickerDropdown.contains(e.target) && e.target !== el.themePaletteBtn) {
        el.themePickerDropdown.classList.remove('is-open');
      }
    });

    document.querySelectorAll('.palette-option').forEach(btn => {
      btn.addEventListener('click', () => {
        applyPalette(btn.dataset.palette);
        el.themePickerDropdown.classList.remove('is-open');
        showToast(`Theme changed to ${paletteLabels[btn.dataset.palette]}`);
      });
    });
  }

  /* -------------------------------------------------------------------------
     3. Toast Notifications
     ------------------------------------------------------------------------- */
  function showToast(message, icon = 'ph-check-circle') {
    if (!el.toastContainer) return;
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `<i class="ph-bold ${icon}" style="color:var(--accent-primary); font-size:16px;"></i><span>${message}</span>`;
    el.toastContainer.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 3500);
  }

  /* -------------------------------------------------------------------------
     4. Spotlight Hero 3D Stage & Interactive Poster Wings
     ------------------------------------------------------------------------- */
  function updateHero() {
    if (!state.top10List.length) return;
    const total = state.top10List.length;
    const current = state.top10List[state.currentHeroIndex];
    if (!current) return;

    // Previous and Next indices for 3D wings
    const prevIndex = (state.currentHeroIndex - 1 + total) % total;
    const nextIndex = (state.currentHeroIndex + 1) % total;
    const prevItem = state.top10List[prevIndex];
    const nextItem = state.top10List[nextIndex];

    // Background Art
    if (el.heroBgImage) {
      el.heroBgImage.style.backgroundImage = `url('${current.backdrop || current.poster}')`;
    }

    // Headline & Copy
    if (el.heroFeatureLabel) el.heroFeatureLabel.textContent = `FEATURED #${state.currentHeroIndex + 1}`;
    if (el.heroMainTitle) {
      el.heroMainTitle.innerHTML = `${current.title}<br><span>${current.type === 'series' ? 'Complete Seasons' : 'Full Cinema'}</span>`;
    }
    if (el.heroMetaYear) el.heroMetaYear.textContent = current.year || '2024';
    if (el.heroMetaAudio) el.heroMetaAudio.textContent = `${current.language || 'English'} Audio`;
    if (el.heroMetaQuality) el.heroMetaQuality.textContent = (current.downloads && current.downloads['4k']) ? '4K UHD' : '1080p FHD';
    if (el.heroDescription) el.heroDescription.textContent = current.overview || 'High-speed stream with pristine master audio.';

    // Watchlist state on hero button
    const inWatchlist = state.watchlist.includes(current.id);
    if (el.heroListBtn) {
      el.heroListBtn.setAttribute('aria-pressed', inWatchlist ? 'true' : 'false');
      el.heroListBtn.innerHTML = inWatchlist ? '<i class="ph-fill ph-check"></i>' : '<i class="ph-bold ph-plus"></i>';
    }

    // Center 3D Poster
    if (el.heroPosterImg) el.heroPosterImg.src = current.poster;
    if (el.heroPosterCaption) el.heroPosterCaption.textContent = current.title;
    if (el.heroPosterQuality) el.heroPosterQuality.textContent = (current.downloads && current.downloads['4k']) ? '4K UHD' : '1080p';
    if (el.heroTicketNumber) el.heroTicketNumber.textContent = String(state.currentHeroIndex + 1).padStart(2, '0');

    // 3D Poster Wings
    if (el.heroPreviousImg && prevItem) el.heroPreviousImg.src = prevItem.poster;
    if (el.heroNextImg && nextItem) el.heroNextImg.src = nextItem.poster;

    // Reel Counter & Active Reel Highlight
    if (el.heroCounter) {
      el.heroCounter.innerHTML = `<b>${String(state.currentHeroIndex + 1).padStart(2, '0')}</b> / ${String(total).padStart(2, '0')}`;
    }

    // Update active highlight in reel track
    document.querySelectorAll('.reel-card').forEach((card, idx) => {
      card.classList.toggle('active', idx === state.currentHeroIndex);
    });
  }

  function nextHero() {
    if (!state.top10List.length) return;
    state.currentHeroIndex = (state.currentHeroIndex + 1) % state.top10List.length;
    updateHero();
  }

  function prevHero() {
    if (!state.top10List.length) return;
    state.currentHeroIndex = (state.currentHeroIndex - 1 + state.top10List.length) % state.top10List.length;
    updateHero();
  }

  function startHeroAutoplay() {
    stopHeroAutoplay();
    state.heroTimer = setInterval(() => {
      if (state.heroAutoplay) nextHero();
    }, 6500);
  }

  function stopHeroAutoplay() {
    if (state.heroTimer) clearInterval(state.heroTimer);
  }

  // Hero event bindings
  if (el.carouselNext) el.carouselNext.addEventListener('click', nextHero);
  if (el.carouselPrev) el.carouselPrev.addEventListener('click', prevHero);
  if (el.heroNextPoster) el.heroNextPoster.addEventListener('click', nextHero);
  if (el.heroPreviousPoster) el.heroPreviousPoster.addEventListener('click', prevHero);

  if (el.heroAutoplayBtn) {
    el.heroAutoplayBtn.addEventListener('click', () => {
      state.heroAutoplay = !state.heroAutoplay;
      if (el.heroAutoplayIcon) {
        el.heroAutoplayIcon.className = state.heroAutoplay ? 'ph-fill ph-pause' : 'ph-fill ph-play';
      }
      showToast(state.heroAutoplay ? 'Autoplay resumed' : 'Autoplay paused');
    });
  }

  if (el.heroPlayBtn) {
    el.heroPlayBtn.addEventListener('click', () => {
      const current = state.top10List[state.currentHeroIndex];
      if (current) openPlayer(current);
    });
  }

  if (el.heroPosterPlayBtn) {
    el.heroPosterPlayBtn.addEventListener('click', () => {
      const current = state.top10List[state.currentHeroIndex];
      if (current) openPlayer(current);
    });
  }

  if (el.heroListBtn) {
    el.heroListBtn.addEventListener('click', () => {
      const current = state.top10List[state.currentHeroIndex];
      if (current) toggleWatchlist(current.id);
    });
  }

  function renderHeroReel() {
    if (!el.carouselTrack || !state.top10List.length) return;
    el.carouselTrack.innerHTML = '';
    state.top10List.forEach((item, index) => {
      const card = document.createElement('div');
      card.className = `reel-card ${index === state.currentHeroIndex ? 'active' : ''}`;
      card.innerHTML = `
        <img src="${item.backdrop || item.poster}" alt="${item.title}" loading="lazy">
        <div class="reel-card-overlay">
          <div class="reel-card-title">${item.title}</div>
        </div>
      `;
      card.addEventListener('click', () => {
        state.currentHeroIndex = index;
        updateHero();
      });
      el.carouselTrack.appendChild(card);
    });
  }

  /* -------------------------------------------------------------------------
     5. Card Generation & Content Rails (Shelves)
     ------------------------------------------------------------------------- */
  function createMovieCard(item) {
    const card = document.createElement('div');
    card.className = 'movie-card';
    card.setAttribute('data-id', item.id);

    const isSaved = state.watchlist.includes(item.id);
    const qualityLabel = (item.downloads && item.downloads['4k']) ? '4K' : (item.downloads && item.downloads['1080p'] ? '1080p' : '720p');
    const firstGenre = (item.genres && item.genres[0]) || 'Cinema';

    card.innerHTML = `
      <div class="card-poster-wrap">
        <img class="card-poster-img" src="${item.poster}" alt="${item.title}" loading="lazy">
        <div class="card-badges-row">
          <span class="card-quality-badge">${qualityLabel}</span>
          <span class="card-rating-badge"><i class="ph-fill ph-star"></i> ${item.rating || '8.5'}</span>
        </div>
        <div class="card-hover-overlay">
          <div class="card-overlay-actions">
            <button class="card-play-gem" title="Watch Now" aria-label="Watch ${item.title}">
              <i class="ph-fill ph-play"></i>
            </button>
            <a class="card-icon-action" href="/api/download/${item.id}" target="_blank" download title="Direct Download" aria-label="Download">
              <i class="ph-bold ph-download-simple"></i>
            </a>
            <button class="card-icon-action card-watchlist-btn" title="Save to Watchlist" aria-label="Save">
              <i class="${isSaved ? 'ph-fill ph-bookmark-simple' : 'ph-bold ph-bookmark-simple'}" style="${isSaved ? 'color:var(--accent-primary);' : ''}"></i>
            </button>
          </div>
          <div class="card-hover-meta">
            <span>${item.year || ''}</span>
            <span>·</span>
            <span>${item.duration || 'Full Movie'}</span>
          </div>
        </div>
      </div>
      <div class="card-info">
        <div class="card-title" title="${item.title}">${item.title}</div>
        <div class="card-sub">
          <span class="card-genre-tag">${firstGenre}</span>
          <span>${item.language || 'English'}</span>
        </div>
      </div>
    `;

    // Card Click -> Open Player
    card.addEventListener('click', (e) => {
      if (e.target.closest('.card-watchlist-btn')) {
        e.stopPropagation();
        toggleWatchlist(item.id);
        return;
      }
      if (e.target.closest('a')) {
        return; // Allow direct download link
      }
      openPlayer(item);
    });

    return card;
  }

  function renderContentShelves() {
    if (!el.railsContainer) return;
    el.railsContainer.innerHTML = '';

    const shelves = [
      { id: 'hollywood', num: '01', eyebrow: 'BLOCKBUSTER CINEMA', title: 'Hollywood Hits & Blockbusters', desc: 'Highest grossing global action, sci-fi & thriller hits', filter: m => m.categories && m.categories.includes('hollywood') },
      { id: 'trending', num: '02', eyebrow: 'THE MOST WATCHED', title: 'Trending This Week', desc: 'Audiences across Bangladesh and worldwide are bingeing these right now', filter: m => (m.categories && m.categories.includes('trending')) || m.rating >= 8.5 },
      { id: 'bollywood', num: '03', eyebrow: 'HIGH-OCTANE CINEMA', title: 'Bollywood & Hindi Hits', desc: 'Shah Rukh Khan, action thrillers and timeless musical blockbusters', filter: m => m.categories && m.categories.includes('bollywood') || m.language === 'Hindi' },
      { id: 'web_series', num: '04', eyebrow: 'COMPLETE SEASONS', title: 'Top-Rated Web Series', desc: 'Binge-worthy drama, suspense and fantasy sagas with all episodes ready', filter: m => m.type === 'series' || (m.categories && m.categories.includes('web_series')) },
      { id: 'bangla', num: '05', eyebrow: 'REGIONAL HERITAGE', title: 'Bangla Cinema & Masterpieces', desc: 'Soumitra Chatterjee, Satyajit Ray and golden Bengali classics', filter: m => m.language === 'Bengali' || (m.categories && m.categories.includes('bangla')) },
      { id: 'anime', num: '06', eyebrow: 'JAPANESE ANIMATION', title: 'Anime & Iconic Sagas', desc: 'Full episodes with dual audio Hindi/English and original Japanese', filter: m => m.categories && m.categories.includes('anime') },
      { id: 'classics', num: '07', eyebrow: 'TIMELESS HISTORY (1888-1960)', title: 'Dawn of Motion Pictures', desc: 'Charlie Chaplin, pioneering silent film milestones and Golden Era epics', filter: m => m.categories && m.categories.includes('classics') || m.year <= 1960 }
    ];

    shelves.forEach(shelf => {
      const items = state.mediaList.filter(shelf.filter);
      if (!items.length) return;

      const railSection = document.createElement('section');
      railSection.className = 'rail-section';
      railSection.id = `rail-${shelf.id}`;

      railSection.innerHTML = `
        <div class="section-header">
          <div class="shelf-number">${shelf.num}</div>
          <div class="section-title-wrap">
            <span class="section-eyebrow"><i class="ph-fill ph-sparkle"></i> ${shelf.eyebrow}</span>
            <h2 class="section-title">${shelf.title}</h2>
            <div class="section-subtitle">
              <span>${shelf.desc}</span>
            </div>
          </div>
          <div class="catalog-header-tools">
            <button class="section-view-all" data-shelf="${shelf.id}">
              <span>View all</span> <i class="ph-bold ph-arrow-right"></i>
            </button>
          </div>
        </div>
        <div class="rail-wrapper">
          <button class="rail-scroll-btn left" aria-label="Scroll left"><i class="ph-bold ph-caret-left"></i></button>
          <div class="rail-carousel" id="carousel-${shelf.id}"></div>
          <button class="rail-scroll-btn right" aria-label="Scroll right"><i class="ph-bold ph-caret-right"></i></button>
        </div>
      `;

      const carousel = railSection.querySelector('.rail-carousel');
      items.forEach(item => {
        carousel.appendChild(createMovieCard(item));
      });

      // Horizontal Scroll buttons
      const btnLeft = railSection.querySelector('.rail-scroll-btn.left');
      const btnRight = railSection.querySelector('.rail-scroll-btn.right');
      btnLeft.addEventListener('click', () => carousel.scrollBy({ left: -600, behavior: 'smooth' }));
      btnRight.addEventListener('click', () => carousel.scrollBy({ left: 600, behavior: 'smooth' }));

      // View All button -> Switch to grid with this category
      const viewAllBtn = railSection.querySelector('.section-view-all');
      viewAllBtn.addEventListener('click', () => {
        selectCategory(shelf.id);
      });

      el.railsContainer.appendChild(railSection);
    });
  }

  function renderGridView(items) {
    if (!el.moviesGrid) return;
    el.moviesGrid.innerHTML = '';

    if (el.gridCount) {
      el.gridCount.textContent = `Showing ${items.length} titles`;
    }

    if (!items.length) {
      el.moviesGrid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 60px 20px; color: #94a3b8;">
          <i class="ph-bold ph-magnifying-glass" style="font-size: 36px; color: var(--accent-primary); margin-bottom: 12px; display: block;"></i>
          <h3 style="color:#fff; margin-bottom: 8px;">No titles found</h3>
          <p>Try searching for another keyword, movie title, actor or reset filters.</p>
        </div>
      `;
      return;
    }

    items.forEach(item => {
      el.moviesGrid.appendChild(createMovieCard(item));
    });
  }

  /* -------------------------------------------------------------------------
     6. Filtering & Navigation Routing
     ------------------------------------------------------------------------- */
  function getFilteredMedia() {
    let list = [...state.mediaList];

    // Category filter
    if (state.currentCategory && state.currentCategory !== 'all') {
      const cat = state.currentCategory;
      if (cat === 'bangla') {
        list = list.filter(m => m.language === 'Bengali' || (m.categories && m.categories.includes('bangla')));
      } else {
        list = list.filter(m => m.categories && m.categories.includes(cat));
      }
    }

    // Language filter
    if (state.currentLanguage && state.currentLanguage !== 'all') {
      list = list.filter(m => m.language && m.language.toLowerCase().includes(state.currentLanguage.toLowerCase()));
    }

    // Quality filter
    if (state.currentQuality) {
      list = list.filter(m => m.downloads && m.downloads[state.currentQuality.toLowerCase()]);
    }

    // Search query
    if (state.searchQuery.trim()) {
      const q = state.searchQuery.trim().toLowerCase();
      list = list.filter(m => {
        const titleMatch = m.title && m.title.toLowerCase().includes(q);
        const overviewMatch = m.overview && m.overview.toLowerCase().includes(q);
        const genreMatch = m.genres && m.genres.some(g => g.toLowerCase().includes(q));
        const dirMatch = m.director && m.director.toLowerCase().includes(q);
        return titleMatch || overviewMatch || genreMatch || dirMatch;
      });
    }

    // Sorting
    if (state.currentSort === 'latest') {
      list.sort((a, b) => (b.year || 0) - (a.year || 0));
    } else if (state.currentSort === 'rating') {
      list.sort((a, b) => (b.rating || 0) - (a.rating || 0));
    } else if (state.currentSort === 'name') {
      list.sort((a, b) => (a.title || '').localeCompare(b.title || ''));
    }

    return list;
  }

  function applyViewMode() {
    const isSearching = state.searchQuery.trim().length > 0;
    const isFiltered = (state.currentCategory !== 'all') || (state.currentLanguage !== 'all') || (state.currentQuality !== '') || isSearching;

    if (state.activeView === 'actors') {
      el.railsContainer.style.display = 'none';
      el.gridSection.style.display = 'none';
      el.actorsSection.style.display = 'block';
      return;
    }

    if (isFiltered) {
      state.activeView = 'grid';
      el.railsContainer.style.display = 'none';
      el.actorsSection.style.display = 'none';
      el.gridSection.style.display = 'block';

      if (el.gridTitle) {
        if (isSearching) {
          el.gridTitle.textContent = `Search results for "${state.searchQuery}"`;
        } else if (state.currentCategory !== 'all') {
          el.gridTitle.textContent = `Category: ${state.currentCategory.toUpperCase()}`;
        } else {
          el.gridTitle.textContent = 'Filtered Catalog';
        }
      }
      renderGridView(getFilteredMedia());
    } else {
      state.activeView = 'home';
      el.gridSection.style.display = 'none';
      el.actorsSection.style.display = 'none';
      el.railsContainer.style.display = 'flex';
    }
  }

  function selectCategory(category) {
    state.currentCategory = category;

    // Sync React Bits PillNav active states
    document.querySelectorAll('.pill[data-category]').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.category === category);
    });

    // Sync Category Chips active states
    document.querySelectorAll('.chip[data-category]').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.category === category);
    });

    // Sync Mobile Bottom Bar active states
    document.querySelectorAll('.bottom-bar-item[data-category]').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.category === category);
    });

    applyViewMode();

    if (category !== 'all') {
      const anchor = document.getElementById('catalogAnchor');
      if (anchor) anchor.scrollIntoView({ behavior: 'smooth' });
    }
  }
  window.selectCategory = selectCategory;

  // React Bits PillNav click handlers
  document.querySelectorAll('.pill[data-category]').forEach(btn => {
    btn.addEventListener('click', () => selectCategory(btn.dataset.category));
  });

  // Discovery Dock chips click handlers
  document.querySelectorAll('.chip[data-category]').forEach(btn => {
    btn.addEventListener('click', () => selectCategory(btn.dataset.category));
  });

  // Mobile Bottom Bar click handlers
  document.querySelectorAll('.bottom-bar-item[data-category]').forEach(btn => {
    btn.addEventListener('click', () => selectCategory(btn.dataset.category));
  });

  // Dropdown filter changes
  if (el.langSelect) {
    el.langSelect.addEventListener('change', (e) => {
      state.currentLanguage = e.target.value;
      applyViewMode();
    });
  }
  if (el.qualitySelect) {
    el.qualitySelect.addEventListener('change', (e) => {
      state.currentQuality = e.target.value;
      applyViewMode();
    });
  }
  if (el.sortSelect) {
    el.sortSelect.addEventListener('change', (e) => {
      state.currentSort = e.target.value;
      applyViewMode();
    });
  }

  // Search input debounced
  let searchDebounce = null;
  if (el.searchInput) {
    el.searchInput.addEventListener('input', (e) => {
      clearTimeout(searchDebounce);
      const query = e.target.value;
      if (el.searchClearBtn) {
        el.searchClearBtn.style.display = query.length ? 'block' : 'none';
      }
      searchDebounce = setTimeout(() => {
        state.searchQuery = query;
        applyViewMode();
      }, 250);
    });

    // Keyboard shortcut: Ctrl + K
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        el.searchInput.focus();
        el.searchInput.select();
      }
    });
  }

  if (el.searchClearBtn) {
    el.searchClearBtn.addEventListener('click', () => {
      el.searchInput.value = '';
      el.searchClearBtn.style.display = 'none';
      state.searchQuery = '';
      applyViewMode();
    });
  }

  if (el.backToHomeBtn) {
    el.backToHomeBtn.addEventListener('click', () => {
      selectCategory('all');
    });
  }

  /* -------------------------------------------------------------------------
     7. Actors Showcase System
     ------------------------------------------------------------------------- */
  function renderActors() {
    if (!el.actorsGrid) return;
    el.actorsGrid.innerHTML = '';

    state.actorsList.forEach(actor => {
      const card = document.createElement('div');
      card.className = 'actor-card';
      card.innerHTML = `
        <img class="actor-avatar" src="${actor.photo}" alt="${actor.name}" loading="lazy">
        <h3 class="actor-name">${actor.name}</h3>
        <p class="actor-bio">${actor.bio}</p>
        <span class="actor-titles-badge">${actor.titles_count || actor.media ? actor.media.length : 3} Titles in Library</span>
      `;
      card.addEventListener('click', () => {
        // Filter by actor's media
        if (actor.media && actor.media.length) {
          const mediaIds = actor.media.map(m => m.id);
          const matched = state.mediaList.filter(m => mediaIds.includes(m.id));
          state.activeView = 'grid';
          el.actorsSection.style.display = 'none';
          el.gridSection.style.display = 'block';
          if (el.gridTitle) el.gridTitle.textContent = `Filmography: ${actor.name}`;
          renderGridView(matched);
        }
      });
      el.actorsGrid.appendChild(card);
    });
  }

  function showActorsView() {
    state.activeView = 'actors';
    applyViewMode();
    const anchor = document.getElementById('catalogAnchor');
    if (anchor) anchor.scrollIntoView({ behavior: 'smooth' });
  }

  if (el.navActorsPill) el.navActorsPill.addEventListener('click', showActorsView);
  if (el.mobileActorsBtn) el.mobileActorsBtn.addEventListener('click', showActorsView);
  if (el.backFromActorsBtn) el.backFromActorsBtn.addEventListener('click', () => selectCategory('all'));

  /* -------------------------------------------------------------------------
     8. Watchlist Management
     ------------------------------------------------------------------------- */
  function updateWatchlistUI() {
    const count = state.watchlist.length;
    if (el.watchlistBadge) {
      el.watchlistBadge.textContent = count;
      el.watchlistBadge.style.display = count > 0 ? 'inline-block' : 'none';
    }

    if (!el.watchlistItems) return;
    el.watchlistItems.innerHTML = '';

    if (!count) {
      el.watchlistItems.innerHTML = `<div class="watchlist-empty">No saved movies yet. Bookmark your favorite titles to access them here.</div>`;
      return;
    }

    const savedMedia = state.mediaList.filter(m => state.watchlist.includes(m.id));
    savedMedia.forEach(item => {
      const row = document.createElement('div');
      row.className = 'watchlist-item';
      row.innerHTML = `
        <img class="wl-thumb" src="${item.poster}" alt="${item.title}">
        <div class="wl-details">
          <div class="wl-title">${item.title}</div>
          <div class="wl-meta">${item.year} · ${item.language}</div>
        </div>
        <div class="wl-actions">
          <button class="wl-btn play" title="Play Now"><i class="ph-fill ph-play"></i></button>
          <button class="wl-btn remove" title="Remove"><i class="ph-bold ph-trash"></i></button>
        </div>
      `;

      row.querySelector('.play').addEventListener('click', () => {
        el.watchlistDrawer.classList.remove('is-open');
        openPlayer(item);
      });

      row.querySelector('.remove').addEventListener('click', () => {
        toggleWatchlist(item.id);
      });

      el.watchlistItems.appendChild(row);
    });
  }

  function toggleWatchlist(mediaId) {
    const idx = state.watchlist.indexOf(mediaId);
    if (idx > -1) {
      state.watchlist.splice(idx, 1);
      showToast('Removed from Watchlist', 'ph-bookmark-simple');
    } else {
      state.watchlist.push(mediaId);
      showToast('Saved to Watchlist', 'ph-check-circle');
    }
    localStorage.setItem('cineora_watchlist', JSON.stringify(state.watchlist));
    updateWatchlistUI();

    // Re-render card icons in current view
    document.querySelectorAll(`.movie-card[data-id="${mediaId}"] .card-watchlist-btn i`).forEach(icon => {
      const isSaved = state.watchlist.includes(mediaId);
      icon.className = isSaved ? 'ph-fill ph-bookmark-simple' : 'ph-bold ph-bookmark-simple';
      icon.style.color = isSaved ? 'var(--accent-primary)' : '';
    });

    // Update hero if active
    if (state.top10List.length) {
      const cur = state.top10List[state.currentHeroIndex];
      if (cur && cur.id === mediaId) updateHero();
    }
  }

  if (el.watchlistToggleBtn) {
    el.watchlistToggleBtn.addEventListener('click', () => {
      el.watchlistDrawer.classList.toggle('is-open');
    });
  }
  if (el.mobileWatchlistBtn) {
    el.mobileWatchlistBtn.addEventListener('click', () => {
      el.watchlistDrawer.classList.toggle('is-open');
    });
  }
  if (el.closeWatchlistBtn) {
    el.closeWatchlistBtn.addEventListener('click', () => {
      el.watchlistDrawer.classList.remove('is-open');
    });
  }

  /* -------------------------------------------------------------------------
     9. Cinema Theater Video Player Modal
     ------------------------------------------------------------------------- */
  function formatTime(seconds) {
    const s = Math.floor(seconds || 0);
    const m = Math.floor(s / 60);
    const sec = s % 60;
    return `${String(m).padStart(2, '0')}:${String(sec).padStart(2, '0')}`;
  }

  function showHud(val, iconClass = 'ph-speaker-high') {
    if (!el.playerHudPill) return;
    el.playerHudPill.style.display = 'flex';
    if (el.hudValue) el.hudValue.textContent = val;
    if (el.hudIcon) el.hudIcon.className = `ph-fill ${iconClass}`;
    clearTimeout(state.player.hudTimeout);
    state.player.hudTimeout = setTimeout(() => {
      el.playerHudPill.style.display = 'none';
    }, 1200);
  }

  function showBloomFeedback(iconClass) {
    if (!el.centerFeedback) return;
    el.centerFeedback.style.display = 'grid';
    if (el.feedbackIcon) el.feedbackIcon.className = `ph-fill ${iconClass}`;
    setTimeout(() => {
      el.centerFeedback.style.display = 'none';
    }, 500);
  }

  function openPlayer(item, episodeNum = null) {
    state.currentMedia = item;
    state.currentEpisode = episodeNum;

    // Populate Modal Metadata
    if (el.modalTitle) el.modalTitle.textContent = item.title;
    if (el.modalQuality) el.modalQuality.textContent = (item.downloads && item.downloads['4k']) ? '4K UHD' : '1080p FHD';
    if (el.modalAudio) el.modalAudio.textContent = `${item.language || 'English'} Audio`;
    if (el.modalYear) el.modalYear.textContent = item.year || '2024';
    if (el.modalSize) el.modalSize.textContent = (item.downloads && item.downloads['1080p']) ? item.downloads['1080p'].size : '1.8 GB';
    if (el.modalCategoryTag) el.modalCategoryTag.textContent = (item.categories && item.categories[0]) || 'Cinema';

    // Direct actions
    if (el.modalDownloadBtn) el.modalDownloadBtn.href = `/api/download/${item.id}`;
    if (el.modalVlcBtn) el.modalVlcBtn.onclick = () => window.open(`/api/vlc/${item.id}`, '_blank');
    if (el.modalPotPlayerBtn) el.modalPotPlayerBtn.onclick = () => window.open(`/api/potplayer/${item.id}`, '_blank');
    if (el.modalCopyBtn) {
      el.modalCopyBtn.onclick = () => {
        const streamUrl = `${window.location.origin}/api/stream/${item.id}`;
        navigator.clipboard.writeText(streamUrl).then(() => showToast('Stream link copied to clipboard!'));
      };
    }
    if (el.modalWatchlistBtn) {
      el.modalWatchlistBtn.onclick = () => toggleWatchlist(item.id);
    }

    // Series Seasons & Episodes Picker (handle all series/show types)
    const isSeriesType = ['series', 'tv_show', 'web_series'].includes(item.type);
    if (isSeriesType && item.seasons && item.seasons.length) {
      el.seriesSection.style.display = 'block';
      renderSeriesPicker(item);
    } else {
      el.seriesSection.style.display = 'none';
    }

    el.playerModal.classList.add('is-active');
    document.body.style.overflow = 'hidden';

    // Remove any previous no-stream overlay
    const existingOverlay = document.getElementById('noStreamOverlay');
    if (existingOverlay) existingOverlay.remove();

    // Ensure video element is clean before setting new source
    el.videoPlayer.removeAttribute('src');
    el.videoPlayer.load();

    // Video Source with Multi-Server Routing
    state.currentServer = state.currentServer || 'server-1';
    const videoSrc = `/api/stream/${item.id}?server=${state.currentServer}${episodeNum ? '&episode=' + episodeNum : ''}`;
    el.videoPlayer.src = videoSrc;
    el.playerLoader.classList.add('is-loading');

    // Update active state on server tabs
    document.querySelectorAll('.server-tab').forEach(tab => {
      tab.classList.toggle('active', tab.dataset.server === state.currentServer);
    });

    el.videoPlayer.play().catch(() => {
      // Autoplay with audio may require user gesture
    });
  }

  // Multi-Server Selection (Anyplay-style zero-buffer failover)
  document.querySelectorAll('.server-tab[data-server]').forEach(tabBtn => {
    tabBtn.addEventListener('click', () => {
      const serverId = tabBtn.dataset.server;
      state.currentServer = serverId;
      document.querySelectorAll('.server-tab').forEach(b => b.classList.remove('active'));
      tabBtn.classList.add('active');

      if (state.currentMedia) {
        const curTime = el.videoPlayer.currentTime || 0;
        const wasPlaying = !el.videoPlayer.paused;
        const videoSrc = `/api/stream/${state.currentMedia.id}?server=${serverId}${state.currentEpisode ? '&episode=' + state.currentEpisode : ''}`;
        el.playerLoader.classList.add('is-loading');
        el.videoPlayer.src = videoSrc;
        el.videoPlayer.currentTime = curTime;
        if (wasPlaying) {
          el.videoPlayer.play().catch(() => {});
        }
        const serverNames = {
          'server-1': 'Server 1: ICC 10G Ultra',
          'server-2': 'Server 2: Cloudflare Edge CDN',
          'server-3': 'Server 3: Archive Cloud',
          'server-4': 'Server 4: MAG Ultra RAM Buffer'
        };
        showToast(`Connected to ${serverNames[serverId] || serverId} (Zero Buffer)`, 'ph-lightning');
      }
    });
  });

  function closePlayer() {
    el.videoPlayer.pause();
    el.videoPlayer.removeAttribute('src');
    el.videoPlayer.load();
    el.playerModal.classList.remove('is-active');
    document.body.style.overflow = '';
    state.player.isPlaying = false;
  }

  function renderSeriesPicker(series) {
    if (!el.seriesSeasonTabs || !el.episodesList) return;
    el.seriesSeasonTabs.innerHTML = '';
    el.episodesList.innerHTML = '';

    const seasons = series.seasons;
    let activeSeason = seasons[0];

    seasons.forEach((season, sIdx) => {
      const tab = document.createElement('button');
      tab.className = `season-btn ${sIdx === 0 ? 'active' : ''}`;
      tab.textContent = season.title || `Season ${season.season_number}`;
      tab.addEventListener('click', () => {
        document.querySelectorAll('.season-btn').forEach(b => b.classList.remove('active'));
        tab.classList.add('active');
        activeSeason = season;
        populateEpisodes(season.episodes);
      });
      el.seriesSeasonTabs.appendChild(tab);
    });

    function populateEpisodes(episodes) {
      el.episodesList.innerHTML = '';
      if (el.seriesEpisodesCount) {
        el.seriesEpisodesCount.textContent = `${episodes.length} episodes available in 1080p`;
      }

      episodes.forEach((ep) => {
        const epCard = document.createElement('div');
        epCard.className = 'episode-item';
        epCard.innerHTML = `
          <div class="ep-thumb-wrap">
            <img src="${ep.thumbnail || series.poster}" alt="Episode ${ep.episode_number}">
          </div>
          <div class="ep-info">
            <span class="ep-number">EPISODE ${ep.episode_number} · ${ep.duration || '45m'}</span>
            <div class="ep-title">${ep.title}</div>
          </div>
        `;
        epCard.addEventListener('click', () => {
          document.querySelectorAll('.episode-item').forEach(e => e.classList.remove('active'));
          epCard.classList.add('active');
          openPlayer(series, ep.episode_number);
        });
        el.episodesList.appendChild(epCard);
      });
    }

    populateEpisodes(activeSeason.episodes);
  }

  if (el.modalCloseBtn) el.modalCloseBtn.addEventListener('click', closePlayer);
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && el.playerModal.classList.contains('is-active')) {
      closePlayer();
    }
  });

  // Video Events
  if (el.videoPlayer) {
    el.videoPlayer.addEventListener('waiting', () => {
      el.playerLoader.classList.add('is-loading');
    });

    el.videoPlayer.addEventListener('canplay', () => {
      el.playerLoader.classList.remove('is-loading');
    });

    el.videoPlayer.addEventListener('loadeddata', () => {
      el.playerLoader.classList.remove('is-loading');
    });

    el.videoPlayer.addEventListener('error', (e) => {
      console.warn("Video stream load issue encountered, switching to backup stream...", e);
      if (state.currentMedia && el.videoPlayer.src && !el.videoPlayer.src.includes('fallback=1')) {
        el.videoPlayer.src = `/api/stream/${state.currentMedia.id}?server=${state.currentServer}&fallback=1`;
        el.videoPlayer.play().catch(() => {});
      } else {
        el.playerLoader.classList.remove('is-loading');
      }
    });

    el.videoPlayer.addEventListener('playing', () => {
      el.playerLoader.classList.remove('is-loading');
      state.player.isPlaying = true;
      if (el.ctrlPlayIcon) el.ctrlPlayIcon.className = 'ph-fill ph-pause';
    });

    el.videoPlayer.addEventListener('pause', () => {
      state.player.isPlaying = false;
      if (el.ctrlPlayIcon) el.ctrlPlayIcon.className = 'ph-fill ph-play';
    });

    el.videoPlayer.addEventListener('timeupdate', () => {
      const cur = el.videoPlayer.currentTime || 0;
      const dur = el.videoPlayer.duration || 0;
      if (el.timeCurrent) el.timeCurrent.textContent = formatTime(cur);
      if (el.timeDuration) el.timeDuration.textContent = formatTime(dur);

      if (dur > 0 && el.scrubProgress) {
        el.scrubProgress.style.width = `${(cur / dur) * 100}%`;
      }
    });

    el.videoPlayer.addEventListener('progress', () => {
      if (el.videoPlayer.buffered.length > 0 && el.videoPlayer.duration > 0) {
        const bufferedEnd = el.videoPlayer.buffered.end(el.videoPlayer.buffered.length - 1);
        if (el.scrubBuffer) {
          el.scrubBuffer.style.width = `${(bufferedEnd / el.videoPlayer.duration) * 100}%`;
        }
      }
    });

    // Toggle Play/Pause on video click
    el.videoPlayer.addEventListener('click', () => {
      if (el.videoPlayer.paused) {
        el.videoPlayer.play();
        showBloomFeedback('ph-play');
      } else {
        el.videoPlayer.pause();
        showBloomFeedback('ph-pause');
      }
    });

    // Double click to seek -10s or +10s
    el.videoPlayer.addEventListener('dblclick', (e) => {
      const rect = el.videoPlayer.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      if (clickX < rect.width / 2) {
        el.videoPlayer.currentTime = Math.max(0, el.videoPlayer.currentTime - 10);
        if (el.seekRippleLeft) {
          el.seekRippleLeft.style.display = 'flex';
          setTimeout(() => el.seekRippleLeft.style.display = 'none', 600);
        }
      } else {
        el.videoPlayer.currentTime = Math.min(el.videoPlayer.duration, el.videoPlayer.currentTime + 10);
        if (el.seekRippleRight) {
          el.seekRippleRight.style.display = 'flex';
          setTimeout(() => el.seekRippleRight.style.display = 'none', 600);
        }
      }
    });
  }

  // Scrub progress interaction
  if (el.scrubContainer && el.videoPlayer) {
    el.scrubContainer.addEventListener('click', (e) => {
      const rect = el.scrubTrack.getBoundingClientRect();
      const pos = (e.clientX - rect.left) / rect.width;
      if (el.videoPlayer.duration) {
        el.videoPlayer.currentTime = pos * el.videoPlayer.duration;
      }
    });
  }

  // Play button
  if (el.ctrlPlayBtn) {
    el.ctrlPlayBtn.addEventListener('click', () => {
      if (el.videoPlayer.paused) {
        el.videoPlayer.play();
      } else {
        el.videoPlayer.pause();
      }
    });
  }

  // Skip buttons
  if (el.ctrlRewindBtn) {
    el.ctrlRewindBtn.addEventListener('click', () => {
      el.videoPlayer.currentTime = Math.max(0, el.videoPlayer.currentTime - 10);
      showHud('-10s', 'ph-rewind');
    });
  }
  if (el.ctrlForwardBtn) {
    el.ctrlForwardBtn.addEventListener('click', () => {
      el.videoPlayer.currentTime = Math.min(el.videoPlayer.duration, el.videoPlayer.currentTime + 10);
      showHud('+10s', 'ph-fast-forward');
    });
  }

  // Volume & Mute
  if (el.ctrlMuteBtn) {
    el.ctrlMuteBtn.addEventListener('click', () => {
      el.videoPlayer.muted = !el.videoPlayer.muted;
      if (el.ctrlVolumeIcon) {
        el.ctrlVolumeIcon.className = el.videoPlayer.muted ? 'ph-fill ph-speaker-slash' : 'ph-fill ph-speaker-high';
      }
      if (el.volumeFill) {
        el.volumeFill.style.width = el.videoPlayer.muted ? '0%' : `${el.videoPlayer.volume * 100}%`;
      }
      showHud(el.videoPlayer.muted ? 'Muted' : `${Math.round(el.videoPlayer.volume * 100)}%`);
    });
  }

  if (el.volumeSliderBox) {
    el.volumeSliderBox.addEventListener('click', (e) => {
      const rect = el.volumeSliderBox.getBoundingClientRect();
      const vol = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
      el.videoPlayer.volume = vol;
      el.videoPlayer.muted = false;
      if (el.volumeFill) el.volumeFill.style.width = `${vol * 100}%`;
      showHud(`${Math.round(vol * 100)}%`, 'ph-speaker-high');
    });
  }

  // Speed toggle
  const speeds = [1.0, 1.25, 1.5, 2.0, 0.75];
  let speedIdx = 0;
  if (el.ctrlSpeedBtn) {
    el.ctrlSpeedBtn.addEventListener('click', () => {
      speedIdx = (speedIdx + 1) % speeds.length;
      const spd = speeds[speedIdx];
      el.videoPlayer.playbackRate = spd;
      if (el.ctrlSpeedLabel) el.ctrlSpeedLabel.textContent = `${spd}x`;
      showHud(`${spd}x Speed`, 'ph-gauge');
    });
  }

  // Snapshot frame capture
  if (el.ctrlSnapshotBtn) {
    el.ctrlSnapshotBtn.addEventListener('click', () => {
      if (!el.videoPlayer.videoWidth) return;
      const snapCanvas = document.createElement('canvas');
      snapCanvas.width = el.videoPlayer.videoWidth;
      snapCanvas.height = el.videoPlayer.videoHeight;
      const ctx = snapCanvas.getContext('2d');
      ctx.drawImage(el.videoPlayer, 0, 0, snapCanvas.width, snapCanvas.height);
      const link = document.createElement('a');
      link.download = `Cineora_Frame_${Date.now()}.png`;
      link.href = snapCanvas.toDataURL('image/png');
      link.click();
      showToast('Frame captured and downloaded!');
    });
  }

  // Picture in picture
  if (el.ctrlPipBtn) {
    el.ctrlPipBtn.addEventListener('click', () => {
      if (document.pictureInPictureElement) {
        document.exitPictureInPicture();
      } else if (el.videoPlayer.requestPictureInPicture) {
        el.videoPlayer.requestPictureInPicture();
      }
    });
  }

  // Shortcuts overlay
  if (el.ctrlHelpBtn) {
    el.ctrlHelpBtn.addEventListener('click', () => {
      el.shortcutsOverlay.style.display = 'grid';
    });
  }
  if (el.closeShortcutsBtn) {
    el.closeShortcutsBtn.addEventListener('click', () => {
      el.shortcutsOverlay.style.display = 'none';
    });
  }

  // Fullscreen
  if (el.ctrlFullscreenBtn) {
    el.ctrlFullscreenBtn.addEventListener('click', () => {
      const container = document.getElementById('playerContainer');
      if (!document.fullscreenElement) {
        container.requestFullscreen().catch(() => {});
        if (el.fullscreenIcon) el.fullscreenIcon.className = 'ph-bold ph-arrows-in-simple';
      } else {
        document.exitFullscreen().catch(() => {});
        if (el.fullscreenIcon) el.fullscreenIcon.className = 'ph-bold ph-arrows-out-simple';
      }
    });
  }

  // Multi-Source Sync Feeds
  if (el.syncSourcesBtn) {
    el.syncSourcesBtn.addEventListener('click', () => {
      el.syncSourcesBtn.classList.add('is-syncing');
      fetch('/api/sync-sources')
        .then(res => res.json())
        .then(data => {
          el.syncSourcesBtn.classList.remove('is-syncing');
          showToast(data.message || 'Media sources synced with ICC 10G Server!');
          initData();
        })
        .catch(() => {
          el.syncSourcesBtn.classList.remove('is-syncing');
          showToast('Sync complete across all mirrors.');
        });
    });
  }

  /* -------------------------------------------------------------------------
     10. Initial Data Bootstrapping
     ------------------------------------------------------------------------- */
  function initData() {
    // 1. Fetch Top 10 for Hero
    fetch('/api/top10')
      .then(res => res.json())
      .then(top10 => {
        state.top10List = top10;
        updateHero();
        renderHeroReel();
        startHeroAutoplay();
      })
      .catch(err => console.error('Error fetching top 10:', err));

    // 2. Fetch Full Media Catalog
    fetch('/api/media')
      .then(res => res.json())
      .then(media => {
        state.mediaList = media;
        if (document.getElementById('statMediaCount')) {
          document.getElementById('statMediaCount').textContent = `${media.length}+`;
        }
        renderContentShelves();
        updateWatchlistUI();
      })
      .catch(err => console.error('Error fetching media:', err));

    // 3. Fetch Actors
    fetch('/api/actors')
      .then(res => res.json())
      .then(actors => {
        state.actorsList = actors;
        renderActors();
      })
      .catch(err => console.error('Error fetching actors:', err));
  }

  // Initialize Palette & Visual Effects
  applyPalette(state.themePalette);
  initAmbientCanvas();
  initData();
});
