import { useState, useEffect } from 'react';
import './index.css';

const App = () => {
  const [cpu, setCpu] = useState(38);
  const [memory, setMemory] = useState(62);
  const [reqPerSec, setReqPerSec] = useState(142);
  const [activeUsers, setActiveUsers] = useState(890);

  useEffect(() => {
    const timer = setInterval(() => {
      setCpu(prev => Math.max(10, Math.min(95, prev + (Math.random() * 14 - 7))));
      setMemory(prev => Math.max(20, Math.min(90, prev + (Math.random() * 6 - 3))));
      setReqPerSec(prev => Math.max(50, Math.floor(prev + (Math.random() * 40 - 20))));
      setActiveUsers(prev => Math.max(100, Math.floor(prev + (Math.random() * 10 - 5))));
    }, 2000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="dashboard-wrapper">
      <nav className="sidebar">
        <div className="brand">
          <div className="logo-pulse"></div>
          <h2>SafeK<span className="accent">.Ops</span></h2>
        </div>
        <ul className="nav-links">
          <li className="active"><i className="icon">📊</i> Overview</li>
          <li><i className="icon">🌐</i> Nginx Metrics</li>
          <li><i className="icon">🦊</i> Grafana View</li>
          <li><i className="icon">⚙️</i> Settings</li>
        </ul>
      </nav>

      <main className="main-content">
        <header className="topbar">
          <div>
            <h1 className="page-title">System Metrics</h1>
            <p className="subtitle">Real-time monitoring infrastructure</p>
          </div>
          <div className="status-badge">
            <span className="dot online"></span> System Healthy
          </div>
        </header>

        <section className="metrics-grid">
          <div className="metric-card">
            <h3>CPU Usage</h3>
            <div className="value">{cpu.toFixed(1)}<span className="unit">%</span></div>
            <div className="progress-bar">
              <div className="fill" style={{ width: `${cpu}%`, background: cpu > 80 ? '#FF3B30' : '#34C759' }}></div>
            </div>
          </div>
          <div className="metric-card">
            <h3>Memory Allocation</h3>
            <div className="value">{memory.toFixed(1)}<span className="unit">%</span></div>
            <div className="progress-bar">
              <div className="fill" style={{ width: `${memory}%`, background: '#007AFF' }}></div>
            </div>
          </div>
          <div className="metric-card">
            <h3>Requests / sec</h3>
            <div className="value">{reqPerSec}</div>
            <div className="sparkline">〰️〰️〰️📈</div>
          </div>
          <div className="metric-card">
            <h3>Active Users</h3>
            <div className="value">{activeUsers}</div>
            <div className="sparkline">〰️〰️📈</div>
          </div>
        </section>

        <section className="charts-section">
          <div className="chart-container large">
            <div className="chart-header">
              <h3>Live Network Traffic</h3>
              <div className="chart-actions">
                <button className="btn-tab active">1H</button>
                <button className="btn-tab">24H</button>
                <button className="btn-tab">7D</button>
              </div>
            </div>
            <div className="fake-chart-area">
               {/* 흉내낸 차트 라인들 */}
               <svg viewBox="0 0 100 30" className="chart-svg" preserveAspectRatio="none">
                 <path d="M0,20 Q10,5 20,15 T40,10 T60,25 T80,5 T100,15 L100,30 L0,30 Z" fill="rgba(88, 86, 214, 0.2)" stroke="none"/>
                 <path d="M0,20 Q10,5 20,15 T40,10 T60,25 T80,5 T100,15" fill="none" stroke="#5856D6" strokeWidth="0.5"/>
               </svg>
            </div>
          </div>

          <div className="chart-container">
            <div className="chart-header">
              <h3>Recent Alerts</h3>
            </div>
            <ul className="alert-list">
              <li className="alert-item warning">
                <span className="time">10:42 AM</span>
                <span className="msg">High memory usage detected on Redis</span>
              </li>
              <li className="alert-item info">
                <span className="time">09:15 AM</span>
                <span className="msg">Prometheus snapshot created successfully</span>
              </li>
              <li className="alert-item error">
                <span className="time">08:03 AM</span>
                <span className="msg">Failed to pull Grafana dashboard changes</span>
              </li>
              <li className="alert-item info">
                <span className="time">Yesterday</span>
                <span className="msg">System resumed normal operations</span>
              </li>
            </ul>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
