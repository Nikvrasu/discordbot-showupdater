import { useState } from 'react'
import './Auth.css'

function Auth({ initialMode = 'login' }) {
  const [mode, setMode] = useState(initialMode)
  const [form, setForm] = useState({ username: '', email: '', password: '', confirm: '' })
  const [error, setError] = useState('')

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value })
    setError('')
  }

  const getErrorMessage = (detail) => {
    if (typeof detail === 'string') return detail
    if (Array.isArray(detail)) {
      return detail.map(err => {
        const loc = err.loc?.slice(1).join(' ') || 'field'
        return `${loc}: ${err.msg}`
      }).join('; ')
    }
    return 'Something went wrong.'
  }

  const clearForm = () => {
    setForm({ username: '', email: '', password: '', confirm: '' })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')

    if (mode === 'register' && form.password !== form.confirm) {
      setError('Passwords do not match.')
      clearForm()
      return
    }

    const endpoint = mode === 'login' ? '/auth/login' : '/auth/register'
    const body = mode === 'login'
      ? { email: form.email, password: form.password }
      : { username: form.username, email: form.email, password: form.password }

    try {
      const res = await fetch(`http://localhost:8000${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      })

      const data = await res.json()

      if (!res.ok) {
        setError(getErrorMessage(data.detail))
        clearForm()
        return
      }

      if (mode === 'login') {
        localStorage.setItem('token', data.access_token)
        window.location.href = '/dashboard'
      } else {
        setMode('login')
        clearForm()
      }
    } catch {
      setError('Could not connect to server.')
      clearForm()
    }
  }

  return (
    <div className="auth-page">
      <nav className="auth-nav">
        <a href="/" className="nav-logo">Notifier</a>
      </nav>

      <main className="auth-main">
        <div className="auth-card">
          <div className="auth-tabs">
            <button
              className={`auth-tab ${mode === 'login' ? 'active' : ''}`}
              onClick={() => { setMode('login'); setError('') }}
            >
              Log in
            </button>
            <button
              className={`auth-tab ${mode === 'register' ? 'active' : ''}`}
              onClick={() => { setMode('register'); setError('') }}
            >
              Register
            </button>
          </div>

          <form className="auth-form" onSubmit={handleSubmit}>
            {mode === 'register' && (
              <div className="field">
                <label>Username</label>
                <input
                  type="text"
                  name="username"
                  value={form.username}
                  onChange={handleChange}
                  placeholder="yourname"
                  required
                />
              </div>
            )}

            <div className="field">
              <label>Email</label>
              <input
                type="email"
                name="email"
                value={form.email}
                onChange={handleChange}
                placeholder="you@example.com"
                required
              />
            </div>

            <div className="field">
              <label>Password</label>
              <input
                type="password"
                name="password"
                value={form.password}
                onChange={handleChange}
                placeholder="••••••••"
                required
              />
            </div>

            {mode === 'register' && (
              <div className="field">
                <label>Confirm password</label>
                <input
                  type="password"
                  name="confirm"
                  value={form.confirm}
                  onChange={handleChange}
                  placeholder="••••••••"
                  required
                />
              </div>
            )}

            {error && <p className="auth-error">{error}</p>}

            <button type="submit" className="auth-submit">
              {mode === 'login' ? 'Log in' : 'Create account'}
            </button>
          </form>
        </div>
      </main>
    </div>
  )
}

export default Auth