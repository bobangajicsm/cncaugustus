// Mobile navigation toggle
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (!toggle || !links) return;
  toggle.addEventListener('click', function () {
    var open = links.classList.toggle('open');
    toggle.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  document.addEventListener('click', function (e) {
    if (!links.contains(e.target) && !toggle.contains(e.target)) {
      links.classList.remove('open');
      toggle.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });
})();

// Contact form: AJAX submit via Formspree so the page never navigates away
(function () {
  var form = document.querySelector('form[data-contact]');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    // Client-side required check
    var required = form.querySelectorAll('[required]');
    for (var i = 0; i < required.length; i++) {
      if (!required[i].value.trim()) {
        required[i].focus();
        return;
      }
    }

    var btn = form.querySelector('button[type="submit"]');
    btn.disabled = true;

    fetch(form.action, {
      method: 'POST',
      body: new FormData(form),
      headers: { 'Accept': 'application/json' }
    }).then(function (res) {
      if (res.ok) {
        form.reset();
        var msg = form.parentNode.querySelector('.form-sent');
        if (msg) msg.style.display = 'block';
        form.style.display = 'none';
      } else {
        btn.disabled = false;
        alert('Something went wrong. Please try again or email us directly.');
      }
    }).catch(function () {
      btn.disabled = false;
      alert('Something went wrong. Please try again or email us directly.');
    });
  });
})();
