import { useEffect, useState } from 'react'

type Status = 'checking' | 'ok' | 'down'

async function checkStatus(path: string): Promise<Status> {
  try {
    const response = await fetch(path)
    return response.ok ? 'ok' : 'down'
  } catch {
    return 'down'
  }
}

function StatusRow({ label, status }: { label: string; status: Status }) {
  const colours: Record<Status, string> = {
    checking: 'bg-gray-100 text-gray-600',
    ok: 'bg-green-100 text-green-800',
    down: 'bg-red-100 text-red-800',
  }

  return (
    <li className="flex items-center justify-between py-3">
      <span className="text-gray-700">{label}</span>
      <span className={`rounded-full px-3 py-1 text-sm font-medium ${colours[status]}`}>
        {status}
      </span>
    </li>
  )
}

function App() {
  const [api, setApi] = useState<Status>('checking')
  const [database, setDatabase] = useState<Status>('checking')

  useEffect(() => {
    checkStatus('/api/v1/health').then(setApi)
    checkStatus('/api/v1/health/db').then(setDatabase)
  }, [])

  return (
    <main className="flex min-h-screen items-center justify-center bg-gray-50 px-4">
      <section className="w-full max-w-sm rounded-2xl bg-white p-6 shadow">
        <h1 className="text-2xl font-bold text-gray-900">ArtisanPro</h1>
        <p className="mt-1 text-sm text-gray-500">Development status</p>
        <ul className="mt-4 divide-y divide-gray-100">
          <StatusRow label="Frontend" status="ok" />
          <StatusRow label="Backend API" status={api} />
          <StatusRow label="Database" status={database} />
        </ul>
      </section>
    </main>
  )
}

export default App
