import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import api from '@/lib/api';

export const useIndustrialLeads = () => {
  const queryClient = useQueryClient();

  // Fetch all leads
  const { data: leads, isLoading, error } = useQuery({
    queryKey: ['industrial-leads'],
    queryFn: async () => {
      const response = await api.get('/clients/');
      return response.data;
    },
  });

  // Mutation to add a new lead
  const addLead = useMutation({
    mutationFn: (newLead: any) => api.post('/clients/', newLead),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['industrial-leads'] });
    },
  });

  return { leads, isLoading, error, addLead };
};
