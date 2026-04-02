'use client';
import { useIndustrialLeads } from '@/hooks/use-industrial-leads';

export default function Dashboard() {
  const { leads, isLoading } = useIndustrialLeads();

  return (
    <main className="p-8 bg-slate-50 min-h-screen">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold text-slate-900 mb-2">AuraWorks</h1>
        <p className="text-slate-500 mb-8">East Rand Industrial Intelligence Dashboard</p>

        {isLoading ? (
          <div className="animate-pulse flex space-x-4">
            <div className="flex-1 space-y-4 py-1">
              <div className="h-4 bg-slate-200 rounded w-3/4"></div>
              <div className="space-y-2">
                <div className="h-4 bg-slate-200 rounded"></div>
                <div className="h-4 bg-slate-200 rounded w-5/6"></div>
              </div>
            </div>
          </div>
        ) : (
          <div className="grid gap-4">
            {leads?.map((lead: any) => (
              <div key={lead.id} className="p-6 bg-white border border-slate-200 rounded-xl shadow-sm">
                <h2 className="text-xl font-semibold text-slate-800">{lead.company_name}</h2>
                <div className="flex justify-between items-center mt-2">
                  <span className="text-sm font-medium px-2 py-1 bg-blue-50 text-blue-700 rounded-md">
                    {lead.sector}
                  </span>
                  <span className="text-lg font-bold text-slate-900">
                    R{lead.contract_value.toLocaleString()}
                  </span>
                </div>
              </div>
            ))}
            {leads?.length === 0 && (
              <div className="text-center py-12 border-2 border-dashed border-slate-200 rounded-2xl">
                <p className="text-slate-400">No industrial leads found in aura_local.db.</p>
              </div>
            )}
          </div>
        )}
      </div>
    </main>
  );
}