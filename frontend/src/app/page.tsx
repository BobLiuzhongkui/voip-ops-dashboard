/**
 * Dashboard - VoIP Operations Dashboard Main Page
 * From Figma design - Email Operations monitoring
 */
'use client';

import { useState } from 'react';
import { Sidebar } from '@/components/layout/sidebar';

type EmailMessage = {
  id: string;
  subject: string;
  from: string;
  sent: string;
  status: 'Processing' | 'Complete' | 'Pending';
};

const mockEmails: EmailMessage[] = [
  { id: 'e1', subject: 'Service inquiry', from: 'john@example.com', sent: '2 min ago', status: 'Processing' },
  { id: 'e2', subject: 'Billing question', from: 'sarah@company.com', sent: '15 min ago', status: 'Complete' },
  { id: 'e3', subject: 'Feature request', from: 'mike@startup.io', sent: '1 hr ago', status: 'Complete' },
  { id: 'e4', subject: 'Support issue', from: 'lisa@corp.com', sent: '2 hr ago', status: 'Pending' },
];

const statusConfig: Record<string, { color: string; dot: string }> = {
  Processing: { color: 'text-blue-600 bg-blue-50', dot: 'bg-blue-500' },
  Complete: { color: 'text-green-600 bg-green-50', dot: 'bg-green-500' },
  Pending: { color: 'text-amber-600 bg-amber-50', dot: 'bg-amber-500' },
};

