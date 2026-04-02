'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';

const navItems = [
  { href: '/', label: 'Dashboard', icon: '📊' },
  { href: '/monitoring/email', label: 'Email', icon: '📧' },
  { href: '/monitoring/sms', label: 'SMS', icon: '💬' },
  { href: '/monitoring/voice', label: 'Voice', icon: '📞' },
  { href: '/alerts', label: 'Alerts', icon: '🔔' },
  { href: '/trunks', label: 'Trunks', icon: '🔗' },
  { href: '/agents', label: 'Agents', icon: '👤' },
  { href: '/reports', label: 'Reports', icon: '📈' },
];

export function Sidebar() {
  const pathname = usePathname();
  return (
    <aside className="w-64 h-screen bg-gray-900 text-white fixed left-0 top-0 flex flex-col">
      <div className="p-6 border-b border-gray-800">
        <h1 className="text-xl font-bold">VoIP Ops</h1>
        <p className="text-xs text-gray-400 mt-1">Operations Dashboard</p>
      </div>
      <nav className="flex-1 p-4 space-y-1">
        {navItems.map((item) => {
          const isActive = pathname === item.href || pathname?.startsWith(item.href + '/');
          return (
            <Link
              key={item.href}
              href={item.href}
              className={`flex items-center gap-3 px-4 py-2.5 rounded-lg text-sm font-medium transition-colors ${
                isActive
                  ? 'bg-blue-600 text-white'
                  : 'text-gray-300 hover:bg-gray-800 hover:text-white'
              }`}
            >
              <span>{item.icon}</span>
              <span>{item.label}</span>
            </Link>
          );
        })}
      </nav>
      <div className="p-4 border-t border-gray-800">
        <div className="flex items-center gap-2">
          <div className="w-2 h-2 rounded-full bg-green-400 animate-pulse" />
          <span className="text-xs text-gray-400">System Online</span>
        </div>
      </div>
    </aside>
  );
}
