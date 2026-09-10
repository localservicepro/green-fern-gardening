/* Green Fern Gardening Services — site behaviour
   Vanilla JS, no dependencies. Everything degrades gracefully without it. */
(function () {
  'use strict';

  document.documentElement.classList.remove('no-js');

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var desktop = window.matchMedia('(min-width: 1000px)');

  /* ---------------- Mobile nav ---------------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');

  function closeNav() {
    if (!toggle || !nav) return;
    toggle.setAttribute('aria-expanded', 'false');
    nav.classList.remove('is-open');
    document.body.style.removeProperty('overflow');
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', open ? 'false' : 'true');
      nav.classList.toggle('is-open', !open);
      document.body.style.overflow = open ? '' : 'hidden';
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeNav();
    });
    desktop.addEventListener('change', function (e) {
      if (e.matches) closeNav();
    });
  }

  /* ---------------- Services dropdown ----------------
     Desktop opens on hover via CSS. This handles touch/keyboard and mobile accordion. */
  Array.prototype.forEach.call(document.querySelectorAll('.has-dropdown'), function (item) {
    var trigger = item.querySelector('.dropdown-trigger');
    if (!trigger) return;

    trigger.addEventListener('click', function (e) {
      e.preventDefault();
      var open = item.getAttribute('data-open') === 'true';
      item.setAttribute('data-open', open ? 'false' : 'true');
      trigger.setAttribute('aria-expanded', open ? 'false' : 'true');
    });

    // On desktop, hovering is the primary interaction — keep ARIA in sync.
    item.addEventListener('mouseenter', function () {
      if (desktop.matches) trigger.setAttribute('aria-expanded', 'true');
    });
    item.addEventListener('mouseleave', function () {
      if (desktop.matches) {
        trigger.setAttribute('aria-expanded', 'false');
        item.setAttribute('data-open', 'false');
      }
    });
    document.addEventListener('click', function (e) {
      if (desktop.matches && !item.contains(e.target)) {
        item.setAttribute('data-open', 'false');
        trigger.setAttribute('aria-expanded', 'false');
      }
    });
  });

  /* ---------------- Sticky header shadow ---------------- */
  var header = document.querySelector('.site-header');
  function onScroll() {
    if (header) header.classList.toggle('is-stuck', window.pageYOffset > 8);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------------- Scroll reveal ---------------- */
  var revealables = document.querySelectorAll('[data-reveal]');
  if (!revealables.length) {
    /* nothing to do */
  } else if (reduceMotion || !('IntersectionObserver' in window)) {
    Array.prototype.forEach.call(revealables, function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    Array.prototype.forEach.call(revealables, function (el) { io.observe(el); });
  }

  /* ---------------- Quote form → GoHighLevel ----------------
     Field names map 1:1 to the GHL contact fields:
       full_name        -> {{contact.full_name}}
       email            -> {{contact.email}}
       phone            -> {{contact.phone}}
       property_address -> {{contact.property_address}}
       property_size    -> {{contact.property_size}}
       service_needed   -> {{contact.service_needed}}
       job_notes        -> {{contact.job_notes}}
     Set the endpoint once in assets/js/config.js (window.GF_CONFIG.ghlEndpoint). */
  Array.prototype.forEach.call(document.querySelectorAll('.quote-form'), function (form) {
    var status = form.querySelector('.form-status');
    var submitBtn = form.querySelector('[type="submit"]');
    var cfg = window.GF_CONFIG || {};
    var endpoint = cfg.ghlEndpoint || form.getAttribute('data-endpoint') || '';
    var thankYou = form.getAttribute('data-thank-you') || '/thank-you/';

    function setError(field, message) {
      field.setAttribute('aria-invalid', 'true');
      var err = field.parentNode.querySelector('.err');
      if (err && message) err.textContent = message;
    }
    function clearError(field) {
      field.removeAttribute('aria-invalid');
    }

    Array.prototype.forEach.call(form.querySelectorAll('input,select,textarea'), function (field) {
      field.addEventListener('input', function () { clearError(field); });
      field.addEventListener('blur', function () {
        if (field.required && !field.value.trim()) setError(field, 'This field is required.');
      });
    });

    function showStatus(message) {
      if (!status) return;
      status.textContent = message;
      status.className = 'form-status is-error';
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // Honeypot — silently succeed for bots.
      var hp = form.querySelector('input[name="company_website"]');
      if (hp && hp.value) { window.location.href = thankYou; return; }

      var invalid = null;
      Array.prototype.forEach.call(form.querySelectorAll('[required]'), function (field) {
        if (!field.value.trim() || (field.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(field.value))) {
          setError(field, field.type === 'email' && field.value.trim() ? 'Enter a valid email address.' : 'This field is required.');
          if (!invalid) invalid = field;
        } else {
          clearError(field);
        }
      });
      if (invalid) {
        invalid.focus();
        showStatus('Please check the highlighted fields and try again.');
        return;
      }

      if (!endpoint) {
        showStatus('This form is not connected yet. Please call 0420 462 848 and we will book you in.');
        return;
      }

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.dataset.label = submitBtn.textContent;
        submitBtn.textContent = 'Sending…';
      }
      if (status) status.className = 'form-status';

      var payload = {};
      new FormData(form).forEach(function (value, key) {
        if (key !== 'company_website') payload[key] = typeof value === 'string' ? value.trim() : value;
      });
      payload.page_url = window.location.href;

      fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      }).then(function (res) {
        if (!res.ok) throw new Error('Request failed with status ' + res.status);
        window.location.href = thankYou;
      }).catch(function () {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = submitBtn.dataset.label || 'Get my free quote';
        }
        showStatus('Something went wrong sending your request. Please call 0420 462 848 and we will sort it out.');
      });
    });
  });

  /* ---------------- Prefill service from ?service= ---------------- */
  var wanted = new URLSearchParams(window.location.search).get('service');
  if (wanted) {
    wanted = wanted.replace(/-/g, ' ');
    Array.prototype.forEach.call(document.querySelectorAll('[name="service_needed"]'), function (sel) {
      Array.prototype.forEach.call(sel.options, function (opt) {
        if (opt.value.toLowerCase() === wanted.toLowerCase()) sel.value = opt.value;
      });
    });
  }

  /* ---------------- Quote modal ----------------
     Opened by any [data-modal-open], closed by [data-modal-close], the backdrop
     or Escape. Focus is trapped while open and returned to the trigger on close. */
  var modal = document.getElementById('quote-modal');
  if (modal) {
    var lastFocused = null;
    var FOCUSABLE = 'a[href],button:not([disabled]),input:not([disabled]),select:not([disabled]),textarea:not([disabled]),[tabindex]:not([tabindex="-1"])';

    function openModal() {
      lastFocused = document.activeElement;
      modal.hidden = false;
      document.body.classList.add('modal-open');
      // Next frame so the transition runs from the hidden state.
      requestAnimationFrame(function () {
        modal.classList.add('is-open');
        var first = modal.querySelector('input:not([tabindex="-1"]),select,textarea');
        if (first) first.focus();
      });
    }

    function closeModal() {
      modal.classList.remove('is-open');
      document.body.classList.remove('modal-open');
      var done = function () {
        modal.hidden = true;
        modal.removeEventListener('transitionend', done);
      };
      if (reduceMotion) done();
      else modal.addEventListener('transitionend', done);
      if (lastFocused && lastFocused.focus) lastFocused.focus();
    }

    Array.prototype.forEach.call(document.querySelectorAll('[data-modal-open]'), function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        closeNav();
        openModal();
      });
    });

    modal.addEventListener('click', function (e) {
      if (e.target.closest('[data-modal-close]')) closeModal();
    });

    document.addEventListener('keydown', function (e) {
      if (modal.hidden) return;
      if (e.key === 'Escape') { closeModal(); return; }
      if (e.key !== 'Tab') return;
      var items = Array.prototype.filter.call(modal.querySelectorAll(FOCUSABLE), function (el) {
        return el.offsetParent !== null;
      });
      if (!items.length) return;
      var first = items[0], last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
  }

  /* ---------------- Current year ---------------- */
  Array.prototype.forEach.call(document.querySelectorAll('[data-year]'), function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
