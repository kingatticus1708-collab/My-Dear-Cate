<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>My Dear Kate 💙</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
<style>
:root{--blue:#4fa8ff;--blue-soft:#b5dcff;--cyan:#6bd5ff;--card:rgba(255,255,255,0.07)}
*{box-sizing:border-box}
::-webkit-scrollbar{width:10px}
::-webkit-scrollbar-track{background:#050d1f}
::-webkit-scrollbar-thumb{background:linear-gradient(180deg,var(--blue),var(--cyan));border-radius:10px}
::selection{background:var(--blue);color:#04122a}

body{
  margin:0;font-family:'Poppins',sans-serif;
  background:radial-gradient(circle at 20% 10%,#123a66 0%,#0a1a33 45%,#050d1f 100%);
  background-size:200% 200%;animation:bgShift 20s ease infinite;
  color:#fff;text-align:center;overflow-x:hidden;min-height:100vh;cursor:none;
}
@keyframes bgShift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}

/* CINEMATIC SPLASH */
#splash{position:fixed;inset:0;background:#050d1f;z-index:10000;display:flex;flex-direction:column;align-items:center;justify-content:center;transition:opacity 1.5s ease,visibility 1.5s ease}
#splash.hidden{opacity:0;visibility:hidden}
.splash-heart{width:80px;height:80px;background:var(--cyan);clip-path:polygon(50% 15%,90% 40%,50% 90%,10% 40%);animation:pulse 1.5s infinite;box-shadow:0 0 40px var(--cyan);cursor:pointer}
@keyframes pulse{0%{transform:scale(1)}50%{transform:scale(1.2)}100%{transform:scale(1)}}
.splash-text{margin-top:30px;font-family:'Dancing Script',cursive;font-size:40px;color:var(--blue-soft);letter-spacing:2px;animation:fadeIn 2s ease}

/* BACKGROUNDS */
.hearts-bg{position:fixed;inset:0;pointer-events:none;overflow:hidden;z-index:0}
.hearts-bg span{position:absolute;bottom:-40px;font-size:22px;color:var(--blue);opacity:0.5;animation:floatUp linear infinite}
@keyframes floatUp{0%{transform:translateY(0) rotate(0deg);opacity:0}10%{opacity:0.6}100%{transform:translateY(-110vh) rotate(360deg);opacity:0}}

/* CURSOR */
.cursor-dot{position:fixed;width:14px;height:14px;border-radius:50%;background:radial-gradient(circle,var(--cyan),var(--blue));box-shadow:0 0 15px var(--cyan);pointer-events:none;z-index:9999;transform:translate(-50%,-50%);transition:width 0.2s,height 0.2s}
.cursor-sparkle{position:fixed;pointer-events:none;z-index:9997;font-size:14px;animation:sparkleFade 0.9s ease forwards;transform:translate(-50%,-50%)}
@keyframes sparkleFade{0%{opacity:1;transform:translate(-50%,-50%) scale(1)}100%{opacity:0;transform:translate(-50%,-80%) scale(0.3)}}

header{position:relative;z-index:2;padding:80px 20px 40px}
.hero-title{font-family:'Dancing Script',cursive;font-size:clamp(48px,9vw,90px);margin:0;background:linear-gradient(90deg,#6bd5ff,#4fa8ff,#2d8cff);-webkit-background-clip:text;color:transparent;animation:glow 3s ease-in-out infinite alternate}
@keyframes glow{from{filter:drop-shadow(0 0 8px rgba(79,168,255,0.4))}to{filter:drop-shadow(0 0 22px rgba(107,213,255,0.85))}}
.hero-sub{font-weight:300;font-size:18px;color:var(--blue-soft);margin:10px 0 35px;letter-spacing:1px}
button{font-family:'Poppins',sans-serif;background:linear-gradient(135deg,var(--blue),var(--cyan));color:#04122a;border:none;padding:14px 30px;border-radius:40px;cursor:none;font-size:16px;font-weight:600;letter-spacing:0.5px;box-shadow:0 8px 25px rgba(79,168,255,0.45);transition:transform 0.2s,box-shadow 0.2s}
button:hover{transform:translateY(-3px) scale(1.04);box-shadow:0 12px 35px rgba(107,213,255,0.7)}

section{position:relative;z-index:2;padding:40px 20px;max-width:1000px;margin:0 auto}
h2{font-family:'Dancing Script',cursive;font-size:38px;color:var(--blue-soft);margin-bottom:25px}

.counter-box,.memory{background:var(--card);backdrop-filter:blur(10px);border:1px solid rgba(181,220,255,0.25);border-radius:24px;padding:40px 30px;margin:20px auto;max-width:640px;box-shadow:0 10px 40px rgba(0,0,0,0.35);transition:transform 0.3s}
.memory:hover{transform:translateY(-5px);box-shadow:0 15px 50px rgba(79,168,255,0.3)}

.days-number{font-family:'Dancing Script',cursive;font-size:clamp(60px,14vw,110px);line-height:1;background:linear-gradient(90deg,#6bd5ff,#4fa8ff);-webkit-background-clip:text;color:transparent;animation:glow 3s ease-in-out infinite alternate}
.counter-label{color:var(--blue-soft);font-weight:300;letter-spacing:2px;text-transform:uppercase;font-size:14px;margin-top:10px}
.counter-detail{margin-top:18px;font-size:14px;color:#a9c7e8;font-weight:300}

.voice-player{background:linear-gradient(135deg, rgba(79,168,255,0.15), rgba(107,213,255,0.05));border:1px solid var(--cyan);border-radius:24px;padding:30px;margin:40px auto;max-width:500px;display:flex;flex-direction:column;align-items:center;gap:15px;box-shadow:0 10px 40px rgba(0,0,0,0.4)}
.voice-wave{display:flex;align-items:center;gap:4px;height:40px}
.voice-wave span{width:6px;background:var(--cyan);border-radius:10px;animation:wave 1.2s ease-in-out infinite}
.voice-wave span:nth-child(odd){animation-duration:0.8s}
.voice-wave span:nth-child(3n){animation-duration:1.5s}
@keyframes wave{0%,100%{height:10px;opacity:0.5}50%{height:35px;opacity:1;box-shadow:0 0 10px var(--cyan)}}

.slideshow{position:relative;width:100%;max-width:620px;height:420px;margin:20px auto;border-radius:22px;overflow:hidden;border:1px solid rgba(181,220,255,0.35);box-shadow:0 0 45px rgba(79,168,255,0.3)}
.slide{position:absolute;inset:0;opacity:0;transition:opacity 1.2s ease}
.slide.active{opacity:1}
.slide img{width:100%;height:100%;object-fit:cover;display:block}
.slide-caption{position:absolute;left:0;right:0;bottom:0;padding:22px 18px 16px;background:linear-gradient(to top,rgba(5,13,31,0.9),transparent);color:var(--blue-soft);font-size:16px;letter-spacing:0.5px}
.slide-dots{position:absolute;bottom:12px;left:0;right:0;z-index:2}
.slide-dots span{display:inline-block;width:9px;height:9px;margin:0 4px;border-radius:50%;background:rgba(181,220,255,0.4);cursor:none;transition:background 0.3s,transform 0.3s}
.slide-dots span.active{background:var(--cyan);transform:scale(1.3);box-shadow:0 0 10px var(--cyan)}

.gallery{padding:50px 20px;perspective:1000px}
.photo-card{display:inline-block;vertical-align:top;background:var(--card);backdrop-filter:blur(8px);padding:14px;margin:16px;border-radius:22px;border:1px solid rgba(181,220,255,0.35);box-shadow:0 0 25px rgba(79,168,255,0.25);width:260px;transition:transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.6s;transform:rotateX(10deg) translateY(0px) scale(0.95)}
.photo-card:hover{transform:rotateX(0deg) translateY(-10px) scale(1.05);box-shadow:0 0 45px rgba(107,213,255,0.65)}
.photo-card img{width:100%;height:250px;object-fit:cover;border-radius:16px;display:block}
.photo-card p{color:var(--blue-soft);font-size:16px;margin:12px 0 4px}

.flip-grid{display:flex;flex-wrap:wrap;justify-content:center;gap:20px;max-width:900px;margin:0 auto}
.flip-card{width:220px;height:160px;perspective:1000px;cursor:none}
.flip-inner{position:relative;width:100%;height:100%;transition:transform 0.7s cubic-bezier(0.4,0.2,0.2,1);transform-style:preserve-3d}
.flip-card.flipped .flip-inner{transform:rotateY(180deg)}
.flip-front,.flip-back{position:absolute;inset:0;border-radius:18px;display:flex;align-items:center;justify-content:center;padding:16px;backface-visibility:hidden;border:1px solid rgba(181,220,255,0.35);box-shadow:0 8px 30px rgba(0,0,0,0.35)}
.flip-front{background:linear-gradient(135deg,rgba(79,168,255,0.25),rgba(107,213,255,0.15));font-family:'Dancing Script',cursive;font-size:26px;color:var(--blue-soft)}
.flip-back{background:linear-gradient(135deg,rgba(45,140,255,0.35),rgba(10,26,51,0.9));transform:rotateY(180deg);font-size:15px;line-height:1.5;color:#e6f2ff;font-weight:300}

.love-message{background:var(--card);backdrop-filter:blur(10px);border:1px solid rgba(181,220,255,0.25);border-radius:24px;padding:45px 30px;margin:40px auto;max-width:720px;box-shadow:0 10px 50px rgba(0,0,0,0.4)}
.typewriter{font-weight:300;line-height:1.9;font-size:17px;color:#e6f2ff;min-height:130px;text-align:left;white-space:pre-wrap}
.cursor-blink{display:inline-block;width:2px;height:1.1em;background:var(--cyan);margin-left:2px;vertical-align:text-bottom;animation:blink 1s step-end infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
.surprise-btn-wrap{margin-top:30px;cursor:none}
.svg-heart{width:70px;height:70px;fill:none;stroke:var(--cyan);stroke-width:3px;transition:all 0.3s ease;filter:drop-shadow(0 0 10px var(--cyan))}
.surprise-btn-wrap:hover .svg-heart{fill:rgba(107,213,255,0.2);transform:scale(1.1)}
#surprise{margin-top:24px;font-family:'Dancing Script',cursive;font-size:30px;color:var(--cyan);animation:pop 0.6s ease}
@keyframes pop{0%{transform:scale(0.5);opacity:0}70%{transform:scale(1.1)}100%{transform:scale(1);opacity:1}}

#secretVault{position:fixed;inset:0;z-index:9990;background:rgba(5,13,31,0.95);backdrop-filter:blur(5px);display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity 0.8s ease}
#secretVault.open{opacity:1;pointer-events:auto}
#secretVault h2{font-size:60px;animation:glow 2s infinite alternate}
#secretVault p{font-size:20px;color:var(--cyan);max-width:600px;line-height:1.6}

#lyric-container{height:60px;margin:20px auto;max-width:600px;overflow:hidden;position:relative;display:flex;align-items:center;justify-content:center;font-family:'Dancing Script',cursive}
.lyric-line{position:absolute;width:100%;font-size:28px;color:rgba(181,220,255,0.3);transition:all 0.5s ease;transform:translateY(20px);opacity:0}
.lyric-line.active{color:var(--cyan);transform:translateY(0);opacity:1;text-shadow:0 0 15px var(--cyan);font-size:34px}

.floating-music{position:fixed;bottom:30px;right:30px;z-index:999;background:var(--card);backdrop-filter:blur(10px);border:1px solid var(--cyan);border-radius:50px;padding:10px 20px;display:flex;align-items:center;gap:10px;box-shadow:0 10px 30px rgba(0,0,0,0.5);cursor:none;transition:transform 0.2s ease}
.floating-music:hover{transform:translateY(-5px);background:rgba(79,168,255,0.2)}
.floating-music button{padding:8px 15px;font-size:14px}
.floating-music h3{margin:0;font-family:'Dancing Script',cursive;font-size:22px;color:var(--blue-soft)}
footer{position:relative;z-index:2;padding:40px 20px 100px;color:var(--blue-soft);font-weight:300;letter-spacing:1px;font-size:15px}

@media(max-width:900px){
  .photo-card{width:88%;margin:12px auto;display:block;transform:none!important}
  header{padding:80px 16px 50px}
  .love-message{padding:30px 20px}
  .slideshow{height:300px}
  .flip-card{width:46%;height:140px}
  .cursor-dot,.cursor-sparkle{display:none}
  body,button,.flip-card,.slide-dots span,.surprise-btn-wrap{cursor:auto}
  .floating-music{bottom:15px;right:15px;padding:5px 15px}
  .floating-music h3{display:none}
  #secretVault h2{font-size:40px}
}
</style>
</head>
<body>

<div id="splash">
  <div class="splash-heart" onclick="enterSite()"></div>
  <div class="splash-text">Click to enter</div>
</div>

<div class="hearts-bg" id="heartsBg"></div>
<div class="cursor-dot" id="cursorDot"></div>

<header>
  <h1 class="hero-title">My Dear Kate</h1>
  <p class="hero-sub">A little website made with love 💙</p>
  <button onclick="showMessage()">Open My Message</button>
</header>

<section>
  <div class="counter-box">
    <div class="days-number" id="daysNumber">0</div>
    <div class="counter-label" id="pastLabel">Days Since We Met</div>
    <div class="counter-detail" id="counterDetail"></div>
  </div>
  <div class="counter-box" style="margin-top:20px;padding:20px">
    <h3 style="font-family:'Dancing Script',cursive;font-size:26px;color:var(--cyan);margin:0 0 10px">Counting down to our future... 💍</h3>
    <div id="futureCountdown" style="font-size:20px;font-weight:600;letter-spacing:1px">Loading...</div>
  </div>
</section>

<section class="voice-player">
  <h2 style="margin:0;font-size:28px;color:var(--cyan)">A Voice Note For You 🎙️</h2>
  <div class="voice-wave"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
  <button onclick="toggleVoiceNote()" id="voiceBtn">▶ Play My Voice</button>
  <audio id="myVoiceNote"><source src="music/voice.m4a" type="audio/mp4"></audio>
</section>

<section>
  <h2>Our Song 🎵</h2>
  <div id="lyric-container">
    <div class="lyric-line" data-time="0">Listen to the music...</div>
    <div class="lyric-line" data-time="5">I found a love, for me 💙</div>
    <div class="lyric-line" data-time="10">Darling just dive right in</div>
    <div class="lyric-line" data-time="15">And follow my lead</div>
    <div class="lyric-line" data-time="20">Well I found a girl, beautiful and sweet</div>
    <div class="lyric-line" data-time="25">Oh, I never knew you were the someone waiting for me</div>
    <div class="lyric-line" data-time="30">'Cause we were just kids when we fell in love</div>
    <div class="lyric-line" data-time="35">Not knowing what it was</div>
    <div class="lyric-line" data-time="40">I will not give you up this time 💙</div>
  </div>
</section>

<section>
  <h2>Our Story in Pictures 💙</h2>
  <div class="slideshow" id="slideshow">
    <div class="slide active"><img src="./images/cate1.jpg" alt="Kate"><div class="slide-caption">My Dear Kate 💙</div></div>
    <div class="slide"><img src="./images/cate2.jpg" alt="Us"><div class="slide-caption">Our beautiful memories 💙</div></div>
    <div class="slide"><img src="./images/cate3.jpg" alt="Memory"><div class="slide-caption">A moment to remember 💙</div></div>
    <div class="slide"><img src="./images/cate4.jpg" alt="Forever"><div class="slide-caption">Forever in my memories 💙</div></div>
    <div class="slide"><img src="./images/cate5.jpg" alt="Heart"><div class="slide-caption">Always in my heart 💙</div></div>
    <div class="slide-dots" id="slideDots"></div>
  </div>
</section>

<section>
  <div class="memory"><h2>Our Beautiful Memories 📸</h2><p>Every picture tells a story.</p></div>
  <div class="memory"><h2>A Special Message ✉️</h2><p>You make ordinary moments special.</p></div>
</section>

<section class="gallery" id="photo-reel">
  <h2>More Special Memories 💙</h2>
  <div class="photo-card"><img src="./images/cate6.jpg" alt="6"><p>A beautiful day 💙</p></div>
  <div class="photo-card"><img src="./images/cate7.jpg" alt="7"><p>Smiles forever 💙</p></div>
  <div class="photo-card"><img src="./images/cate8.jpg" alt="8"><p>My favorite person 💙</p></div>
  <div class="photo-card"><img src="./images/cate9.jpg" alt="9"><p>Good times 💙</p></div>
  <div class="photo-card"><img src="./images/cate10.jpg" alt="10"><p>Endless love 💙</p></div>
</section>

<section>
  <h2>Reasons I Love You 💙</h2>
  <div class="flip-grid">
    <div class="flip-card"><div class="flip-inner"><div class="flip-front">Reason #1</div><div class="flip-back">Your smile lights up every room you walk into.</div></div></div>
    <div class="flip-card"><div class="flip-inner"><div class="flip-front">Reason #2</div><div class="flip-back">You make ordinary days feel like adventures.</div></div></div>
    <div class="flip-card"><div class="flip-inner"><div class="flip-front">Reason #3</div><div class="flip-back">You listen like no one else does.</div></div></div>
    <div class="flip-card"><div class="flip-inner"><div class="flip-front">Reason #4</div><div class="flip-back">Your laugh is my favorite sound.</div></div></div>
    <div class="flip-card"><div class="flip-inner"><div class="flip-front">Reason #5</div><div class="flip-back">You're kind even when no one is watching.</div></div></div>
    <div class="flip-card"><div class="flip-inner"><div class="flip-front">Reason #6</div><div class="flip-back">Being with you feels like home.</div></div></div>
  </div>
</section>

<section class="love-message">
  <h2>A Message From My Heart 💙</h2>
  <p class="typewriter" id="typewriter"></p>
  <div class="surprise-btn-wrap" onclick="openVault()">
    <svg class="svg-heart" viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
  </div>
  <p id="surprise" style="display:none;">You make my world a little brighter every day. 💙</p>
</section>

<div id="secretVault">
  <h2>You found the secret! 💙</h2>
  <p>I wanted to hide this here just for you. You mean more to me than any words on this page could ever say. Thank you for being my everything.</p>
</div>

<div class="floating-music" onclick="toggleMusic()">
  <h3>🎵 Our Song</h3><button id="musicBtn">▶ Play</button>
</div>
<audio id="ourSong" loop><source src="music/love.mp3" type="audio/mpeg"></audio>
<footer>Made specially for Kate 💙</footer>

<script>
// 1. SPLASH SCREEN
function enterSite() {
  document.getElementById('splash').classList.add('hidden');
  if (!window.hasEntered) {
    window.hasEntered = true;
    // Auto-start the music after entering
    toggleMusic();
  }
}

// 2. UI & LOAD
const isMobile = window.matchMedia('(max-width: 900px)').matches;

// 3. SAFE FLOATING HEARTS
const bg = document.getElementById('heartsBg');
for (let i = 0; i < 20; i++) {
  const el = document.createElement('span');
  el.textContent = ['💙','🩵','💠','✨'][Math.floor(Math.random()*4)];
  el.style.left = Math.random() * 100 + 'vw';
  el.style.fontSize = (14 + Math.random() * 20) + 'px';
  el.style.animationDuration = (8 + Math.random() * 10) + 's';
  el.style.animationDelay = (Math.random() * 5) + 's';
  bg.appendChild(el);
}

// 4. CURSOR & PHOTO REEL SCROLL
if (!isMobile) {
  const dot = document.getElementById('cursorDot');
  let lastSparkle = 0;
  document.addEventListener('mousemove', (e) => {
    dot.style.left = e.clientX + 'px'; dot.style.top = e.clientY + 'px';
    if (Date.now() - lastSparkle > 50) {
      lastSparkle = Date.now();
      const s = document.createElement('span');
      s.className = 'cursor-sparkle';
      s.textContent = ['✨','💙'][Math.floor(Math.random()*2)];
      s.style.left = e.clientX + 'px'; s.style.top = e.clientY + 'px';
      document.body.appendChild(s);
      setTimeout(() => s.remove(), 900);
    }
  });
  document.addEventListener('mousedown', () => { dot.style.width = '8px'; dot.style.height = '8px'; });
  document.addEventListener('mouseup', () => { dot.style.width = '14px'; dot.style.height = '14px'; });

  window.addEventListener('scroll', () => {
    const reel = document.getElementById('photo-reel');
    if(!reel) return;
    const rect = reel.getBoundingClientRect();
    const viewHeight = window.innerHeight;
    if (rect.top < viewHeight && rect.bottom > 0) {
      const offset = (viewHeight - rect.top) / viewHeight;
      document.querySelectorAll('.photo-card').forEach((card) => {
        card.style.transform = `rotateX(${10 - offset * 15}deg) translateY(${offset * -20}px) scale(${0.95 + offset * 0.05})`;
      });
    }
  });
}

// 5. COUNTERS
const startDate = new Date("2018-02-01T00:00:00"), nextDate = new Date("2033-11-29T00:00:00");
function updateCounters() {
  const now = new Date(), diffPast = now - startDate;
  if(diffPast > 0) {
    document.getElementById("daysNumber").textContent = Math.floor(diffPast / 86400000).toLocaleString();
    document.getElementById("counterDetail").textContent = `${Math.floor((diffPast / 3600000) % 24)}h · ${Math.floor((diffPast / 60000) % 60)}m · ${Math.floor((diffPast / 1000) % 60)}s and counting…`;
  }
  const diffFuture = nextDate - now;
  if (diffFuture > 0) document.getElementById("futureCountdown").textContent = `${Math.floor(diffFuture / 86400000)} days, ${Math.floor((diffFuture / 3600000) % 24)} hrs, ${Math.floor((diffFuture / 60000) % 60)} mins`;
}
updateCounters(); setInterval(updateCounters, 1000);

// 6. SLIDESHOW
const slides = document.querySelectorAll('.slide'), dotsContainer = document.getElementById('slideDots'); let currentSlide = 0, slideTimer;
slides.forEach((_, i) => {
  const dot = document.createElement('span'); if (i === 0) dot.classList.add('active');
  dot.addEventListener('click', () => goToSlide(i)); dotsContainer.appendChild(dot);
});
const dots = dotsContainer.querySelectorAll('span');
function goToSlide(index) {
  slides[currentSlide].classList.remove('active'); dots[currentSlide].classList.remove('active');
  currentSlide = index; slides[currentSlide].classList.add('active'); dots[currentSlide].classList.add('active');
  clearInterval(slideTimer); slideTimer = setInterval(() => goToSlide((currentSlide + 1) % slides.length), 4000);
}
slideTimer = setInterval(() => goToSlide((currentSlide + 1) % slides.length), 4000);

// 7. TYPEWRITER
const letterText = "My Dear Kate,\n\nYou are someone special to me. Every moment we share becomes a beautiful memory. I hope this little website reminds you how much you mean to me. Thank you for being you. 💙";
const typeTarget = document.getElementById('typewriter'); let charIndex = 0;
function typeLetter() {
  if (charIndex < letterText.length) { typeTarget.textContent += letterText.charAt(charIndex); charIndex++; setTimeout(typeLetter, 50); }
  else { const cursor = document.createElement('span'); cursor.className = 'cursor-blink'; typeTarget.appendChild(cursor); }
}
setTimeout(typeLetter, 1000);

// 8. INTERACTIONS
function showMessage() { alert("Kate, you're truly special! 💙"); }
function openVault() {
  document.getElementById("secretVault").classList.add('open');
  document.getElementById("surprise").style.display = "block";
}
const song = document.getElementById("ourSong"), btn = document.getElementById("musicBtn");
const lyrics = document.querySelectorAll('.lyric-line');
function toggleMusic() {
  if (song.paused) { song.play(); btn.innerHTML = "⏸ Pause"; syncLyrics(); }
  else { song.pause(); btn.innerHTML = "▶ Play"; }
}
function syncLyrics() {
  if (song.paused) return;
  const time = song.currentTime;
  lyrics.forEach(line => {
    const startTime = parseFloat(line.getAttribute('data-time'));
    if (time >= startTime && time < startTime + 5) line.classList.add('active');
    else line.classList.remove('active');
  });
  requestAnimationFrame(syncLyrics);
}

const voiceNote = document.getElementById("myVoiceNote"), voiceBtn = document.getElementById("voiceBtn");
function toggleVoiceNote() {
  if (voiceNote.paused) { voiceNote.play(); voiceBtn.innerHTML = "⏸ Pause Voice Note"; }
  else { voiceNote.pause(); voiceBtn.innerHTML = "▶ Play My Voice"; }
}

document.querySelectorAll('.flip-card').forEach(card => card.addEventListener('click', () => card.classList.toggle('flipped')));
let keys = "";
document.addEventListener('keydown', (e) => {
  keys = (keys + e.key.toLowerCase()).slice(-4);
  if (keys === "open") { openVault(); keys = ""; }
});
</script>
</body>
</html>