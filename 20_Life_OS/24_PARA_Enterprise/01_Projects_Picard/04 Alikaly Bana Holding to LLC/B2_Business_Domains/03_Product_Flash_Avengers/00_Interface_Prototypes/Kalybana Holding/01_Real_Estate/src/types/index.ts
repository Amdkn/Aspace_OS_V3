export interface AuditRequest {
  id?: string;
  firstName: string;
  lastName: string;
  propertyAddress: string;
  caseNumber?: string;
  status?: 'PENDING' | 'INVESTIGATING' | 'RECOVERED' | 'DENIED';
  createdAt?: string;
}

export interface SEOProps {
  title: string;
  description?: string;
  ogImage?: string;
}
