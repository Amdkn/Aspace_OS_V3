-- Schema Setup for Alykaly OS (Supabase / PostgreSQL)

-- 1. Alpha Leads Table (Data source for "Docket & OSINT" Matrix)
CREATE TABLE alpha_leads (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_number VARCHAR(50) NOT NULL UNIQUE,
    defendant_name VARCHAR(255) NOT NULL,
    surplus_amount DECIMAL(12, 2) NOT NULL,
    priority_tag VARCHAR(50) CHECK (priority_tag IN ('Généalogie', 'B2B', 'Expulsion')),
    osint_status VARCHAR(50) DEFAULT 'new' CHECK (osint_status IN ('new', 'tracking', 'ready')),
    confidence_score INT DEFAULT 0 CHECK (confidence_score >= 0 AND confidence_score <= 5),
    
    -- Enrichment Data
    primary_mobile VARCHAR(20),
    relatives_notes TEXT,
    obituary_links TEXT,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now())
);

-- 2. Clients Table (Data source for "Clients" CRM)
CREATE TABLE clients (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    alpha_lead_id UUID NOT NULL REFERENCES alpha_leads(id) ON DELETE RESTRICT,
    module_type VARCHAR(50) NOT NULL CHECK (module_type IN ('cession', 'buyout')),
    status VARCHAR(50) DEFAULT 'Lead Converti',
    
    -- Compliance Flags
    is_id_valid BOOLEAN DEFAULT FALSE,
    is_poa_signed BOOLEAN DEFAULT FALSE,
    is_affidavit_signed BOOLEAN DEFAULT FALSE,
    
    last_active_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now()),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now())
);

-- 3. Document Vault Table (Linked to Clients)
CREATE TABLE document_vault (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    file_name VARCHAR(255) NOT NULL,
    file_url TEXT NOT NULL,
    file_type VARCHAR(50),
    file_size_bytes BIGINT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now())
);

-- 4. Client Activity Timeline Table
CREATE TABLE client_timeline (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    activity_type VARCHAR(100) NOT NULL, -- e.g., 'docusign_completed', 'sms_sent'
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now())
);

-- 5. Legal Pipeline Table (Data source for "Legal" Kanban)
CREATE TABLE legal_pipeline (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    client_id UUID NOT NULL REFERENCES clients(id) ON DELETE RESTRICT,
    stage VARCHAR(50) DEFAULT 'ready' CHECK (stage IN ('ready', 'filed', 'hearing', 'signed', 'completed')),
    
    -- Critical Dates
    statute_of_limitations_date DATE NOT NULL,
    filing_date DATE,
    hearing_date DATE,
    order_signed_date DATE,
    
    assigned_attorney VARCHAR(255),
    notes TEXT,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc', now())
);

-- Triggers for updated_at timestamps could be added here