export default function DashboardPage() {
  return (
    <div className="flex h-screen bg-gray-50">
      <Sidebar />
      <main className="flex-1 overflow-y-auto">
        <div className="px-6 py-4">
          {/* Header */}
          <div className="flex items-center justify-between mb-6">
            <div>
              <h1 className="text-xl font-semibold text-gray-900">Email Operations</h1>
              <p className="text-sm text-gray-500 mt-0.5">Real-time email monitoring and analytics</p>
            </div>
            <div className="flex items-center gap-3">
              {/* Tab switcher */}
              <div className="flex bg-gray-100 rounded-lg p-1">
                {['Email', 'SMS', 'Voice'].map(tab => (
                  <button
                    key={tab}
                    className={`px-4 py-1.5 rounded-md text-sm font-medium transition-colors ${
                      tab === 'Email' ? 'bg-white shadow-sm text-gray-900' : 'text-gray-500'
                    }`}
                  >
                    {tab}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-4 gap-4 mb-6">
            <div className="bg-white rounded-xl border border-gray-200 p-4">
              <div className="flex items-center gap-2 mb-2">
                <svg className="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
                <span className="text-sm text-gray-500">Total Messages</span>
              </div>
              <div className="text-2xl font-bold text-gray-900">5,247</div>
              <p className="text-xs text-green-600 mt-1">↑ 12.5% from last week</p>
            </div>

            <div className="bg-white rounded-xl border border-gray-200 p-4">
              <div className="flex items-center gap-2 mb-2">
                <svg className="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
                </svg>
                <span className="text-sm text-gray-500">Unread</span>
              </div>
              <div className="text-2xl font-bold text-gray-900">48</div>
              <p className="text-xs text-green-600 mt-1">↓ 8% from last week</p>
            </div>

            <div className="bg-white rounded-xl border border-gray-200 p-4">
              <div className="flex items-center gap-2 mb-2">
                <svg className="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 21v-4m0 0V5a2 2 0 012-2h6.5l1 1H21l-3 6 3 6h-8.5l-1-1H5a2 2 0 00-2 2zm9-13.5V9" />
                </svg>
                <span className="text-sm text-gray-500">Flagged</span>
              </div>
              <div className="text-2xl font-bold text-gray-900">12</div>
              <p className="text-xs text-amber-600 mt-1">↑ 3 from last week</p>
            </div>

            <div className="bg-white rounded-xl border border-gray-200 p-4">
              <div className="flex items-center gap-2 mb-2">
                <svg className="w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span className="text-sm text-gray-500">Avg Response Time</span>
              </div>
              <div className="text-2xl font-bold text-gray-900">2.3<span className="text-base font-normal text-gray-500">min</span></div>
              <p className="text-xs text-green-600 mt-1">↓ 15% from last week</p>
            </div>
          </div>

          {/* Chart Section */}
          <div className="bg-white rounded-xl border border-gray-200 p-5 mb-6">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-sm font-semibold text-gray-900">Messages Per Channel</h3>
              <div className="flex items-center gap-4 text-xs">
                <span className="flex items-center gap-1.5"><span className="w-2.5 h-0.5 bg-blue-500 rounded"></span> Email</span>
                <span className="flex items-center gap-1.5"><span className="w-2.5 h-0.5 bg-green-500 rounded"></span> SMS</span>
                <span className="flex items-center gap-1.5"><span className="w-2.5 h-0.5 bg-orange-500 rounded"></span> Voice</span>
              </div>
            </div>
            <div className="h-64 relative">
              {/* Placeholder - would use Recharts in production */}
              <div className="absolute inset-0 flex items-center justify-center text-gray-400 text-sm">
                📈 Line chart - Messages per channel over time
              </div>
            </div>
          </div>

          {/* Recent Emails Table */}
          <div className="bg-white rounded-xl border border-gray-200 overflow-hidden mb-6">
            <div className="px-5 py-4 border-b border-gray-100">
              <h3 className="text-sm font-semibold text-gray-900">Recent Emails</h3>
            </div>
            <table className="w-full">
              <thead>
                <tr className="bg-gray-50">
                  <th className="text-left px-5 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">Subject</th>
                  <th className="text-left px-5 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">From</th>
                  <th className="text-left px-5 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">Sent</th>
                  <th className="text-left px-5 py-3 text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                  <th className="w-10"></th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-100">
                {mockEmails.map(email => (
                  <tr key={email.id} className="hover:bg-gray-50">
                    <td className="px-5 py-3.5 text-sm font-medium text-gray-900">{email.subject}</td>
                    <td className="px-5 py-3.5 text-sm text-gray-500">{email.from}</td>
                    <td className="px-5 py-3.5 text-sm text-gray-500">{email.sent}</td>
                    <td className="px-5 py-3.5">
                      <span className={`inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-xs font-medium ${statusConfig[email.status].color}`}>
                        <span className={`w-1.5 h-1.5 rounded-full ${statusConfig[email.status].dot}`}></span>
                        {email.status}
                      </span>
                    </td>
                    <td className="px-5 py-3.5">
                      <button className="text-gray-400 hover:text-gray-600">
                        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 12h.01M12 12h.01M19 12h.01" />
                        </svg>
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          {/* Bottom Stats */}
          <div className="grid grid-cols-3 gap-4">
            <div className="bg-white rounded-xl border border-gray-200 p-5">
              <div className="flex items-center gap-2 mb-2">
                <span className="text-lg">📥</span>
                <span className="text-sm text-gray-500">Total Inbound Messages</span>
              </div>
              <div className="text-2xl font-bold text-gray-900">3,241</div>
            </div>

            <div className="bg-white rounded-xl border border-gray-200 p-5">
              <div className="flex items-center gap-2 mb-2">
                <span className="text-lg">📤</span>
                <span className="text-sm text-gray-500">Total Outbound Messages</span>
              </div>
              <div className="text-2xl font-bold text-gray-900">2,006</div>
            </div>

            <div className="bg-white rounded-xl border border-gray-200 p-5">
              <div className="flex items-center gap-2 mb-2">
                <span className="text-lg">📊</span>
                <span className="text-sm text-gray-500">Response Rate</span>
              </div>
              <div className="text-2xl font-bold text-green-600">92.4<span className="text-base font-normal text-gray-500">%</span></div>
              <div className="mt-2 bg-gray-100 rounded-full h-1.5">
                <div className="bg-green-500 h-1.5 rounded-full" style={{ width: '92.4%' }}></div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
