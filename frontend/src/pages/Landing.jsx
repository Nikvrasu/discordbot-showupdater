import { Link } from 'react-router-dom'
import './Landing.css'

function Landing() {
  return (
    <div className="page">
      <nav className="nav">
        <span className="nav-logo">Notifier</span>
        <div className="nav-links">
          <Link to="/login" className="btn-ghost">Log in</Link>
          <Link to="/register" className="btn-primary">Get started</Link>
        </div>
      </nav>

      <main className="hero">
        <div className="badge">Discord · TMDB · YouTube</div>
        <h1 className="headline">
          Never miss<br />
          <span className="accent">a new episode.</span>
        </h1>
        <p className="subline">
          Track your favourite shows and channels. Get a Discord ping the moment something new drops.
        </p>
        <div className="cta-group">
          <Link to="/register" className="btn-primary large">Start tracking</Link>
          <Link to="/login" className="btn-ghost large">I have an account</Link>
        </div>
      </main>

      <section className="features">
        <div className="feature-card">
          <div className="feature-icon">&#9654;</div>
          <h3>Shows &amp; movies</h3>
          <p>Search any title via TMDB and get notified when a new episode or season lands.</p>
        </div>
        <div className="feature-card">
          <div className="feature-icon">&#9679;</div>
          <h3>YouTube channels</h3>
          <p>Follow any YouTube channel and get a ping when a new video goes live.</p>
        </div>
        <div className="feature-card">
          <div className="feature-icon">&#9650;</div>
          <h3>Discord notifications</h3>
          <p>All updates delivered straight to your Discord server. No app switching needed.</p>
        </div>
      </section>

      <footer className="footer">
        <span>Notifier &copy; {new Date().getFullYear()}</span>
      </footer>
    </div>
  )
}

export default Landing
